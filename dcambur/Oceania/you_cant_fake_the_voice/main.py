import os
from TTS.api import TTS

# Paths to all sample audios
sample_audio_paths = [
    "videos/sample-1.mp3",
    "videos/sample-2.mp3",
    "videos/sample-3.mp3",
    "videos/sample-4.mp3",
    "videos/sample-5.mp3"
]
# Path to the passphrase text
passphrase_path = "passphrase.txt"
# Output path for the generated audio
output_audio_path = "passphrase.mp3"

# Read the passphrase
with open(passphrase_path, "r") as f:
    passphrase = f.read().strip()


# Get available models as a list of names
tts = TTS()
model_manager = tts.list_models()
if hasattr(model_manager, 'list'):
    available_models = model_manager.list()
elif hasattr(model_manager, 'keys'):
    available_models = list(model_manager.keys())
else:
    print("Unknown ModelManager structure, available attributes:", dir(model_manager))
    available_models = []

print("Available models:", available_models)
# Pick a multi-speaker or voice cloning model (e.g., "tts_models/multilingual/multi-dataset/your_tts")
model_name = None
for m in available_models:
    if "your_tts" in m or "vits" in m or "voice" in m:
        model_name = m
        break
if model_name is None and available_models:
    model_name = available_models[0]  # fallback
elif model_name is None:
    model_name = "tts_models/multilingual/multi-dataset/your_tts"  # hardcoded fallback

# Initialize TTS
tts = TTS(model_name)


# Synthesize using voice cloning from the sample audio
# (If the model does not support voice cloning, it will use the default speaker)
try:
    # Try passing all samples if supported, else try each one
    try:
        tts.tts_to_file(
            text=passphrase,
            speaker_wav=sample_audio_paths,
            language='en',
            file_path=output_audio_path
        )
        print(f"Generated {output_audio_path} using voice cloning from all samples.")
    except Exception as e2:
        print(f"Voice cloning with all samples failed: {e2}\nTrying each sample individually.")
        success = False
        for sample_audio_path in sample_audio_paths:
            try:
                tts.tts_to_file(
                    text=passphrase,
                    speaker_wav=sample_audio_path,
                    language='en',
                    file_path=output_audio_path
                )
                print(f"Generated {output_audio_path} using voice cloning from {sample_audio_path}.")
                success = True
                break
            except Exception as e3:
                print(f"Voice cloning failed for {sample_audio_path}: {e3}")
        if not success:
            raise RuntimeError("Voice cloning failed for all samples.")
except Exception as e:
    print(f"Voice cloning failed: {e}\nFalling back to default speaker.")
    # Try to get a default speaker if required
    speaker = None
    if hasattr(tts, 'speakers') and tts.speakers:
        speaker = tts.speakers[0]
    try:
        tts.tts_to_file(
            text=passphrase,
            language='en',
            speaker=speaker,
            file_path=output_audio_path
        )
        print(f"Generated {output_audio_path} using default TTS voice.")
    except Exception as e2:
        print(f"Default TTS voice failed: {e2}")
