import json
from typing import List, Dict


def read_txt_file(file_path: str) -> Dict[str, object]:
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
    return data


def cost_matrix(data: Dict[str, object]) -> List[List[int]]:

    return data["matrix"]
    # TODO

def transportation_NorthWestCornerRule(data: Dict[str, object]) -> List[List[int]]:
    """
    Solves the transportation problem using the North-West Corner rule.

    :param data: A dictionary containing the cost matrix, provisions, and orders.
    :return: A matrix representing the initial transportation plan.
    """
    supply = data['provisions'][:]
    demand = data['orders'][:]

    num_suppliers = len(supply)
    num_customers = len(demand)
    plan = [[0] * num_customers for _ in range(num_suppliers)]

    i, j = 0, 0
    while i < num_suppliers and j < num_customers:
        amount = min(supply[i], demand[j])
        plan[i][j] = amount
        supply[i] -= amount
        demand[j] -= amount

        if supply[i] == 0:
            i += 1
        elif demand[j] == 0:
            j += 1

    return plan
    # TODO

def potential_costs_table(data: Dict[str, object]) -> List[List[int]]:

    return data["matrix"]
    # TODO

def marginal_costs_table(data: Dict[str, object]) -> List[List[int]]:

    return data["matrix"]
    # TODO


def transportation_balas_hammer(data: Dict[str, object]) -> List[List[int]]:
    """
    Solves the transportation problem using the Balas-Hammer rule.

    :param data: A dictionary containing the cost matrix, provisions, and orders.
    :return: A matrix representing the transportation plan.
    """
    cost_matrix = data['cost_matrix']
    supply = data['provisions'][:]
    demand = data['orders'][:]
    num_suppliers: int = len(supply)
    num_customers: int = len(demand)
    plan = [[0] * num_customers for _ in range(num_suppliers)]

    while any(supply) and any(demand):
        # Find the least cost cell with remaining supply and demand
        min_cost: float = float('inf')
        min_i, min_j = -1, -1
        for i in range(num_suppliers):
            for j in range(num_customers):
                if supply[i] > 0 and demand[j] > 0 and cost_matrix[i][j] < min_cost:
                    min_cost = cost_matrix[i][j]
                    min_i, min_j = i, j

        # Calculate the maximum possible shipment
        shipment = min(supply[min_i], demand[min_j])
        plan[min_i][min_j] = shipment
        supply[min_i] -= shipment
        demand[min_j] -= shipment

    return plan