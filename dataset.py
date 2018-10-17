import pandas, analyzer;

# Dataset class
class Dataset:
    
    # Constructor
    def __init__(self, file):
        self.currentFile = file;
        self.data = pandas.read_csv(self.currentFile.filepath);
        self.currentAnalyzer = analyzer.Analyzer(self.data);
    
    # Return raw data in array
    def getData(self):
        return self.data;

    # Return columns types in array
    def getColumnsTypes(self):
        return self.data.dtypes;
    
    # Return number of columns
    def getNbColumns(self):
        return self.data.shape[1];
    
    # Return number of lines
    def getNbLines(self):
        return self.data.shape[0];
    
    # Return dataset analyzer instance
    def getAnalyzer(self):
        return self.currentAnalyzer;