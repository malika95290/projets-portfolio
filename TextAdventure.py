import random

personnage = {
    "PV": 70
}

pouvoirs = [
    "Un pour Tous",
    "Contrôler la gravité",
    "Faire des explosions",
    "Être une grenouille",
    "Créer des objets",
    "Mi-chaud mi-froid",
    "Aller très vite"
]

plats = "Ramen,Onigiri,Udon,Curry"  
plats_liste = plats.split(",")  # Transformation en liste en séparant les éléments par ","
plats_stock = {plat: 2 for plat in plats_liste}  # Création du dictionnaire avec les plats et leur stock initial à 0

objets_cles = ["smartphone"]
inventaire = {}

quetes_en_cours = { 
    "bibliothèque": False,
}

plats_japonais = {
    "sushi": "Un plat japonais composé de riz vinaigré garni de poisson cru ou cuit, ou d'autres ingrédients comme les légumes.",
    "ramen": "Une soupe de nouilles japonaise servie dans un bouillon de viande ou de poisson, souvent accompagnée de divers ingrédients.",
    "tempura": "Des ingrédients tels que des crevettes, des légumes ou du poisson enrobés de pâte à frire et frits.",
}



# ********************************************************************************
# FONCTIONS UTILITAIRES
# ********************************************************************************

def proposer_lieux(mots_cles):
    message = "│[Lieux] "
    lieux_disponibles = [lieu.capitalize() for lieu in mots_cles]
    message += ", ".join(lieux_disponibles)
    print(message)

def proposer_actions(actions):
    message = "│[Actions] "
    actions_disponibles = [action.capitalize() for action in actions]
    message += ", ".join(actions_disponibles)
    print(message)

def observer(lieu):
    print(f'Vous observez attentivement {lieu}')

def action_demander_passe():
    if "passe" in objets_cles:
        print("Vous avez déjà le passe.")
    else:
        print("Le professeur vous donne le passe.")
        objets_cles.append("passe")

def action_montrer_badges():
    if "badge" in inventaire and inventaire["badge"] >= 3:
        print("Félicitations ! Vous avez montré trois badges et terminé le jeu.")
        print("Fin du jeu.")
        exit()
    else:
        print("M. Miyagi vous regarde étrangement. Vous n'avez pas assez de badges.")
    conditions_reussite()

def action_manger():
    for i, plat in enumerate(plats_stock):  
        print(f"{i+1} : {plat}")

    plat_demander = int(input("Quel plat voulez-vous manger ?"))
    nom_plat = (plats_liste[plat_demander - 1])
    if plats_stock[plats_liste[plat_demander - 1]] > 0:
        print(f"Vous mangez {nom_plat}. Bon appétit !")
        plats_stock[nom_plat] -= 1
        personnage["PV"] += 10
        print(f"Vos PV ont augmenté à {personnage['PV']}.")
    else:
        print(f"Désolé, {nom_plat} n'est plus disponible.")

    conditions_echec()

def action_combattre():
    mannequin_pv = 50
    print("Vous commencez le combat avec le mannequin d'entraînement.")
    afficher_combat(personnage["PV"], mannequin_pv)
    
    while True:
        print("┌────────────────────────────────────────")
        print("Que voulez-vous faire ?")
        print("1. Attaquer")
        print("2. Fuir")
        print("3. Utiliser mon pouvoir")
        choix = input("├─> ")
        print("└────────────────────────────────────────")

        if choix == "1":
            print("Vous attaquez le mannequin d'entraînement.")
            mannequin_pv -= 15
            print(f"Le mannequin d'entraînement a maintenant {mannequin_pv} PV.")

            if mannequin_pv <= 0:
                print("Vous avez vaincu le mannequin d'entraînement !")
                print("Vous obtenez un badge.")
                if "badge" in inventaire:
                    inventaire["badge"] += 1
                else :
                    inventaire["badge"] = 1
                break

            print("Le mannequin d'entraînement riposte.")
            degats_personnage = random.randint(10, 20)
            personnage["PV"] -= degats_personnage
            print(f"Vos PV ont diminué à {personnage['PV']}.")

            if personnage["PV"] <= 0:
                print("Vous avez été vaincu ! Fin du jeu. ")
                conditions_echec()
                exit()

        elif choix == "2":
            print("Vous avez fui le combat.")
            break

        elif choix == "3":
            utiliser_pouvoir(personnage["Pouvoir"])

        else:
            print("Action invalide. Veuillez choisir une action parmi celles proposées.")

