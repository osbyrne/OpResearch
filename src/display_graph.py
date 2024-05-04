
import networkx as nx

def display_graph(datalist,p=True):
    G = nx.Graph()
    
    cols = len(datalist[0])
    for j in range(cols):
        G.add_node(f"C{j+1}", pos=(j, 1))  
    
    rows = len(datalist)
    for i in range(rows):
        G.add_node(f"P{i+1}", pos=(i, 0))
    
    
    for i in range(rows):
        for j in range(cols):
            if datalist[i][j] != 0:
                G.add_edge(f"P{i+1}", f"C{j+1}", weight=datalist[i][j])
    
    # pos = nx.get_node_attributes(G, 'pos')
    # nx.draw(G, pos, with_labels=True, node_size=1000, font_size=10, node_color='skyblue', font_color='black')
    # labels = nx.get_edge_attributes(G, 'weight')
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # if p:
    #     plt.show()
    return G