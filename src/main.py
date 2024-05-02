import json
from typing import List, Dict
import json
from pprint import pprint

"""copilot prompt
write a function that reads a txt file like the one below and returns a json object with the following structure:
4 3
30 20 20 450
10 50 20 250
50 40 30 250
30 20 30 450
500 600 300


{
    "lines": 4,
    "columns": 3,
    "matrix": [
        [30, 20, 20],
        [10, 50, 20],
        [50, 40, 30],
        [30, 20, 30]
    ],
    "provisons": [450, 250, 250, 450],
    "orders": [500, 600, 300]
}

note that the first line of the txt file contains the number of lines and columns of the matrix, 
the following lines contain the matrix itself where each last number of the line is the provision for that line,
and the last line contains the orders.
"""

def read_txt_file(file_path: str) -> str:
    """
    Reads a text file and returns its contents as a JSON string.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The contents of the text file as a JSON string.
    """
    with open(file_path, 'r') as file:
        # Read the first line to get the number of lines and columns
        lines, columns = map(int, file.readline().split())

        matrix: List[List[int]] = []
        provisions: List[int] = []

        # Read the matrix and provisions from the file
        for _ in range(lines):
            # Read each row
            row = list(map(int, file.readline().split()))
            # The last element of the row is the provision
            provision = row.pop()
            # Append the row to the matrix and the provision to the provisions list
            matrix.append(row)
            provisions.append(provision)

        # Read the orders from the file
        orders = list(map(int, file.readline().split()))
        
    data: Dict[str, object] = {
        "lines": lines,
        "columns": columns,
        "matrix": matrix,
        "provisions": provisions,
        "orders": orders
    }
    
    # Convert the data dictionary to a JSON string
    return json.dumps(data)

if __name__ == "__main__":
    file_path = "src/constraints/example.txt"
    pprint(read_txt_file(file_path))