def afficher_combat(joueur_pv, adversaire_pv):
    print("      O            \\ | /            O")
    print("     /|\\            \\|/            /|\\")
    print("     / \\            / \\            / \\")
    print("\n    Joueur           |           Adversaire")
    print(f"   PV: {joueur_pv}          (•‿•)            PV: {adversaire_pv}\n")
    print("  [1. Attaquer]    [2. Fuir]    [3. Utiliser pouvoir]")

def conditions_reussite(): #Fonction appelé pour l'action montrer
    if "badge" in inventaire and inventaire["badge"] >= 3:
        print("Félicitations ! Vous avez montré trois badges et terminé le jeu.")
        print("Fin du jeu.")
        exit()

def conditions_echec(): #Fonction appelé pour l'action combattre
    if personnage["PV"] <= 0:
        print("Vos points de vie sont tombés à zéro. Vous avez perdu !")
        print("Fin du jeu.")
        exit()

def perso_devinette(): #Personnage du jeu de la devinette
    print("Vous rencontrez Yuki, un étudiant, dans le couloir.")
    print("Yuki : Bonjour ! Voulez-vous jouer à un jeu de devinette avec moi ?")
    print("Yuki : Si tu le trouves, tu gagnes 10 points de vie sinon tu en perds 10 !")
    choix = input("Répondez 'oui' ou 'non' : ").lower()
    if choix == "oui":
        mini_jeu_devinette()
    elif choix == "non":
        print("Yuki : D'accord, peut-être une prochaine fois alors. Si tu me cherches, tu sais où me trouver maintenant.")
    else:
        print("Yuki : Désolé, je n'ai pas compris. Voulez-vous jouer à un jeu de devinette avec moi ?")

def mini_jeu_devinette(): # Jeu de devinette pour gagner 20 points de vie
    print("Bienvenue au jeu de devinette !")
    print("Je vais choisir un nombre entre 1 et 30, et vous devrez deviner ce nombre en 5 essais.")
    nombre_a_deviner = random.randint(1, 30)
    nombre_d_essais = 5

    for essai in range(nombre_d_essais):
        print(f"Il vous reste {nombre_d_essais - essai} essais.")
        essai_utilisateur = int(input("Devinez le nombre : "))

        if essai_utilisateur == nombre_a_deviner:
            print("Félicitations ! Vous avez deviné le nombre correctement.")
            print("Vous gagnez 20 points de vie.")
            personnage["PV"] += 20
            return
        elif essai_utilisateur < nombre_a_deviner:
            print("Le nombre à deviner est plus grand.")
        else:
            print("Le nombre à deviner est plus petit.")

    print("Désolé, vous n'avez pas deviné le nombre correctement.")
    print("Le nombre à deviner était :", nombre_a_deviner)
    print("Retente ta chance une prochaine fois !")

def utiliser_pouvoir(pouvoir):
    if pouvoir == "Un pour Tous":
        # Effets spéciaux ici
        pass
    elif pouvoir == "Contrôler la gravité":
        print("Vous utilisez votre pouvoir 'Contrôler la gravité' ! Vous manipulez la gravité pour immobiliser votre ennemi ou modifier son environnement.")
        print("Le mannequin d'entraînement est immobilisé !")
        degats_infliges = random.randint(15, 25)
        print(f"Vous infligez {degats_infliges} points de dégâts au mannequin.")
    elif pouvoir == "Faire des explosions":
        print("Vous déclenchez des explosions avec votre pouvoir !")
        degats_explosion = random.randint(20, 30)
        mannequin_pv -= degats_explosion
        print(f"Le mannequin d'entraînement subit {degats_explosion} points de dégâts de l'explosion.")
    elif pouvoir == "Être une grenouille":
        print("Vous vous transformez en une grenouille avec votre pouvoir ! Vous gagnez en agilité et en régénération, mais perdez en puissance.")
        print("Vous récupérez 10 points de vie.")
        personnage["PV"] += 10
    elif pouvoir == "Créer des objets":
        print("Vous matérialisez des objets avec votre pouvoir !")
        print("Vous créez un bouclier pour vous protéger des attaques du mannequin.")
        personnage["PV"] += 20
    elif pouvoir == "Mi-chaud mi-froid":
        print("Vous manipulez les températures avec votre pouvoir 'Mi-chaud mi-froid' ! Vous brûlez vos ennemis avec des flammes intenses ou les congeler avec un froid glacial.")
        type_degats = random.choice(["feu", "glace"])
        if type_degats == "feu":
            print("Vous brûlez le mannequin d'entraînement avec des flammes intenses !")
        else:
            print("Vous congeler le mannequin d'entraînement avec un froid glacial !")
        mannequin_pv -= 30
    elif pouvoir == "Aller très vite":
        print("Vous activez votre pouvoir 'Aller très vite' ! Vous vous déplacez à une vitesse éclair, esquivant les attaques ennemies et frappant avec une rapidité dévastatrice.")
        print("Vous esquivez habilement les attaques du mannequin et ripostez avec une rapidité dévastatrice ! Vous récupérez 10 points de vie.")
        personnage["PV"] += 10
    else:
        print("Ce pouvoir n'est pas encore implémenté. Continuez à vous entraîner !")

