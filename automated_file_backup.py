import os
import shutil
import datetime
import schedule
import time

source_dir = "F:\\3d-objects\\1\\public\\images"
destination_dir="F:\\3d-objects\1\\chatify-master"

def copy_folder_to_directory(source, destination):
    today = datetime.date.today()
    dest_dir = os.path.join(destination, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {destination}")

schedule.every().day.at("01:14").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)


