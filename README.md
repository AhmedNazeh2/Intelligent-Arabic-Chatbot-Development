
# Project: Arabic Chatbot using FastAPI and Google Generative AI

This project implements an intelligent chatbot system using FastAPI and Google Generative AI (Gemini 1.5). The chatbot is designed to provide accurate answers in Arabic and support multi-session handling for different users.

---

## Features

- **Arabic Language Support**: The chatbot specializes in generating responses in Arabic, tailored to user queries.
- **Session Management**: Each user has an isolated chat session, ensuring continuity of conversations.
- **Chat History**: Keeps track of conversation history for each user.
- **Reset Functionality**: Allows users to reset their chat history.
- **Health Check Endpoint**: Verifies server health and readiness.

---

## Prerequisites

- Python 3.8+
- FastAPI
- Google Generative AI API Key
- `dotenv` library for managing environment variables

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <https://github.com/AhmedNazeh2/chatbot_system_using_Gemini_API.git>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory with the following content:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   ```

4. **Run the Application**:
   ```bash
   uvicorn app:app --reload
   ```

---

## Endpoints

### 1. **Chat Endpoint**
   - **URL**: `/chat/`
   - **Method**: `POST`
   - **Description**: Sends a query to the chatbot and receives a response.
   - **Parameters**:
     - `user_id` (form): Unique identifier for the user.
     - `query` (form): User's question or message.
   - **Response**:
     ```json
     {
       "user_id": "123",
       "query": "كيف حالك؟",
       "response": "أنا بخير، كيف يمكنني مساعدتك؟",
       "history": [
         {
           "role": "user",
           "content": "كيف حالك؟"
         },
         {
           "role": "assistant",
           "content": "أنا بخير، كيف يمكنني مساعدتك؟"
         }
       ]
     }
     ```

### 2. **Reset Chat Endpoint**
   - **URL**: `/reset/`
   - **Method**: `POST`
   - **Description**: Resets the chat history for a user.
   - **Parameters**:
     - `user_id` (form): Unique identifier for the user.
   - **Response**:
     ```json
     {
       "message": "Chat history for user 123 has been reset."
     }
     ```

### 3. **Health Check Endpoint**
   - **URL**: `/health`
   - **Method**: `GET`
   - **Description**: Checks the server's health status.
   - **Response**:
     ```json
     {
       "status": "Server is running and healthy."
     }
     ```

---

## Technologies Used

- **FastAPI**: For creating the REST API.
- **Google Generative AI**: To power the chatbot.
- **asyncio**: For managing asynchronous tasks like chat sessions.
- **dotenv**: To manage environment variables.

---

## Project Structure

```
.
├── app.py            # Main application file
├── requirements.txt   # Dependencies
├── .env               # Environment variables
├── README.md          # Project documentation
```

---

## Best Practices

- **Secure API Key**: Ensure the `GOOGLE_API_KEY` is kept confidential and not exposed in the code.
- **Concurrency Handling**: The project uses locks to prevent concurrent access to the same user's chat session.
- **Error Handling**: Comprehensive exception handling ensures meaningful error messages and stable operation.

---

## Future Enhancements

- Add multilingual support.
- Improve session persistence using a database.
- Implement rate limiting to prevent abuse.
- Add support for richer responses like images or links.

---

## Contributing

Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

