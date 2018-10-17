import os, argparse, file, dataset;

# Allow to clear console
def clear(withHeader = True): 
    # For windows 
    if os.name == 'nt': 
         _ = os.system('cls');
  
    # For mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear');
    
    if (withHeader):
        print("|-------------------- Data Analysis v1.1 --------------------|\n")

clear();

parser = argparse.ArgumentParser();
parser.add_argument("-f","--filepath", nargs="?", help="Chemin du fichier de donnees");
parser.add_argument("-u","--user", action="store_true", help="Activer l'interaction utilisateur");
parser.add_argument("-l","--log", action="store_true", help="Activer l'enregistrement dans un fichier de log");
args=parser.parse_args(); 

print(args);

currentFile = file.File(args.filepath);

currentDataset = dataset.Dataset(currentFile);

if args.user:
    mainAnswer = "";
    secondAnswer = "";
    while mainAnswer != "q":
        print("Que voulez-vous faire ?");
        print("    f - Afficher les informations sur le fichier");
        print("    d - Afficher les informations sur les donnees");
        print("    q - Quitter\n");
        
        mainAnswer = raw_input("Reponse: ");
        clear();
        
        while (secondAnswer != "r"):
            
            print("Quelle informations voulez-vous afficher ?");
                
            if (mainAnswer == "f"):
                print("    t - Afficher la taille du fichier");
                print("    e - Afficher l'encodage du fichier");
                print("    d - Afficher la date de derniere modification du fichier");
                print("    a - Afficher l'ensemble des informations");
                print("    r - Retour au menu principal\n");
                
            elif (mainAnswer == "d"):
                print("    t - Afficher q");
                print("    e - Afficher qq");
                print("    r - Retour au menu principal\n");
                
            elif (mainAnswer == "q"):
                break;
            
            else:
                print("Commande invalide\n");
            
            secondAnswer = raw_input("Reponse: ");
            clear();
                
            if (secondAnswer == "t"):
                print("Taille du fichier: " + str(currentFile.getSize()) + "\n");
                
            elif (secondAnswer == "e"):
                print("Encodage: "+ str(currentFile.getEncoding()) + "\n");
                
            elif (secondAnswer == "d"):
                print("Date de derniere modification: "+ str(currentFile.getLastModificationDate()) + "\n");
                
            elif (secondAnswer == "a"):
                print("Taille du fichier: " + str(currentFile.getSize()));
                print("Encodage: "+ str(currentFile.getEncoding()));
                print("Date de derniere modification: "+ str(currentFile.getLastModificationDate()) + "\n");
                
            elif (secondAnswer == "r"):
                break;
            
            else:
                print("Commande invalide\n");
                
else:
    print("Taille du fichier: " + str(currentFile.getSize()));
    print("Date de derniere modification: "+ str(currentFile.getLastModificationDate()));
    print("Encodage: "+ str(currentFile.getEncoding()));

    print(currentDataset.getData());
    print(currentDataset.getColumnsTypes());
    print(currentDataset.getNbColumns());
    print(currentDataset.getNbLines());

    print("Liste variables qualitatives: " + currentDataset.getAnalyzer().getQualitativesVarList().__str__());
    print("Nombre variables qualitatives: " + currentDataset.getAnalyzer().getNbQualitativesVar().__str__());
    print("Liste variables qantitatives: " + currentDataset.getAnalyzer().getQuantitativesVarList().__str__());
    print("Nombre variables qantitatives: " + currentDataset.getAnalyzer().getNbQuantitativesVar().__str__());
    print("Les valeurs minimales des variables quantitatives sont: " + currentDataset.getAnalyzer().getMinValues().__str__());
    print("Les valeurs maximales des variables quantitatives sont: " + currentDataset.getAnalyzer().getMaxValues().__str__());
    print("Les valeurs medianes des variables quantitatives sont: " + currentDataset.getAnalyzer().getMedianValues().__str__());
    print("Les moyennes des variables quantitatives sont: " + currentDataset.getAnalyzer().getAverageValues().__str__());
    print("Les ecarts types des variables quantitatives sont: " + currentDataset.getAnalyzer().getStandardDeviationValues().__str__());

clear(False);
print("Bye !");
