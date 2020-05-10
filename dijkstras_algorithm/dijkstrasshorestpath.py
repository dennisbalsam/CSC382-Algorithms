# import libraries
import networkx as nx
import matplotlib.pyplot as plt
import sys
import random

# Dijkstras shortest path
def dijkastra(Weights, Neighborhood):

    # declare visited dictionary
    Visited = {i: False for i in G.nodes}
    # cost to get to node
    Lambda =  {i: sys.maxsize for i in G.nodes} # using sys.maxsize to represent infinity 
    Lambda.update({'0': 0}) # make starting node 0
    # when we remove from lambda we will put them here
    FinalCosts =  {i: 0 for i in G.nodes} 
    # father nodes of node
    Father = {i: ' ' for i in G.nodes}
    
    # loop until desired node is reached
    while Visited[str(desiredNode)] == False:
        # set u to be node with minimum lambda
        u = min(Lambda.items(), key=lambda x: x[1]) # min value in lambda array
        # go through each of its neighbors unlessss it has been visited already
        for w in Neighborhood[int(u[0])]:
            if Visited[str(w)] == False and Lambda[str(w)] > Lambda[str(u[0])] + Weights[u[0], w]:
                # update new lambda and its father
                Lambda.update({str(w):  Lambda[str(u[0])] + Weights[u[0], w]})
                Father.update({str(w): u[0]})


        FinalCosts.update({u[0]: Lambda.pop(u[0])})
        Visited.update({u[0] : True})
        
    
    return('Shortest Path to Node {0} has cost of: {1}'.format(desiredNode, FinalCosts[str(desiredNode)]))
        

# create graph 1
G=nx.Graph()


G.add_edge('0','1',weight=2.0)
G.add_edge('1','2',weight=1.0)
G.add_edge('2','3',weight=5.0)
G.add_edge('4','1',weight=1.0)
G.add_edge('4','3',weight=1.0)
G.add_edge('5','4',weight=1.0)
G.add_edge('6','7',weight=6.0)
G.add_edge('3','7',weight=3.0)
G.add_edge('7','5',weight=1.0)
G.add_edge('6','8',weight=3.0)
G.add_edge('6','9',weight=1.0)
G.add_edge('10','5',weight=1.0)
G.add_edge('0','10',weight=6.0)

pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=260)
nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif')

# edges
nx.draw_networkx_edges(G,pos,edgelist=G.edges,width=6)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos,edge_labels=labels, font_size=9)


# get data needed for dijkstras search (neighbors of nodes, edge weights)
Neighborhood = {i: [*G.neighbors(str(i))] for i in range(len(G.nodes))}
Weights = nx.get_edge_attributes(G,'weight')

#changing the the order of edges in weight dictionary (some stupid error was popping up)
Weights.pop('3','4')
Weights.update({('4','3'):1.0})
Weights.pop('6','7')
Weights.update({('7','6'):6.0})

#pick a node to go to
desiredNode = desiredNode = random.randint(1,10)


# calculate the distance
plt.title('Graph 1')
plt.xlabel(dijkastra(Weights, Neighborhood))
plt.show() # display



# create graph 2
G=nx.Graph()


G.add_edge('0','1',weight=3.0)
G.add_edge('0','2',weight=1.0)
G.add_edge('1','2',weight=1.0)
G.add_edge('1','3',weight=4.0)
G.add_edge('2','3',weight=3.0)
G.add_edge('1','4',weight=2.0)
G.add_edge('2','4',weight=2.0)
G.add_edge('3','5',weight=2.0)
G.add_edge('4','5',weight=1.0)


pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=260)
nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif')

# edges
nx.draw_networkx_edges(G,pos,edgelist=G.edges,width=6)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos,edge_labels=labels, font_size=9)





# get data needed for dijkstras search (neighbors of nodes, edge weights)
Neighborhood = {i: [*G.neighbors(str(i))] for i in range(len(G.nodes))}
Weights = nx.get_edge_attributes(G,'weight')


#changing the the order of edges in weight dictionary (some stupid error was popping up)
Weights.pop('1','2')
Weights.update({('2','1'):1.0})


#pick a node to go to
desiredNode = random.randint(1,5)


# calculate the distance
plt.title('Graph 2')
plt.xlabel(dijkastra(Weights, Neighborhood))
plt.show() # display



# create graph 3
G=nx.Graph()


G.add_edge('0','1',weight=1.0)
G.add_edge('0','2',weight=2.0)
G.add_edge('1','2',weight=3.0)
G.add_edge('1','3',weight=4.0)
G.add_edge('2','3',weight=1.0)
G.add_edge('1','4',weight=2.0)
G.add_edge('1','5',weight=3.0)
G.add_edge('3','5',weight=2.0)
G.add_edge('4','5',weight=1.0)
G.add_edge('1','6',weight=5.0)
G.add_edge('4','6',weight=3.0)
G.add_edge('2','7',weight=1.0)
G.add_edge('5','7',weight=6.0)


pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=260)
nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif')

# edges
nx.draw_networkx_edges(G,pos,edgelist=G.edges,width=6)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos,edge_labels=labels, font_size=9)



# get data needed for dijkstras search (neighbors of nodes, edge weights)
Neighborhood = {i: [*G.neighbors(str(i))] for i in range(len(G.nodes))}
Weights = nx.get_edge_attributes(G,'weight')


#changing the the order of edges in weight dictionary (some stupid error was popping up)
Weights.pop('5','7')
Weights.update({('7','5'):6.0})


#pick a node to go to
desiredNode = random.randint(1,7)


plt.title('Graph 3')
plt.xlabel(dijkastra(Weights, Neighborhood))
plt.show() # display