import argparse, file, dataset, gui;

parser = argparse.ArgumentParser();
parser.add_argument("-f","--filepath", nargs="?", help="Chemin du fichier de donnees");
parser.add_argument("-u","--user", action="store_true", help="Activer l'interaction utilisateur");
parser.add_argument("-l","--log", action="store_true", help="Activer l'enregistrement dans un fichier de log");
args=parser.parse_args();

currentFile = file.File(args.filepath);

currentDataset = dataset.Dataset(currentFile);

gui = gui.GUI("Data Analysis - v1.1", currentFile, currentDataset);

gui.clear();
gui.getDisplayer().displayHeader();

if args.user:
    mainAnswer = "";
    secondAnswer = "";
    while mainAnswer != "q":
        gui.getDisplayer().displayMainMenu();
        
        mainAnswer = gui.newAnswer("Reponse: ");
        
        while (secondAnswer != "r"):
            
            gui.getDisplayer().displaySecondMenu();
                
            if (mainAnswer == "f"):
                gui.getDisplayer().displayFileMenu();
                
            elif (mainAnswer == "d"):
                gui.getDisplayer().displayDataMenu();
        
            elif (mainAnswer == "q"):
                break;
            
            else:
                gui.getDisplayer().displayInvalidCommand();
            
            secondAnswer = gui.newAnswer("Reponse: ");
                
            if (secondAnswer == "t"):
                gui.getDisplayer().displayFileSize();
                
            elif (secondAnswer == "e"):
                gui.getDisplayer().displayFileEncoding();
                
            elif (secondAnswer == "d"):
                gui.getDisplayer().displayLastFileModificationDate();
                
            elif (secondAnswer == "a"):
                gui.getDisplayer().displayFileSize();
                gui.getDisplayer().displayFileEncoding();
                gui.getDisplayer().displayLastFileModificationDate();
                
            elif (secondAnswer == "v"):
               gui.getDisplayer().displayNbQuantitativesVar();
               gui.getDisplayer().displayQuantitativesVarList();
               gui.getDisplayer().displayMinValues();
               gui.getDisplayer().displayMaxValues();
               gui.getDisplayer().displayMedianValues();
               gui.getDisplayer().displayAverageValues();
               gui.getDisplayer().displayStandardDeviationValues();
                
            elif (secondAnswer == "l"):
                gui.getDisplayer().displayNbQualitativesVar();
                gui.getDisplayer().displayQualitativesVarList();
                gui.getDisplayer().displayModalityValues();
                gui.getDisplayer().displayEffectiveValues();
                
            elif (secondAnswer == "r"):
                secondAnswer = False;
                break;
            
            else:
                gui.getDisplayer().displayInvalidCommand();
                
            gui.pressAnyKey();
                
else:
    gui.getDisplayer().displayFileSize();
    gui.getDisplayer().displayFileEncoding();
    gui.getDisplayer().displayLastFileModificationDate();
    
    gui.getDisplayer().displayData();
    gui.getDisplayer().displayColumnsTypes();
    gui.getDisplayer().displayNbColumns();
    gui.getDisplayer().displayNbLines();
    
    gui.getDisplayer().displayNbQualitativesVar();
    gui.getDisplayer().displayQualitativesVarList();
    gui.getDisplayer().displayModalityValues();
    gui.getDisplayer().displayEffectiveValues();
    
    gui.getDisplayer().displayNbQuantitativesVar();
    gui.getDisplayer().displayQuantitativesVarList();
    gui.getDisplayer().displayMinValues();
    gui.getDisplayer().displayMaxValues();
    gui.getDisplayer().displayMedianValues();
    gui.getDisplayer().displayAverageValues();
    gui.getDisplayer().displayStandardDeviationValues();

gui.clear();

print("Bye !");
