import os, time, chardet, magic;

# File class
class File:
    
    # Constructor
    def __init__(self, filepath):
        self.filepath = filepath; 
    
    # Return the file size
    def getSize(self):
        return os.stat(self.filepath).st_size.__str__();

    # Return the file extension
    def getExtension(self):
        return self.filepath.split('.')[1].__str__();

    # Return the last modification date of file
    def getLastModificationDate(self):
        return time.asctime(time.localtime(os.stat(self.filepath).st_mtime)).__str__();

    # Return the file encoding
    def getEncoding(self):
        return magic.Magic(mime_encoding=True).from_buffer(open(self.filepath).read());