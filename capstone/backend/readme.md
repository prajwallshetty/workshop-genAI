# 🚀 CampusAI Backend

FastAPI backend for CampusAI — handles AI responses using Groq API.

---

## 🛠 Tech Stack

- FastAPI
- Uvicorn
- Groq SDK
- Python Dotenv
- Pydantic

---

## 📁 Project Structure

backend/
│── main.py  
│── ai_engine.py  
│── .env  
│── requirements.txt  

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate (Windows):

```bash
venv\Scripts\activate
```

---

### 2️⃣ Install Dependencies

If `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

Otherwise install manually:

```bash
pip install fastapi uvicorn groq python-dotenv
```

---

### 3️⃣ Create `.env` File

Create a `.env` file inside `backend/`:

```
GROQ_API_KEY=your_api_key_here
```

---

### 4️⃣ Run Server

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### POST `/chat`

### Request Body

```json
{
  "mode": "academic",
  "query": "Explain machine learning"
}
```

### Response

```json
{
  "mode": "academic",
  "response": "Machine learning is..."
}
```

---

## 🔐 CORS Configuration

CORS is enabled for:

```
http://localhost:3000
```

---

## 🧠 Available Modes

- academic
- placement
- research
- debug
- startup

---

## 👨‍💻 Project

CampusAI Capstone Backend