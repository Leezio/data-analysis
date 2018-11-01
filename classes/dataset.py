from classes import analyzer;
import pandas;

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
        return self.data.shape[1].__str__();
    
    # Return number of lines
    def getNbLines(self):
        return self.data.shape[0].__str__();
    
    # Return dataset analyzer instance
    def getAnalyzer(self):
        return self.currentAnalyzer;
    
    # Create plot box as png
    def createPlotBox(self):
        self.data.plot.box().get_figure().savefig('plot-box.png');