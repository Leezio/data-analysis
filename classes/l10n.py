import configparser, os;

# L10n class
class L10n:
    
    # Constructor
    def __init__(self, language):
        currentCwd = os.getcwd();
        os.chdir("./classes/l10n");
        self.config = configparser.ConfigParser();
        self.config.read(language + ".ini");
        os.chdir(currentCwd);
        
    # Return l10n object
    def getL10n(self, key):
        return self.config['DEFAULT'][key];