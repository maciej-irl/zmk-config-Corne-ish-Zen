from pathlib import Path
import tempfile
import subprocess
import sys
import shutil
import time


VOLUME = Path("/Volumes/CORNEISHZEN")


def die(err):
    print(err)
    sys.exit(1)


def move_and_wait(path, msg):
    if input(msg) == "s":
        print("Skipped.")
        return
    while not VOLUME.exists():
        input("Volume not detected. Press enter to try again.")
    shutil.move(path, VOLUME)
    while VOLUME.exists():
        time.sleep(0.33)


def main():
    firmware = Path.home() / "Downloads" / "firmware.zip"
    with tempfile.TemporaryDirectory() as temp:
        subprocess.run(["unzip", "-q", firmware, "-d", temp])
        left_path = Path(temp) / "corneish_zen_left.uf2"
        right_path = Path(temp) / "corneish_zen_right.uf2"
        if not left_path.exists():
            die("Left ut2 file does not exist")
        if not right_path.exists():
            die("Right ut2 file does not exist")
        move_and_wait(left_path, "Plug in left side. Press enter. (s to skip) ")
        move_and_wait(right_path, "Plug in right side. Press enter. (s to skip) ")


if __name__ == "__main__":
    main()
