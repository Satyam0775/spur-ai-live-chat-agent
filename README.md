# Spur AI Live Chat – Take Home Assignment

This project is a mini AI-powered customer support chat application built as part of the **Spur – Founding Full-Stack Engineer Take-Home Assignment**.

It simulates a live chat widget where users can ask questions and receive contextual responses from an AI support agent using a real LLM API.

**Deployed Project Link:**  
[[https://spur-ai-live-chat-6s9a.onrender.com/](https://spur-ai-live-chat-ntxl.onrender.com/)](https://spur-ai-live-chat-ntxl.onrender.com)


---

## 🚀 Features

- AI-powered live chat using a real LLM (Groq LLaMA)
- Session-based conversation memory
- Backend API built with FastAPI
- Frontend served directly from the backend
- SQLite database for conversation persistence
- Clean, modular, production-style architecture

---

## 🧱 Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

### Frontend
- HTML
- CSS
- Vanilla JavaScript

### LLM
- Groq API (LLaMA 3.1)

---

## 📁 Project Structure
# Spur AI Live Chat – Take Home Assignment

This project is a mini AI-powered customer support chat application built as part of the **Spur – Founding Full-Stack Engineer Take-Home Assignment**.

It simulates a live chat widget where users can ask questions and receive contextual responses from an AI support agent using a real LLM API.

---

## 🚀 Features

- AI-powered live chat using a real LLM (Groq LLaMA)
- Session-based conversation memory
- Backend API built with FastAPI
- Frontend served directly from the backend
- SQLite database for conversation persistence
- Clean, modular, production-style architecture

---

## 🧱 Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

### Frontend
- HTML
- CSS
- Vanilla JavaScript

### LLM
- Groq API (LLaMA 3.1)

---

## 📁 Project Structure
# Spur AI Live Chat – Take Home Assignment

This project is a mini AI-powered customer support chat application built as part of the **Spur – Founding Full-Stack Engineer Take-Home Assignment**.

It simulates a live chat widget where users can ask questions and receive contextual responses from an AI support agent using a real LLM API.

---

## 🚀 Features

- AI-powered live chat using a real LLM (Groq LLaMA)
- Session-based conversation memory
- Backend API built with FastAPI
- Frontend served directly from the backend
- SQLite database for conversation persistence
- Clean, modular, production-style architecture

---

## 🧱 Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

### Frontend
- HTML
- CSS
- Vanilla JavaScript

### LLM
- Groq API (LLaMA 3.1)

---

## 📁 Project Structure
backend/
├── app/
│ ├── api/ # API routes
│ ├── core/ # Config & system prompt
│ ├── db/ # DB models, session, CRUD
│ ├── services/ # LLM integration
│ ├── utils/ # Input validation
│ └── static/ # Frontend (HTML/CSS/JS)
│
├── main.py # FastAPI entry point
├── requirements.txt
└── .env


---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd backend

2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables

Create a .env file in the backend folder:

GROQ_API_KEY=your_groq_api_key_here

5️⃣ Run the application
python -m uvicorn main:app --reload

🌐 Access the App

Frontend UI:
http://127.0.0.1:8000/

API Docs (Swagger):
http://127.0.0.1:8000/docs

🤖 LLM Details

Provider: Groq

Model: LLaMA 3.1

Prompting Strategy

A system prompt defines store policies (shipping, returns, support hours)

Conversation history is included to maintain context

Guardrails

Graceful error handling

Max token limit for cost control

🗃️ Data Persistence

SQLite database (chat.db)

Tables:

conversations

messages

Each session maintains full chat history

🧪 Backend API Testing (Postman)

The backend API was tested independently using Postman to verify correctness without relying on the frontend.

Endpoint
POST /chat/message

URL
http://127.0.0.1:8000/chat/message

Headers
Content-Type: application/json

Request Body (JSON)
{
  "message": "What is your return policy?"
}

Sample Response
{
  "reply": "Our return policy is a 7-day no-questions-asked return policy. If you're not satisfied with your purchase, you can return it within 7 days for a full refund.",
  "sessionId": "ea4cb8d5-03b0-4994-9b4c-a991c46efa33"
}

Session Continuity Test
{
  "message": "Do you ship to the USA?",
  "sessionId": "ea4cb8d5-03b0-4994-9b4c-a991c46efa33"
}


The AI successfully maintained context across messages, confirming correct session-based conversation handling.

✅ Verification Summary

Backend API works independently via Postman
LLM responses are generated correctly
Conversation history is persisted per session
Frontend and backend behavior are consistent
This confirms the backend is robust and correctly implemented as per the assignment requirements.

🧠 Design Decisions
Frontend served via FastAPI static files to avoid CORS issues
Clean separation of concerns (API, DB, services, utils)
Simple UI to focus on functionality over styling
No authentication to keep scope aligned with the assignment

🔄 Trade-offs & Future Improvements

If I had more time, I would:
Add streaming responses for better UX
Improve frontend UI/UX
Add Redis for session caching

Add authentication and multi-agent support
Deploy with CI/CD

Status✅ 
All core requirements of the Spur Founding Full-Stack Engineer take-home assignment are fully implemented and working end-to-end.
