import os, time, chardet

def file_size(fname):
    return os.stat(fname).st_size;

def file_extension(fname):
    return fname.split('.')[1];

def file_modification(fname):
    return time.asctime(time.localtime(os.stat(fname).st_mtime));

def file_encoding(fname):
    return chardet.detect(open(fname,"r").read());
