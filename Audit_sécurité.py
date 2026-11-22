#Mini_programme pour auditer la sécurité d'un mot de passe
print("===AUDIT-SECURITE===")

#On prepare nos boîtes pour compter
compteur_fort = 0
compteur_faible = 0
compteur_interdit = 0

#On prepare la liste des employés interpeller
liste_a_interpeller = []

#On boucle à 5 employés

for i in range(1 , 6):
    prenom=input(f"Prénom employé {i} : ")
    mdp=input(f"Mot de passe de {prenom} :")

#On normalise pour détecter PASSWORD, Password, etc...
    mdp_petit=mdp.lower()

#On analyse
    if "password" in mdp_petit:
        print("INTERDIT")
        compteur_interdit = compteur_interdit + 1
        liste_a_interpeller.append(prenom)

    elif len(mdp)<8 :
        print("FAIBLE")
        compteur_faible = compteur_faible + 1
        liste_a_interpeller.append(prenom)

    else:
        print("FORT")
        compteur_fort = compteur_fort + 1

    print("---")

#Le rapport final pour le chef
print("===RAPPORT FINAL===")
print("")
print(f"TOTAL FORT : {compteur_fort}")
print(f"TOTAL FAIBLE :  {compteur_faible}")    
print(f"TOTAL INTERDIT :  {compteur_interdit}")

#On affiche la liste des prénoms à interpeller
print(f"Les employés à interpeller sont : {liste_a_interpeller}")
    