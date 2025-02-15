import numpy as np
import matplotlib.pyplot as plt


def profil_symetrique_naca(nombre_naca, corde, nombre_points, type_distribution):
    # Extraction de l'épaisseur maximale
    t = int(nombre_naca[2:]) / 100  # XX/100

    # Génération des coordonnées selon la distribution choisie
    if type_distribution == "l":
        xc = np.linspace(0, 1, nombre_points)
    elif type_distribution == "nu":
        theta = np.linspace(0, np.pi, nombre_points)
        xc = 0.5 * (1 - np.cos(theta))
    else:
        raise ValueError("Type de distribution inconnu. Utiliser 'linéaire' ou 'non-uniforme'")

    # Calcul de la demi-épaisseur yt
    yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)

    # Calcul des coordonnées des points sur l'extrados et l'intrados
    xup = xc * corde
    yup = yt * corde
    xdown = xc * corde
    ydown = -yt * corde

    # Épaisseur maximale et sa position
    epaisseur_max = np.max(yt) * corde
    position_epaisseur_max = xc[np.argmax(yt)] * corde

    # Affichage des résultats
    print(f"Épaisseur maximale : {position_epaisseur_max:.4f} m")
    print(f"Position de l'épaisseur maximale : {position_epaisseur_max:.4f} m")

    # Tracé du profil
    plt.figure(figsize=(10, 4))
    plt.plot(xup, yup, label='Extrados', color='b')
    plt.plot(xdown, ydown, label='Intrados', color='r')
    plt.xlabel("Longueur de la corde (m)")
    plt.ylabel("Épaisseur (m)")
    plt.title(f"Profil NACA {nombre_naca}")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()


# Entrées utilisateur
nombre_naca = input("Entrez le numéro du profil NACA (ex: 0012) : ")
corde = float(input("Entrez la longueur de la corde (m) : "))
nombre_points = int(input("Entrez le nombre de points pour le tracé : "))
type_distribution = input("Type de distribution des points linéaire/non-uniforme (l/nu) : ")

# Exécution du programme
profil_symetrique_naca(nombre_naca, corde, nombre_points, type_distribution)
