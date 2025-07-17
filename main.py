import os
import json
import torch
from nemo.collections.asr.models import ClusteringDiarizer
from omegaconf import OmegaConf

def main():
    # ========== PATH SETUP ==========
    audio_path = "my_audio/toefl_mono.wav"
    audio_basename = os.path.basename(audio_path).replace(".wav", "")
    manifest_path = "manifest.json"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # ========== CREATE MANIFEST ==========
    with open(manifest_path, "w") as f:
        f.write(json.dumps({
            "audio_filepath": audio_path,
            "offset": 0,
            "duration": None,
            "label": "infer",
            "text": "NA",
            "num_speakers": None,
            "rttm_filepath": None,
            "uem_filepath": None
        }) + "\n")

    # ========== FULL CONFIG ==========
    cfg = OmegaConf.create({
        "name": "ClusterDiarizer",
        "num_workers": 0,  # ✅ Prevent multiprocessing issues on Windows
        "sample_rate": 16000,
        "batch_size": 64,
        "device": None,
        "verbose": True,

        "diarizer": {
            "manifest_filepath": manifest_path,
            "out_dir": output_dir,
            "oracle_vad": False,
            "collar": 0.25,
            "ignore_overlap": True,

            "vad": {
                "model_path": "vad_multilingual_marblenet",
                "external_vad_manifest": None,
                "parameters": {
                    "window_length_in_sec": 0.63,
                    "shift_length_in_sec": 0.08,
                    "smoothing": False,
                    "overlap": 0.5,
                    "onset": 0.5,
                    "offset": 0.3,
                    "pad_onset": 0.2,
                    "pad_offset": 0.2,
                    "min_duration_on": 0.5,
                    "min_duration_off": 0.5,
                    "filter_speech_first": True,
                }
            },

            "speaker_embeddings": {
                "model_path": "titanet_large",
                "parameters": {
                    "window_length_in_sec": [1.9, 1.2, 0.5],
                    "shift_length_in_sec": [0.95, 0.6, 0.25],
                    "multiscale_weights": [1, 1, 1],
                    "save_embeddings": True,
                }
            },

            "clustering": {
                "parameters": {
                    "oracle_num_speakers": False,
                    "max_num_speakers": 8,
                    "enhanced_count_thres": 80,
                    "max_rp_threshold": 0.25,
                    "sparse_search_volume": 10,
                    "maj_vote_spk_count": False,
                }
            },

            "msdd_model": {
                "model_path": None,
                "parameters": {
                    "use_speaker_model_from_ckpt": True,
                    "infer_batch_size": 25,
                    "sigmoid_threshold": [0.7],
                    "seq_eval_mode": False,
                    "split_infer": True,
                    "diar_window_length": 50,
                    "overlap_infer_spk_limit": 5,
                }
            },

            "asr": {
                "model_path": None,
                "parameters": {
                    "asr_based_vad": False,
                    "asr_based_vad_threshold": 1.0,
                    "asr_batch_size": None,
                    "decoder_delay_in_sec": None,
                    "word_ts_anchor_offset": None,
                    "word_ts_anchor_pos": "start",
                    "fix_word_ts_with_VAD": False,
                    "colored_text": False,
                    "print_time": True,
                    "break_lines": False,
                },
                "ctc_decoder_parameters": {
                    "pretrained_language_model": None,
                    "beam_width": 32,
                    "alpha": 0.5,
                    "beta": 2.5,
                },
                "realigning_lm_parameters": {
                    "arpa_language_model": None,
                    "min_number_of_words": 3,
                    "max_number_of_words": 10,
                    "logprob_diff_threshold": 1.2,
                }
            }
        }
    })

    # ========== RUN DIARIZATION ==========
    print("\n🚀 Running Clustering Diarizer...")
    model = ClusteringDiarizer(cfg=cfg)
    model.diarize()
    print("✅ Diarization complete!")

    # ========== PARSE RTTM ==========
    rttm_path = os.path.join(output_dir,"pred_rttms", f"{audio_basename}.rttm")
    if os.path.exists(rttm_path):
        print("\n🧠 Speaker Segments Timeline:\n")
        with open(rttm_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                start = float(parts[3])
                duration = float(parts[4])
                speaker = parts[7]
                print(f"🕒 {start:.2f}s - {start+duration:.2f}s → {speaker}")
    else:
        print(f"❌ RTTM not found at {rttm_path}")


if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # ✅ Windows compatibility
    main()
