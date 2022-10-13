from watchdog.events import FileSystemEventHandler

symbols :list = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч','ш', 'щ', 'b', 'l', 'm','n','d','q', 'k', 'p','t','f','h','z','v','j']

class FileShedule(FileSystemEventHandler):
    def on_created(self, event):
        # print(event.event_type, event.src_path)
        file_name: str = event.src_path.split("\\")
        name: str = file_name[-1].split(".")
        name_two: str = name[0]
        name_two.lower()
        for sim in name_two:
            if sim in symbols:
                print(sim.upper())
            else:
                print(sim.lower())