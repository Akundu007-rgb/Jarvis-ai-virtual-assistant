<h1 align="center">🤖 Jarvis AI Virtual Assistant</h1>

<p align="center">
  Your personal AI-powered assistant inspired by Iron Man's J.A.R.V.I.S.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/AI-Groq%20%7C%20Llama%203.3%2070B-8A2BE2?logo=meta">
  <img src="https://img.shields.io/badge/Backend-Flask-black?logo=flask">
  <img src="https://img.shields.io/badge/Voice-SpeechRecognition-orange?logo=google">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen">
</p>

---

## 🚀 Overview

**Jarvis** is an AI-powered virtual assistant built with Python and Flask that responds to both **voice commands** and **text input** via a web interface. It leverages **Groq's ultra-fast Llama 3.3 70B** model to deliver intelligent, real-time responses — completely free.

Inspired by **Iron Man's J.A.R.V.I.S.**, this project brings together speech recognition, AI inference, web automation, and a sleek browser-based UI into one cohesive assistant.

---

## ✨ Features

- 🎙️ **Voice Activation** — Wake Jarvis by saying *"Hello"*, then speak your command
- 🧠 **AI Responses** — Powered by Groq's Llama 3.3 70B for fast, accurate answers
- 🌐 **Web Automation** — Opens Google, YouTube, Facebook, LinkedIn on command
- 🎵 **Music Playback** — Plays songs from your personal music library
- 📰 **Live News** — Fetches and reads the latest headlines via NewsData.io
- 🔊 **Text-to-Speech** — Speaks responses aloud using `pyttsx3`
- 🖥️ **Web Frontend** — Browser-based UI to send commands and read responses
- 🔌 **REST API** — Clean Flask backend connecting frontend to the AI engine

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| 🤖 AI / LLM | [Groq](https://groq.com) — Llama 3.3 70B Versatile (Free) |
| 🎤 Voice Input | `SpeechRecognition` + Google Speech API |
| 🔊 Voice Output | `pyttsx3` (offline TTS) |
| 🌐 Backend | Python + Flask |
| 🖥️ Frontend | HTML / CSS / JavaScript |
| 📰 News API | [NewsData.io](https://newsdata.io) |
| ⚙️ Env Config | `python-dotenv` |

---

## ⚙️ How It Works

```
User Input (Voice / Text)
        ↓
  Wake Word Detected ("Hello")
        ↓
  Command Processed by main.py
        ↓
   ┌────────────────────────────┐
   │  Web command?  → Browser opened   │
   │  Music command? → Song played     │
   │  News command?  → Headlines read  │
   │  Anything else? → Groq AI responds│
   └────────────────────────────┘
        ↓
  Response spoken aloud + shown in UI
```

### Flow:
1. User speaks or types a command
2. Wake word (`"Hello"`) activates voice mode
3. Command is matched against built-in actions
4. Unknown commands are forwarded to **Groq AI** for a smart response
5. Response is returned via speech and/or the web UI

---

## 📂 Project Structure

```
Jarvis-ai-virtual-assistant/
│
├── main.py               # Core assistant logic (voice, AI, commands)
├── server.py             # Flask REST API backend
├── musiclibrary.py       # Song name → URL mapping
├── requirements.txt      # Python dependencies
├── .env                  # API keys (not committed)
├── .env.example          # Environment variable template
│
├── templates/
│   └── index.html        # Web frontend served by Flask
│
└── static/               # CSS, JS, and assets
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Akundu007-rgb/Jarvis-ai-virtual-assistant.git
cd Jarvis-ai-virtual-assistant
```

### 2️⃣ Create and activate virtual environment
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS / Linux
python -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

> ⚠️ **Windows users:** If `pyaudio` fails, install it manually from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

### 4️⃣ Configure environment variables

Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```
Get your **free** Groq API key at 👉 https://console.groq.com

### 5️⃣ Run the assistant

**Web interface (recommended):**
```bash
python server.py
```
Then open 👉 `http://localhost:5000`

**Voice-only mode:**
```bash
python main.py
```

---

## 🎮 Example Commands

| Command | Action |
|---|---|
| `"Hello"` | Wake word — activates Jarvis |
| `"Open Google"` | Opens google.com |
| `"Open YouTube"` | Opens youtube.com |
| `"Open Facebook"` | Opens facebook.com |
| `"Open LinkedIn"` | Opens linkedin.com |
| `"Play <song>"` | Plays song from music library |
| `"News"` | Reads latest headlines |
| `"What is machine learning?"` | AI-generated response via Groq |

---

## 🔌 API Reference

### `POST /api/command`
Send a text command to Jarvis.

```json
// Request
{ "command": "What is Python?" }

// Response
{ "success": true, "result": "Python is a high-level programming language..." }
```

### `GET /api/health`
Check server and API key status.

```json
{ "success": true, "groq_key_present": true }
```

---

## 🚧 Future Improvements

- 🧠 Memory-based conversation (multi-turn context)
- 🖥️ Full desktop GUI
- 📱 Mobile app integration
- 🌍 Multi-language support
- 🔐 User authentication
- 📅 Calendar & reminder integration
- 🏠 Smart home device control

---

## 🧠 Learning Outcomes

- AI assistant architecture design
- REST API development with Flask
- Voice recognition & TTS integration
- LLM API integration (Groq / Llama)
- Real-world Python project building
- Frontend–backend communication

---

## 👨‍💻 Author

**Anirban Kundu**  
🎓 B.Tech CSE &nbsp;|&nbsp; 🚀 Aspiring AI Engineer  
[![GitHub](https://img.shields.io/badge/GitHub-Akundu007--rgb-181717?logo=github)](https://github.com/Akundu007-rgb)

---

## 🌟 Support

If you like this project:
- ⭐ **Star** this repository
- 🍴 **Fork** it and build your own version
- 📢 **Share** it with others

---

## 📜 Disclaimer

This project is for **educational purposes only** and is inspired by the fictional AI system J.A.R.V.I.S. from Marvel's Iron Man. Not affiliated with Marvel or any related entities.
