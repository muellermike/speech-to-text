from datalayer.recording_datalayer import load_recordings_by_user

def get_user_recordings(user_id):
    """
    load all recordings from the storage
    """
    return load_recordings_by_user(user_id)