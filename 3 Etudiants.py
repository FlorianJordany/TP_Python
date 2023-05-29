# Créer une promotion comme un tableau d'étudiants

promotion = [
    {
        "nom": "Dupont",
        "prenom": "Jean",
        "matieres": [
            {"nom": "Mathématiques", "note": 15},
            {"nom": "Physique", "note": 12},
            {"nom": "Anglais", "note": 18}
        ]
    },
    {
        "nom": "Martin",
        "prenom": "Sophie",
        "matieres": [
            {"nom": "Mathématiques", "note": 14},
            {"nom": "Physique", "note": 16},
            {"nom": "Anglais", "note": 19}
        ]
    },
    {
        "nom": "Durand",
        "prenom": "Pierre",
        "matieres": [
            {"nom": "Mathématiques", "note": 17},
            {"nom": "Physique", "note": 13},
            {"nom": "Anglais", "note": 15}
        ]
    }
]

# Implémenter la fonction moyenne d'un étudiant dédiée cette représentation

def moyenne_etudiant(etudiant):
    notes = [matiere["note"] for matiere in etudiant["matieres"]]
    return sum(notes) / len(notes)

print(30*"*")
for etudiant in promotion:
    moyenne = moyenne_etudiant(etudiant)
    print(etudiant["prenom"], " à une moyenne de ", moyenne)

# Pour chaque discipline, la fonction moyenne de la promotion

def moyenne_promotion(promotion):
    moyennes = {}

    for etudiant in promotion:
        for matiere in etudiant["matieres"]:
            nom_matiere = matiere["nom"]
            note = matiere["note"]

            if nom_matiere not in moyennes:
                moyennes[nom_matiere] = []

            moyennes[nom_matiere].append(note)

    for matiere, notes in moyennes.items():
        moyenne = sum(notes) / len(notes)
        moyennes[matiere] = moyenne

    return moyennes

moyennes_promotion = moyenne_promotion(promotion)

print(30*"*")
for matiere, moyenne in moyennes_promotion.items():
    print("Moyenne ", matiere, ":", moyenne)

# Lafonction qui trouve l'étudiant ayant eu la note moyenne maximale,etc.

def etudiant_max_moyenne(promotion):
    meilleure_moyenne = 0
    meilleure_moyenne_etudiant = ""

    for etudiant in promotion:
        moyenne = moyenne_etudiant(etudiant)

        if moyenne > meilleure_moyenne:
            meilleure_moyenne = moyenne
            meilleure_moyenne_etudiant = etudiant

    return meilleure_moyenne_etudiant

meilleur_etudiant = etudiant_max_moyenne(promotion)

print(30*"*")
print("Meilleur étudiant :", meilleur_etudiant["prenom"])

# Généraliser à un type d'étudiant qui possède un nombre quelconque de notes
