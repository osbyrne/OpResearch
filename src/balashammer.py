import copy
import networkx as nx

from printing import printing, printingPenalty

def BalasHammer(datalist,order,provision,costlist):
    datalistcp=copy.deepcopy(datalist)
    ordercp=copy.deepcopy(order)
    provisioncp=copy.deepcopy(provision)
    
    data=[]
    for i in datalist:
        temp=[]
        for j in i:
            temp.append(None)
        data.append(temp)
    cpt=0
    while(asnozero(ordercp)==0 and asnozero(provisioncp)==0):
        cpt+=1
        linePenalty=[]
        columnPenalty=[]
        
        for i in datalistcp:
            min1=None
            min2=None
            for j in i:
                if min1==None:
                    min1=j
                elif min2==None:
                    if j<min1:
                        min2=min1
                        min1=j
                    else:
                        min2=j
                else:
                    if j<min1:
                        min2=min1
                        min1=j
                    elif j<min2:
                        min2=j
            if min2==100000000000 and min1!=100000000000:
                linePenalty.append(min1)
            else:
                linePenalty.append(min2-min1)
        for j in range(len(datalistcp[0])):
            min1 = None
            min2 = None
    
            for i in range(len(datalistcp)):
                if min1 is None:
                    min1 = datalistcp[i][j]
                elif min2 is None:
                    if datalistcp[i][j] < min1:
                        min2 = min1
                        min1 = datalistcp[i][j]
                    else:
                        min2 = datalistcp[i][j]
                else:
                    if datalistcp[i][j] < min1:
                        min2 = min1
                        min1 = datalistcp[i][j]
                    elif datalistcp[i][j] < min2:
                        min2 = datalistcp[i][j]
            if min2==100000000000 and min1!=100000000000:
                columnPenalty.append(min1)
            else:
                columnPenalty.append(min2 - min1)
        maxiPenalty=-1
        cost=None
        print(costlist)
        for i in range(len(linePenalty)):
            if cost==None:
                maxiPenalty=linePenalty[i]
                changei=i
                for j in range(len(costlist[i])):
                    if data[i][j]==None:
                        if cost==None:
                            cost=costlist[i][j]
                            changej=j
                            tempcost=cost
                        elif cost>costlist[i][j]:
                            cost=costlist[i][j]
                            tempcost=cost
                            changej=j
            elif linePenalty[i]>maxiPenalty:
                maxiPenalty=linePenalty[i]
                changei=i
                cost=None
                for j in range(len(costlist[i])):
                    if data[i][j]==None:
                        if cost==None:
                            cost=costlist[i][j]
                            tempcost=cost
                            changej=j
                        elif cost>costlist[i][j]:
                            cost=costlist[i][j]
                            changej=j
                            tempcost=cost
            elif linePenalty[i]==maxiPenalty:
                cost=tempcost
                for j in range(len(costlist[i])):
                    if data[i][j]==None:
                        if cost>costlist[i][j]:
                            cost=costlist[i][j]
                            changei=i
                            changej=j
                            tempcost=cost
            print(cost,maxiPenalty,changei,changej)
        for j in range(len(columnPenalty)):
            
            if columnPenalty[j]>maxiPenalty:
                maxiPenalty=columnPenalty[j]
                changej=j
                cost=None
                for i in range(len(costlist)):
                    if data[i][j]==None:
                        if cost==None:
                            cost=costlist[i][j]
                            tempcost=cost
                            changei=i
                                
                        elif cost>costlist[i][j]:
                            cost=costlist[i][j]
                            tempcost=cost
                            changei=i
            elif columnPenalty[j]==maxiPenalty:
                cost=tempcost
                for i in range(len(costlist)):
                    if data[i][j]==None:
                        if cost>costlist[i][j]:
                            cost=costlist[i][j]
                            changei=i
                            changej=j
                            tempcost=cost
            print(cost,maxiPenalty,changei,changej)
        print(cost,maxiPenalty)

                
        if data[changei][changej]==None:
            orderprint=copy.deepcopy(ordercp)
            provisionprint=copy.deepcopy(provisioncp)
            quantity=min(ordercp[changej],provisioncp[changei])
            data[changei][changej]=quantity
            datalistcp[changei][changej]=100000000000
            provisioncp[changei]-=quantity
            ordercp[changej]-=quantity
    
            if provisioncp[changei]==0:
                for j in range(len(data[changei])):
                    if data[changei][j]==None:
                        data[changei][j]=0
                        datalistcp[changei][j]=100000000000
            if ordercp[changej]==0:
                for i in range(len(data)):
                    if data[i][changej]==None:
                        data[i][changej]=0
                        datalistcp[i][changej]=100000000000
            printingPenalty(data, orderprint, provisionprint,linePenalty,columnPenalty)
    return(data,ordercp,provisioncp)

