import os;

# Class log
class Log:

    # Constructor
    def __init__(self, filepath, file, dataset, l10n):
        try:
            os.remove(filepath)
        except OSError:
            pass
        self.logFile = open(filepath, "a");
        self.file = file;
        self.dataset = dataset;
        self.l10n = l10n;

    def write(self, text):
        self.logFile.write(text + "\n\n");

    def save(self):
        list = [];
        
        # Log all file informations
        list.append(self.l10n.getL10n("FILE_SIZE") + " " + self.file.getSize());
        list.append(self.l10n.getL10n("FILE_DATE") + " " + self.file.getLastModificationDate());
        list.append(self.l10n.getL10n("FILE_ENCODING") + " " + self.file.getEncoding());

        # Log all data informations
        list.append(self.l10n.getL10n("DATA_NB_COLUMNS") + " " + self.dataset.getNbColumns());
        list.append(self.l10n.getL10n("DATA_NB_LINES") + " " + self.dataset.getNbLines());
        list.append(self.l10n.getL10n("DATA_NB_VAR_QUALI") + " " + self.dataset.getAnalyzer().getNbQualitativesVar().__str__());
        list.append(self.l10n.getL10n("DATA_LIST_VAR_QUALI") + " " + self.dataset.getAnalyzer().getQualitativesVarList().__str__());
        list.append(self.l10n.getL10n("DATA_NB_VAR_QUANT") + " " + self.dataset.getAnalyzer().getNbQuantitativesVar().__str__());
        list.append(self.l10n.getL10n("DATA_LIST_VAR_QUANT") + " " + self.dataset.getAnalyzer().getQuantitativesVarList().__str__());

        # Log all qualitatives variables informations
        list.append(self.l10n.getL10n("DATA_MOD_QUALI") + " " + self.dataset.getAnalyzer().getModalityValues().__str__());
        list.append(self.l10n.getL10n("DATA_EFF_QUALI") + " " + self.dataset.getAnalyzer().getEffectiveValues().__str__());
        list.append(self.l10n.getL10n("DATA_FREQ_QUALI") + " " + self.dataset.getAnalyzer().getFrequencyValues().__str__());

        # Log all quantitatives variables informations
        list.append(self.l10n.getL10n("DATA_MIN_QUANT") + " " + self.dataset.getAnalyzer().getMinValues().__str__());
        list.append(self.l10n.getL10n("DATA_MAX_QUANT") + " " + self.dataset.getAnalyzer().getMaxValues().__str__());
        list.append(self.l10n.getL10n("DATA_MED_QUANT") + " " +  self.dataset.getAnalyzer().getMedianValues().__str__());
        list.append(self.l10n.getL10n("DATA_AVG_QUANT") + " " +  self.dataset.getAnalyzer().getAverageValues().__str__());
        list.append(self.l10n.getL10n("DATA_SDV_QUANT") + " " +  self.dataset.getAnalyzer().getStandardDeviationValues().__str__());

        for i in range(0, len(list)):
            self.write(list[i]);
