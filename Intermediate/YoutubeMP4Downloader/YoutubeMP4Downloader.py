from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy.editor import VideoFileClip, AudioFileClip
import subprocess
import os

def download_video(url):

    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True, resolution='1080p').first()
    audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()

    video_stream.download(filename='video.mp4')
    audio_stream.download(filename='audio.mp4')

    print("Your video has been downloaded sucessfully, merging audio and video now!")

    merge(yt.title)

    print("Merge sucessful, cleaning up files now.")

    os.remove('audio.mp4')
    os.remove('video.mp4')

    print("Done!")

def merge(title,output_path):
    subprocess.run(['ffmpeg',
    '-i', 'video.mp4',
    '-i', 'audio.mp4',
    '-c:v', 'copy',
    '-c:a', 'aac',
    '-strict', 'experimental',
    f'{title}.mp4',
    str(output_path)
    ])

def main():
    url = input("Please enter the url you would like to download: ")
    save = input("Please enter the path you would like the video to be downloaded to: ")
    download_video(url, save)

main()



