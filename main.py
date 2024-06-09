import streamlit as st
import streamlit.components.v1 as components
import os
from emotion import GET_EMOTION
from tlabs import transcript, get_transcript
from constants import *
from video import GET_TRIMMED_VIDEO
import moviepy.editor as mp
from st_social_media_links import SocialMediaIcons



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




social_media_links = [
    """
        http://www.facebook.com/dialog/feed?  
        app_id=123050457758183&  
        link=http://developers.facebook.com/docs/reference/dialogs/&
        picture=http://fbrell.com/f8.jpg&  
        name=Facebook%20Dialogs&  
        caption=Reference%20Documentation& 
        description=Dialogs%20provide%20a%20simple,%20consistent%20interface%20for%20applications%20to%20interact%20with%20users.&
        message=text goes here&
        redirect_uri=http://www.example.com/response
    """,
    # "https://www.instagram.com/ThisIsAnExampleLink",
    "http://twitter.com/share?text=text goes here&url=http://url goes here&hashtags=hashtag1,hashtag2,hashtag3",
]

social_media_icons = SocialMediaIcons(social_media_links)
social_media_icons.render()



# Handle the submit button click
if submit_button:
    # Display the entered URL and text
    st.write('Entered URL:', url_input)
    st.write('Entered Text:', text_input)
    idx = video_names.index(selected_option)

    video_id = video_details[idx]["video_id"]

    index_id = os.environ.get("INDEX_ID")

    transcription_list = [1]

    # transcription_list, start_points, end_points = get_transcript(index_id, video_id)

    for i in range(len(transcription_list)):
        # st.write(f"Transcription: {transcription_list[i]}")
        # st.write(f"Start Time: {start_points[i]}")
        # st.write(f"End Time: {end_points[i]}")
        # st.write("")


        video = GET_TRIMMED_VIDEO()

        clip = mp.VideoFileClip("Donut (15-Second Ad).mp4")
        clip.audio.write_audiofile("theaudio.mp3")
        clip.close()

        emotion = GET_EMOTION()

        st.write(f"Emotion: {emotion}")

        video_file = open('Donut (15-Second Ad).mp4', 'rb')
        video_bytes = video_file.read()


        st.text_area("Output", value="omkar", height=200)

        st.write("Generated Highlight:")
        st.video(video_bytes)




    exit()

    transcript(index_id, url_input)