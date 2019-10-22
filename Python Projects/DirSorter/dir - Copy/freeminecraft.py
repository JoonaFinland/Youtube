import time
import random
import os

def open_cmd(how_long_in_seconds):
    start_time = time.time()
    time_elapsed = time.time() - start_time
    while time_elapsed < how_long_in_seconds:
        os.system('start cmd')
        time_elapsed = time.time() - start_time
if __name__ == "__main__":
    open_cmd(10)