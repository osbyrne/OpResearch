def calculate_potential_costs(table, potentials):

    potential_costs = []
    tableC=[]
    tableP=[]
                
    for i in range(len(table)):
        tableP.append(i)
    for i in range(len(table[0])):
        tableC.append(i)
    for i in range(len(tableP)):
        temp=[]
        for j in range(len(tableC)):
            temp.append(potentials["P"+str(i+1)]-potentials["C"+str(j+1)])
        potential_costs.append(temp)
    return potential_costs

def calculate_marginal_costs(costs, potential_costs):
    marginal_costs=[]
    for i in range(len(potential_costs)):
        temp=[]
        for j in range(len(potential_costs[i])):
            temp.append(costs[i][j]-potential_costs[i][j])
        marginal_costs.append(temp)
    return(marginal_costs)