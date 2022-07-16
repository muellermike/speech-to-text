from datalayer.db import execute

def load_recordings_by_user(user_id):
    """
    Load entire recording data from the database
    """
    sql = "SELECT r.`PK`, r.`StoredTimestamp`, r.`TimeToRecording`, r.`Transcript`, r.`Value`, r.`RecordingString` FROM `Recording` r JOIN ExperimentExercise ee ON ee.RecordingFK = r.PK JOIN Experiment e ON e.PK = ee.ExperimentFK JOIN User u ON u.PK = e.UserFK WHERE u.ID = %s"

    result = execute(sql, (user_id), "SELECT")

    return result

def store_transcript():
    """
    store the transcript of one specific recording
    """
    sql = "UPDATE Recording SET Transcript = %s WHERE PK = %s"

    result = execute(sql, ("test", 621), "UPDATE")

    return result

def store_recording_to_file(filename: str):
    """
    store the recording to a file with the filename
    """
    print(filename)
    return True