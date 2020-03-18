#0.0.0.5
import Core_Functions as cf


class Error:
    one = "ERROR ONE: ACCESS DENIED"


#System Block
password = "zalasystems2020"
cf.line("Please enter a name.")
username = input(">>> ")
cf.line(f"So your name is {username}?")
confirm = input("Y/N>>> ")
while confirm.lower() == "n":
    cf.line("Please enter a name.")
    username = input(">>> ")
    cf.line(f"So your name is {username}?")

#Introduction and Entry Block
cf.line(f"Welcome, {username}!")
cf.line("Please enter the current password")
access = input(">>> ")
while access != password:
    cf.line(Error.one)
    cf.line("Please enter the current password")
    access = input(">>> ")
cf.line(f"Welcome, {username}, to Zala Systems.")
cf.custom_line("LOADING...", 0.25)
cf.line("Loaded")