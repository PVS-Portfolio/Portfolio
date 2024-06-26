# CSC486 - Spring 2022
# Author: Dr. Patrick Shepherd

# NOTE: This file contains several functions, some of which already do something
# when run, even before you start writing code.  For your convenience, in the
# main function, you may want to comment out the functions you are not currently
# using so they are not running each time you modify the code.

import networkx as nx
import matplotlib.pyplot as plt


# A convenient function to create an undirected scale free graph.
def undirected_scale_free_graph(n):
    H = nx.scale_free_graph(n)
    G = nx.Graph()
    for (u, v) in H.edges():
        G.add_edge(u, v)
    del H
    return G


def task1():
    # Task 1: Examine some Erdos Renyi random graphs (named G1)
    # to see how the parameter 'p' affects them.
    n = 100

    # Modify this parameter and run the code again
    p = .05
    G1 = nx.erdos_renyi_graph(n, p)

    nx.draw_networkx(G1)
    plt.show()


def task2():
    # Task 2: Create a small world graph named G2
    # The function you will call is nx.watts_strogatz_graph
    # Call the function with parameters n, k, and p, in that order.
    n = 100
    k = 10
    p = .3

    # Create the variable G2 here, then plot the network as above.


def task3():
    # Task 3: Create a scale free network named G3.
    # The function you will call is nx.scale_free_graph
    # The function only takes the parameter n.
    n = 100

    # Create the variable G3 here, then plot the network as above.


def task4():
    # Task 4: Fill in the for loop below.
    # Inside the loop, create a new random network, collect graph metric values,
    # and plot them.
    n = 100

    for i in range(21):
        # Set the current iteration's value of p
        p = i * .05

        # Create a new random network here

        # Gather metric values here

        # The x-coordinate list is already made for you.
        # Pass it as the first argument to plt.scatter().
        x = [p for j in range(n)]

        # Plot the current set of points here

    # Show the network
    plt.show()


def task5and6():
    # Task 5, 6: Fill in the for loop below.
    # Inside the loop, create a new small world network, collect graph metric values,
    # and plot them.
    n = 100

    for i in range(21):
        # Task 6: after completing task 5, modify this parameter and
        k = 3

        # Set the current iteration's value of p
        p = i * .05

        # Create a new small world network here

        # Gather metric values here

        # The x-coordinate list is already made for you.
        # Pass it as the first argument to plt.scatter().
        x = [p for j in range(n)]

        # Plot the current set of points here

    # Show the network
    plt.show()


def worked_example():
    ###############################################################
    # WORKED EXAMPLE                                              #
    ###############################################################

    n = 100
    p = .2
    k = 4

    # First, we create one of each network, using most of the parameters above.
    G4 = nx.erdos_renyi_graph(n, p)
    G5 = nx.watts_strogatz_graph(n, k, p)
    G6 = undirected_scale_free_graph(n)

    # Then, we collect the closeness centrality scores for all vertices in
    # each network.
    # These are dictionaries, in which the keys are vertex indices (0, 1, 2, ...)
    # and values are the corresponding centrality scores for each vertex.
    close4 = nx.closeness_centrality(G4)
    close5 = nx.closeness_centrality(G5)
    close6 = nx.closeness_centrality(G6)

    # A handy way to get the values from a dictionary as a 1D list.
    # NOTE: This is all we need to do here, as we don't need to know which
    # score corresponds to which vertex in this case.  We are just plotting
    # all the scores from each network as a group.
    y4 = close4.values()
    y5 = close5.values()
    y6 = close6.values()

    # We will plot the scores out in such a way that all vertex scores from the
    # random graph are on the left, all small world scores are in the middle,
    # and all scale free scores are on the right.  These lists are just meant
    # to hold the x-values of each score so that we can plot them together.
    # This way, all random network scores will be displayed vertically above
    # x=1, all small world scores above x=2, and all scale free scores above
    # x=3.
    x4 = [1 for i in range(n)]
    x5 = [2 for i in range(n)]
    x6 = [3 for i in range(n)]

    # Finally, we can use the function plt.scatter(x, y), where x and y are
    # either numbers or lists of numbers, and are the coordinates of the points
    # to plot.  In other words, to plot three points, one at (1, 3), one at
    # (2, 4), and one at (6, 5), you would call
    # plt.scatter( [1, 2, 6], [3, 4, 5] )

    # You can call plt.scatter as many times as you like before displaying the
    # plot, and each call will place dots on the screen of a different color.
    # Since there are three calls made below, the dots on the plot show up in
    # three differently colored groups.
    plt.scatter(x4, y4)
    plt.scatter(x5, y5)
    plt.scatter(x6, y6)

    # Add a couple helpful labels to the x- and y- axis.
    plt.xlabel('Graph type')
    plt.ylabel('Closeness centrality')

    # Once you have plotted all your points, call plt.show() to display the plot.
    plt.show()


def main():
    task1()
    # task2()
    # task3()
    # worked_example()
    # task4()
    # task5and6()


if __name__ == '__main__':
    main()