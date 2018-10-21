import os;

# GUI class
class GUI:
    
    # Constructor
    def __init__(self, header):
        self.header = header + "\n";
    
    # Allow to clear console
    def clear(self): 
        # For windows 
        if os.name == 'nt': 
            _ = os.system('cls');
  
        # For mac and linux(here, os.name is 'posix') 
        else: 
            _ = os.system('clear');
       
    # Wait the user press any key       
    def pressAnyKey(self):
        try:
            input("Appuyez sur une touhe pour continuer ...");
        except SyntaxError:
            pass
        
    # Return GUI header    
    def getHeader(self):
        return self.header;