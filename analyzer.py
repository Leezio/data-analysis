# Analyzer class
class Analyzer:
    
    QUALITATIVE_OBJECT_TYPE = "object";
    QUANTITATIVE_FLOAT_TYPE = "float64";
    QUANTITATIVE_INT_TYPE = "int64";
    
    # Constructor
    def __init__(self, dataset):
        self.dataset = dataset;
    
    # Return number of qualitatives variables 
    def getNbQualitativesVar(self):
        return len(self.getQualitativesVarList());
    
    # Return a list with qualitatives variables
    def getQualitativesVarList(self):
        list = [];
        for i in range(0, len(self.dataset.dtypes)):
            if self.dataset.dtypes[i] == self.QUALITATIVE_OBJECT_TYPE:
                list.append(self.dataset.columns.values[i]);
        return list;
    
    # Return number of quantitatives variables
    def getNbQuantitativesVar(self):
        return len(self.getQuantitativesVarList());
    
    # Return a list with quantitatives variables
    def getQuantitativesVarList(self):
        list = [];
        for i in range(0, len(self.dataset.dtypes)):
            if self.dataset.dtypes[i] == self.QUANTITATIVE_FLOAT_TYPE or self.dataset.dtypes[i] == self.QUANTITATIVE_INT_TYPE:
                list.append(self.dataset.columns.values[i]);
        return list;
    
    # Return a list with minimal values of quantitatives variables by columns
    def getMinValues(self):
        list = [];
        for i in range(0, self.getNbQuantitativesVar()):
            list.append(self.getQuantitativesVarList()[i] + ": " + self.dataset[self.getQuantitativesVarList()[i]].min().__str__());
        return list;
    
    # Return a list with maximal values of quantitatives variables by columns
    def getMaxValues(self):
        list = [];
        for i in range(0, self.getNbQuantitativesVar()):
            list.append(self.getQuantitativesVarList()[i] + ": " + self.dataset[self.getQuantitativesVarList()[i]].max().__str__());
        return list;
    
    # Return a list with median of quantitatives variables by columns
    def getMedianValues(self):
        list = [];
        for i in range(0, self.getNbQuantitativesVar()):
            list.append(self.getQuantitativesVarList()[i] + ": " + self.dataset[self.getQuantitativesVarList()[i]].median().__str__());
        return list;
    
    # Return a list with average of quantitatives variables by columns
    def getAverageValues(self):
        list = [];
        for i in range(0, self.getNbQuantitativesVar()):
            list.append(self.getQuantitativesVarList()[i] + ": " + self.dataset[self.getQuantitativesVarList()[i]].mean().__str__());
        return list;

    # Return a list with standard deviation of quantitatives variables by columns
    def getStandardDeviationValues(self):
        list = [];
        for i in range(0, self.getNbQuantitativesVar()):
            list.append(self.getQuantitativesVarList()[i] + ": " + self.dataset[self.getQuantitativesVarList()[i]].std().__str__());
        return list;
    