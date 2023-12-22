################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2023                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 10     #  Variables I : valeurs et types                              #
#               #                                                              #
################################################################################
#
#  - Déclarer une variable
#  - Conventions de nommage
#  - Variables et types de valeurs
#  - Lire et modifier une variable
#  - Affectation multiple
#  - Quelques fonctions sur les variables
#
#######################################

# Déclarer une variable
########################

"""
Une variable est un espace mémoire où l'utilisateur peut stocker une valeur.
Cet espace mémoire est nommé par l'utilisateur pour pouvoir être référencé
plus tard.

L'utilisateur peut ensuite lire le contenu de la variable et la modifier
pendant l'exécution du programme.
"""


# Conventions de nommage
#########################

"""
On peut nommer sa variable comme on le souhaite, ou presque. La convention
Python est de nommer ses variables avec des minuscules_et_underscores, et sans
accents.
"""
une_belle_variable = 5  # 👍
uneVariableMoche = 2    # moche
uNeVrAIEMocheté = 7     # atroce : jamais d'accents dans vos noms de variables

# Exception : on utilisera des capitales pour les variables globales (voir
# chap. 19)
VARIABLE_GLOBALE = "Des majuscules partout !"

# Python accepte tous les caractères pour les variables, mais il est
# déconseillé de s'écarter des caractères ASCII : prenez l'habitude d'écrire
# avec les 26 lettres minuscules, les 10 chiffres, et les underscore ("_")
àêïœú = 34              # ça fonctionne mais c'est moche

"""
Pourquoi est-ce dangereux ? Parce que ces caractères ne font pas partie du jeu
de caractères "ASCII" (American Standard Code for Information Interchange) :
ce jeu est composé d'une centaine de caractères "de base" garantis d'être
reconnus partout.
"""


# Variables et types de valeurs
################################

# Une variable peut contenir tous les types proposés par Python :
un_super_entier = 3                      # => int
un_super_flottant = 46.2                 # => float
une_super_chaine_de_caractere = "pouet"  # => string
un_super_booleen = False                 # => boolean
une_super_liste = [True, 46.2, "pouet"]  # => list

# On rappelle que les int peuvent conserver des nombres très élevés
entier_gigantesque = 9999999999999999999999999999999
print(entier_gigantesque)  # => 9999999999999999999999999999999


# Lire et modifier une variable
################################

# On peut écrire dans une variable (y ranger une valeur), puis plus tard aller
# modifier cette valeur.
nombre_voitures = 4
nombre_voitures += 1
nombre_voitures  # => 5

# Tenter d'accéder à une variable non-définie soulève une exception.
try:
    une_variable_inconnue  # => NameError
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Note : l'affectation utilise le symbole "=", mais il est différent du "=" en
mathématiques : c'est un égal d'affectation.
"""

# Ainsi, cette équation n'a aucune solution en mathématiques…
nombre_voitures = nombre_voitures + 1
# …mais en Python c'est une expression tout à fait valide, qui veut dire :
# ajoute 1 à la variable nombre_voitures.

# Note : on peut utiliser un raccourci pour l'expression précédente grâce à
# l'opérateur "+="
nombre_voitures += 7  # ajoute 7 à nombre_voitures

# IMPT : on dit qu'on "incrémente" un int quand on lui ajoute 1
nb_girafes = 5
nb_girafes += 1   # on incrémente la variable nb_girafes

# Ces raccourcis fonctionnent aussi avec "-=", "*=" et "/=".
nombre_voitures *= 2  # multiplie nombre_voitures par 2
nombre_voitures -= 5  # enlève 5 à nombre_voitures


# Affectation multiple
############################

"""
Il est possible d'affecter plusieurs variables à la fois en séparant les
valeurs à affecter, et les variables, par des virgules
"""
a, b, c = 1, 2, 3
print(a) # => 1
print(b) # => 2
print(c) # => 3

"""
On verra plus loin que la valeur à droite est un "tuple" (chap. 17).
"""


# Quelques fonctions sur les variables
############################

# Prenons des variables toute bêtes :
a = 2
b = "test"
c = False

#   1. La fonction type() retourne leur type :
print(type(a))  # => <class 'int'>
print(type(b))  # => <class 'str'>
print(type(c))  # => <class 'bool'>

#   2. La fonction str() peut les transformer en string :
print(str(a))  # => '2'
print(str(b))  # => 'test'
print(str(c))  # => 'False'

# Note : print() appelle toujours str() sur les variables passées en paramètre :

#   3. La fonction id() retourne l'identifiant interne de la variable :
print(id(a))  # => 4466972408
print(id(b))  # => 4460299696
print(id(c))  # => 4466971336

#   4. La fonction hash() retourne son hash (s'il en a un) :
print(hash(a))  # => 2
print(hash(b))  # => 8482357589469416518
print(hash(c))  # => 0

#   5. La fonction dir() retourne toutes les méthodes que l'on peut appeler sur
#      l'objet a
print(dir(a))

#   6. La fonction help() retourne une aide sur le type de l'objet
help(a)  # => Help on int object: