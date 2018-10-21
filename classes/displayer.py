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
    
    # Override print function and add breakline
    def printr(self, value):
        print(value + "\n");
        
    # Display header
    def displayHeader(self):
        self.printr(self.header);
        
    # Display file size
    def displayFileSize(self):
        self.printr("Taille du fichier: " + self.file.getSize());
        
    # Display last file modification date
    def displayLastFileModificationDate(self):
        self.printr("Date de derniere modification: "+ self.file.getLastModificationDate());
        
    # Display file encoding
    def displayFileEncoding(self):
        self.printr("Encodage: "+ self.file.getEncoding());

    # Display data
    def displayData(self):
        print(self.dataset.getData());

    # Display columns types
    def displayColumnsTypes(self):
        print(self.dataset.getColumnsTypes());

    # Display number of columns
    def displayNbColumns(self):
        self.printr(self.dataset.getNbColumns());

    # Display number of line
    def displayNbLines(self):
        self.printr(self.dataset.getNbLines());

    # Dislpay number of qualitatices varibales
    def displayNbQualitativesVar(self):
        self.printr("Nombre variables qualitatives: " + self.dataset.getAnalyzer().getNbQualitativesVar().__str__());

    # Display list of qualitatives variable
    def displayQualitativesVarList(self):
        self.printr("Liste variables qualitatives: " + self.dataset.getAnalyzer().getQualitativesVarList().__str__());

    # Display list with modality of qualitatives variables
    def displayModalityValues(self):
        self.printr("Les modalites des variables qualitatives sont: " + self.dataset.getAnalyzer().getModalityValues().__str__());

    # Display a list with effective of qualitatives variables
    def displayEffectiveValues(self):
        self.printr("Les effectifes des variables qualitatives sont: " + self.dataset.getAnalyzer().getEffectiveValues().__str__());

    # Display number of quantitatives variables
    def displayNbQuantitativesVar(self):
        self.printr("Nombre variables qantitatives: " + self.dataset.getAnalyzer().getNbQuantitativesVar().__str__());

    # Display list of quantitatives variables
    def displayQuantitativesVarList(self):
        self.printr("Liste variables qantitatives: " + self.dataset.getAnalyzer().getQuantitativesVarList().__str__());

    # Display list with minimal values of quantitatives variables
    def displayMinValues(self):
        self.printr("Les valeurs minimales des variables quantitatives sont: " + self.dataset.getAnalyzer().getMinValues().__str__());

    # Display list with maximal values of quantitatives variables
    def displayMaxValues(self):
        self.printr("Les valeurs maximales des variables quantitatives sont: " + self.dataset.getAnalyzer().getMaxValues().__str__());

    # Display list with median of quantitatives variables
    def displayMedianValues(self):
        self.printr("Les valeurs medianes des variables quantitatives sont: " + self.dataset.getAnalyzer().getMedianValues().__str__());

    # Display list with average of quantitatives variables
    def displayAverageValues(self):
        self.printr("Les moyennes des variables quantitatives sont: " + self.dataset.getAnalyzer().getAverageValues().__str__());

    # Display list with standard deviation of quantitatives variables
    def displayStandardDeviationValues(self):
        self.printr("Les ecarts types des variables quantitatives sont: " + self.dataset.getAnalyzer().getStandardDeviationValues().__str__());
       
    # Display main menu 
    def displayMainMenu(self):
        self.printr("Que voulez-vous faire ?");
        print("\u0009" + self.SECOND_MENU_FILE + " - Afficher les informations sur le fichier");
        print("\u0009" + self.SECOND_MENU_DATA + " - Afficher les informations sur les donnees");
        self.printr("\u0009" + self.MAIN_MENU_EXIT + " - Quitter")
     
    # Display second menu   
    def displaySecondMenu(self):
        self.printr("Quelle informations voulez-vous afficher ?");
    
    # Display file menu    
    def displayFileMenu(self):
        print("\u0009" + self.FILE_INFORMATION_SIZE + " - Afficher la taille du fichier");
        print("\u0009" + self.FILE_INFORMATION_ENCODING + " - Afficher l'encodage du fichier");
        print("\u0009" + self.FILE_INFORMATION_DATE + " - Afficher la date de derniere modification du fichier");
        print("\u0009" + self.FILE_INFORMATION_ALL + " - Afficher l'ensemble des informations");
        self.printr("\u0009" + self.SECOND_MENU_RETURN + " - Retour au menu principal")
     
    # Display data menu
    def displayDataMenu(self):
        print("\u0009" + self.DATA_INFORMATION_QUANTITATIVES + " - Afficher les informations sur les variables quantitatives");
        print("\u0009" + self.DATA_INFORMATION_QUALITATIVES + " - Afficher les informations sur les variables qualitatives");
        self.printr("\u0009" + self.SECOND_MENU_RETURN + " - Retour au menu principal")
    
    # Display invalid command message    
    def displayInvalidCommand(self):
        self.printr("Commande invalide")
    