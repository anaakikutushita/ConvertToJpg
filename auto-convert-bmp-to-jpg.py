# -*- coding: utf-8 -*-

import time
import os
from PIL import Image
import numpy as np

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

BASEDIR = os.path.abspath("E:\VideoGames\【キャプチャ映像】")

def get_ext(filename):
    return os.path.splitext(filename)[-1].lower()

class ChangeHandler(FileSystemEventHandler):

    def on_created(self, event):
        time.sleep(1)
        if event.is_directory:
            return
        if get_ext(event.src_path) == '.bmp':
            img_path = event.src_path
            bmp_img = Image.open(img_path)
            resized = bmp_img.resize(
                (round(bmp_img.width / 2), round(bmp_img.height / 2)),
                Image.NEAREST)
            filename = os.path.splitext(event.src_path)[0]
            resized.save(filename + '.jpg')

if __name__ in '__main__':
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler,BASEDIR,recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
