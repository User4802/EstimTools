version = "0.4"

from sys import argv
script, initMethod = argv
import os



im = str(initMethod)

def methodBasic():

    print("Project Deploy Kit V{0}".format(version))

    express_path = input("Main Path ? ")

    os.mkdir(main_path)
    os.mkdir(main_path + "/plans")
    os.mkdir(main_path + "/documents")
    os.mkdir(main_path + "/soumission")
    os.mkdir(main_path + "/cotations")

def methodCustom():

    print("Project Deploy Kit V{0}".format(version))

    main_path = input("Main Path ? ")

    os.mkdir(main_path)
    os.mkdir(main_path + "/plans")
    os.mkdir(main_path + "/documents")
    os.mkdir(main_path + "/soumission")
    os.mkdir(main_path + "/cotations")

def methodExpress():

    express_path = os.getcwd() + "/" + im
    os.mkdir(express_path)
    os.mkdir(express_path + "/plans")
    os.mkdir(express_path + "/documents")
    os.mkdir(express_path + "/soumission")
    os.mkdir(express_path + "/cotations")
    os.mkdir(express_path + "/dossier")

def methodChoice(im):
    if im == "basic":
        #run the basic setup
        methodBasic()
    elif im == "custom":
        #run the custom setup
        methodCustom()
    else:
        # run the express setup
        print("express")
        methodExpress()


methodChoice(im)
