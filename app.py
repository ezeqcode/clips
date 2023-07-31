import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from create_video import create_new_video

def handle_video(videoPath):
    create_new_video(videoPath)

class PastaMonitorHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            video_path = event.src_path
            handle_video(video_path)

def monitorar_pasta(pasta):
    print('Monitorando')
    event_handler = PastaMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path=pasta, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    pasta_monitorada = "./src/assets/videos"  

    
    thread_monitorar = threading.Thread(target=monitorar_pasta, args=(pasta_monitorada,))
    thread_monitorar.daemon = True  # A thread será finalizada automaticamente quando o programa principal encerrar
    thread_monitorar.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break


    print("Aplicação encerrada.")
   
   

   