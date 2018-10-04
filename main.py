import argparse
import fileinfo

parser = argparse.ArgumentParser();
parser.add_argument("-f","--file", nargs="?", help="Chemin du fichier de donnees");
parser.add_argument("-u","--user", action="store_true", help="Activer l'interaction utilisateur");
parser.add_argument("-l","--log", action="store_true", help="Activer l'enregistrement dans un fichier de log");
args=parser.parse_args(); 

print("Taille du fichier: : ",fileinfo.file_size(args.file))
print("Date de derniere modification: : ",fileinfo.file_modification(args.file))
print("Encodage: ",fileinfo.file_encoding(args.file))
