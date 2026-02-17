# 🤖 IntelliBot — AI Voice Assistant (FastAPI + React + ChatGPT + ElevenLabs)

> 🎙️ A full-stack AI voice chatbot that understands human speech, generates intelligent responses using AI, and speaks back using real-time voice synthesis.

---

## 🚀 Project Overview

**IntelliBot** is a modern AI-powered conversational assistant built using **FastAPI**, **React**, and advanced **AI frameworks**.  
It combines speech-to-text, natural language processing, and text-to-speech to create a seamless voice interaction experience.

The system captures audio from users, processes it with AI models, generates intelligent responses, and returns synthesized voice output — enabling a real-time conversational workflow.

This project demonstrates:

✅ Full-stack architecture  
✅ REST API development  
✅ AI integration  
✅ Voice interaction pipelines  
✅ Modern developer tooling

---

## 🧠 Key Features

✨ Voice input processing (Speech → Text)  
✨ AI conversational responses using ChatGPT  
✨ Natural voice synthesis using ElevenLabs  
✨ FastAPI backend with async processing  
✨ React frontend interface  
✨ Streaming audio responses  
✨ RESTful API architecture  
✨ Modular project structure

---

## 🏗️ Architecture

```
Frontend (React)
        ↓
FastAPI Backend
        ↓
AI Processing Layer
   ├── Speech Recognition
   ├── ChatGPT NLP
   └── ElevenLabs TTS
        ↓
Audio Streaming Response
```

---

## 🖥️ Tech Stack

### ⚡ Backend
- 🐍 Python
- ⚡ FastAPI
- 🧩 Pydantic
- 🔗 REST APIs
- 🌐 CORS Middleware
- Async Streaming Responses

### 🎨 Frontend
- ⚛️ React
- 🎨 TailwindCSS
- Modern JavaScript (ES6+)

### 🤖 AI & Voice
- ChatGPT (Natural Language Processing)
- ElevenLabs (Voice Synthesis)
- Audio Processing Pipelines

### 🧰 Tools
- Postman (API Testing)
- Git & GitHub
- VS Code

---

## 📂 Project Structure

```
IntelliBot/
│
├── backend/
│   ├── main.py
│   ├── functions/
│   │     ├── openai_requests.py
│   │     ├── text_to_speech.py
│   │     └── database.py
│   └── .env.example
│
├── frontend/
│   ├── src/
│   └── components/
│
└── README.md
```

---

## ⚙️ How It Works

### 🎙️ Step 1 — User Voice Input
User records audio from the React frontend.

### 🧾 Step 2 — Speech Recognition
Audio is sent to FastAPI backend where speech is converted into text.

### 🧠 Step 3 — AI Processing
Text input is processed using ChatGPT for intelligent responses.

### 🔊 Step 4 — Voice Generation
Response text is converted into natural speech using ElevenLabs.

### 📡 Step 5 — Streaming Response
Audio response is streamed back to frontend.

---

## 🔌 API Endpoints

### Health Check
```
GET /health
```

### Reset Conversation
```
GET /reset
```

### Send Voice Message
```
POST /post-audio/
```

Accepts:
```
multipart/form-data → audio file
```

Returns:
```
Streaming audio response
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Dharvipatel10/IntelliBot.git
cd IntelliBot
```

---

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run server:

```bash
python -m uvicorn main:app --reload
```

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 🔐 Environment Variables

Create:

```
backend/.env
```

Example:

```env
OPENAI_API_KEY=your_key_here
ELEVENLABS_API_KEY=your_key_here
```

⚠️ Never commit `.env` files.

---

## 🧪 Testing

API endpoints tested using:

✅ Postman  
✅ Swagger Docs (`/docs`)  
✅ Browser testing

---

## 🎯 Learning Outcomes

This project showcases:

✔️ AI integration into full-stack applications  
✔️ FastAPI async API design  
✔️ Voice-enabled interfaces  
✔️ Real-time streaming responses  
✔️ Secure environment handling  
✔️ Clean modular architecture

---

## 👨‍💻 Author

**Dharvi Rakeshkumar Patel**  
Full-Stack Engineer | TU Chemnitz

