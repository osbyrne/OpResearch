from functions import read_txt_file, cost_matrix, transportation_NorthWestCornerRule, transportation_balas_hammer, potential_costs_table, marginal_costs_table
from typing import List
from display import display_cost_matrix, display_transport_plan, display_potentials, display_reduced_costs
import os

def example_function(table: dict) -> None:
    return(table)

def main():
    print("Welcome to an exploration in OpResarch!")

    while True:

        # enumerate files in src/constraints/
        directory = "/workspaces/OpResearch/src/constraints/"
        files = os.listdir(directory)

        for i, file in enumerate(files):
            print(f"{i+1}. {file}")
        
        # adding "quit" option
        print(f"{len(files)+2}. Quit \n Execute all files")
        
        # get user input
        file_number = int(input("Enter the number of the file you would like to study: \n> "))

        # validate user input
        if file_number < 1 or file_number > len(files)+2:
            print("Invalid input. Please try again.\n")
            continue
        
        # quit if user selects "Quit"
        if file_number == len(files)+2:
            print("\nGoodbye!\n")
            break


        # get the file path
        file_path = directory + files[file_number-1]
        print(f"\nReading file: {file_path}\n")

        # read the file
        dict_obj = read_txt_file(file_path)

        

        while True:
            options: List[str] = [
                "JSON string", 
                "Cost matrix", 
                "transportation_NorthWestCornerRule", 
                "transportation_balas_hammer",
                "Potential costs table", 
                "Marginal costs table",
                "exit"
            ]
            for i, option in enumerate(options):
                print(f"{i+1}. {option}")

            # get user input
            option_number = int(input("\nEnter the number of the option you would like to see: \n> "))

            # validate user input
            if option_number < 1 or option_number > len(options):
                print("Invalid input. Please try again.\n")
                continue        
            
            if option_number == 1:
                print(dict_obj)
            elif option_number == 2:
                display_cost_matrix(cost_matrix(dict_obj))
            elif option_number == 3:
                display_transport_plan(transportation_NorthWestCornerRule(dict_obj))
            elif option_number == 4:
                display_transport_plan(transportation_balas_hammer(dict_obj))
            elif option_number == 5:
                display_potentials(potential_costs_table(dict_obj))
            elif option_number == 6:
                display_reduced_costs(marginal_costs_table(dict_obj))
            elif option_number == 7:
                print("\nReturning to file selection\n")
                break
            print("\n")
        

if __name__ == "__main__":
    main()

