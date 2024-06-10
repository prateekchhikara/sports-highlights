from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *

from moviepy.config import change_settings
change_settings({"FFMPEG_BINARY": "/usr/bin/ffmpeg"})

clip = VideoFileClip("video.mp4").subclip(69.1, 99.58) 
clip.write_videofile("_testVideo1.mp4")