def jeu_devine_plat_japonais():
    print("Bienvenue dans le jeu de devinette des plats japonais!")
    print("Sato-san, le cuisinier, vous défie de deviner le nom de certains plats.")
    print("Si vous devinez correctement, vous gagnez 10 points de vie")
    print("=========================================")    

    while True:
        plat = random.choice(list(plats_japonais.keys()))
        description = plats_japonais[plat]
        print("\nSato-san, le cuisinier, vous défie de deviner le nom de ce plat :")
        print("\n" + description)
        reponse = input("Quel est le nom de ce plat ? ").strip().lower()

        if reponse == plat:
            print("Bravo ! C'est correct.")
            print("Vous retournez à la cafétéria.")
            personnage["PV"] += 10
            lieu_cafeteria()
        else:
            print(f"Désolé, ce n'est pas correct. Le plat était {plat}.")
            print("\nSato-san : N'hésite pas à revenir me voir")
            lieu_cafeteria()

# ********************************************************************************
# INTRODUCTION
# ********************************************************************************


def intro():
    print("      ////////    ///  ///")
    print("      ///  ///    ///  ///")
    print("      ////////    ///  ///")
    print("      ///  ///    ////////")
    print("===============================")
    print("|| Bienvenue au lycée A.U. ! ||")
    print("===============================")

    # Rencontre avec le professeur M. Miyagi
    print("\nVous rencontrez le professeur M. Miyagi dans le hall d'entrée.")
    print("M. Miyagi : Bienvenue, jeune héros, au lycée A.U. !")
    print("M. Miyagi : Je suis ici pour vous aider à démarrer votre aventure.")
    print("M. Miyagi : Dans ce lycée, vous rencontrerez divers défis et quêtes.")
    print("M. Miyagi : Certaines quêtes peuvent vous demander de trouver des objets perdus,")
    print("M. Miyagi : tandis que d'autres pourraient vous mettre au défi de combattre des adversaires redoutables.")
    print("M. Miyagi : N'oubliez pas, l'entraînement et la sagesse sont les clés de la réussite.")

    print("Commençons par créer ton personnage.")
    age = input("\nQuel âge as-tu ? ")
    personnage["Age"] = age

    # Afficher la liste des pouvoirs (avec leur position) et demander d'en choisir un
    print("\nVoici la liste des pouvoirs :")
    for i, pouvoir in enumerate(pouvoirs):
        print(f"{i + 1}. {pouvoir}")
    
    #On demande le numéro et on vérifie son existence
    choix_pouvoir = None
    while choix_pouvoir is None :
        choix_pouvoir = int(input("Choisis ton pouvoir (1-7) : ")) - 1
        if 0 <= choix_pouvoir < len(pouvoirs):
                personnage["Pouvoir"] = pouvoirs[choix_pouvoir]
        else:
            print("Nombre invalide. Veuillez saisir un nombre entre 1 et 7.")
            choix_pouvoir = None  # Réinitialiser la variable pour redemander à l'utilisateur
        
    
    # Stocker le nom du pouvoir choisi dans le dictionnaire "personnage"
    personnage["Pouvoir"] = pouvoirs[choix_pouvoir]

    # Afficher tout le contenu (clé et valeur) du dictionnaire "personnage"
    print("\nRécapitulatif du personnage :")
    for key, value in personnage.items():
        print(f"{key}: {value}")   

    print("\nM. Miyagi : Maintenant que vous avez créé votre personnage, votre aventure commence !")
    print("M. Miyagi : N'ayez pas peur d'explorer le lycée et de relever les défis qui se présentent à vous.")
    print("M. Miyagi : Rappelez-vous, la clé du succès réside dans votre détermination et votre courage.")
    print("M. Miyagi : Bonne chance, jeune héros ! Que votre voyage soit rempli de gloire et de succès.")

    # Informer le joueur de la nouvelle quête
    print("M. Miyagi : Oh, j'ai entendu dire qu'un manuel important avait été perdu dans la bibliothèque.")
    print("M. Miyagi : Peut-être que cela vaut la peine de jeter un coup d'œil là-bas.")
    print("M. Miyagi : Si vous le trouvez, cela pourrait vous être très utile.")

    lieu_hall()

