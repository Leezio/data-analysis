import argparse

parser = argparse.ArgumentParser();
parser.add_argument("-f","--file", nargs="+", help="Chemin du fichier de données");
parser.add_argument("-u","--user", action="store_true", help="Activer l'interaction utilisateur");
parser.add_argument("-l","--log", action="store_true", help="Activer l'enregistrement dans un fichier de log");
args=parser.parse_args();

print(args);