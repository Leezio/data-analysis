import os, displayer;

# GUI class
class GUI:
    
    # Constructor
    def __init__(self, header, file, dataset):
        self.displayer = displayer.Displayer(header, file, dataset); 
    
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
            input("Appuyez sur une touche pour continuer ...");
            self.clear();
            self.getDisplayer().displayHeader();
        except SyntaxError:
            pass
    
    # Return displayer
    def getDisplayer(self):
        return self.displayer;
        
    # Return value of new input and clear current tty
    def newAnswer(self, text):
        value = input(text);
        self.clear();
        self.getDisplayer().displayHeader();
        return value;
        