import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("app.py",base=base, icon ="ngan.ico")]

setup(
    name = "ngan",
    version = "0.1",
    description = "My app!",
    options = {"build_exe": {"packages": ["tkinter","PIL","pygame"],"include_files":[
        "ngan.ico","chao.ogg","giangsinh_1.ogg","dep.ogg","thi.ogg","yeu.ogg"
    ]}},
    executables = executables
)