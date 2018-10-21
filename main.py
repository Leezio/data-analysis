from classes import file, dataset, gui;
import argparse;

version = "v1.1";

parser = argparse.ArgumentParser();
parser.add_argument("-f","--filepath", nargs="?", help="Chemin du fichier de donnees");
parser.add_argument("-u","--user", action="store_true", help="Activer l'interaction utilisateur");
parser.add_argument("-l","--log", action="store_true", help="Activer l'enregistrement dans un fichier de log");
parser.add_argument("-v","--version", action="store_true", help="Retourne la version du script");
args=parser.parse_args();

if args.version:
    print(version);
    exit();

# End if

# Init file instance
currentFile = file.File(args.filepath);

# Init dataset instance
currentDataset = dataset.Dataset(currentFile);

# Init GUI instance
gui = gui.GUI("Data Analysis - " + version, currentFile, currentDataset);

gui.clear();
gui.getDisplayer().displayHeader();

# If user want options menu
if args.user:
    
    mainAnswer = secondAnswer = "";
    
    while (mainAnswer != gui.getDisplayer().MAIN_MENU_EXIT):
        
        gui.getDisplayer().displayMainMenu();
        
        mainAnswer = gui.newAnswer("Reponse: ");
        
        while (mainAnswer != gui.getDisplayer().MAIN_MENU_EXIT and secondAnswer != gui.getDisplayer().SECOND_MENU_RETURN):
            
            gui.getDisplayer().displaySecondMenu();
                
            if (mainAnswer == gui.getDisplayer().SECOND_MENU_FILE):
                gui.getDisplayer().displayFileMenu();
                
            elif (mainAnswer == gui.getDisplayer().SECOND_MENU_DATA):
                gui.getDisplayer().displayDataMenu();
        
            elif (mainAnswer == gui.getDisplayer().MAIN_MENU_EXIT):
                break;
            
            else:
                gui.getDisplayer().displayInvalidCommand();
            
            # End if
            
            secondAnswer = gui.newAnswer("Reponse: ");
                
            if (secondAnswer == gui.getDisplayer().FILE_INFORMATION_SIZE):
                gui.getDisplayer().displayFileSize();
                
            elif (secondAnswer == gui.getDisplayer().FILE_INFORMATION_ENCODING):
                gui.getDisplayer().displayFileEncoding();
                
            elif (secondAnswer == gui.getDisplayer().FILE_INFORMATION_DATE):
                gui.getDisplayer().displayLastFileModificationDate();
                
            elif (secondAnswer == gui.getDisplayer().FILE_INFORMATION_ALL):
                # Display all file informations
                gui.getDisplayer().displayFileSize();
                gui.getDisplayer().displayFileEncoding();
                gui.getDisplayer().displayLastFileModificationDate();
                
            elif (secondAnswer == gui.getDisplayer().DATA_INFORMATION_QUANTITATIVES):
                # Display quantitatives variables informations
               gui.getDisplayer().displayNbQuantitativesVar();
               gui.getDisplayer().displayQuantitativesVarList();
               gui.getDisplayer().displayMinValues();
               gui.getDisplayer().displayMaxValues();
               gui.getDisplayer().displayMedianValues();
               gui.getDisplayer().displayAverageValues();
               gui.getDisplayer().displayStandardDeviationValues();
                
            elif (secondAnswer == gui.getDisplayer().DATA_INFORMATION_QUALITATIVES):
                # Display qualitatives variables informations
                gui.getDisplayer().displayNbQualitativesVar();
                gui.getDisplayer().displayQualitativesVarList();
                gui.getDisplayer().displayModalityValues();
                gui.getDisplayer().displayEffectiveValues();
                gui.getDisplayer().displayFrequencyValues();
                
            elif (secondAnswer == gui.getDisplayer().SECOND_MENU_RETURN):
                secondAnswer = False;
                break;
            
            else:
                gui.getDisplayer().displayInvalidCommand();
            
            # End if
            
            gui.pressAnyKey(); 
        
        # End while
        
    #End while      
else:
    # Display all file informations
    gui.getDisplayer().displayFileSize();
    gui.getDisplayer().displayFileEncoding();
    gui.getDisplayer().displayLastFileModificationDate();
    
    # Display all data informations
    gui.getDisplayer().displayData();
    gui.getDisplayer().displayColumnsTypes();
    gui.getDisplayer().displayNbColumns();
    gui.getDisplayer().displayNbLines();
    
    # Display all qualitatives variables informations
    gui.getDisplayer().displayNbQualitativesVar();
    gui.getDisplayer().displayQualitativesVarList();
    gui.getDisplayer().displayModalityValues();
    gui.getDisplayer().displayEffectiveValues();
    gui.getDisplayer().displayFrequencyValues();
    
    # Display all quantitatives variables informations
    gui.getDisplayer().displayNbQuantitativesVar();
    gui.getDisplayer().displayQuantitativesVarList();
    gui.getDisplayer().displayMinValues();
    gui.getDisplayer().displayMaxValues();
    gui.getDisplayer().displayMedianValues();
    gui.getDisplayer().displayAverageValues();
    gui.getDisplayer().displayStandardDeviationValues();

# End if

gui.pressAnyKey();

gui.clear();

print("Bye !");
