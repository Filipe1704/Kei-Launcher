import ctypes
import sys
import os

def is_admin():
    if os.name == 'nt':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except Exception:
            return False
            
    return True

def run_admin():
    if os.name == 'nt':
        executable = sys.executable
        if executable.lower().endswith(("python.exe", "pythonw.exe")):
            params = " ".join([f'"{arg}"' for arg in sys.argv])
        else:
            params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
            
        try:
            res = ctypes.windll.shell32.ShellExecuteW(None, "runas", executable, params, None, 1)
            return res > 32
        except Exception:
            return False
            
    print("Admin not supported, or no need.")
    return False
