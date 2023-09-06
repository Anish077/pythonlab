import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def prim_mst(self):
        parent = [-1] * self.V
        key = [sys.maxsize] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            min_key = min((key[i], i) for i in range(self.V) if not mst_set[i])
            u = min_key[1]
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Thermal Station   --   Connected to   -->   Thermal Station   Cost")
        for i in range(1, self.V):
            print(f"   {i}                    --                    {parent[i]}                 {self.graph[i][parent[i]]}")

# Accepting user input
n = int(input("Enter the number of thermal power stations: "))
g = Graph(n)

print("Enter the cost of electrification for each connection:")
for i in range(n):
    for j in range(i + 1, n):
        cost = int(input(f"Enter the cost between thermal station {i} and {j}: "))
        g.add_edge(i, j, cost)

# Compute and display the minimum cost connection
g.prim_mst()
