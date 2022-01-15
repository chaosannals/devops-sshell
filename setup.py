import sys
from cx_Freeze import setup, Executable

base = 'Win32GUI' if sys.platform == 'win32' else None

setup(
    name='devops-sshell',
    version='0.1.0',
    options={
        'build_exe': {
            'include_files': [
                'app.ico',
            ],
        },
    },
    executables=[
        Executable(
            'app.py',
            base=base,
            icon='app.ico',
            shortcut_name='DevOps SShell',
            shortcut_dir='DesktopFolder',
        )
    ]
)
