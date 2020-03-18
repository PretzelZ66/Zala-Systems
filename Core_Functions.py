#0.0.0.2
import time, random

def pause(number):
    """Pauses the program for a given number of time."""
    time.sleep(number)


def line(text):
    """Prints a line of text, then  pauses the program for 1 second."""
    print(text)
    pause(1)


def custom_line(text, number):
    """Prints a line of text, then pauses the program for a given number of time."""
    print(text)
    pause(number)


def ask():
    """Asks the user a question, then puts it into a variable."""
    query = input(">>> ")
    return  query