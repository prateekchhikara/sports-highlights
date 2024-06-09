from twelvelabs import TwelveLabs
from twelvelabs.models.task import Task
import os

api_key = os.environ.get("TLABS")


client = TwelveLabs(api_key = api_key)

def upload_video(index_id, video_url, transcription_url=None):
    print("INSIDE UPLOAD VIDEO FUNCTION")
    task = client.task.external_provider(
        index_id = index_id,
        url = video_url
        )
    
    print(f"Task id={task.id}")

    return task.id


def get_transcript(index_id, video_id):
    print("INSIDE GET TRANSCRIPT FUNCTION")
    transcriptions = client.index.video.transcription(
        index_id = index_id,
        id = video_id
    )

    transcription_list = []
    start_points = []
    end_points = []

    for transcription in transcriptions:
        print(
            f"value={transcription.value} start={transcription.start} end={transcription.end}"
        )

        transcription_list.append(transcription.value)
        start_points.append(transcription.start)
        end_points.append(transcription.end)

    return transcription_list, start_points, end_points


def transcript(index_id, video_url):
    print("INSIDE TRANSCRIPT FUNCTION")
    # video_id = upload_video(index_id, video_url)

    transcription_list, start_points, end_points = get_transcript(index_id, video_id=None)


