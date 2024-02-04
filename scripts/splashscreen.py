from scripts import debug
from scripts import status

def show_splash():
    debug.log("showing splash screen")

    debug.clear_screen()

    print ("\n Engine Displacement Calculator (EDC)")
    print (" Version: " + status.edc_version)
    print ("\n\n Made by: " + status.edc_developer_name)
    print (" Last commit by: " + status.edc_last_commit_name)