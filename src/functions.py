import json
from typing import List, Dict


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