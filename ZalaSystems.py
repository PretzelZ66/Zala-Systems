#0.0.0.12
import Core_Functions as cf


class Error:
    one = "ERROR ONE: ACCESS DENIED"
    two = "ERROR TWO: UNRECOGNISED COMMAND"
    three = "ERROR THREE: PASSWORDS DO NOT MATCH"


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

#Main Loop
while True:
    cf.line("Current menus: System")
    cf.line("Which menu would you like to open?")
    command = cf.ask()

    #System Block
    if command.lower() == "system":
        cf.line("Current system options: Change password, Exit")
        cf.line("Which option would you like to access?")
        option = cf.ask()

        #Password Alterations
        if option.lower() == "change password":
            cf.line("Would you like to change the password?")
            confirmation = cf.yn_ask()

            if confirmation.lower() == "y":
                cf.line("Please enter the current password")
                access = cf.ask()

                while access != password:
                    cf.line(Error.one)
                    cf.line("Please enter the current password")
                    access = cf.ask()

                cf.line("Please enter the new password")
                password = cf.ask()
                cf.line("Please confirm the new password")
                confirm_password = cf.ask()

                while confirm_password != password:
                    cf.line(Error.three)
                    cf.line("Please confirm the new password")
                    confirm_password = cf.ask()

                cf.line("Password Updated!")
                cf.line(f"The new password is {password}!")

        #Exit block
        elif option.lower() == "exit":
            cf.line("Are you sure?")
            confirm = cf.yn_ask()

            if confirm.lower() == "y":
                break

        else:
            cf.line(Error.two)

    else:
        cf.line(Error.two)