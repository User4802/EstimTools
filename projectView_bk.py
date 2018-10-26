version = "beta_v0.3"
module = "ProjectView"
spacer = len(module) * "-"
splash = "\n{} {} {} {}\n".format(spacer,module,version,spacer)

print(splash)

def htmlExport(newAdd):
    with open("block.html", "a") as index:
        add = "<p>{0}</p>\n".format(newAdd)
        index.write(add)

def ajout():
    print("----- Mode Ajout -----")
    prName = input("Nom Du Projet\n ")
    prGen = input("Entrepreneur Général\n ")
    prAdr = input("Adresse Du Projet\n ")
    prVend = input("Vendeur\n ")
    prDate = input("date De Fermeture\n ")
    prFull = "{} -- {} -- {} -- {} -- {}\n".format(prName,prGen,prAdr,prVend,prDate)
    with open("projet.txt", "a") as file:
        file.write(prFull)
    user_input()
    htmlExport(prFull)

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