# ********************************************************************************
# LIEUX
# ********************************************************************************


def lieu_hall():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans le hall d'entrée de l'école.")
    print("On peut aller à de nombreux endroits d'ici.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["\n 1 - quitter","\n 2 - observer"]) 
        proposer_lieux(["\n 3 - Couloir rez-de-chaussé","\n 4 - Classe 1-A", "\n 5 - Bibliothèque"])  
        reponse = int(input("├─> "))
        print("└────────────────────────────────────────")

        # Gérer ici toutes les réponses possibles, qu'elles soient correctes ou non
        if reponse == 1:
            print("À bientôt !")
            break
        elif reponse == 2:
            observer("le hall d'entrée")
        elif reponse == 3:
            lieu_couloir_rdc()
        elif reponse == 4:
            lieu_classe_1A()
        elif reponse == 5:
            lieu_bibliotheque()
        else:
            print("Action invalide. Veuillez choisir une action parmi celles proposées.")

def lieu_couloir_rdc():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est le couloir du rez de chaussé.")
    print("On y trouve entre autres la classe 1-A et le couloir qui mène à l'étage.")
    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["\n 1 - quitter", "\n 2 - observer"])  
        proposer_lieux(["\n 3 - hall d'entrée", "\n 4 - classe 1-A", "\n 5 - couloir étage"])  
        reponse = int(input("├─> "))
        print("└────────────────────────────────────────")

        if reponse == 1:
            print("À bientôt !")
            break
        elif reponse == 2:
            observer("le couloir du rez-de-chaussé")
        elif reponse == 3:
            lieu_hall()
        elif reponse == 4:
            lieu_classe_1A()
        elif reponse == 5:
            lieu_couloir_etage()
        else:
            print("Action invalide. Veuillez choisir une action parmi celles proposées.")

def lieu_classe_1A():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est la classe 1-A.")
    print("Le professeur vous regarde attentivement.")
    
    if "manuel" not in inventaire:
        print("Vous voyez une note sur le bureau du professeur. Peut-être que vous devriez l'examiner.")
    
    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["\n 1 - quitter", "\n 2 - observer", "\n 3 - demander", "\n 4 - montrer"])  
        proposer_lieux(["\n 5 - Hall", "\n 6 - Couloir rez-de-chaussée"])
        reponse = int(input("├─> "))
        print("└────────────────────────────────────────")

        if reponse == 1:
            print("À bientôt !")
            break
        elif reponse == 2:
            observer("la classe 1-A")
        elif reponse == 3:
            action_demander_passe()
        elif reponse == 4:
            action_montrer_badges()
        elif reponse == 5:
            lieu_hall()
        elif reponse == 6:
            lieu_couloir_rdc()
        else:
            print("Action invalide. Veuillez choisir une action parmi celles proposées.")
        
        if reponse == 2 and "manuel" not in inventaire:
            print("Vous trouvez une note sur le bureau du professeur.")
            print("« Cherche le manuel perdu pour une récompense, ne rate pas le coupon pour un ramen gratuit. »")
            print(" >> Vous avez commencé la quête : 'Trouver le manuel perdu dans la bibliothèque'.")
            quetes_en_cours["bibliothèque"] = True
            inventaire["manuel"] = 1

    conditions_echec()

