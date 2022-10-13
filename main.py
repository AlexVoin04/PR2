from shedule_class import FileShedule
from watchdog.observers import Observer

try:
    while True:
        print("Введите слово: ")
        true: bool = True
        slovo: str = input()
        if slovo.isalpha() and len(slovo) > 3:
            file = f"C:\\Alex\\PythonProject\\PR2\\txt\\{slovo}.txt"
            with open(file, "w"):
                print("Файл создан")
        else:
            print("Введите другое слово:")
except Exception:
    print("Что-то пошло не так ...")
except KeyboardInterrupt:
    print("Завершение")