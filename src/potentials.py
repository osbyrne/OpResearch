import copy

def calculate_potentials(graph, costs):
    num_nodes = len(graph.nodes())
    potentials = {}
    for i in graph.nodes:
        potentials[i]=None
    
    start_node = list(graph.nodes())[0]
    potentials[start_node] = 0
    todo=copy.deepcopy(graph.edges)
    while None in potentials.values():
        for i in todo:
    
            if potentials[i[0]]!=None and potentials[i[1]]==None:
                if "C" in i[0]:
                    ical=int(i[1][1:])-1
                    jcal=int(i[0][1:])-1
                    potentials[i[1]]=costs[ical][jcal]+potentials[i[0]]
                else:
                    ical=int(i[0][1:])-1
                    jcal=int(i[1][1:])-1
                    potentials[i[1]]=potentials[i[0]]-costs[ical][jcal]
            elif potentials[i[1]]!=None and potentials[i[0]]==None:
                if "C" in i[0]:
                    ical=int(i[1][1:])-1
                    jcal=int(i[0][1:])-1
                    potentials[i[0]]=-costs[ical][jcal]+potentials[i[1]]
                else:
                    ical=int(i[0][1:])-1
                    jcal=int(i[1][1:])-1
                    potentials[i[0]]=potentials[i[1]]-costs[ical][jcal]
    return potentials

def display_potentials(potentials):
    print("Potentiels par sommet :")
    for node, potential in potentials.items():
        print(f"Sommet {node}: {potential}")
    print()