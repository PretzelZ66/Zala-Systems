#0.0.0.6
import Core_Functions as cf


class Error:
    one = "ERROR ONE: ACCESS DENIED"


#System Block
password = "zalasystems2020"
cf.line("Please enter a name.")
username = cf.ask()
cf.line(f"So your name is {username}?")
confirm = cf.yn_ask()
while confirm.lower() == "n":
    cf.line("Please enter a name.")
    username = cf.ask()
    cf.line(f"So your name is {username}?")

#Introduction and Entry Block
cf.line(f"Welcome, {username}!")
cf.line("Please enter the current password")
access = cf.ask()
while access != password:
    cf.line(Error.one)
    cf.line("Please enter the current password")
    access = cf.ask()
cf.line(f"Welcome, {username}, to Zala Systems.")
cf.custom_line("LOADING...", 0.25)
cf.line("Loaded")

while True:
    cf.line("Current menus: ")
    cf.line("Which menu would you like to open?")