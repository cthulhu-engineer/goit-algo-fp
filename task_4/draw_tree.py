import heapq
import uuid

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    """
    :class: Node

    Node represents a single node in a binary tree.

    Attributes:
        left (Node): The left child of the node.
        right (Node): The right child of the node.
        val (Any): The value stored in the node.
        color (str): The color of the node. Default is "skyblue".
        id (str): The unique identifier of the node.

    Methods:
        __init__(self, key, color="skyblue"): Initializes a new instance of the Node class.

            Parameters:
                key (Any): The value to be stored in the node.
                color (str): The color of the node. Default is "skyblue".
    """
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def heapify(elements):
    """
    Rearranges the elements in the given list into a valid heap structure.

    :param elements: A list of elements to be heapified.
    :return: A list of nodes representing the heap structure.
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
    :param graph: The graph object to add the nodes and edges to.
    :param node: The current node in the binary tree.
    :param pos: A dictionary to store the position of each node in the graph.
    :param x: The x-coordinate of the current node.
    :param y: The y-coordinate of the current node.
    :param layer: The current layer of the binary tree.

    :return: The updated graph object with added nodes and edges.

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
    return graph


def draw_tree(tree_root):
    """
    :param tree_root: The root node of the tree.
    :return: None

    This method takes the root node of a tree and draws the tree using networkx and matplotlib libraries. The tree is drawn as a directed graph, with nodes represented as circles. The position
    * of each node is determined by its id attribute. The edges of the tree are added to the graph using the `add_edges` function. The colors and labels of the nodes are obtained from the
    * attributes stored in the graph. The resulting graph is displayed using matplotlib.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)} if tree_root else {}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2, 3, 4, 5, 7, 9, 34]
    heap_root = heapify(nums)
    draw_tree(heap_root)
