import copy
from tabulate import tabulate
import math

def printing(datalist, order, provision):
    datalist_copy = copy.deepcopy(datalist)
    order_copy = copy.deepcopy(order)
    provision_copy = copy.deepcopy(provision)

    headers = ["-"]
    for i in range(len(datalist_copy[0])):
        headers.append(f"C{i+1}")
    headers.append("Provision")

    for i in range(len(datalist_copy)):
        datalist_copy[i].insert(0, f"P{i+1}")
        datalist_copy[i].append(provision_copy[i])
    order_copy.insert(0, "Order")
    order_copy.append("-")
    datalist_copy.append(order_copy)

    table = tabulate(datalist_copy, headers=headers, tablefmt="grid")
    print(table)

def printingPenalty(datalist, order, provision,linePenalty,columnPenalty):
    datalist_copy = copy.deepcopy(datalist)
    order_copy = copy.deepcopy(order)
    provision_copy = copy.deepcopy(provision)
    columnPenaltycp= copy.deepcopy(columnPenalty)
    linePenaltycp= copy.deepcopy(linePenalty)
    headers = ["-"]
    for i in range(len(datalist_copy[0])):
        headers.append(f"C{i+1}")
    headers.append("Provision")
    headers.append("Penalty")
    for i in range(len(datalist_copy)):
        datalist_copy[i].insert(0, f"P{i+1}")
        datalist_copy[i].append(provision_copy[i])
        if provision_copy[i]==0:
            datalist_copy[i].append("-")
        else:
            datalist_copy[i].append(linePenaltycp[i])
    order_copy.insert(0, "Order")
    order_copy.append("-")
    columnPenaltycp.insert(0,"Penalty")
    columnPenaltycp.append("-")
    for i in range(len(order_copy)):
        if order_copy[i]==0:
            columnPenaltycp[i]="-"
    datalist_copy.append(order_copy)
    datalist_copy.append(columnPenaltycp)
    table = tabulate(datalist_copy, headers=headers, tablefmt="grid")
    print(table)

def printingMarginal(marginal_costs):
    for i in range(len(marginal_costs)):
        for j in range(len(marginal_costs[i])):
            marginal_costs[i][j]=math.sqrt(marginal_costs[i][j]**2)
    print(tabulate(marginal_costs, tablefmt="grid"))