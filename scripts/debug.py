from scripts import status

import datetime
import os

def log(message):
    if (status.program_must_debug):
        print("---DEBUG.LOG---")
        print(message)
        print("---------------\n")

    if (status.program_must_log):
        log_to_file(message, 0)

def error(message):
    if (status.program_must_debug):
        print("---ERROR.LOG---")
        print(message)
        print("---------------\n")

    if (status.program_must_log):
        log_to_file(message, 1)
    
def write_session_time():
    debug_file = open(str(status.debug_folder_location + "log.txt"), "a")
    debug_file.write("\n\n--- Session: " + str(datetime.datetime.now()) + " ---")

def log_to_file(message, ID):
    debug_file = open(str(status.debug_folder_location + "log.txt"), "a")
    if (ID == 0):
        debug_file.write("\n")
        debug_file.write("DEBUG.LOG: ")
        debug_file.write(message)
    else:
        debug_file.write("\n")
        debug_file.write("ERROR.LOG: ")
        debug_file.write(message + ", code: " + str(ID))

def clear_screen():
    os.system('cls')