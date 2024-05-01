from TTS.api import TTS

# class model_load:
#     tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
    
def converter(text):
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
    tts.tts_to_file(text=text,
                file_path="Backend/summaraize_app/audio_convert/temp_files/output_audio.mp4",
                speaker_wav="Backend\\summaraize_app\\audio_convert\\reference_voice.wav",
                language="en")
    return True

converter("hi how are you?")