def detect_best_improvement(marginal_costs,transportdata):
    maxi=0
    for i in marginal_costs:
        for j in i:
            if transportdata[marginal_costs.index(i)][i.index(j)]==0:
                if maxi>j:
                    maxi=j
                    imaxi=marginal_costs.index(i)
                    jmaxi=i.index(j)
    if maxi!=0:
        return (jmaxi,imaxi)
