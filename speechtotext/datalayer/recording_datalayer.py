from datalayer.db import execute
from models.recording import Recording
import gc
from base64 import b64decode
import moviepy.editor as moviepy

def load_recordings_by_user(user_id):
    """
    Load entire recording data from the database
    """
    sql = "SELECT r.`PK`, r.`TimeToRecording`, r.`Transcript`, r.`Value`, r.`RecordingString`, u.ID as UserID, ee.ExerciseFK, ee.ExperimentFK FROM `Recording` r JOIN ExperimentExercise ee ON ee.RecordingFK = r.PK JOIN Experiment e ON e.PK = ee.ExperimentFK JOIN User u ON u.PK = e.UserFK WHERE u.ID = %s"

    result = execute(sql, (user_id), "SELECT")

    out_list = make_list(result)
    del result
    gc.collect()

    return out_list

def store_transcript(transcript: str, recording_id):
    """
    store the transcript of one specific recording
    """
    sql = "UPDATE Recording SET Transcript = %s WHERE PK = %s"

    result = execute(sql, (transcript, recording_id), "UPDATE")

    return result

def store_recording_to_file(filename: str, recordingString: str):
    """
    store the recording to a file with the filename
    """
    wav_file = open("speechtotext/output/wavs/" + filename, "wb")
    decode_string = b64decode(recordingString.split(",")[1])
    wav_file.write(decode_string)

    #moviepy.ffmpeg_tools.ffmpeg_extract_audio("output/wavs/temp.webm", "output/wavs/" + filename)
    return True

def make_list(recordings):
	def apply(x):
		return Recording(x["PK"], x["TimeToRecording"], x["Transcript"], x["Value"], x["RecordingString"], x["ExperimentFK"], x["UserID"], x["ExerciseFK"])

	return list(map(apply, recordings))