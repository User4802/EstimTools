# query user for the init method view / add
    ## admin can bypass by typing admin here
        ### admin can delete, modify, force add
# if view display the current DB
# if add ask the following
    ## Job Name *
    ## General Contractor *
    ## postal code of worksite * (needed to not get duplicate)
    ## due date (not mandatory)

version = "beta_v0.2"
module = "ProjectView"
spacer = len(module) * "-"
splash = "\n{} {} {} {}\n".format(spacer,module,version,spacer)

print(splash)

def ajout():
    print("----- Mode Ajout -----")
    prName = input("name ")
    prGen = input("general ")
    prAdr = input("adress ")
    prPostal = input("code postal ")
    prDate = input("date de fermeture ")
    prFull = "{}, {}, {}, {}, {}\n".format(prName,prGen,prAdr,prPostal,prDate)
    with open("projet.txt", "a") as file:
        file.write(prFull)
    user_input()

def voir():
    print("----- Mode Voir -----\n")
    with open("projet.txt", "r") as file:
        body = file.read()
        print(body)
    input("Enter pour retourner au menu principal")
    user_input()

def adminMode():
    print("----- Admin Mode -----")
    password = input("Password ?\n >>>")
    print("Acces Denied")
    user_input()

def quit():
    print("\nPrograme fermer avec succes \n")

def user_input():
    init_method = input("Voir les projet inscrit ? (voir) | Ajouter un projet ? (ajout) | Quitter ? (quit) \n >>> ")
    init(init_method)

def init(method):
    if method == "voir":
        voir()
    elif method == "ajout":
        ajout()
    elif method == "admin":
        adminMode()
    elif method == "quit":
        quit()
    else:
        print("Entré invalide\n")
        user_input()

user_input()
