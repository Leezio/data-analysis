# Dataset class
class Displayer:
    
    # Constructor
    def __init__(self, header, file, dataset):
        self.header = header;
        self.file = file;
        self.dataset = dataset;
        
    def printr(self, value):
        print(value + "\n");
        
    def displayHeader(self):
        self.printr(self.header);
        
    def displayFileSize(self):
        self.printr("Taille du fichier: " + self.file.getSize());
        
    def displayLastFileModificationDate(self):
        self.printr("Date de derniere modification: "+ self.file.getLastModificationDate());
        
    def displayFileEncoding(self):
        self.printr("Encodage: "+ self.file.getEncoding());

    def displayData(self):
        self.printr(self.dataset.getData());

    def displayColumnsTypes(self):
        self.printr(cself.dataset.getColumnsTypes());

    def displayNbColumns(self):
        self.printr(self.dataset.getNbColumns());

    def displayNbLines(self):
        self.printr(self.dataset.getNbLines());

    def displayNbQualitativesVar(self):
        self.printr("Nombre variables qualitatives: " + self.dataset.getAnalyzer().getNbQualitativesVar().__str__());

    def displayQualitativesVarList(self):
        self.printr("Liste variables qualitatives: " + self.dataset.getAnalyzer().getQualitativesVarList().__str__());

    def displayModalityValues(self):
        self.printr("Les modalites des variables qualitatives sont: " + self.dataset.getAnalyzer().getModalityValues().__str__());

    def displayEffectiveValues(self):
        self.printr("Les effectifes des variables qualitatives sont: " + self.dataset.getAnalyzer().getEffectiveValues().__str__());

    def displayNbQuantitativesVar(self):
        self.printr("Nombre variables qantitatives: " + self.dataset.getAnalyzer().getNbQuantitativesVar().__str__());

    def displayQuantitativesVarList(self):
        self.printr("Liste variables qantitatives: " + self.dataset.getAnalyzer().getQuantitativesVarList().__str__());

    def displayMinValues(self):
        self.printr("Les valeurs minimales des variables quantitatives sont: " + self.dataset.getAnalyzer().getMinValues().__str__());

    def displayMaxValues(self):
        self.printr("Les valeurs maximales des variables quantitatives sont: " + self.dataset.getAnalyzer().getMaxValues().__str__());

    def displayMedianValues(self):
        self.printr("Les valeurs medianes des variables quantitatives sont: " + self.dataset.getAnalyzer().getMedianValues().__str__());

    def displayAverageValues(self):
        self.printr("Les moyennes des variables quantitatives sont: " + self.dataset.getAnalyzer().getAverageValues().__str__());

    def displayStandardDeviationValues(self):
        self.printr("Les ecarts types des variables quantitatives sont: " + self.dataset.getAnalyzer().getStandardDeviationValues().__str__());
        
    def displayMainMenu(self):
        print("Que voulez-vous faire ?");
        print("    f - Afficher les informations sur le fichier");
        print("    d - Afficher les informations sur les donnees");
        self.printr("    q - Quitter")
        
    def displaySecondMenu(self):
        print("Quelle informations voulez-vous afficher ?");
        
    def displayFileMenu(self):
        print("    t - Afficher la taille du fichier");
        print("    e - Afficher l'encodage du fichier");
        print("    d - Afficher la date de derniere modification du fichier");
        print("    a - Afficher l'ensemble des informations");
        self.printr("    r - Retour au menu principal")
     
    def displayDataMenu(self):
        print("    v - Afficher les informations sur les variables quantitatives");
        print("    l - Afficher les informations sur les variables qualitatives");
        self.printr("    r - Retour au menu principal")
        
    def displayInvalidCommand(self):
        self.printr("Commande invalide")
    