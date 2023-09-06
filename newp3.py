import heapq

def dijkstra(graph, start, destination):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    previous = {}

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_node == destination:
            break
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    if distances[destination] == float('inf'):
        return None

    path = []
    while destination:
        path.insert(0, destination)
        destination = previous.get(destination)

    return path

# Get user input for the graph
graph = {}
num_edges = int(input("Enter the number of edges in the graph: "))
print("Enter the edges in the format 'node1 node2 weight':")
for _ in range(num_edges):
    node1, node2, weight = input().split()
    weight = int(weight)
    graph.setdefault(node1, {})[node2] = weight
    graph.setdefault(node2, {})[node1] = weight

# Get user input for the start and destination nodes
start_node = input("Enter the start node: ")
destination_node = input("Enter the destination node: ")

# Find the optimal route
route = dijkstra(graph, start_node, destination_node)

# Print the result
if route is None:
    print("No route found.")
else:
    print("Optimal route:", " -> ".join(route))
