import pandas as pd

# Vérifier si le fichier CSV existe déjà
try:
    df = pd.read_csv('entreprises.csv')
except FileNotFoundError:
    # Si le fichier n'existe pas, créer une nouvelle DataFrame
    df = pd.DataFrame(columns=['nom', 'adresse', 'telephone', 'site_web', 'secteur_activite'])

def entrer_informations():
    nom = input("Nom de l'entreprise: ")
    adresse = input("Adresse de l'entreprise: ")
    telephone = input("Téléphone de l'entreprise: ")
    site_web = input("Site web de l'entreprise: ")
    secteur_activite = input("Secteur d'activité de l'entreprise: ")

    return {
        'nom': nom,
        'adresse': adresse,
        'telephone': telephone,
        'site_web': site_web,
        'secteur_activite': secteur_activite
    }

def enregistrer_informations(entreprise, dataframe):
    # Convertir le dictionnaire en DataFrame
    df_nouvelle_entreprise = pd.DataFrame([entreprise])
    # Concaténer la nouvelle DataFrame avec l'ancienne
    dataframe = pd.concat([dataframe, df_nouvelle_entreprise], ignore_index=True)
    # Sauvegarder dans le fichier CSV
    dataframe.to_csv('entreprises.csv', index=False)
    return dataframe


def main():
    global df
    while True:
        entreprise_info = entrer_informations()
        df = enregistrer_informations(entreprise_info, df)
        print("Informations enregistrées avec succès.")

        continuer = input("Voulez-vous entrer les informations d'une autre entreprise? (oui/non): ")
        if continuer.lower() != 'oui':
            break

    print("Fin du programme.")

if __name__ == "__main__":
    main()

