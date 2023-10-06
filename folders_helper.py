from pathlib import Path
import threading


def move_file(file_path):
    ext = file_path.suffix
    target_dir = source / ext[1:]
    target_dir.mkdir(parents=True, exist_ok=True)
    file_path.rename(target_dir / file_path.name)


def process_folder(folder):
    for item in folder.iterdir():
        if item.is_file():
            move_file(item)
        elif item.is_dir():
            process_folder(item)


if __name__ == '__main__':
    source = Path('////')
    thread = threading.Thread(target=process_folder, args=(source,))
    thread.start()
    thread.join()

# from pathlib import Path
# import threading
#
#
# def move_file(file_path):
#     ext = file_path.suffix
#     ext_folder = Path.cwd() / ext[1:]
#     ext_folder.mkdir(parents=True, exist_ok=True)
#     new_path = ext_folder / file_path.name
#     file_path.rename(new_path)
#     print(f"Файл {file_path.name} перемещен в {ext_folder}")
#
#
# def process_directory(dir_path):
#     files = [f for f in dir_path.iterdir() if f.is_file()]
#     for file in files:
#         threading.Thread(target=move_file, args=(file,)).start()
#
#     subdirs = [d for d in dir_path.iterdir() if d.is_dir()]
#     for subdir in subdirs:
#         process_directory(subdir)
#
#
# if __name__ == "__main__":
#     target_directory = Path('//////')
#     process_directory(target_directory)
