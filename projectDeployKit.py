version = "0.48A"

from sys import argv
script, deployType = argv
import os

userType = str(deployType)
localDir = os.getcwd()
default_struct = ["plans", "documents", "soumission", "cotations", "dossier", "devis" ]


# NOTESCREATION

def notesTemps(p):
    fileName = "notes.txt"
    path = p +"/" + fileName
    output = ("""
------
Remise
------


-----------
Info Projet
-----------



--------
Produits
--------



-----
Notes
-----



---
QRT
---


---------------
Demande de prix
---------------



    """)
    file = open(path, 'x')
    file.write(output)

# SCREEN PRINT

def screenPrint(type, dir):

    print("\nThe following folder : {0}, have been created at this location: {1}\n".format(type, dir))  #PRINT THE COMPLETED MESSAGE

# EXPRESS DEPLOY BELOW THIS LINE

def methodExpress(type, dir, default):  #CREATE THE STRUCTURE IN THE CURRENT DIRECTORY, FOLDER NAME SPECIFIED IN THE ARGV

    express_dir = dir + "/" + type  #CONCAT THE CWD, / AND THE SPEFIFIED FOLDER NAME IN ARGV
    os.mkdir(express_dir)   #CREATE THE FOLDER
    for names in default:   #loop the the element of the default array to create each subfolder
        os.mkdir(express_dir + "/" + names)

    notesTemps(express_dir)
    screenPrint(type, dir)  #PRINT FONCTION CALL

# BASIC DEPLOY BELOW THIS LINE

def methodBasic(default): #CREATE THE STRUCTURE IN A USER SPECIFIED DIRECTORY

    print("Project Deploy Kit V{0}".format(version))    #indicate that the script is running and display version

    basic_choice = input("Use the current directory or specify a new one ? ")   #USER CHOICE ABOUT THE CREATION LOCATION

    if basic_choice == "current":   #IF CURRENT FOLDER IS CHOSEN

        basic_current = os.getcwd() #GET THE CWD
        basic_folder = str(input("folder name ? ")) #ASK FOR THE FOLDER NAME
        basic_path = basic_current + "/" + basic_folder #CONCAT THE CWD, / AND THE USER FOLDER NAME
        os.mkdir(basic_path)    #CREATE THE FOLDER
        for names in default:   #loop the the element of the default array to create each subfolder
            os.mkdir(basic_path + "/" + names)

        screenPrint(basic_folder, basic_current)#PRINT FONCTION CALL

    elif basic_choice == "new": #IF NEW FOLDER IS CHOSEN
        print("new")
    else:
        print("not a valid input")  # WRONG INPUT AND FUNCTION RECALL
        methodBasic()

# CUSTOM DEPLOY BELOW THIS LINE

def methodCustom(): #CREATE THE STRUCTURE IN A USER SPECIFIED DIRECTORY + CUSTOM NAME, CUSTOM SUBFOLDER, CUSTOM AMOUNT
    print("custom")

# CHOICE EVALUATING below this line

def methodChoice(type, dir, default):
    if type == "basic":
        #run the basic setup
        methodBasic(default)
    elif type == "custom":
        #run the custom setup
        methodCustom()
    else:
        # run the express setup
        methodExpress(type, dir, default)


methodChoice(userType, localDir, default_struct)
