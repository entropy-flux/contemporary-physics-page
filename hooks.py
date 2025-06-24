import shutil
import os


def copy_folder(*args, **kwargs):
    src = os.path.abspath("stylesheets")
    dest = os.path.abspath("contemporary-physics/stylesheets")
     
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def cleanup_folder(*args, **kwargs):
    dest = os.path.abspath("contemporary-physics/stylesheets")
    
    if os.path.exists(dest):
        shutil.rmtree(dest)
        print(f"Cleaned up: {dest}")