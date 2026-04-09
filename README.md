# 🤖 Jarvis — AI Virtual Assistant

A voice-activated and web-based AI assistant inspired by Tony Stark's J.A.R.V.I.S., built with Python, Flask, and Groq's blazing-fast LLM inference. Jarvis listens for your voice, answers questions using the Llama 3.3 70B model, opens websites, plays music, and fetches the latest news — all hands-free.

---

## ✨ Features

- 🎙️ **Voice Activation** — Wake word detection using `SpeechRecognition`; just say "Hello" to activate
- 🧠 **AI-Powered Responses** — Powered by Groq's Llama 3.3 70B model for fast, high-quality answers
- 🌐 **Web Control** — Open Google, YouTube, Facebook, and LinkedIn by voice or web command
- 🎵 **Music Playback** — Play songs from your personal music library
- 📰 **Live News** — Fetches and reads out the latest headlines via NewsData.io
- 🖥️ **Web Frontend** — A sleek browser-based interface to send commands and read responses
- 🔌 **Flask REST API** — Clean backend API connecting the web frontend to the AI engine

---

## 🗂️ Project Structure

```
Jarvis-ai-virtual-assistant/
│
├── main.py               # Core voice assistant logic (speech recognition, AI, commands)
├── server.py             # Flask backend exposing REST API for the web frontend
├── musiclibrary.py       # Dictionary of song names mapped to URLs
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not committed to git)
├── .env.example          # Template for setting up environment variables
│
├── templates/
│   └── index.html        # Jarvis web frontend (served by Flask)
│
└── static/               # Static assets (CSS, JS, images)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- A free [Groq API key](https://console.groq.com)
- A free [NewsData.io API key](https://newsdata.io) *(for news feature)*
- A working microphone *(for voice mode)*

---

### 1. Clone the Repository

```bash
git clone https://github.com/Akundu007-rgb/Jarvis-ai-virtual-assistant.git
cd Jarvis-ai-virtual-assistant
```

### 2. Create and Activate a Virtual Environment

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS / Linux
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> **Get your free Groq API key at:** https://console.groq.com

---

## 🖥️ Running the Web Interface

Start the Flask server:

```bash
python server.py
```

Then open your browser and go to:

```
http://localhost:5000
```

Type any command in the input box and Jarvis will respond instantly.

---

## 🎙️ Running Voice Mode

To run the standalone voice assistant (no browser required):

```bash
python main.py
```

Jarvis will initialize and start listening. Say **"Hello"** to wake it up, then speak your command.

---

## 🗣️ Supported Commands

| Command | Action |
|---|---|
| `Hello` | Wake word — activates Jarvis |
| `Open Google` | Opens google.com in browser |
| `Open YouTube` | Opens youtube.com in browser |
| `Open Facebook` | Opens facebook.com in browser |
| `Open LinkedIn` | Opens linkedin.com in browser |
| `Play <song name>` | Plays song from music library |
| `News` | Reads latest headlines aloud |
| Any other query | Sent to Groq AI for a smart response |

---

## 🔌 API Reference

The Flask server exposes the following endpoints:

### `POST /api/command`

Send a command to Jarvis.

**Request body:**
```json
{
  "command": "What is machine learning?"
}
```

**Response:**
```json
{
  "success": true,
  "result": "Machine learning is a subset of AI...",
  "command": "What is machine learning?"
}
```

---

### `GET /api/health`

Check backend status and environment configuration.

**Response:**
```json
{
  "success": true,
  "groq_key_present": true,
  "python_executable": "...",
  "cwd": "..."
}
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| AI / LLM | [Groq](https://groq.com) — Llama 3.3 70B Versatile |
| Voice Input | `SpeechRecognition` + Google Speech API |
| Voice Output | `pyttsx3` (offline TTS) |
| Backend | Python + Flask |
| Frontend | HTML / CSS / JavaScript |
| News API | [NewsData.io](https://newsdata.io) |
| Env Management | `python-dotenv` |

---

## 📦 Requirements

Key dependencies from `requirements.txt`:

```
flask
flask-cors
groq
speechrecognition
pyttsx3
requests
python-dotenv
pyaudio
```

Install all with:

```bash
pip install -r requirements.txt
```

> **Note for Windows users:** If `pyaudio` fails to install, download the matching `.whl` file from [this repository](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually.

---

## 🔒 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `GROQ_API_KEY` | Your Groq API key for LLM inference | ✅ Yes |

Never commit your `.env` file. It is already listed in `.gitignore`.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- Inspired by J.A.R.V.I.S. from Marvel's Iron Man
- Powered by [Groq](https://groq.com) for ultra-fast LLM inference
- Built as part of a Python learning journey 🚀

---

<p align="center">Made with ❤️ by <a href="https://github.com/Akundu007-rgb">Akundu007-rgb</a></p>
