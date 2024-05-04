import networkx as nx

def testContinuity(g,cost):
    while not nx.is_connected(g):
        connected_components = list(nx.connected_components(g))
        i1=[]
        j1=[]
        i2=[]
        j2=[]
        for i in connected_components[0]:
            if "C" in i:
                j1.append(int(i[1:])-1)
            else:
                i1.append(int(i[1:])-1)
        for i in connected_components[1]:
            if "C" in i:
                j2.append(int(i[1:])-1)
            else:
                i2.append(int(i[1:])-1)
        mini=None
        for i in i1:
            for j in j2:
                if mini==None:
                    doi=i
                    doj=j
                    mini=cost[i][j]
                elif mini>cost[i][j]:
                    doi=i
                    doj=j
                    mini=cost[i][j]
        for i in i2:
            for j in j1:
                if mini==None:
                    doi=i
                    doj=j
                    mini=cost[i][j]
                elif mini>cost[i][j]:
                    doi=i
                    doj=j
                    mini=cost[i][j]
        g.add_edge("P"+str(doi+1),"C"+str(doj+1))
    return g