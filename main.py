import streamlit as st
import requests

# Define your FastAPI server URL
API_URL = "http://127.0.0.1:8000"

st.title("Chatbot Demo")
st.write("Interact with the AI chatbot!")

user_id = st.text_input("Enter User ID:")
query = st.text_area("Enter your query:")

if st.button("Send Query"):
    if user_id and query:
        response = requests.post(
            f"{API_URL}/chat/",
            data={"user_id": user_id, "query": query},
        )
        if response.status_code == 200:
            data = response.json()
            st.write("### Response:")
            st.write(data["response"])
        else:
            st.error("Error communicating with the API.")

if st.button("Reset Chat History"):
    if user_id:
        response = requests.post(f"{API_URL}/reset/", data={"user_id": user_id})
        if response.status_code == 200:
            st.success("Chat history reset.")
        else:
            st.error("Error resetting chat history.")
