# Assignment 3: CSC 486 - Spring 2022
# Author: Dr. Patrick Shepherd

# The purpose of this assignment is to guide you through building
# some common contagion models from scratch and use them to
# understand some of the dynamics underlying the spread of a
# phenomenon through a network.

import matplotlib.pyplot as plt
import networkx as nx
import random

# A convenient function to create an undirected scale free graph.
def undirected_scale_free_graph(n):
    """
    Create an undirected scale free networkx graph.
    :param n: Number of nodes
    :return: A networkx graph
    """
    H = nx.scale_free_graph(n)
    G = nx.Graph()
    for (u, v) in H.edges():
        G.add_edge(u, v)
    del H
    return G

def all_affected(G):
    """
    A function that checks the 'state' attribute of all vertices,
    and returns True if all states are set to True.
    :param G: A networkx graph
    :return: True if all state attributes are True, False otherwise
    """
    return all([G.nodes[i]['state'] for i in G.nodes()])

def num_affected(G):
    """
    A function to calculate the number of affected vertices on a graph
    :param G: A networkx graph
    :return: The number of affected nodes
    """
    states = [G.nodes[i]['state'] for i in G.nodes()]
    return states.count(True)

def perc_affected(G):
    """
    A function to calculate the percentage of affected vertices on a graph
    :param G: A networkx graph
    :return: The percentage of affected nodes
    """
    states = [G.nodes[i]['state'] for i in G.nodes()]
    return states.count(True) / G.number_of_nodes()

def display_states(G):
    """
    Print all vertex states as a list
    :param G: A networkx graph
    :return: None
    """
    print([G.nodes[j]['state'] for j in G.nodes()])

def display_steps(G):
    """
    Print the number of steps until exposure for each vertex as a list
    :param G: A networkx graph
    :return: None
    """
    print([G.nodes[j]['numsteps'] for j in G.nodes()])

def plot_steps_histogram(G):
    """
    Plot a histogram displaying the number of vertices corresponding
    to each possible number of steps since exposure.
    :param G: A networkx graph
    :return: None
    """
    x = list(range(-1, G.number_of_nodes() + 1))
    y = []

    steps = [G.nodes[j]['numsteps'] for j in G.nodes()]
    for i in x:
        y.append(steps.count(i))

    plt.bar(x, y)
    plt.xlabel('Number of steps to exposure')
    plt.ylabel('Number of nodes')
    plt.show()

def initialize_states(G):
    """
    Initialize states for vertices in G.
    States can have values True (active), or False (inactive).
    :param G: A networkx Graph object to modify.
    :return: None - this function will modify the Graph in place,
    so when the function returns the changes will remain.
    """
    for i in G.nodes():
        G.nodes[i]['state'] = False

def initialize_numsteps(G):
    """
    Initialize counter to track when vertices in G were exposed.
    Values are integers representing the number of steps it took for
    the contagion to reach each vertex.
    :param G: A networkx Graph object to modify.
    :return: None - this function will modify the Graph in place,
    so when the function returns the changes will remain.
    """
    # TODO: Task 2
    # Replace 'pass' with your code
    pass

def generate_structures_random(n, p):
    """
    Generate an Erdos-Renyi random network.
    :param n: Number of nodes
    :param p: Probability for each edge to be created
    :return: A networkx graph object
    """
    G = nx.erdos_renyi_graph(n, p)
    initialize_states(G)
    initialize_numsteps(G)
    return G

def generate_structures_smallworld(n, k, p):
    """
    Generate an Watts-Strogatz small world network.
    :param n: Number of nodes
    :param k: Number of immediate neighbors for each vertex
    :param p: Probability for each edge to be rewired
    :return: A networkx graph object
    """
    # TODO: Task 1
    pass

def generate_structures_scalefree(n):
    """
    Generate an Barbasi-Albert scale free network.
    :param n: Number of nodes
    :return: A networkx graph object
    """
    # TODO: Task 1
    pass

def seed_diffusion_random(G, numnodes=1):
    """
    Seed a number of randomly selected vertices equal to numnodes
    to spread the contagion.
    :param G: A networkx graph
    :param numnodes: The number of nodes to affect
    :return: None, the graph will be modified in place
    """
    # TODO: Task 3
    nodes = list(G.nodes())

    # Randomly choose 'numnodes' vertices to initially affect.
    # Set the 'state' and 'numsteps' attributes of these vertices
    # appropriately.

def seed_diffusion_neighborhood(G):
    """
    Seed a randomly selected vertex and all its immediate
    neighbors as initial spreaders.
    :param G: A networkx graph object
    :return: None, the graph will be modified in place
    """
    # TODO: Task 3
    i = random.randint(0, G.number_of_nodes())
    neighborhood = [i] + list(G.neighbors(i))

    # Use the list 'neighborhood' to set the 'state' and 'numsteps'
    # attributes of a random neighborhood of vertices.


def update(G, numnbrs=1, stepnum=1):
    """
    Update the state of all vertices
    :param G: A networkx graph
    :param numnbrs: The minimum number of affected neighbors required
                    for a vertex to become affected
    :param stepnum: The simulation step number, used to record which
                    step a vertex was affected
    :return: None, the graph is updated in place
    """
    # TODO: Task 4
    # Iterate over all vertices and decide which need updates,
    # then update any 'state' and 'numsteps' properties as needed.
    pass

def simulation1(steps):
    """
    Driver function for random network simulations.
    :param steps: The number of steps to run the simulation.
    :return: None
    """
    # TODO: Task 5
    # Create a random graph called G here

    # Then, seed its initially affected vertices

    # Iterate the appropriate number of times, updating the
    #   graph each step.

    # Finally, print the percentage of affected vertices and
    #   plot the histogram once your loop exits.

def simulation2(steps):
    """
    Driver function for small world network simulations.
    :param steps: The number of steps to run the simulation.
    :return: None
    """
    # TODO: Task 6
    # Create a small world graph called G here

    # Then, seed its initially affected vertices

    # Iterate the appropriate number of times, updating the
    #   graph each step.

    # Finally, print the percentage of affected vertices and
    #   plot the histogram once your loop exits.
    pass

def simulation3(steps):
    """
    Driver function for scale free network simulations.
    :param steps: The number of steps to run the simulation.
    :return: None
    """
    # TODO: Task 7
    # Create a scale free graph called G here

    # Then, seed its initially affected vertices

    # Iterate the appropriate number of times, updating the
    #   graph each step.

    # Finally, print the percentage of affected vertices and
    #   plot the histogram once your loop exits.

def main():
    # Fill this in with calls to simulation1(), simulation2(), and
    # simulation3().
    pass

if __name__ == '__main__':
    main()