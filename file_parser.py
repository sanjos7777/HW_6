import sys
from pathlib import Path

IMAGES = []
AUDIO = []
DOCUMENTS = []
VIDEO = []
OTHER = []
ARCHIVES = []

REGISTER_EXTENSION = {
    'JPEG': IMAGES,
    'JPG': IMAGES,
    'PNG': IMAGES,
    'SVG': IMAGES,
    'MP3': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,
    'OGG': AUDIO,
    'DOC' : DOCUMENTS,
    'DOCX' : DOCUMENTS,
    'TXT' : DOCUMENTS,
    'PDF' : DOCUMENTS,
    'XLSX' : DOCUMENTS,
    'PPTX' : DOCUMENTS,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'MKV': VIDEO,

}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()  # suffix[1:] -> .jpg -> jpg

def scan(folder: Path):
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():  # перевіряємо чи обєкт папка
            print("iteName ", item.name)
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue
        # Робота з файлом
        extension = get_extension(item.name)  # беремо розширення файлу
        print("fileName ", item.name)
        full_name = folder / item.name  # беремо повний шлях до файлу
        if not extension:
            OTHER.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTENSION[extension]
                ext_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)  
                OTHER.append(full_name)

if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))

    print(f'Folders: {FOLDERS}')
    print(f'Images: {IMAGES}')
    print(f'Video: {VIDEO}')
    print(f'Documents: {DOCUMENTS}')
    print(f'AUDIO: {AUDIO}')
    print(f'Archives zip: {ARCHIVES}')

    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')



