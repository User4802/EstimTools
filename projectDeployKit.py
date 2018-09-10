version = "0.3"
import os

print("Project Deploy Kit V{0}".format(version))

main_path = input("Main Path ? ")

os.mkdir(main_path)
os.mkdir(main_path + "/plans")
os.mkdir(main_path + "/documents")
os.mkdir(main_path + "/soumission")
os.mkdir(main_path + "/cotations")
