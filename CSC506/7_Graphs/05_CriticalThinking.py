import heapq
# Sample program to explain real-time route optimization using Dijkstra's algorithm

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        """Add a directed edge from u -> v with given travel time."""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def update_edge_weight(self, u, v, new_weight):
        """Simulate real-time traffic update."""
        if u in self.graph:
            for i, (neighbor, weight) in enumerate(self.graph[u]):
                if neighbor == v:
                    self.graph[u][i] = (neighbor, new_weight)
                    print(f"Traffic update: travel time from {u} to {v} changed to {new_weight}")
                    return
        print(f"No direct route from {u} to {v} found for update.")

    def dijkstra(self, start):
        """Compute shortest paths from start to all others."""
        # ✅ Collect all unique nodes (including destinations)
        nodes = set(self.graph.keys())
        for edges in self.graph.values():
            for neighbor, _ in edges:
                nodes.add(neighbor)

        # Initialize distances
        distances = {node: float('inf') for node in nodes}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph.get(current_node, []):
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances


# ------------------ Simulation ------------------
if __name__ == "__main__":
    city_graph = Graph()
    city_graph.add_edge("Restaurant", "ZoneA", 10)
    city_graph.add_edge("Restaurant", "ZoneB", 5)
    city_graph.add_edge("ZoneA", "ZoneC", 2)
    city_graph.add_edge("ZoneB", "ZoneA", 3)
    city_graph.add_edge("ZoneB", "ZoneD", 9)
    city_graph.add_edge("ZoneC", "ZoneD", 1)
    city_graph.add_edge("ZoneD", "Customer", 4)

    print("\n=== Initial Route Plan ===")
    distances = city_graph.dijkstra("Restaurant")
    for location, time in distances.items():
        print(f"Shortest travel time from Restaurant to {location}: {time} mins")

    print("\n=== Real-Time Traffic Update ===")
    city_graph.update_edge_weight("ZoneB", "ZoneD", 15)
    city_graph.update_edge_weight("ZoneA", "ZoneC", 1)

    print("\n=== Updated Route Plan ===")
    updated_distances = city_graph.dijkstra("Restaurant")
    for location, time in updated_distances.items():
        print(f"Updated travel time from Restaurant to {location}: {time} mins")
