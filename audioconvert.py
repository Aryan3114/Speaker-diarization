from pydub import AudioSegment
import os

# === INPUT & OUTPUT PATHS ===
input_path = r"C:\Users\Aryan\OneDrive\Desktop\drdo\NemoModel\my_audio\TOEFL Listening Practice Test.mp3"
output_path = r"C:\Users\Aryan\OneDrive\Desktop\drdo\NemoModel\my_audio\toefl_mono.wav"

# === CONVERT TO MONO ===
audio = AudioSegment.from_file(input_path)
mono_audio = audio.set_channels(1)

# === EXPORT AS WAV ===
mono_audio.export(output_path, format="wav")

print(f"✅ Converted to mono and saved at:\n{output_path}")
