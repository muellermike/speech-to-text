# ------------------------------------------
# this file covers the main script procedure
# ------------------------------------------
import configparser
from services.recording_service import get_user_recordings

recordings = get_user_recordings("968949c6b97f721219c6")
print(recordings)