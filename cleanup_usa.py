import os
import shutil

USA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "usa")

if os.path.exists(USA_DIR):
    for root, dirs, files in os.walk(USA_DIR, topdown=False):
        for f in files:
            os.remove(os.path.join(root, f))
        for d in dirs:
            os.rmdir(os.path.join(root, d))
    os.rmdir(USA_DIR)
    print("Successfully deleted legacy usa/ directory.")
else:
    print("usa/ directory does not exist.")
