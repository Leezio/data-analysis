import pandas 

# Dataset class
class Dataset:
    
    def __init__(self, file):
        self.file = file;
        self.data = pandas.read_csv(self.file.filepath);
    
    # Return the file size
    def getData(self):
        return self.data;

    # Return the file size
    def getColumnsTypes(self):
        return self.data.dtypes;