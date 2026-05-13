# Silence Detection Module

## 📌 Overview

The Silence Detection Module is a Python-based audio processing system that detects periods of silence or no-response in an audio file. The module analyzes sound levels and identifies whether the audio remains below a specified threshold for a certain duration.

This project is useful for:

- AI Interview Systems
- Voice Assistants
- Online Assessment Platforms
- Speech-Based Applications
- Call Monitoring Systems

---

# 🎯 Objective

The objective of this project is to:

- Detect silence/no-response situations
- Measure silence duration
- Return structured JSON output
- Handle basic audio edge cases

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| pydub | Audio Processing |
| FFmpeg | Audio Decoding |
| JSON | Structured Output |

---

# 📂 Project Structure

```text
silence_detection.-main 2/
│
├── main.py
├── detector.py
├── config.py
└── samples/
    └── sample.wav

### 📤 Output
Example 1 — Silence Detected
{
  "silence_detected": true,
  "duration_sec": 5
}
Example 2 — No Silence
{
  "silence_detected": false,
  "duration_sec": 0
}
