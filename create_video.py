from moviepy.editor import VideoFileClip, CompositeVideoClip
import random
import os
import datetime
from PIL import Image


def delete_video(video_path):
    try:
        if os.path.exists(video_path):
            os.remove(video_path)
            print(f"O vídeo {video_path} foi deletado com sucesso.")
        else:
            print(f"O arquivo {video_path} não existe.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar deletar o vídeo: {e}")

def create_new_video(videoPath):
    videos_folder = "./src/assets/templates"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    print(videoPath)
    video1_path = videoPath

    video2_path = os.path.join(videos_folder, random.choice(os.listdir(videos_folder)))

    print(video2_path)

    video1 = VideoFileClip(video1_path).resize((1080, 1280))
    video2 = VideoFileClip(video2_path, audio=False).resize((1080, 640))
    
    width, height = video1.size

    video2 = video2.set_position(("center", "bottom"))

    final_video = CompositeVideoClip([video1, video2], size=(width, 1920))

    output_dir = "./src/exported"
    os.makedirs(output_dir, exist_ok=True)

    # Salvar o vídeo final
    video_filename = os.path.splitext(os.path.basename(videoPath))[0]
    output_filename = f"{video_filename}_{current_time}.mp4"
    
    output_path = os.path.join(output_dir, output_filename)
    final_video.write_videofile(output_path, codec="libx264")
    delete_video(videoPath)
