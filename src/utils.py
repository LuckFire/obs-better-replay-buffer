import psutil, win32process, win32gui
from pathlib import Path
from json import load
from os import getcwd

def get_folder_name(fromName: str) -> str:
    '''
    Get a folder name based on a process name.
    This helps make them more coherent. ShadowPlay also does something similar to this.
    '''

    file = open(Path.joinpath(Path(__file__).parent, './override_folder_names.json'))
    override_names = load(file)

    if (override_names[fromName]):
        return override_names[fromName]

    return fromName

def get_forground_process_name() -> str:
    '''Get the currently selectoed window's process name.'''
    
    foreground_window = win32gui.GetForegroundWindow()
    pid = win32process.GetWindowThreadProcessId(foreground_window)
    process_id = pid[-1]

    return Path(psutil.Process(process_id).name()).stem

def move_file(old: Path, new: Path) -> None:
    '''Move the file to a different path.'''

    if (not new.parent.exists()):
        new.parent.mkdir(parents=True, exist_ok=True)
    
    old.rename(new)