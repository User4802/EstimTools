# THIS LIB WILL PROVIDE IF ASKED, THE LOG OF THE CREATION, AND THE NOTES TEMPLATE

version = "v0.4"


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
