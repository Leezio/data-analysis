import os;

# Class log
class Log:
    
    # Constructor
    def __init__(self, filepath, file, dataset):
        try:
            os.remove(filepath)
        except OSError:
            pass
        self.logFile = open(filepath, "a");
        self.file = file;
        self.dataset = dataset;
        
    def write(self, text):
        self.logFile.write(text + "\n\n");
        
    def save(self):
        
        list = [];
        
        # Log all file informations
        list.append("Taille du fichier: " + self.file.getSize());
        list.append("Encodage: "+ self.file.getEncoding());
        list.append("Date de derniere modification: " + self.file.getLastModificationDate());
    
        # Log all data informations
        #list.append(currentDataset.getData().__str__());
        #list.append(currentDataset.getColumnsTypes().__str__());
        #list.append(currentDataset.getNbColumns());
        #list.append(currentDataset.getNbLines());
    
        # Log all qualitatives variables informations
        list.append("Nombre variables qualitatives: " + self.dataset.getAnalyzer().getNbQualitativesVar().__str__());
        list.append("Liste variables qualitatives: " + self.dataset.getAnalyzer().getQualitativesVarList().__str__());
        list.append("Les modalites des variables qualitatives sont: " + self.dataset.getAnalyzer().getModalityValues().__str__());
        list.append("Les effectifes des variables qualitatives sont: " + self.dataset.getAnalyzer().getEffectiveValues().__str__());
        list.append("Les frequences des variables qualitatives sont: " + self.dataset.getAnalyzer().getFrequencyValues().__str__());
    
        # Log all quantitatives variables informations
        list.append("Nombre variables qantitatives: " + self.dataset.getAnalyzer().getNbQuantitativesVar().__str__());
        list.append("Liste variables qantitatives: " + self.dataset.getAnalyzer().getQuantitativesVarList().__str__());
        list.append("Les valeurs minimales des variables quantitatives sont: " + self.dataset.getAnalyzer().getMinValues().__str__());
        list.append("Les valeurs maximales des variables quantitatives sont: " + self.dataset.getAnalyzer().getMaxValues().__str__());
        list.append("Les valeurs medianes des variables quantitatives sont: " + self.dataset.getAnalyzer().getMedianValues().__str__());
        list.append("Les moyennes des variables quantitatives sont: " + self.dataset.getAnalyzer().getAverageValues().__str__());
        list.append("Les ecarts types des variables quantitatives sont: " +  self.dataset.getAnalyzer().getStandardDeviationValues().__str__());
        
        for i in range(0, len(list)):
            self.write(list[i]);
            