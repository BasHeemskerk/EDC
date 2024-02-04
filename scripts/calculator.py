from scripts import debug
from scripts import status

import math
import time

def show_calculator():

    debug.clear_screen()

    debug.log("at the calculator screen")

    print("\nWelcome to the engine displacement calculator")
    print("---------------------------------------------")
    print(" Measurement unit: mm")
    print(" Output measurement unit: cc")
    print("\n")

    print("Please input the bore of 1 cilinder")
    bore = input(" engine bore (per cilinder) in mm: ")
    print("\nPlease input the stroke of the engine")
    stroke = input(" engine stroke in mm: ")
    print("\nPlease input the number of cilinders")
    cilinders = input(" number of cilinders: ")

    calculate_final_displacement(bore, stroke, cilinders)


def calculate_final_displacement(bore, stroke, cilinders):

    debug.clear_screen()

    debug.log("calculating the result")

    converted_bore = float(bore)
    converted_stroke = float (stroke)
    converted_cilinder = float (cilinders)

    pi = math.pi
    displacement = (pi / 4) * (converted_bore * converted_bore) * (converted_stroke) / 1000
    final_displacement = displacement * converted_cilinder

    displacement_rounded = round(displacement, 2)
    final_displacement_rounded = round(final_displacement, 2)

    converted_displacement = str(displacement)
    converted_final_displacement = str(final_displacement)

    converted_displacement_rounded = str(displacement_rounded)
    converted_final_displacement_rounded = str(final_displacement_rounded)

    print (converted_displacement + "cc displacement per cilinder. (" + converted_displacement_rounded + "cc)")
    print(converted_final_displacement + "cc is the entire engine displacement. (" + converted_final_displacement_rounded + "cc)")

    debug.log("calculated the results")

    print("\nDo you want to save the result to the calculations folder?")
    save_to_file = input(" (yes/no): ")
    if (save_to_file == "yes"):
        print("\nThe file will be saved.")
        print("\nEnter the filename you would like the file to have.")
        filename = input(" Decide the filename you want to use: ")
        final_input_string = "(pi / 4) * (" + str(bore) + "^2) * (" +str(stroke) + ") / 1000"
        save_result_in_file(filename, str(bore), str(stroke), str(cilinders), final_input_string, converted_displacement, converted_final_displacement, converted_displacement_rounded, converted_final_displacement_rounded)
    else:
        print("\nThe file will not be saved.")
        print("Go back to calculator?")
        go_back = input(" (yes): ")
        if (go_back != ""):
            print("\nReturning.")
            time.sleep(3)
            show_calculator()



    

def save_result_in_file(filename, bore, stroke, cilinders, input_calculation, output_result, full_output_result, output_result_rounded, full_output_result_rounded):
    
    output_file = open(str(status.calculations_folder_location + str(filename) + ".txt"), "a")
    output_file.write("\n\n\nYour calculation has been made!")
    output_file.write("\n\n")
    output_file.write("You gave the following values:")
    output_file.write("\nBore: " + bore + "mm.")
    output_file.write("\nStroke: " + stroke + "mm.")
    output_file.write("\nCilinders: x" + cilinders + ".")
    output_file.write("\n\n")
    output_file.write("The formula EDC used to calculate was: " + input_calculation)
    output_file.write("\n\n")
    output_file.write("For 1 cilinder: " + output_result + "cc of displacement.")
    output_file.write("\nRounded to: " + output_result_rounded + "cc.")
    output_file.write("\n\n")
    output_file.write("For " + cilinders + " cilinders: " + full_output_result + "cc of displacement.")
    output_file.write("\nRounded to: " + full_output_result_rounded + "cc.")
    output_file.write("\n\n")
    output_file.write("End of calculation")
    output_file.write("\n\n\n")
    output_file.close()

    debug.log("saved results to file: " + filename + ".txt")

    print("\nYour calculation has been made and can be found in the file: " + status.calculations_folder_location + str(filename) + ".txt")

    show_calculator()