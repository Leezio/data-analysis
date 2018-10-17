import os, time, chardet;

# File class
class File:
    
    # Constructor
    def __init__(self, filepath):
        self.filepath = filepath; 
    
    # Return the file size
    def getSize(self):
        return os.stat(self.filepath).st_size;

    # Return the file extension
    def getExtension(self):
        return self.filepath.split('.')[1];

    # Return the last modification date of file
    def getLastModificationDate(self):
        return time.asctime(time.localtime(os.stat(self.filepath).st_mtime));

    # Return the file encoding
    def getEncoding(self):
        return chardet.detect(open(self.filepath,"r").read()).get("encoding");
        # Other solution, but more slow
        #import magic
        #return magic.Magic(mime_encoding=True).from_buffer(open(self.filepath).read());