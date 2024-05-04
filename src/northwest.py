import copy
from printing import printing

def NorthWest(datalist,order,provision):
    ordercp=copy.deepcopy(order)
    provisioncp=copy.deepcopy(provision)
    data=[]
    for i in datalist:
        temp=[]
        for j in i:
            temp.append(0)
        data.append(temp)
    i=0
    j=0
    while(i<len(provisioncp) and j<len(ordercp)):
        quantity=min(ordercp[j],provisioncp[i])
        data[i][j]=quantity
        provisioncp[i]-=quantity
        ordercp[j]-=quantity
        if provisioncp[i]==0:
            i+=1
        if ordercp[j]==0:
            j+=1
        printing(data,ordercp,provisioncp)
    return(data,ordercp,provisioncp)