def Costculation(transportdata,datalist,p=True) -> int:
    cal=0
    for i in range(len(transportdata)):
        for j in range(len(transportdata[i])):
            cal+=transportdata[i][j]*datalist[i][j]
    if p:
        print(cal)
    return cal

def asnozero(liste):
    for i in liste:
        if i!=0:
            return 0
    return 1

def testcircular(g,p=False) -> bool:
    """
    Thanks to networkx librairy we can directly check if there is a cycle in our graph
    """
    try:
        cycle=nx.find_cycle(g, orientation='original')
        if p:
            print("There is a cycle in the graphe")
        string=""
        for i in cycle:
            string=string + " ==> "+ i[0]
        if p!=False:
            print(string)
        a=cycle
    except:
        a=1
        if p:
            print("there is no cycle in this graph")
    return a

def rectifCircular(test,transportdata, graph,order,provision,upgrade) -> tuple:
    transporcp=copy.deepcopy(transportdata) 
    
    do=None
    mini=None
    for data in test:
        if "P" in data[1]:
            i=int(data[1][1:])-1
            j=int(data[0][1:])-1
            if mini==None:
                do="P"
                mini=transporcp[i][j]
            if transporcp[i][j]<mini:
                do="P"
                mini=transporcp[i][j]
        else:
            i=int(data[0][1:])-1
            j=int(data[1][1:])-1
            if mini==None:
                do="C"
                mini=transporcp[i][j]
            if transporcp[i][j]<mini:
                do="C"
                mini=transporcp[i][j]
    quantity=None
    
    for data in test:
        if do=="C":
            i=int(data[1][1:])-1
            j=int(data[0][1:])-1
            if "P" in data[1]:
                if quantity ==None:
                    
                    quantity=transporcp[i][j]
                if quantity>transporcp[i][j]:
                    quantity=transporcp[i][j]
        else:
            i=int(data[0][1:])-1
            j=int(data[1][1:])-1
            if "C" in data[1]:
                if quantity ==None:
                    quantity=transporcp[i][j]
                if quantity>transporcp[i][j]:
                    quantity=transporcp[i][j]
    if quantity==0:
        for data in test:
            if "C" in data[0]:
                i=int(data[1][1:])-1
                j=int(data[0][1:])-1
            else:
                i=int(data[0][1:])-1
                j=int(data[1][1:])-1
            if transporcp[i][j]==0:
                if upgrade[1]!=i or upgrade[0]!=j:
                    graph.remove_edge(data[0],data[1])

    else:
        for data in test:
            if do=="C":
                i=int(data[1][1:])-1
                j=int(data[0][1:])-1
                if "P" in data[1]:
                    transporcp[i][j]-=quantity
                else:
                    transporcp[j][i]+=quantity
            else:
                i=int(data[1][1:])-1
                j=int(data[0][1:])-1
                if "P" in data[1]:
                    transporcp[i][j]+=quantity
                else:
                    transporcp[j][i]-=quantity
        transportdata=transporcp
        
        for data in test:
            
            if "P" in data[1]:
                i=int(data[1][1:])-1
                j=int(data[0][1:])-1
                if transporcp[i][j]==0:
                    graph.remove_edge(data[0],data[1])
            else:
                
                i=int(data[0][1:])-1
                j=int(data[1][1:])-1
                if transporcp[i][j]==0:
                    graph.remove_edge(data[0],data[1])
    return(transportdata,graph)


def can_reach_all_nodes(graph):
    num_nodes = len(graph.nodes())
    
    # Parcourir tous les nœuds du graphe
    for node in graph.nodes():
        visited = set()  # Pour stocker les nœuds visités
        
        # Fonction DFS pour explorer le graphe à partir du nœud actuel
        def dfs(current_node):
            visited.add(current_node)
            
            # Parcourir tous les voisins du nœud actuel
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    dfs(neighbor)
        
        # Exécuter DFS à partir du nœud actuel
        dfs(node)
        
        # Vérifier si tous les nœuds ont été visités
        if len(visited) != num_nodes:
            return False  # Si tous les nœuds ne sont pas accessibles, retourner False
    
    return True