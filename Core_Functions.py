#0.0.0.0
import time, random

def pause(number):
    """Pauses the program for a given number of time."""
    time.sleep(number)


def line(text):
    """Prints a line of text, then  pauses the program for 1 second."""
    print(text)
    pause(1)