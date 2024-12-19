from fastapi import FastAPI, HTTPException, Form
import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import Dict, Any
import asyncio

load_dotenv()

app = FastAPI()

genai_api_key = os.getenv("GOOGLE_API_KEY")
if not genai_api_key:
    raise EnvironmentError("GOOGLE_API_KEY is not set in the environment variables.")

genai.configure(api_key=genai_api_key)

chat_sessions: Dict[str, Any] = {}

chat_locks: Dict[str, asyncio.locks.Lock] = {}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    generation_config={
        "temperature": 0.2,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2000,
    },
    system_instruction="أنت مساعد ذكي متخصص في تقديم إجابات دقيقة باللغة العربية."
)

@app.post("/chat/")
async def chat(user_id: str = Form(...), query: str = Form(...)):
    try:
        if user_id not in chat_locks:
            chat_locks[user_id] = asyncio.locks.Lock()

        async with chat_locks[user_id]:
            if user_id not in chat_sessions:
                chat_sessions[user_id] = model.start_chat(history=[])

            chat_session = chat_sessions[user_id]

            response = chat_session.send_message(query)

            # Do not delete chat_sessions here. This may cause issues when trying to access it later.
            return {
                "user_id": user_id,
                "query": query,
                "response": response.text.strip(),
                "history": [
                    {"role": h.role, "content": h.parts[0].text} for h in chat_session.history
                ],
            }

    except KeyError as ke:
        raise HTTPException(status_code=400, detail=f"Invalid user ID: {str(ke)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")


@app.post("/reset/")
async def reset_chat(user_id: str = Form(...)):
    try:
        if user_id not in chat_locks:
            raise HTTPException(status_code=404, detail="User ID not found.")

        async with chat_locks[user_id]:
            if user_id in chat_sessions:
                del chat_sessions[user_id]
                return {"message": f"Chat history for user {user_id} has been reset."}
            else:
                raise HTTPException(status_code=404, detail="User ID not found.")

    except KeyError as ke:
        raise HTTPException(status_code=400, detail=f"Error resetting chat history: {str(ke)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error resetting chat history: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "Server is running and healthy."}

