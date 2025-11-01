# You Can't Fake The Voice

This task demonstrates voice cloning using the [TTS](https://github.com/coqui-ai/TTS) library. The goal is to generate a `passphrase.mp3` audio file that matches the voice characteristics of provided sample MP3 files.

## Task Description
- You are given several sample audio files in `videos/` (sample-1.mp3 to sample-5.mp3).
- The passphrase to synthesize is in `passphrase.txt`.
- The script uses all sample audios to clone the voice and generate `passphrase.mp3`.

## Requirements
- Python 3.9, 3.10, or 3.11 (tested on 3.10)
- [TTS library (Coqui-AI)](https://github.com/coqui-ai/TTS)
- Other dependencies: numpy, torch, etc. (see TTS documentation)

## Setup
1. (Recommended) Create a virtual environment:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   ```
2. Install TTS and dependencies:
   ```bash
   pip install TTS
   ```

## Usage
1. Place your sample MP3 files in the `videos/` folder.
2. Ensure your passphrase is in `passphrase.txt`.
3. Run the script:
   ```bash
   python main.py
   ```
4. The generated audio will be saved as `passphrase.mp3` in the same folder.

## Notes
- The script will attempt to use all sample audios for voice cloning. If the model does not support multiple samples, it will try each sample individually.
- If voice cloning fails, the script will fall back to the default TTS voice.
- For best results, use a GPU and a supported TTS model (e.g., `your_tts`).

## Troubleshooting
- If you encounter errors about missing `language` or `speaker`, ensure the script and TTS model are compatible and that you are using Python 3.9–3.11.
- For more details, see the [TTS documentation](https://github.com/coqui-ai/TTS).
