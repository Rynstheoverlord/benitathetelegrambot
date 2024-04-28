from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()

    # download the video
    try:
      video.download("", filename="video.mp4")
      return [True, 0]
    except Exception as e:
      return [False, e]

