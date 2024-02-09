import heapq
import uuid
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    """
    :class: Node

    This class represents a node in a binary tree.

    Attributes:
        left (Node): The left child of the node.
        right (Node): The right child of the node.
        val (Any): The value stored in the node.
        color (str): The color of the node.
        id (str): The unique identifier of the node.

    Methods:
        __init__(self, key): Initializes a new instance of the Node class.

    """
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "skyblue"
        self.id = str(uuid.uuid4())


def heapify(elements):
    """
    Heapify a list of elements and construct a binary tree structure.

    :param elements: A list of elements to be heapified.
    :return: The root node of the binary tree structure, or None if the input list is empty.
    """
    heapq.heapify(elements)
    nodes = [Node(el) for el in elements]
    for i in range(len(elements)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(elements):
            nodes[i].left = nodes[left_index]
        if right_index < len(elements):
            nodes[i].right = nodes[right_index]
    return nodes[0] if nodes else None


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    :param graph: The graph object where the nodes and edges will be added.
    :param node: The current node being processed.
    :param pos: A dictionary that stores the positions of each node in the graph.
    :param x: The x-coordinate of the current node.
    :param y: The y-coordinate of the current node.
    :param layer: The layer of the current node in the tree.
    :return: The updated dictionary containing the positions of each node.

    This method adds nodes and edges to the graph object in a recursive manner, representing a binary tree structure. Each node's position is calculated based on its layer and coordinates
    * given. The positions are stored in the pos dictionary.

    Example usage:
    graph = create_empty_graph()  # Create an empty graph object
    root = Node(1)  # Create the root node with a value of 1
    pos = add_edges(graph, root, {})  # Add nodes and edges to the graph, storing positions in pos dictionary
    """
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        pos[node.id] = (x, y)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            add_edges(graph, node.left, pos, x=x - 1 / 2 ** layer, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            add_edges(graph, node.right, pos, x=x + 1 / 2 ** layer, y=y - 1, layer=layer + 1)
    return pos


def draw_tree(tree, pos, labels, node_colors):
    """
    Draws a tree graph with specified parameters.

    :param tree: The tree graph to be drawn.
    :param pos: The position of each node in the graph.
    :param labels: The labels to be displayed on each node.
    :param node_colors: The colors to be assigned to each node.
    :return: None

    """
    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()


def traverse_and_color(graph, method='bfs'):
    """
    :param graph: The graph to traverse and color.
    :param method: The traversal method to use. Can be either 'bfs' (Breadth-First Search) or 'dfs' (Depth-First Search). Default is 'bfs'.
    :return: A dictionary mapping each node's ID to its assigned color.

    Traverses the given graph using the specified method and assigns a color to each node. The color values are generated based on the node's position in the traversal order.

    The graph should be provided as a data structure compatible with the traversal algorithm used (e.g., adjacency list for BFS, adjacency matrix for DFS).

    Examples:
        graph = ...  # construct the graph
        color_map = traverse_and_color(graph)  # Use BFS as the default traversal method
        color_map = traverse_and_color(graph, 'dfs')  # Use DFS as the traversal method

    Note:
        - The traversal order may vary depending on the graph structure and traversal method.
        - The assigned colors are hexadecimal RGB values in the format "#RRGGBB".
        - The color values are generated based on the node's position in the traversal order, with decreasing red (RR) values and increasing green (GG) values.
        - The blue (BB) value is set to a constant value of 180.

    """
    queue = deque([heap_root]) if method == 'bfs' else [heap_root]
    colors = []
    color_map = {}
    i = 0
    while queue:
        node = queue.popleft() if method == 'bfs' else queue.pop()
        if node and node.id not in color_map:
            color_value = "#{:02x}{:02x}{:02x}".format(255 - i * 10, 105 + i * 10 % 150, 180)
            color_map[node.id] = color_value
            colors.append(color_value)
            i += 1
            if method == 'bfs':
                queue.extend([node.left, node.right])
            else:  # DFS uses stack, so we add right first to visit left first
                queue.extend([child for child in [node.right, node.left] if child])
    return color_map


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2, 3, 4, 5, 7, 9, 34]
    heap_root = heapify(nums)

    # Build the tree and positions
    tree = nx.DiGraph()
    pos = add_edges(tree, heap_root, {})
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    # BFS traversal and coloring
    bfs_colors = traverse_and_color(tree, method='bfs')
    draw_tree(tree, pos, labels, [bfs_colors[node] for node in tree.nodes()])

    # DFS traversal and coloring
    dfs_colors = traverse_and_color(tree, method='dfs')
    draw_tree(tree, pos, labels, [dfs_colors[node] for node in tree.nodes()])
