Google Gemini API Chatbot
This project is a web application that uses the Google Gemini API to create a smart chatbot via FastAPI. It allows users to send queries in Arabic and get accurate responses based on the gemini-1.5-flash-latest model. The project features session management, chat reset functionality, and a health check endpoint.

Features
Smart Chat Interface: The model interacts with users in multiple languages, including Arabic.
Session Management: Each user has a separate session to ensure continuous conversations.
Chat Reset: Users can reset their chat history.
Health and Status Check: Includes an endpoint to check the server's health.

Requirements
Python 3.7 or higher.
FastAPI: For building the API.
Google Generative AI SDK: For using the Google Gemini model.
python-dotenv: For loading environment variables from .env files.
asyncio: For managing asynchronous sessions.
Uvicorn: For running the application using an ASGI server.
Setup Locally
1. Install Dependencies
Start by installing the required packages using pip:

pip install -r requirements.txt

2. Set up the Environment
Make sure you have created a .env file in the root directory of your project, and add your Google API key to it:
.env file
GOOGLE_API_KEY=your_google_api_key_here

3. Run the Application
Once the environment is set up, you can run the server using uvicorn:

uvicorn main:app --reload
main:app refers to the application object (app) in the main.py file.

4. Access the API
After running the server, you can access the API at the following endpoints:

/chat/: Send a query and get a response from the Google Gemini model.
/reset/: Reset the user's chat session.
/health: A health check endpoint to verify the server is working.
Example Usage:
Sending a Query: To send a query via the API, use the following request:

POST http://127.0.0.1:8000/chat/
Content-Type: application/x-www-form-urlencoded
Form Data:
- user_id: unique_user_id
- query: What is the capital of Egypt?
Resetting the Session: To reset the chat history for a user:

POST http://127.0.0.1:8000/reset/
Content-Type: application/x-www-form-urlencoded
Form Data:
- user_id: unique_user_id
Health Check: To check if the server is running properly:

GET http://127.0.0.1:8000/health

Project Structure


├── main.py                
├── .env                   
├── requirements.txt      
└── README.md             

Notes
Session Management: Each user has a separate session that stores their conversation history.
Error Handling: HTTPException is used to handle errors resulting from invalid requests or server issues.
Extending the Project

1. Improving Responses:
The generation parameters, such as temperature and top_p, can be fine-tuned to better suit user needs.
2. Adding a Frontend:
This API can be integrated with a frontend to provide an interactive user experience.

3. Expanding Supported Languages:
You can add additional language models to support more languages beyond Arabic.
