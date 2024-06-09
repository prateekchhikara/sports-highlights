import streamlit as st
import streamlit.components.v1 as components
import os
from emotion import GET_EMOTION
from backend import generate_transcript, get_intervals, get_text_from_gpt, get_clippings_from_intervals, get_summary_and_title_from_gpt
# from tlabs import transcript, get_transcript
from constants import *
from video import GET_TRIMMED_VIDEO
import moviepy.editor as mp
from st_social_media_links import SocialMediaIcons
from feedback import FEEDBACK



def centered_spinner(text):
    text_placeholder = st.empty()
    return text_placeholder.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
            <div>
                <h2 style="text-align: center;">{text}</h2>
                <div style="display: flex; justify-content: center;">
                    <div class="loader"></div>
                </div>
            </div>
        </div>
        <style>
            .loader {{
                border: 8px solid #f3f3f3; /* Light grey */
                border-top: 8px solid #3498db; /* Blue */
                border-radius: 50%;
                width: 50px;
                height: 50px;
                animation: spin 2s linear infinite;
            }}
            @keyframes spin {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )



st.set_page_config(page_title="AISP", page_icon="🏀")


# Set the title of the Streamlit app
st.title('AI Sports Recap')

# Create a text input field for the URL
url_input = st.text_input('Enter a URL:', '')
st.write('OR')
selected_option = st.selectbox('Select an option:', video_names)

# Create a text area for additional text input
text_input = st.text_area('Enter Your Question:')

# Create a submit button
submit_button = st.button('Submit')




st.write(" ")
st.write(" ")

FEEDBACK()


# Handle the submit button click
if submit_button:
    load_circle = centered_spinner('Please wait... 🕰️👀')
    idx = video_names.index(selected_option)

    video_id = video_details[idx]["video_id"]

    index_id = os.environ.get("INDEX_ID")

    

    transcript_string = generate_transcript(index_id, video_id)
    gpt_content = get_text_from_gpt(text_input, transcript_string)
    final_clippings = get_intervals(gpt_content)
    clipped_video = get_clippings_from_intervals(video_details[idx]["video_url"], final_clippings)

    summarized_content = get_summary_and_title_from_gpt(text_input, transcript_string, video_details[idx]["video_name"])
    # for i in range(len(transcription_list)):
        # st.write(f"Transcription: {transcription_list[i]}")
        # st.write(f"Start Time: {start_points[i]}")
        # st.write(f"End Time: {end_points[i]}")
        # st.write("")


    # video = GET_TRIMMED_VIDEO()

    # clip = mp.VideoFileClip("Donut (15-Second Ad).mp4")
    # clip.audio.write_audiofile("theaudio.mp3")
    # clip.close()

    clip = mp.VideoFileClip("combined_video.mp4")
    clip.audio.write_audiofile("theaudio.mp3")
    clip.close()

    emotion = GET_EMOTION()

    st.write(f"Emotion: {emotion}")

    
    load_circle.empty()

    video_file = open('combined_video.mp4', 'rb')
    video_bytes = video_file.read()

    # st.text_area("Summary", value=summarized_content, height=200)
    st.markdown(summarized_content, unsafe_allow_html=True)

    st.markdown("<h3>Highlights</h3>", unsafe_allow_html=True)
    st.video(video_bytes)

    


    social_media_links = [
        """
            http://www.facebook.com/dialog/feed?  
            app_id=123050457758183&  
            link=http://developers.facebook.com/&
            caption=Reference%20Documentation& 
            description=Andy Murray Hints at Retirement Possibilities but Stays Focused on the Present  Wimbledon&
            message=Andy Murray Hints at Retirement Possibilities but Stays Focused on the Present  Wimbledon&
        """,
        # "https://www.instagram.com/ThisIsAnExampleLink",
        f"http://twitter.com/share?text={gpt_content}&url=http://url goes here&hashtags=hashtag1,hashtag2,hashtag3",
    ]

    social_media_icons = SocialMediaIcons(social_media_links)
    social_media_icons.render()



exit()

transcript(index_id, url_input)


