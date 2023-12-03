class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

def breadth_first_search(start_node):
    queue = [start_node]
    start_node.visited = True

    while queue:
        # remove and return the item at the front
        node = queue.pop(0)
        print(node.name)

        for neighbor in node.adjacency_list:
            if not neighbor.visited:
                neighbor.visited = True
                queue.append(neighbor)

if __name__ == '__main__':

    # nodes
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # vertices
    node1.adjacency_list.append(node2)
    node2.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node3.adjacency_list.append(node4)

    # bfs
    breadth_first_search(node1)
