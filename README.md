# 🎙️ Speech-to-Text Transcription with OpenAI Whisper

A simple Python script that transcribes audio files into text using [OpenAI Whisper](https://github.com/openai/whisper) — a state-of-the-art, open-source speech recognition model that runs **locally** (no API key needed).

---

## 📋 What It Does

1. **Loads** an audio file (WAV, MP3, M4A, FLAC, OGG, MP4, etc.)
2. **Transcribes** the speech to text using Whisper's `base` model
3. **Prints** the full transcript with timestamps per segment
4. **Saves** the results to:
   - `transcript.txt` — plain text output
   - `transcript.json` — structured output with start/end timestamps

---

## 🗂️ Project Structure

```
volgaparnters/
├── stt.py              # Main transcription script
├── transcript.txt      # Output: plain text transcript
├── transcript.json     # Output: timestamped transcript (JSON)
├── README.md           # This file
└── venv/               # Python virtual environment
```

---

## ⚙️ Requirements

- Python 3.8+
- [FFmpeg](https://ffmpeg.org/download.html) (for audio format conversion)
- OpenAI Whisper

---

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/volgaparnters.git
cd volgaparnters
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install openai-whisper
```

> **Note:** FFmpeg must also be installed on your system. On Windows, you can use `winget install ffmpeg` or download it from the [official site](https://ffmpeg.org/download.html).

---

## ▶️ Usage

1. Open `stt.py` and update the `AUDIO_FILE` path to point to your audio file:

```python
AUDIO_FILE = "path/to/your/audio.wav"
```

2. Run the script:
```bash
python stt.py
```

### Example Output

```
Step 1: Loading audio file...
  File: eternalfeminine.wav

Step 2: Loading Whisper model (base)...
  Model ready!

Step 3: Transcribing audio (this may take a moment on CPU)...
  Transcription done!

Step 4: Full Transcript
--------------------------------------------------
The eternal feminine draws us upward...

Step 5: Transcript with Timestamps
--------------------------------------------------
[00:00.00 --> 00:04.50]  The eternal feminine draws us upward...

Step 6: Saving results...
  Saved: transcript.txt
  Saved: transcript.json

Done!
```

---

## 🤖 Whisper Model Sizes

You can change the model in `stt.py` to trade off between speed and accuracy:

| Model  | Speed   | Accuracy | VRAM   |
|--------|---------|----------|--------|
| tiny   | Fastest | Lower    | ~1 GB  |
| base   | Fast    | Good     | ~1 GB  |
| small  | Medium  | Better   | ~2 GB  |
| medium | Slow    | Great    | ~5 GB  |
| large  | Slowest | Best     | ~10 GB |

To change the model, edit this line in `stt.py`:
```python
model = whisper.load_model("base")  # Change "base" to any model name above
```

---

## 📄 Output Files

### `transcript.txt`
Plain text of the full transcription.

### `transcript.json`
Structured JSON with timestamps:
```json
{
    "audio_file": "eternalfeminine.wav",
    "full_text": "The eternal feminine draws us upward...",
    "segments": [
        {
            "start": 0.0,
            "end": 4.5,
            "text": "The eternal feminine draws us upward..."
        }
    ]
}
```

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
