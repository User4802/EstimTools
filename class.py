class ProjectAdd:
    def __init__(self, titre, general, date, vendeur):
        self.titre = titre
        self.general = general
        self.date = date
        self.vendeur = vendeur
    
    def addProject(self):
        projects = []
        test = tuple((self.titre, self.general, self.date, self.vendeur))
        projects.append(test)
        print(projects)


def projectInfo():
    titre = input("Nom du projet ?  ")
    general = input("general du projet ?  ")
    date = input("date du projet ?  ")
    vendeur = input("vendeur du projet ?  ")

    p = ProjectAdd(titre, general, date, vendeur)

    p.addProject()


projectInfo()