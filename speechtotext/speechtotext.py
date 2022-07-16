# ------------------------------------------
# this file covers the main script procedure
# ------------------------------------------
from services.recording_service import get_user_recordings

recordings = get_user_recordings("968949c6b97f721219c6")

for r in recordings:
    print(r.id)
    #print(r.recording)