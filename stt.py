import whisper
import json

# ── STEP 1: Set the audio file path ──────────────────────────────────────────
# Whisper supports MP3, WAV, M4A, OGG, FLAC, MP4 etc.
# FFmpeg (bundled in venv/Scripts) handles format conversion automatically.
print("Step 1: Loading audio file...")

AUDIO_FILE = "C:/Users/Muhammad Bilal/Desktop/volgaparnters/eternalfeminine.wav"
print(f"  File: {AUDIO_FILE}")


# ── STEP 2: Load the Whisper model ───────────────────────────────────────────
# Model sizes: tiny (fastest) → base → small → medium → large (most accurate)
# For tests/demos, 'base' is a good choice.
print("\nStep 2: Loading Whisper model (base)...")

model = whisper.load_model("base")
print("  Model ready!")


# ── STEP 3: Transcribe the audio ─────────────────────────────────────────────
# Whisper automatically handles long audio by splitting it into 30-second chunks.
# Each chunk is processed and the results are merged — no manual splitting needed.
print("\nStep 3: Transcribing audio (this may take a moment on CPU)...")

result = model.transcribe(AUDIO_FILE, language="en", verbose=False)
print("  Transcription done!")


# ── STEP 4: Print the full transcript ────────────────────────────────────────
print("\nStep 4: Full Transcript")
print("-" * 50)
print(result["text"].strip())


# ── STEP 5: Print timestamps per segment ─────────────────────────────────────
# Each segment has a start time, end time, and the spoken text.
print("\nStep 5: Transcript with Timestamps")
print("-" * 50)

for seg in result["segments"]:
    start = seg["start"]
    end   = seg["end"]
    text  = seg["text"].strip()

    # Format seconds as MM:SS
    start_fmt = f"{int(start // 60):02d}:{start % 60:05.2f}"
    end_fmt   = f"{int(end   // 60):02d}:{end   % 60:05.2f}"

    print(f"[{start_fmt} --> {end_fmt}]  {text}")


# ── STEP 6: Save results to files ────────────────────────────────────────────
print("\nStep 6: Saving results...")

# Save plain text
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"].strip())
print("  Saved: transcript.txt")

# Save JSON with timestamps
output = {
    "audio_file": AUDIO_FILE,
    "full_text": result["text"].strip(),
    "segments": [
        {
            "start": round(seg["start"], 2),
            "end":   round(seg["end"],   2),
            "text":  seg["text"].strip()
        }
        for seg in result["segments"]
    ]
}
with open("transcript.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4, ensure_ascii=False)
print("  Saved: transcript.json")

print("\nDone!")