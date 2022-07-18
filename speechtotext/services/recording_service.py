from datalayer.recording_datalayer import load_recordings_by_user, store_transcript, store_recording_to_file
from models.recording import Recording
import speech_recognition as sr

def get_user_recordings(user_id):
    """
    load all recordings from the storage
    """
    return load_recordings_by_user(user_id)

def transcript_recordings(recordings: list[Recording]):
    recognizer = sr.Recognizer()

    for r in recordings:
        filename = str(r.user_id) + "_" + str(r.experiment_id) + "_" + str(r.exercise_id) + "_" + str(r.id) + ".wav"
        
        store_recording_to_file(filename, r.recording)
        
        with sr.AudioFile("output/wavs/" + filename) as source:
            # listen for the data (load audio to memory)
            audio_data = recognizer.record(source)
            # recognize (convert from speech to text)
            try:
                text = recognizer.recognize_google(audio_data)
            except sr.UnknownValueError:
                text = ""
            
            print(text)
            r.transcript = text

    return True

def store_transcripts(recordings: list[Recording]):
    """
    store all transcripts into the database
    """
    for r in recordings:
        store_transcript(r.transcript, r.id)
    
    return True