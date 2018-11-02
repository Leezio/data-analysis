import os, time, chardet, magic;

# File class
class File:
    
    # Constructor
    def __init__(self, filepath, l10n):
        self.filepath = filepath;
        self.l10n = l10n;
        try:
            self.file = os.stat(self.filepath); 
        except os.error:
            print(self.l10n.getL10n("FILE_NOT_FOUND"));
            exit();
    
    # Return the file size
    def getSize(self):
        return self.file.st_size.__str__();

    # Return the file extension
    def getExtension(self):
        return self.filepath.split('.')[1].__str__();

    # Return the last modification date of file
    def getLastModificationDate(self):
        return time.asctime(time.localtime(self.file.st_mtime)).__str__();

    # Return the file encoding
    def getEncoding(self):
        return magic.Magic(mime_encoding=True).from_buffer(open(self.filepath).read());