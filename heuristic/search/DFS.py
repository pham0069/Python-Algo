# applications: path finding, topological ordering, strongly connected components, cycle detection
class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

def depth_first_search(start_node):
    stack = [start_node]
    while stack:
        node = stack.pop()
        node.visited = True
        print(node.name)

        for neighbor in node.adjacency_list:
            if not neighbor.visited:
                stack.append(neighbor)

def recursive_dfs(node):
    node.visited = True
    print(node.name)

    for neighbor in node.adjacency_list:
        if not neighbor.visited:
            recursive_dfs(neighbor)

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

    # either dfs
    # depth_first_search(node1)
    recursive_dfs(node1)
