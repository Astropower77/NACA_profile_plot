Génération de Profil Symétrique NACA :

Ce script Python permet de générer et d'afficher le profil d'un aérodynamique symétrique NACA à partir d'un numéro de 
profil, d'une longueur de corde, du nombre de points à tracer et du type de distribution des points.

Prérequis

Avant d'exécuter le script, assurez-vous d'avoir installé les bibliothèques suivantes dans le terminal :

pip install numpy

pip install matplotlib

L'utilisateur devra fournir les informations suivantes :

Numéro du profil NACA (ex: 0012 pour un profil NACA 0012)

Longueur de la corde (en mètres)

Nombre de points utilisés pour générer le profil

Type de distribution des points :

l pour une distribution linéaire

nu pour une distribution non-uniforme basée sur la méthode de Cosinus

Fonctionnement

Le script :

Extrait l'épaisseur maximale à partir du numéro NACA.

Génère les coordonnées en fonction du type de distribution choisi.

Calcule la demi-épaisseur du profil.

Construit les points de l'extrados et de l'intrados.

Affiche l'épaisseur maximale et sa position.

Trace le profil aérodynamique en utilisant Matplotlib.

