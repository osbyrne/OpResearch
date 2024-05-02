from pprint import pprint
import os

def main():
    while True:
        print("Welcome to an exploration in OpResarch!")
        print("Choose a file to study:")

        # enumerate files in src/constraints/
        directory = "/workspaces/OpResearch/src/constraints/"
        files = os.listdir(directory)

        for i, file in enumerate(files):
            print(f"{i+1}. {file}")
        
        # adding "quit" option
        print(f"{len(files)+1}. Quit")
        
        # get user input
        file_number = int(input("Enter the number of the file you would like to study: "))

        # validate user input
        if file_number < 1 or file_number > len(files)+1:
            print("Invalid input. Please try again.")
            continue
        
        # quit if user selects "Quit"
        if file_number == len(files)+1:
            print("Goodbye!")
            break

        # get the file path
        file_path = directory + files[file_number-1]
        print(f"Reading file: {file_path}")

        # read the file
        json_str = read_txt_file(file_path)
        pprint(json_str)

if __name__ == "__main__":
    main()

