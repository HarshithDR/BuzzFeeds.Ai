from TTS.api import TTS

# class model_load:
#     tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
    
def converter(text):
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
    tts.tts_to_file(text=text,
                file_path="Backend\\audio_convert_and_final_video_generator\\temp_files\\output_audio.mp4",
                speaker_wav="Backend\\audio_convert_and_final_video_generator\\reference_voice.wav",
                language="en")
    return True

# converter("hi how are you?")