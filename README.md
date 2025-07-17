# Speaker-diarization using (MSDD+TITANET)
Speaker diarization is the process of segmenting an audio stream by speaker identity, answering the question: "Who spoke when?".
This project uses NVIDIA NeMo framework with TitaNet embeddings and MSDD (Multi-Scale Diarization Decoder) for state-of-the-art diarization.

✅ Features
Detects speaker boundaries in audio.
Supports 16kHz mono WAV files.
Uses TitaNet for speaker embeddings.
Uses MSDD for diarization inference.
GPU acceleration supported via PyTorch and CUDA.

⚡ Requirements
Python 3.8+
NVIDIA NeMo
PyTorch (with CUDA for GPU)
ffmpeg (for audio processing)
