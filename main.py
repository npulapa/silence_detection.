from detector import detect_audio_silence

audio_file = "samples/sample.wav"

result = detect_audio_silence(audio_file)

print(result)
