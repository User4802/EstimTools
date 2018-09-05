version = "v0.1"

def carpet_calc():
    print("carpet")

def vinyl_calc():
    print("vinyl")

def print_info():
    print("info")
    input("Press any key to return")
    main_input()

def exit():
    choice = input("Are you sure you want to quit ? y/n ?   ")
    if choice == "y":
        print("Terminated")
    elif choice == "n":
        main_input()
    else:
        print("Invalid input, returning to main menu")
        main_input()

def chooser(mats):
    if mats == "carpet":
        carpet_calc()
    elif mats == "vinyl":
        vinyl_calc()
    elif mats == "info":
        print_info()
    elif mats == "exit":
        exit()
    else:
        print("invalid input")
        main_input()

print("""

WallBase Solver Version : {0}
At Any time enter : info for instruction or exit to quit

""".format(version))

def main_input():
    mats = input("Enter the material type \n    ")
    chooser(mats)

main_input()
