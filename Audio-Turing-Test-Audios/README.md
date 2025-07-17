---
license: cc-by-nc-4.0
language:
- zh
tags:
- Audio
- Corpus
- mlcroissant
task_categories:
- text-to-speech
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: trap_audio
    path: Trap_Audio/audio-*
dataset_info:
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  download_size: 28587042
  dataset_size: 29982460
---

# 📚 Audio Turing Test Audios

> A high‑quality, multidimensional Chinese audio corpus generated from textual transcripts, designed to evaluate the human-likeness and naturalness of Text-to-Speech (TTS) systems—the “Audio Turing Test.”

## About Audio Turing Test (ATT)

ATT is an evaluation framework featuring a standardized human evaluation protocol and an accompanying dataset, addressing the lack of unified evaluation standards in TTS research. To enhance rapid iteration and evaluation, we trained the Auto-ATT model based on Qwen2-Audio-7B, enabling a model-as-a-judge evaluation on the ATT dataset. Full details and related resources are available in the [ATT Collection](https://huggingface.co/collections/meituan/audio-turing-test-682446320368164faeaf38a4).

## Dataset Description

The dataset includes 104 "trap" audio clips for attentiveness checks during evaluations:

* **35 flawed synthetic audio clips:** intentionally synthesized to highlight obvious flaws and unnaturalness.
* **69 authentic human recordings:** genuine human speech, serving as control samples.

## How to Use This Dataset

1. **Evaluate:** Use our [Auto-ATT evaluation model](https://huggingface.co/Meituan/Auto-ATT) to score your own or existing TTS audio clips.
2. **Benchmark:** Compare your evaluation scores against these reference audio samples from top-performing TTS models described in our research paper and these "trap" audio clips.


## Data Format

Audio files are provided in high-quality `.wav` format.

## Citation

If you use this dataset, please cite:

```
@software{Audio-Turing-Test-Audios,
  author = {Wang, Xihuai and Zhao, Ziyi and Ren, Siyu and Zhang, Shao and Li, Song and Li, Xiaoyu and Wang, Ziwen and Qiu, Lin and Wan, Guanglu and Cao, Xuezhi and Cai, Xunliang and Zhang, Weinan},
  title = {Audio Turing Test: Benchmarking the Human-likeness and Naturalness of Large Language Model-based Text-to-Speech Systems in Chinese},
  year = {2025},
  url = {https://huggingface.co/datasets/Meituan/Audio-Turing-Test-Audios},
  publisher = {huggingface},
}
```