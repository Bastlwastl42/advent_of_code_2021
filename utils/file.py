import os
from pathlib import Path
def readin_files(filename: str, folder: Path = Path.cwd()):
    """read data from given file and do default restructions"""

    with open(Path(folder, filename), 'r', encoding='utf-8') as file:
        content = file.readlines()
    return content
