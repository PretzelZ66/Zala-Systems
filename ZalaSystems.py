#0.0.0.2
import time, random

def pause(number):
    """Pauses the program for a given time"""
    time.sleep(number)


def line(text):
    """Prints a line of text, then pauses the program for 1 second"""
    print(text)
    pause(1)


#System Block
password = "zalasystems2020"
line("Please enter a name.")
username = input(">>> ")
line(f"So your name is {username}?")
confirm = input("Y/N>>> ")
while confirm.lower() == "n":
    line("Please enter a name.")
    username = input(">>> ")
    line(f"So your name is {username}?")