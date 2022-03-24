import numpy as np
import networkx as nx
from scipy.stats import bernoulli
import matplotlib.pyplot as plt

graph = nx.karate_club_graph()

nx.draw(graph, with_labels = True, node_color = "lightblue", edge_color = "g")
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Social Network Analysis/karate_graph.pdf")
plt.show()

def er_graph(N, p):
    """Creates a graph of N nodes with the probability p for each pair of nodes to form an edge"""

    graph = nx.Graph()
    graph.add_nodes_from(range(N))

    for node1 in graph.nodes():
        for node2 in graph.nodes():

            if node1 >= node2 or bernoulli.rvs(p = p) == 0: 
                continue
            
            graph.add_edge(node1, node2)

    return graph

graph = er_graph(50, 0.08)

nx.draw(graph, node_size = 40, node_color = "gray")
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Social Network Analysis/er1.pdf")
plt.show()


def plot_degree_distribution(graph):
    degree_sequence = [d for n, d in graph.degree()]

    plt.hist(degree_sequence, histtype = "step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")

graph = er_graph(50, 0.08)

plot_degree_distribution(graph)
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Social Network Analysis/hist1.pdf")
plt.show()

graph = er_graph(500, 0.08)

plot_degree_distribution(graph)
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Social Network Analysis/hist2.pdf")
plt.show()

graph = er_graph(500, 0.08)
plot_degree_distribution(graph)

graph = er_graph(500, 0.08)
plot_degree_distribution(graph)

graph = er_graph(500, 0.08)
plot_degree_distribution(graph)

plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Social Network Analysis/hist3.pdf")
plt.show()

plot_degree_distribution(nx.erdos_renyi_graph(100, 0.03))
plot_degree_distribution(nx.erdos_renyi_graph(100, 0.3))
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Social Network Analysis/er2.pdf")
plt.show()


def basic_net_stats(graph):
    print("Number of nodes: %d" % graph.number_of_nodes())
    print("Number of edges: %d" % graph.number_of_edges())

    degree_sequence = [d for n, d in graph.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence)) 

adj_matrix_1 = np.loadtxt("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Social Network Analysis/adj_allVillageRelationships_vilno_1.csv", delimiter = ",")
adj_matrix_2 = np.loadtxt("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Social Network Analysis/adj_allVillageRelationships_vilno_2.csv", delimiter = ",")

graph_1 = nx.to_networkx_graph(adj_matrix_1)
graph_2 = nx.to_networkx_graph(adj_matrix_2)

basic_net_stats(graph_1)
basic_net_stats(graph_2)

plot_degree_distribution(graph_1)
plot_degree_distribution(graph_2)
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Social Network Analysis/village_hist.pdf")
plt.show()


graph_1_lcc = max((graph_1.subgraph(c) for c in nx.connected_components(graph_1)), key = len)
graph_2_lcc = max((graph_2.subgraph(c) for c in nx.connected_components(graph_2)), key = len)

print(graph_1_lcc)
print(graph_2_lcc)

print(graph_1_lcc.number_of_nodes() / graph_1.number_of_nodes())
print(graph_2_lcc.number_of_nodes() / graph_2.number_of_nodes())

plt.figure()
nx.draw(graph_1_lcc, node_color = "red", edge_color = "gray", node_size = 20)
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Social Network Analysis/village1.pdf")
plt.show()

plt.figure()
nx.draw(graph_2_lcc, node_color = "green", edge_color = "gray", node_size = 20)
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Social Network Analysis/village2.pdf")
plt.show()