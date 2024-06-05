import psutil, win32process, win32gui
from pathlib import Path

def get_forground_process_name() -> str:
    foreground_window = win32gui.GetForegroundWindow()
    pid = win32process.GetWindowThreadProcessId(foreground_window)
    process_id = pid[-1]

    return Path(psutil.Process(process_id).name()).stem

def move_file(old: Path, new: Path) -> None:
    if (not new.parent.exists()):
        new.parent.mkdir(parents=True, exist_ok=True)
    
    old.rename(new)
