import os
import os.path
import time

from scripts import status

from scripts import splashscreen
from scripts import calculator
from scripts import debug

def __mainloop__():

    #perform all checking functions on startup
    if (status.at_splash):
        check_for_folders()
        check_for_debug_file()
        log_startup()
    
    #initiate the splash screen
    if (status.at_splash):
        splashscreen.show_splash()
        time.sleep(5)
        status.at_splash = False
        status.at_calculator = True
    #initiate the calculator
    elif (status.at_calculator):
        calculator.show_calculator()

    #loop the mainloop
    time.sleep(0.01)
    __mainloop__()


def log_startup():
    debug.write_session_time()
    debug.log("started up program")


def check_for_folders():

    #check for calculations folder and create it if it does not exist
    if (os.path.exists(status.calculations_folder_location)):
        status.calculations_folder_exists = True
    else:
        os.mkdir(status.calculations_folder_name)

    #check for debug folder and create it if it does not exist
    if (os.path.exists(status.debug_folder_location)):
        status.debug_folder_exists = True
    else:
        os.mkdir(status.debug_folder_name)

def check_for_debug_file():

    #check if log file exists and create it if it does not exist
    if ((os.path.exists(status.debug_folder_location + "log.txt")) == False):
        debug_file = open(str(status.debug_folder_location + "log.txt"), "a")

#start the program from the mainloop function
__mainloop__()