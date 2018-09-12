version = "0.45"

from sys import argv
script, deployType = argv
import os

userType = str(deployType)
localDir = os.getcwd()


# EXPRESS DEPLOY BELOW THIS LINE

def methodExpress(type, dir): #CREATE THE STRUCTURE IN THE CURRENT DIRECTORY, FOLDER NAME SPECIFIED IN THE ARGV

    express_path = dir + "/" + type
    os.mkdir(express_path)
    os.mkdir(express_path + "/plans")
    os.mkdir(express_path + "/documents")
    os.mkdir(express_path + "/soumission")
    os.mkdir(express_path + "/cotations")
    os.mkdir(express_path + "/dossier")

    print("\nThe following folder : {0}, have been created at this location: {1}\n".format(type, dir))

# BASIC DEPLOY BELOW THIS LINE

def methodBasic(): #CREATE THE STRUCTURE IN A USER SPECIFIED DIRECTORY

    print("Project Deploy Kit V{0}".format(version))

    basic_choice = input("Use the current directory or specify a new one ? ")

    if basic_choice == "current":
        basic_current = os.getcwd()
        basic_folder = str(input("folder name ? "))
        basic_path = basic_current + "/" + basic_folder
        os.mkdir(basic_path)
        os.mkdir(basic_path + "/plans")
        os.mkdir(basic_path + "/documents")
        os.mkdir(basic_path + "/soumission")
        os.mkdir(basic_path + "/cotations")
        os.mkdir(basic_path + "/dossier")

        print("\nThe following folder : {0}, have been created at this location: {1}\n".format(basic_folder, basic_current))

    elif basic_choice == "new":
        print("new")
    else:
        print("not a valid input")
        methodBasic()

# CUSTOM DEPLOY BELOW THIS LINE

def methodCustom(): #CREATE THE STRUCTURE IN A USER SPECIFIED DIRECTORY + CUSTOM NAME, CUSTOM SUBFOLDER, CUSTOM AMOUNT
    print("custom")

# CHOICE EVALUATING below this line

def methodChoice(type, dir):
    if type == "basic":
        #run the basic setup
        methodBasic()
    elif type == "custom":
        #run the custom setup
        methodCustom()
    else:
        # run the express setup
        methodExpress(type, dir)


methodChoice(userType, localDir)
