import time
from idlelib.run import MyHandler

from shedule_class import FileShedule
from watchdog.observers import Observer

event_handler = FileShedule()
path = r"C:\Alex\PythonProject\PR2\txt"
observer = Observer()
observer.schedule(event_handler, path=path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()