import argparse, file, dataset;

parser = argparse.ArgumentParser();
parser.add_argument("-f","--filepath", nargs="?", help="Chemin du fichier de donnees");
parser.add_argument("-u","--user", action="store_true", help="Activer l'interaction utilisateur");
parser.add_argument("-l","--log", action="store_true", help="Activer l'enregistrement dans un fichier de log");
args=parser.parse_args(); 

currentFile = file.File(args.filepath);

currentDataset = dataset.Dataset(currentFile);

print("Taille du fichier: " + str(currentFile.size()));
print("Date de derniere modification: "+ str(currentFile.lastModification()));
print("Encodage: "+ str(currentFile.encoding()));

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
 