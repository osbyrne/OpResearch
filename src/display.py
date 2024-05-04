from tabulate import tabulate
from typing import List


def display_cost_matrix(cost_matrix, provisions, orders) -> None:
    """
    Display the cost matrix with headers and row labels for clarity using tabulate.

    :param cost_matrix: 2D list of costs between suppliers and customers.
    :param provisions: List of provisions available at each supplier.
    :param orders: List of orders required by each customer.
    """
    # Determine the number of customers based on the length of the orders list
    num_customers = len(orders)
    headers = [f"C{i+1}" for i in range(num_customers)] + ["Provisions"]

    # Prepare the rows with provisions included
    rows = [row + [provision]
            for row, provision in zip(cost_matrix, provisions)]
    # Prepend supplier labels
    rows = [[f"P{i+1}"] + rows[i] for i in range(len(rows))]

    # Add the orders row at the bottom
    orders_row = ["Orders"] + orders + [""]
    rows.append(orders_row)

    # Print using tabulate
    print(tabulate(rows, headers=headers, tablefmt="grid"))


def display_transport_plan(plan) -> None:
    """
    Displays the transportation plan in a formatted table using tabulate.

    :param plan: 2D list representing the amounts transported from suppliers to customers.
    """
    headers = [f"C{i+1}" for i in range(len(plan[0]))]
    rows = [[f"P{i+1}"] + row for i, row in enumerate(plan)]

    print(tabulate(rows, headers=headers, tablefmt="grid"))


def display_potentials(u: List[float], v: List[float]) -> None:
    print("\nPotentials:")
    print("\nu (dual variables for rows):", u)
    print("v (dual variables for columns):", v)


def display_reduced_costs(reduced_costs) -> None:
    print("\nReduced Costs Table:")
    print(tabulate(reduced_costs, tablefmt="grid"))
