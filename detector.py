from pydub import AudioSegment
from pydub.silence import detect_silence
from config import THRESHOLD_DB, MIN_SILENCE_LEN


def detect_audio_silence(audio_path):

    audio = AudioSegment.from_file(audio_path)

    silent_ranges = detect_silence(
        audio,
        min_silence_len=MIN_SILENCE_LEN,
        silence_thresh=THRESHOLD_DB
    )

    if silent_ranges:

        start, end = silent_ranges[0]

        duration_sec = (end - start) / 1000

        return {
            "silence_detected": True,
            "duration_sec": duration_sec
        }

    return {
        "silence_detected": False,
        "duration_sec": 0
    }
