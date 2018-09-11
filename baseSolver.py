version = "v0.2"

def calc():
    cpt_lenght = float(input("Enter the full lengt needed   "))
    cpt_lenght_unit = input("Enter the unit used   ")
    base_height = float(input("Enter The desired height in inch   "))
    base_height_ratio = float((1 / 12) * base_height)
    cpt_area_ft = round(float(base_height_ratio * cpt_lenght),2)
    print("""

    For a total lenght of {0}{1}, whith a base height of {2} inch.
    the required amount of carpet is {3}{4} whitout loss

    """.format(cpt_lenght,cpt_lenght_unit, base_height, cpt_area_ft," square " + cpt_lenght_unit))

def vinyl_calc():
    print("vinyl")

def print_info():
    print("info")
    print("""

    Guidelines :

            1 - Always Use the same Unit (inch, feet, yard, etc)
            2 - Software Provided Has is, always double check your math

    """)
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

def chooser(tool):
    if tool == "carpet":
        carpet_calc()
    elif tool == "vinyl":
        vinyl_calc()
    elif tool == "info":
        print_info()
    elif tool == "exit":
        exit()
    elif tool == "carpet +":
        print("Advance Carpet")
    else:
        print("invalid input")
        main_input()

def navigation():
    tool = input("input>   ")
    chooser(tool)

print("""

WallBase Solver Version : {0}

""".format(version))

def main_menu():
    menu_string = ("MENU: Carpet  Vinyle(boxed)  Linoleum  Info  Exit")
    divider = len(menu_string) * "*"
    print(divider + "\n" + menu_string + "\n" + divider)
    navigation()


main_menu()
