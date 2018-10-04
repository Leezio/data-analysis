import argparse
import file
import dataset

parser = argparse.ArgumentParser();
parser.add_argument("-f","--filepath", nargs="?", help="Chemin du fichier de donnees");
parser.add_argument("-u","--user", action="store_true", help="Activer l'interaction utilisateur");
parser.add_argument("-l","--log", action="store_true", help="Activer l'enregistrement dans un fichier de log");
args=parser.parse_args(); 

currentFile = file.File(args.filepath);

currentDataset = dataset.Dataset(currentFile);

print("Taille du fichier: " + str(currentFile.size()))
print("Date de derniere modification: "+ str(currentFile.lastModification()))
print("Encodage: "+ str(currentFile.encoding()))

print(currentDataset.getData())

print(currentDataset.getColumnsTypes())