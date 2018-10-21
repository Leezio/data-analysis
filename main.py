import argparse, file, dataset, gui;

parser = argparse.ArgumentParser();
parser.add_argument("-f","--filepath", nargs="?", help="Chemin du fichier de donnees");
parser.add_argument("-u","--user", action="store_true", help="Activer l'interaction utilisateur");
parser.add_argument("-l","--log", action="store_true", help="Activer l'enregistrement dans un fichier de log");
args=parser.parse_args();

gui = gui.GUI("Data Analysis - v1.1");

gui.clear();
print(gui.getHeader());

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
        
        mainAnswer = input("Reponse: ");
        gui.clear();
        print(gui.getHeader());
        
        while (secondAnswer != "r"):
            
            print("Quelle informations voulez-vous afficher ?");
                
            if (mainAnswer == "f"):
                print("    t - Afficher la taille du fichier");
                print("    e - Afficher l'encodage du fichier");
                print("    d - Afficher la date de derniere modification du fichier");
                print("    a - Afficher l'ensemble des informations");
                print("    r - Retour au menu principal\n");
                
            elif (mainAnswer == "d"):
                print("    v - Afficher les informations sur les variables quantitatives");
                print("    l - Afficher les informations sur les variables qualitatives");
                print("    r - Retour au menu principal\n");
                
            elif (mainAnswer == "q"):
                break;
            
            else:
                print("Commande invalide\n");
            
            secondAnswer = input("Reponse: ");
            gui.clear();
            print(gui.getHeader());
                
            if (secondAnswer == "t"):
                print("Taille du fichier: " + currentFile.getSize() + "\n");
                
            elif (secondAnswer == "e"):
                print("Encodage: "+ currentFile.getEncoding() + "\n");
                
            elif (secondAnswer == "d"):
                print("Date de derniere modification: "+ currentFile.getLastModificationDate() + "\n");
                
            elif (secondAnswer == "a"):
                print("Taille du fichier: " + currentFile.getSize());
                print("Encodage: "+ currentFile.getEncoding());
                print("Date de derniere modification: "+ currentFile.getLastModificationDate() + "\n");
                
            elif (secondAnswer == "v"):
                print("Liste variables qantitatives: " + currentDataset.getAnalyzer().getQuantitativesVarList().__str__() + "\n");
                print("Nombre variables qantitatives: " + currentDataset.getAnalyzer().getNbQuantitativesVar().__str__() + "\n");
                print("Les valeurs minimales des variables quantitatives sont: " + currentDataset.getAnalyzer().getMinValues().__str__() + "\n");
                print("Les valeurs maximales des variables quantitatives sont: " + currentDataset.getAnalyzer().getMaxValues().__str__() + "\n");
                print("Les valeurs medianes des variables quantitatives sont: " + currentDataset.getAnalyzer().getMedianValues().__str__() + "\n");
                print("Les moyennes des variables quantitatives sont: " + currentDataset.getAnalyzer().getAverageValues().__str__() + "\n");
                print("Les ecarts types des variables quantitatives sont: " + currentDataset.getAnalyzer().getStandardDeviationValues().__str__() + "\n");

                
            elif (secondAnswer == "l"):
                print("Taille du fichier: " + currentFile.getSize());
                print("Encodage: "+ currentFile.getEncoding());
                print("Date de derniere modification: "+ currentFile.getLastModificationDate() + "\n");
                
            elif (secondAnswer == "r"):
                secondAnswer = False;
                break;
            
            else:
                print("Commande invalide\n");
                
            gui.pressAnyKey();
            gui.clear();
            print(gui.getHeader());
                
else:
    print("Taille du fichier: " + currentFile.getSize() + "\n");
    print("Date de derniere modification: "+ currentFile.getLastModificationDate() + "\n");
    print("Encodage: "+ currentFile.getEncoding() + "\n");

    print(currentDataset.getData() + "\n");
    print(currentDataset.getColumnsTypes() + "\n");
    print(currentDataset.getNbColumns() + "\n");
    print(currentDataset.getNbLines() + "\n");

    print("Liste variables qualitatives: " + currentDataset.getAnalyzer().getQualitativesVarList().__str__() + "\n");
    print("Nombre variables qualitatives: " + currentDataset.getAnalyzer().getNbQualitativesVar().__str__() + "\n");
    print("Liste variables qantitatives: " + currentDataset.getAnalyzer().getQuantitativesVarList().__str__() + "\n");
    print("Nombre variables qantitatives: " + currentDataset.getAnalyzer().getNbQuantitativesVar().__str__() + "\n");
    print("Les valeurs minimales des variables quantitatives sont: " + currentDataset.getAnalyzer().getMinValues().__str__() + "\n");
    print("Les valeurs maximales des variables quantitatives sont: " + currentDataset.getAnalyzer().getMaxValues().__str__() + "\n");
    print("Les valeurs medianes des variables quantitatives sont: " + currentDataset.getAnalyzer().getMedianValues().__str__() + "\n");
    print("Les moyennes des variables quantitatives sont: " + currentDataset.getAnalyzer().getAverageValues().__str__() + "\n");
    print("Les ecarts types des variables quantitatives sont: " + currentDataset.getAnalyzer().getStandardDeviationValues().__str__() + "\n");

gui.clear();
print("Bye !");
