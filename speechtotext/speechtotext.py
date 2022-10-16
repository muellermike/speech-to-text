# ------------------------------------------
# this file covers the main script procedure
# ------------------------------------------
from services.recording_service import get_user_recordings, transcript_recordings, store_transcripts
import csv, sys

# get first argument as input filename
inFile = sys.argv[1]

with open(inFile, newline='') as csvfile:
    userreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in userreader:
        print("---------------------")
        print("START")
        print("---------------------")
        print(row[0])
        recordings = get_user_recordings(row[0])
        for r in recordings:
            print(r.user_id)
            print(r.experiment_id)
            print(r.exercise_id)
        print("start transcription")
        transcript_recordings(recordings)
        print("end transcription")
        print("start storing")
        store_transcripts(recordings)
        print("end storing")

        print("---------------------")
        print("END")
        print("---------------------")

