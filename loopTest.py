import os

default = ["plans", "devis", "dossier"]

dir = os.getcwd()

def loopDeploy(default, dir):
    for names in default:
        os.mkdir(dir + "/" + names)

input("start ? ")


loopDeploy(default, dir)
