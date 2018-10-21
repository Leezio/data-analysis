# Dataset class
class Displayer:
    
    MAIN_MENU_EXIT = "q";
    SECOND_MENU_RETURN = "r";
    SECOND_MENU_FILE = "f";
    SECOND_MENU_DATA = "d";
    FILE_INFORMATION_SIZE = "t";
    FILE_INFORMATION_ENCODING = "e";
    FILE_INFORMATION_DATE = "d";
    FILE_INFORMATION_ALL = "a";
    DATA_INFORMATION_QUANTITATIVES = "v";
    DATA_INFORMATION_QUALITATIVES = "l";
    
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
        print("    " + self.SECOND_MENU_FILE + " - Afficher les informations sur le fichier");
        print("    " + self.SECOND_MENU_DATA + " - Afficher les informations sur les donnees");
        self.printr("    " + self.MAIN_MENU_EXIT + " - Quitter")
        
    def displaySecondMenu(self):
        print("Quelle informations voulez-vous afficher ?");
        
    def displayFileMenu(self):
        print("    " + self.FILE_INFORMATION_SIZE + " - Afficher la taille du fichier");
        print("    " + self.FILE_INFORMATION_ENCODING + " - Afficher l'encodage du fichier");
        print("    " + self.FILE_INFORMATION_DATE + " - Afficher la date de derniere modification du fichier");
        print("    " + self.FILE_INFORMATION_ALL + " - Afficher l'ensemble des informations");
        self.printr("    " + self.SECOND_MENU_RETURN + " - Retour au menu principal")
     
    def displayDataMenu(self):
        print("    " + self.DATA_INFORMATION_QUANTITATIVES + " - Afficher les informations sur les variables quantitatives");
        print("    " + self.DATA_INFORMATION_QUALITATIVES + " - Afficher les informations sur les variables qualitatives");
        self.printr("    " + self.SECOND_MENU_RETURN + " - Retour au menu principal")
        
    def displayInvalidCommand(self):
        self.printr("Commande invalide")
    