from twelvelabs import TwelveLabs
from twelvelabs.models.task import Task
import time
import os
from openai import OpenAI
from dotenv import load_dotenv
import re
from moviepy.editor import VideoFileClip, concatenate_videoclips
from pytube import YouTube

# Generate Transcript from Video
def generate_transcript(index_id, video_id):
    load_dotenv()
    value = os.getenv('TLABS')
    client = TwelveLabs(api_key=value)

    # Generate Transcripts
    transcriptions = client.index.video.transcription(
        index_id=index_id,
        id=video_id
    )

    # Define the file path
    file_path = "transcriptions.txt"
    transcript_string = ""

    # Check if the file exists and delete it if it does
    if os.path.exists(file_path):
        os.remove(file_path)

    # Open the file in write mode and write the transcriptions
    with open(file_path, "w") as file:
        time_per_segment = 0
        for transcription in transcriptions:
            flag = False
            start_time = transcription.start
            end_time = transcription.end
            if(end_time - start_time >= 5):
                file.write(
                    f"{transcription.value} start={start_time} end={transcription.end}\n"
                )
                transcript_string += f"{transcription.value} start={start_time} end={transcription.end}\n"
            else:
                time_per_segment += (end_time - start_time)
                file.write(
                    f"{transcription.value} "
                )
                transcript_string += f"{transcription.value} "
                if time_per_segment >= 5:
                    flag = True
                    file.write(f" start={(transcription.end - time_per_segment): .2f} end={transcription.end}\n")
                    transcript_string += f" start={(transcription.end - time_per_segment): .2f} end={transcription.end}\n"
                    time_per_segment = 0
        if flag == False:
            file.write(f" start={(transcription.end - time_per_segment): .2f} end={transcription.end}\n")
            transcript_string += f" start={(transcription.end - time_per_segment): .2f} end={transcription.end}\n"
    return transcript_string


# Function to filter transcript for relevant content from ChatGPT
def get_summary_and_title_from_gpt(question, transcript, video_title):
    load_dotenv()
    value = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=value)

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
            {"role": "system", "content": "You are the best sports editor who understands all sports very intricately. You are capable of summarizing sports interviews. You write newspaper articles and give very catchy titles to them."},
            {"role": "user", "content": f"Give a catchy title and news article in the following format. <b>TITLE: <title></b>\n <article> for a press conference excerpt about {video_title} which answer the question: {question}. The news excerpt is: {transcript}. Separate the paragrpahs in the article with <p> tags. The format is <p align='justify'> Paragraph <p>. Strictly limit your article to two paragraphs only."},
        ]
    )
    
    return completion.choices[0].message.content

# def get_summary_and_title_from_gpt(question, transcript, video_title):
#     load_dotenv()
#     import streamlit as st
#     value = os.getenv('OPENAI_API_KEY')
#     client = OpenAI(api_key=value)

#     completion = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#             {"role": "system", "content": "You are the best sports editor who understands all sports very intricately. You are capable of summarizing sports interviews. You write newspaper articles and give very catchy titles to them."},
#             {"role": "user", "content": f"Give a catchy title and news article in the following format. <b>TITLE: <title></b>\n <article> for a press conference excerpt about {video_title} which answer the question: {question}. The news excerpt is: {transcript}. Separate the paragrpahs in the article with <p> tags. The format is <p align='justify'> Paragraph <p>. Strictly limit your article to two paragraphs only."},
#         ],
#         stream=True,
#     )

#     response = st.write_stream(completion)
    

#     return response
    
    # return completion.choices[0].message.content


def get_text_from_gpt(question, transcript):
    load_dotenv()
    value = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=value)

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are the best sports editor who understands all sports very intricately. You are capable of summarizing text by picking the right sentences from a list of sentences of interviews. You pick sentences so that the resultant block answers the question asked. You will be given a transcript containing a list of sentences followed by the start time (start=) and end time (end=) of when it occurs in a video. For a selected sentence, also check whether the next sentence in combination with current selected sentence adds more value and context to the answer. If yes, pick both individually."},
        {"role": "system", "content": "Your output should be in this format: <Sentence> | start= | end=. Just give answer."},
        {"role": "user", "content": f'''{question}
        {transcript}'''}
        ]
    )
    
    return completion.choices[0].message.content




# Functions to parse from generated GPT content
def extract_numbers(string):
    # Define the regex pattern to match numbers (including decimals)
    pattern = r'\d+\.\d+|\d+'
    
    # Use re.findall() to find all numbers in the string
    numbers = re.findall(pattern, string)
    
    # Convert the extracted numbers from strings to floats or integers
    numbers = [float(num) if '.' in num else int(num) for num in numbers]
    
    return numbers


def merge_intervals(intervals):
    # First, sort the intervals by the starting time
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    
    merged = []
    for interval in intervals:
        # If the merged list is empty or if the current interval does not overlap with the last merged interval, add it to the merged list

        if not merged or int(merged[-1][1]) != int(interval[0]):
            merged.append(interval)
        else:
            # Otherwise, there is an overlap, so we merge the current and previous intervals
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged


def get_intervals(texts):
    texts = texts.strip()

    list_texts = texts.split("\n")
    intervals = []
    for text in list_texts:
        split_texts = text.split("|")

        intervals.append([extract_numbers(split_texts[1])[0], extract_numbers(split_texts[2])[0]])
    intervals = sorted(intervals, key=lambda x: x[0])

    return merge_intervals(intervals)


# def get_clippings_from_intervals(intervals):
#     # Load and extract the subclips
#     clip1 = VideoFileClip("Video.mp4").subclip(19.1, 28.46)
#     clip2 = VideoFileClip("Video.mp4").subclip(69.1, 99.58)

#     # Combine the clips
#     final_clip = concatenate_videoclips([clip1, clip2])

#     # Save the new video file
#     final_clip.write_videofile("__combined_video.mp4")

def download_youtube_video(url, filename):
    yt = YouTube(url)
    ys = yt.streams.filter(file_extension='mp4').first()
    ys.download(filename=filename)

def get_clippings_from_intervals(url, intervals):
    # Download YouTube videos
    download_youtube_video(url, "vid1.mp4")

    clip_list = []
    for interval in intervals:
        clip_list.append(VideoFileClip("vid1.mp4").subclip(interval[0], interval[1]))

    # Combine the clips
    final_clip = concatenate_videoclips(clip_list)

    # Save the new video file
    final_clip.write_videofile("combined_video.mp4")
    return final_clip