def lieu_bibliotheque():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est la bibliothèque de l'école.")
    print("C'est un endroit calme rempli de livres et de connaissances.")
    print("Vous cherchez activement le manuel perdu.")

   # Vérifier si la quête du manuel est en cours
    if quetes_en_cours["bibliothèque"]:
        print("Vous êtes à la recherche du manuel perdu.")
        print("En explorant les étagères, vous trouvez un vieux livre poussiéreux.")
        print("Vous l'ouvrez et réalisez que c'est le manuel que vous cherchez !")
        print("Félicitations ! Vous avez trouvé le manuel perdu.")
        print("Votre récompense est un coupon pour des ramen gratuits à la cafétéria.")
        print("Votre stock de ramen a augmenté de 1.")
        plats_stock["Ramen"] += 1
        
        # Marquer la quête comme terminée
        quetes_en_cours["bibliothèque"] = False
        
        # Ajouter le manuel à l'inventaire
        objets_cles.append("manuel")
    else:
        print("Il y a beaucoup de livres ici, mais vous ne trouvez pas ce que vous cherchez.")
    

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["\n 1 - quitter", "\n 2 - observer"])  
        proposer_lieux(["\n 3 - Hall", "\n 4 - Couloir rez-de-chaussée"])
        reponse = int(input("├─> "))
        print("└────────────────────────────────────────")

        if reponse == 1:
            print("À bientôt !")
            break
        elif reponse == 2:
            observer("la bibliothèque")
        elif reponse == 3:
            lieu_hall()
        elif reponse == 4:
            lieu_couloir_rdc()
        else:
            print("Action invalide. Veuillez choisir une action parmi celles proposées.")

    conditions_echec()

def lieu_couloir_etage():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nVous venez d'arriver au couloir du premier étage.")
    perso_devinette()   

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["\n 1 - quitter", "\n 2 - observer"])  
        proposer_lieux(["\n 3 - cafétéria","\n 4 - salle d'entrainement","\n 5 - couloir rdc"])  
        reponse = int(input("├─> "))
        print("└────────────────────────────────────────")

        if reponse == 1:
            print("À bientôt !")
            break
        elif reponse == 2:
            observer("le couloir du premier étage")
        elif reponse == 3:
            lieu_cafeteria()
        elif reponse == 4:
            lieu_salle_entrainement()
        elif reponse == 5:
            lieu_couloir_rdc()
        else:
            print("Action invalide. Veuillez choisir une action parmi celles proposées.")
        
def lieu_cafeteria():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est la cafétéria.")
    print("Vous avez faim après une longue journée de cours.")
    print("Le cuisinier, Sato-san, vous fait signe de venir jouer à son jeu.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["\n 1 - quitter", "\n 2 - observer", "\n 3 - manger", "\n 6 - Jeu"])  
        proposer_lieux(["\n 4 - Salle d'entrainement", "\n 5 - Couloir étage"])
        reponse = int(input("├─> "))
        print("└────────────────────────────────────────")

        if reponse == 1:
            print("À bientôt !")
            break
        elif reponse == 2:
            observer("la cafétéria")
        elif reponse == 3:
            action_manger()
        elif reponse == 4 :
            lieu_salle_entrainement()
        elif reponse == 5 :
            lieu_couloir_etage()
        elif reponse == 6:
            jeu_devine_plat_japonais()
        else:
            print("Action invalide. Veuillez choisir une action parmi celles proposées.")

def lieu_salle_entrainement():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est la salle d'entraînement.")
    print("Vous voyez un mannequin d'entraînement au centre de la salle.")

    if "passe" not in objets_cles:
        print("Vous avez besoin d'un badge pour accéder à la salle d'entraînement.")
        print("Retournez à la classe 1-A pour en récupérer un.")
        return
    
    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["\n 1 - quitter", "\n 2 - observer", "\n 3 - combattre"])  
        proposer_lieux(["\n 4 - Cafétéria", "\n 5 - Couloir étage"])
        reponse = int(input("├─> "))
        print("└────────────────────────────────────────")

        if reponse == 1:
            print("À bientôt !")
            break
        elif reponse == 2:
            observer("la salle d'entrainement")
        elif reponse == 3:
            action_combattre()
        elif reponse == 4:
            lieu_cafeteria()
        elif reponse == 5 :
            lieu_couloir_etage()
        else:
            print("Action invalide. Veuillez choisir une action parmi celles proposées.")
    conditions_echec()

# ********************************************************************************
# EXECUTION
# ********************************************************************************


# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")
