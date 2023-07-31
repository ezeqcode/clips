from pytube import YouTube 

def download_video(link):
    yt = YouTube(f"{link}")
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    
download_video("https://www.youtube.com/shorts/fonV8rw7h5Q")
    