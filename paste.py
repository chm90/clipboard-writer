from pyautogui import press, typewrite, hotkey
import time
import clipboard
from argparse import ArgumentParser

parser = ArgumentParser(description="Writes text from clipboard to any input source")
parser.add_argument("--time-delay","-t",type=int,help="The number of seconds before the clipboard is written out")
args = parser.parse_args()
text = clipboard.paste()

time.sleep(args.time_delay)
typewrite(text)
