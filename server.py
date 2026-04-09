from flask import Flask, request, jsonify, render_template
import os
import sys
from pathlib import Path
from dotenv import load_dotenv


def load_env():
    env_path = Path(__file__).resolve().parent / '.env'
    load_dotenv(dotenv_path=env_path, override=True)
    print(f"[server] Python executable: {sys.executable}")
    print(f"[server] cwd: {Path.cwd()}")
    print(f"[server] server file: {Path(__file__).resolve()}")
    print(f"[server] Loaded .env from {env_path}, GROQ_API_KEY set: {bool(os.getenv('GROQ_API_KEY'))}")

load_env()

import main

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/command", methods=["POST"])
def api_command():
    load_env()
    print(f"[server.api_command] GROQ_API_KEY set: {bool(os.getenv('GROQ_API_KEY'))}")

    data = request.get_json(silent=True)
    if not data or "command" not in data:
        return jsonify({"success": False, "error": "No command provided."}), 400

    command = str(data.get("command", "")).strip()
    if not command:
        return jsonify({"success": False, "error": "Empty command."}), 400

    lowered = command.lower()
    try:
        # Use the existing backend logic from main.py.
        if any(keyword in lowered for keyword in ["open google", "open youtube", "open facebook", "open linkedin", "news"]) or lowered.startswith("play"):
            main.processCommand(command)
            return jsonify({
                "success": True,
                "result": "Command executed. If it opened a browser or spoke audio, the backend handled it.",
                "command": command
            })

        output = main.aiProcess(command)
        if output is None or output == "":
            return jsonify({"success": False, "error": "AI response was empty. Please check your OpenAI API configuration.", "command": command}), 500
        if output.startswith("OpenAI API key is missing") or output.startswith("An error occurred during the API call"):
            return jsonify({"success": False, "error": output, "command": command}), 500
        return jsonify({"success": True, "result": output, "command": command})

    except Exception as e:
        return jsonify({"success": False, "error": str(e), "command": command}), 500

@app.route("/api/health", methods=["GET"])
def health_check():
    load_env()
    return jsonify({
        "success": True,
        "python_executable": sys.executable,
        "cwd": str(Path.cwd()),
        "server_file": str(Path(__file__).resolve()),
        "groq_key_present": bool(os.getenv("GROQ_API_KEY"))
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
