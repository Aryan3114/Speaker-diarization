import os
from pydub import AudioSegment
import simpleaudio as sa
from nemo.collections.asr.models import ClusteringDiarizer

# === Step 1: Configuration ===
input_audio_path = "my_audio/84-121123-0000.wav"            
output_rttm_dir = "diarization_outputs"
os.makedirs(output_rttm_dir, exist_ok=True)

# === Step 2: Run diarization using NeMo ===
print(" Running speaker diarization...")
diarizer = ClusteringDiarizer.from_pretrained("diar_msdd_telephonic")
diarizer.diarize(
    paths2audio_files=[input_audio_path],
    output_dir=output_rttm_dir
)
print(" Diarization complete!")

# === Step 3: Parse RTTM and play segments ===
base_name = os.path.splitext(os.path.basename(input_audio_path))[0]
rttm_path = os.path.join(output_rttm_dir, base_name + ".rttm")

if not os.path.exists(rttm_path):
    print(" RTTM file not found. Diarization might have failed.")
    exit()

print(f"\n Parsing RTTM: {rttm_path}")
audio = AudioSegment.from_wav(input_audio_path)

with open(rttm_path, "r") as f:
    for idx, line in enumerate(f):
        parts = line.strip().split()
        if len(parts) >= 8:
            start_time = float(parts[3]) * 1000  # Convert to ms
            duration = float(parts[4]) * 1000
            end_time = start_time + duration
            speaker = parts[7]

            # Slice and play
            segment = audio[start_time:end_time]
            print(f"{start_time/1000:.2f}s --- {end_time/1000:.2f}s : {speaker}")

            play_obj = sa.play_buffer(
                segment.raw_data,
                num_channels=segment.channels,
                bytes_per_sample=segment.sample_width,
                sample_rate=segment.frame_rate
            )
            play_obj.wait_done()
