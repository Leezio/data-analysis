import numpy, os;

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

    DATA_INFORMATION_TABLE = "b";
    DATA_INFORMATION_QUANTITATIVES = "v";
    DATA_INFORMATION_QUALITATIVES = "l";
    DATA_INFORMATION_PLOT = "p";

    # Constructor
    def __init__(self, header, file, dataset, l10n):
        self.header = header;
        self.file = file;
        self.dataset = dataset;
        self.l10n = l10n;

    # Override print function and add breakline
    def printr(self, value = ""):
        print(value + "\n");

    # Display header
    def displayHeader(self):
        self.printr(self.header);

    # Display file size
    def displayFileSize(self):
        self.printr(self.l10n.getL10n("FILE_SIZE") + " " + self.file.getSize());

    # Display last file modification date
    def displayLastFileModificationDate(self):
        self.printr(self.l10n.getL10n("FILE_DATE") + " " + self.file.getLastModificationDate());

    # Display file encoding
    def displayFileEncoding(self):
        self.printr(self.l10n.getL10n("FILE_ENCODING") + " " + self.file.getEncoding());

    # Display data
    def displayData(self):
        print(self.dataset.getData());

    # Display columns types
    def displayColumnsTypes(self):
        print(self.dataset.getColumnsTypes());

    # Display number of columns
    def displayNbColumns(self):
        self.printr(self.l10n.getL10n("DATA_NB_COLUMNS") + " " + self.dataset.getNbColumns());

    # Display number of line
    def displayNbLines(self):
        self.printr(self.l10n.getL10n("DATA_NB_LINES") + " " + self.dataset.getNbLines());

    # Dislpay number of qualitatices varibales
    def displayNbQualitativesVar(self):
        self.printr(self.l10n.getL10n("DATA_NB_VAR_QUALI") + " " + self.dataset.getAnalyzer().getNbQualitativesVar().__str__());

    # Display list of qualitatives variable
    def displayQualitativesVarList(self):
        self.printr(self.l10n.getL10n("DATA_LIST_VAR_QUALI") + " " + self.dataset.getAnalyzer().getQualitativesVarList().__str__());

    # Display list with modality of qualitatives variables
    def displayModalityValues(self):
        self.printr(self.l10n.getL10n("DATA_MOD_QUALI") + " " + self.dataset.getAnalyzer().getModalityValues().__str__());

    # Display a list with effective of qualitatives variables
    def displayEffectiveValues(self):
        self.printr(self.l10n.getL10n("DATA_EFF_QUALI"));
        for i in range(0, len(self.dataset.getAnalyzer().getEffectiveValues())):
            print(self.dataset.getAnalyzer().getEffectiveValues()[i]);

    # Display a list with frequency of qualitatives variables
    def displayFrequencyValues(self):
        self.printr(self.l10n.getL10n("DATA_FREQ_QUALI"));
        for i in range(0, len(self.dataset.getAnalyzer().getFrequencyValues())):
            print(self.dataset.getAnalyzer().getFrequencyValues()[i]);

    # Display number of quantitatives variables
    def displayNbQuantitativesVar(self):
        self.printr(self.l10n.getL10n("DATA_NB_VAR_QUANT") + " " + self.dataset.getAnalyzer().getNbQuantitativesVar().__str__());

    # Display list of quantitatives variables
    def displayQuantitativesVarList(self):
        self.printr(self.l10n.getL10n("DATA_LIST_VAR_QUANT") + " " + self.dataset.getAnalyzer().getQuantitativesVarList().__str__());

    # Display list with minimal values of quantitatives variables
    def displayMinValues(self):
        self.printr(self.l10n.getL10n("DATA_MIN_QUANT") + " " + self.dataset.getAnalyzer().getMinValues().__str__());

    # Display list with maximal values of quantitatives variables
    def displayMaxValues(self):
        self.printr(self.l10n.getL10n("DATA_MAX_QUANT") + " " + self.dataset.getAnalyzer().getMaxValues().__str__());

    # Display list with median of quantitatives variables
    def displayMedianValues(self):
        self.printr(self.l10n.getL10n("DATA_MED_QUANT") + " " +  self.dataset.getAnalyzer().getMedianValues().__str__());

    # Display list with average of quantitatives variables
    def displayAverageValues(self):
        self.printr(self.l10n.getL10n("DATA_AVG_QUANT") + " " +  self.dataset.getAnalyzer().getAverageValues().__str__());

    # Display list with standard deviation of quantitatives variables
    def displayStandardDeviationValues(self):
        self.printr(self.l10n.getL10n("DATA_SDV_QUANT") + " " +  self.dataset.getAnalyzer().getStandardDeviationValues().__str__());

    def displayCreatePlotSuccess(self):
        self.printr(self.l10n.getL10n("PLOT_SUCCESS") + " " + os.getcwd());

    # Display main menu
    def displayMainMenu(self):
        self.printr(self.l10n.getL10n("QUEST_DO"));
        print("\u0009" + self.SECOND_MENU_FILE + " - " + self.l10n.getL10n("QUEST_FILE_INFO"));
        print("\u0009" + self.SECOND_MENU_DATA + " - " + self.l10n.getL10n("QUEST_DATA_INFO"));
        self.printr("\u0009" + self.MAIN_MENU_EXIT + " - " + self.l10n.getL10n("EXIT"))

    # Display second menu
    def displaySecondMenu(self):
        self.printr(self.l10n.getL10n("QUEST_DISPLAY"));

    # Display file menu
    def displayFileMenu(self):
        print("\u0009" + self.FILE_INFORMATION_SIZE + " - " + self.l10n.getL10n("QUEST_FILE_INFORMATION_SIZE"));
        print("\u0009" + self.FILE_INFORMATION_ENCODING + " - " + self.l10n.getL10n("QUEST_FILE_INFORMATION_ENCODING"));
        print("\u0009" + self.FILE_INFORMATION_DATE + " - " + self.l10n.getL10n("QUEST_FILE_INFORMATION_DATE"));
        print("\u0009" + self.FILE_INFORMATION_ALL + " - " + self.l10n.getL10n("QUEST_FILE_INFORMATION_ALL"));
        self.printr("\u0009" + self.SECOND_MENU_RETURN + " - " + self.l10n.getL10n("RETURN"))

    # Display data menu
    def displayDataMenu(self):
        print("\u0009" + self.DATA_INFORMATION_TABLE + " - " + self.l10n.getL10n("QUEST_DATA_INFORMATION_TABLE"));
        print("\u0009" + self.DATA_INFORMATION_QUANTITATIVES + " - " + self.l10n.getL10n("QUEST_DATA_INFORMATION_QUANTITATIVES"));
        print("\u0009" + self.DATA_INFORMATION_QUALITATIVES + " - " + self.l10n.getL10n("QUEST_DATA_INFORMATION_QUALITATIVES"));
        print("\u0009" + self.DATA_INFORMATION_PLOT + " - " + self.l10n.getL10n("QUEST_DATA_INFORMATION_PLOT"));
        self.printr("\u0009" + self.SECOND_MENU_RETURN + " - " + self.l10n.getL10n("RETURN"))

    # Display invalid command message
    def displayInvalidCommand(self):
        self.printr(self.l10n.getL10n("ERROR"))
