from classes import l10n, file, dataset, gui, log;
import argparse;

try:
    
    version = "v1.4";

    parser = argparse.ArgumentParser();
    parser.add_argument("-f","--filepath", nargs="?", help="Chemin du fichier de donnees");
    parser.add_argument("-u","--user", action="store_true", help="Activer l'interaction utilisateur");
    parser.add_argument("-l","--log", action="store_true", help="Activer l'enregistrement dans un fichier de log");
    parser.add_argument("-v","--version", action="store_true", help="Retourne la version du script");
    args=parser.parse_args();

    # Display script version
    if args.version:
        print(version);
        exit();

    # End if

    # Init l10n instance
    currentL10n = l10n.L10n("fr");

    # Init file instance
    currentFile = file.File(args.filepath, currentL10n);

    # Init dataset instance
    currentDataset = dataset.Dataset(currentFile);

    # Init GUI instance
    gui = gui.GUI("Data Analysis - " + version, currentFile, currentDataset, currentL10n);

    gui.clear();
    gui.getDisplayer().displayHeader();

    # If user want options menu
    if args.user:
    
        if args.log:
            currentLogFile = log.Log("log.txt", currentFile, currentDataset);
            currentLogFile.save();
    
        mainAnswer = secondAnswer = "";
    
        while (mainAnswer != gui.getDisplayer().MAIN_MENU_EXIT):
        
            gui.getDisplayer().displayMainMenu();
        
            mainAnswer = gui.newAnswer(currentL10n.getL10n("ANSWER") + " ");
        
            while (mainAnswer != gui.getDisplayer().MAIN_MENU_EXIT and secondAnswer != gui.getDisplayer().SECOND_MENU_RETURN):
                 
                if (mainAnswer == gui.getDisplayer().SECOND_MENU_FILE):
                    gui.getDisplayer().displaySecondMenu();
                    gui.getDisplayer().displayFileMenu();
                
                elif (mainAnswer == gui.getDisplayer().SECOND_MENU_DATA):
                    gui.getDisplayer().displaySecondMenu();
                    gui.getDisplayer().displayDataMenu();
        
                elif (mainAnswer == gui.getDisplayer().MAIN_MENU_EXIT):
                    break;
            
                else:
                    gui.getDisplayer().displayInvalidCommand();
                    break;
            
                # End if
            
                secondAnswer = gui.newAnswer(currentL10n.getL10n("ANSWER") + " ");
                
                if (secondAnswer == gui.getDisplayer().FILE_INFORMATION_SIZE):
                    gui.getDisplayer().displayFileSize();
                
                elif (secondAnswer == gui.getDisplayer().FILE_INFORMATION_ENCODING):
                    gui.getDisplayer().displayFileEncoding();
                
                elif (secondAnswer == gui.getDisplayer().FILE_INFORMATION_DATE):
                    gui.getDisplayer().displayLastFileModificationDate();
                
                elif (secondAnswer == gui.getDisplayer().FILE_INFORMATION_ALL):
                    # Display all file informations
                    gui.getDisplayer().displayAllFileInformations();
                
                elif (secondAnswer == gui.getDisplayer().DATA_INFORMATION_TABLE):
                    # Display all data informations
                    gui.getDisplayer().displayAllDataInformations();
                
                elif (secondAnswer == gui.getDisplayer().DATA_INFORMATION_QUANTITATIVES):
                    # Display quantitatives variables informations
                    gui.getDisplayer().displayAllQualitativesVariablesInformations();
                
                elif (secondAnswer == gui.getDisplayer().DATA_INFORMATION_QUALITATIVES):
                    # Display qualitatives variables informations
                    gui.getDisplayer().displayAllQuantitativesVariablesInformations();
                
                elif (secondAnswer == gui.getDisplayer().DATA_INFORMATION_PLOT):
                    # Create plot box
                    gui.getDisplayer().displayCreatePlotSuccess();
                    currentDataset.createPlotBox();
                
                elif (secondAnswer == gui.getDisplayer().SECOND_MENU_RETURN):
                    secondAnswer = False;
                    break;
            
                else:
                    gui.getDisplayer().displayInvalidCommand();
                    break;
            
                # End if
            
                gui.pressAnyKey(); 
        
            # End while
        
        #End while      
    else:
    
        gui.getDisplayer().displayAll();
    
        # Create plot box
        gui.getDisplayer().displayCreatePlotSuccess();
        currentDataset.createPlotBox();
    
        # Enable log file
        if args.log:
            currentLogFile = log.Log("log.txt", currentFile, currentDataset, currentL10n);
            currentLogFile.save();
    
        # End if

        gui.pressAnyKey();
    
    # End if

    gui.clear();

    print(currentL10n.getL10n("BYE"));

except (KeyboardInterrupt):
    exit();
