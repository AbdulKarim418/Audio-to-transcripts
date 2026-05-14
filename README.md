# 🎙️ Speech-to-Text Transcription with OpenAI Whisper

A simple Python script that transcribes audio files into text using OpenAI Whisper open-source speech recognition model that runs locally.
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
├── README.md           
```

---

## ⚙️ Requirements

- Python 3.8+
- [FFmpeg] (for audio format conversion)
- OpenAI Whisper

---

###  Install dependencies
pip install openai-whisper
> **Note:** FFmpeg must also be installed on your system.
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
