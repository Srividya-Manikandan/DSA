class GraphAdjList:
    """Graph represented using an adjacency list."""

    def __init__(self):
        self.graph = {}  # Initialize an empty adjacency list

    def add_vertex(self, vertex):
        """Add a new vertex to the graph."""
        if vertex in self.graph:
            print(f"Error: Vertex {vertex} already exists in the graph.")
        else:
            self.graph[vertex] = []  # Initialize an empty list for the new vertex

    def add_edge(self, u, v):
        """Add a directed edge from vertex u to vertex v."""
        if u not in self.graph or v not in self.graph:
            print(f"Error: One or both vertices {u}, {v} do not exist in the graph.")
        else:
            self.graph[u].append(v)  # Add v to u's adjacency list

    def remove_edge(self, u, v):
        """Remove a directed edge from vertex u to vertex v."""
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        else:
            print(f"Error: Edge from {u} to {v} does not exist.")

    def remove_vertex(self, vertex):
        """Remove a vertex and all associated edges."""
        if vertex in self.graph:
            # Remove all edges directed towards the vertex
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)
            # Remove the vertex itself
            del self.graph[vertex]
        else:
            print(f"Error: Vertex {vertex} does not exist in the graph.")

    def get_in_degree(self, vertex):
        """Calculate the in-degree of a vertex."""
        if vertex not in self.graph:
            print(f"Error: Vertex {vertex} does not exist in the graph.")
            return
        in_degree = 0
        for v in self.graph:
            in_degree += self.graph[v].count(vertex)
        return in_degree

    def get_out_degree(self, vertex):
        """Calculate the out-degree of a vertex."""
        if vertex not in self.graph:
            print(f"Error: Vertex {vertex} does not exist in the graph.")
            return
        return len(self.graph[vertex])

    def display(self):
        """Display the adjacency list."""
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")


# Example usage
g = GraphAdjList()

# Adding vertices
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)

# Adding edges for a directed graph
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Adjacency List Representation:")
g.display()

# Removing edge
g.remove_edge(1, 3)
print("\nAfter removing edge 1 -> 3:")
g.display()

# Removing vertex
g.remove_vertex(4)
print("\nAfter removing vertex 4:")
g.display()

# Getting in-degree and out-degree
vertex = 1
print(f"\nIn-degree of vertex {vertex}: {g.get_in_degree(vertex)}")
print(f"Out-degree of vertex {vertex}: {g.get_out_degree(vertex)}")

import heapq

class GraphAdjMatrix:
    """Graph represented using an adjacency matrix."""

    def __init__(self, initial_vertices=0):
        self.vertices = initial_vertices
        self.graph = [[0]*initial_vertices for _ in range(initial_vertices)]

    def add_vertex(self):
        """Add a new vertex to the graph."""
        self.vertices += 1
        # Add a new row and column for the new vertex
        for row in self.graph:
            row.append(0)
        self.graph.append([0] * self.vertices)
        print(f"Vertex {self.vertices - 1} added.")

    def add_edge(self, u, v, weight):
        """Add a directed edge from vertex u to vertex v with the given weight."""
        if u >= self.vertices or v >= self.vertices:
            print(f"Error: One or both vertices {u}, {v} are out of range.")
        else:
            self.graph[u][v] = weight  # Directed edge from u to v with weight
            self.graph[v][u] = weight  # Undirected edge from v to u with weight

    def remove_edge(self, u, v):
        """Remove a directed edge from vertex u to vertex v."""
        if u >= self.vertices or v >= self.vertices:
            print(f"Error: One or both vertices {u}, {v} are out of range.")
        elif self.graph[u][v] == 0:
            print(f"Error: Edge from {u} to {v} does not exist.")
        else:
            self.graph[u][v] = 0
            self.graph[v][u] = 0

    def remove_vertex(self, vertex):
        """Remove a vertex and all associated edges."""
        if vertex >= self.vertices:
            print(f"Error: Vertex {vertex} is out of range.")
            return
        # Remove the corresponding row and column
        del self.graph[vertex]  # Remove the row
        for row in self.graph:
            del row[vertex]  # Remove the column
        self.vertices -= 1
        print(f"Vertex {vertex} removed.")

    def get_in_degree(self, vertex):
        """Calculate the in-degree of a vertex."""
        if vertex >= self.vertices:
            print(f"Error: Vertex {vertex} is out of range.")
            return
        # Count the number of non-zero entries in the column corresponding to the vertex
        in_degree = sum(1 for i in range(self.vertices) if self.graph[i][vertex] != 0)
        return in_degree

    def get_out_degree(self, vertex):
        """Calculate the out-degree of a vertex."""
        if vertex >= self.vertices:
            print(f"Error: Vertex {vertex} is out of range.")
            return
        # Count the number of non-zero entries in the row corresponding to the vertex
        out_degree = sum(1 for v in range(self.vertices) if self.graph[vertex][v] != 0)
        return out_degree

    def display(self):
        """Display the adjacency matrix."""
        for row in self.graph:
            print(row)


    def bfs(self, start_vertex):
        """Perform BFS starting from the given vertex."""
        if start_vertex >= self.vertices:
            print(f"Error: Start vertex {start_vertex} is out of range.")
            return

        visited = [False] * self.vertices  # Track visited vertices
        queue =[start_vertex]  # Initialize queue with the start vertex
        visited[start_vertex] = True
        bfs_order = []

        while queue: 
            current = queue.pop(0)
            bfs_order.append(current)

            # Visit all adjacent vertices
            for neighbor in range(self.vertices):
                if self.graph[current][neighbor] != 0 and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

        return bfs_order

    def dfs(self, start_vertex):
        """Perform DFS from a given start vertex using a stack."""
        if start_vertex >= self.vertices:
            print(f"Error: Vertex {start_vertex} is out of range.")
            return

        visited = [False] * self.vertices
        stack = [start_vertex]

        print("DFS Traversal (using stack):", end=" ")
        while stack:
            current = stack.pop()  # Get the top of the stack
            if not visited[current]:
                print(current, end=" ")
                visited[current] = True

                # Push all neighbors to the stack in reverse order for correct traversal
                for neighbor in range(self.vertices - 1, -1, -1):
                    if self.graph[current][neighbor] != 0 and not visited[neighbor]:
                        stack.append(neighbor)
        print()

    def topological_sort(self):
        """Perform topological sort of the directed acyclic graph."""
        in_degree = [0] * self.vertices
        # Calculate in-degree for all vertices
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.graph[i][j] != 0:
                    in_degree[j] += 1
        # Initialize stack with vertices having in-degree 0
        stack = [i for i in range(self.vertices) if in_degree[i] == 0]
        result = []

        while stack:
            u = stack.pop()
            result.append(u)

            # Reduce in-degree of neighbors
            for v in range(self.vertices):
                if self.graph[u][v] != 0:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        stack.append(v)

        # Check if there's a cycle (if result doesn't contain all vertices)
        if len(result) != self.vertices:
            print("Error: The graph has a cycle, topological sorting is not possible.")
        else:
            print("Topological Sort:", result)

    def dijkstra(self,start):
        if start>=self.vertices:
            print(f"Error: Vertex {start} is out of Range")
            return
        # Initialize distances as infinity
        distances=[float('inf')]*self.vertices
        distances[start]=0
        visited=[False]*self.vertices

        # Priority queue for the Dijkstra's algorithm (min-heap)
        pq=[(0,start)] # distance, vertex

        while pq:
            # Get the vertex with the minimum distance
            current_distance, current_vertex=heapq.heappop(pq)
            
            if visited[current_vertex]:
                continue
            visited[current_vertex] = True

            # Explore neighbors of the current vertex
            for neighbor in range(self.vertices):
                if self.graph[current_vertex][neighbor]>0:
                    weight=self.graph[current_vertex][neighbor]
                    distance=current_distance + weight

                    # If a shorter path is found
                    if distance < distances[neighbor]:
                        distances[neighbor]=distance
                        heapq.heappush(pq, (distance,neighbor))
        return distances

    def floyd_warshall(self):
        """Floyd-Warshall Algorithm to find shortest paths between all pairs of vertices."""
        # Initialize a distance matrix with 'inf'
        distance = [[float('inf')] * self.vertices for _ in range(self.vertices)]

        # Copy weights from the adjacency matrix to the distance matrix
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i == j:  # Distance to itself is zero
                    distance[i][j] = 0
                elif self.graph[i][j] != 0:  # Copy existing edge weights
                    distance[i][j] = self.graph[i][j]

        for k in range(self.vertices):  # Intermediate vertices
            for i in range(self.vertices):  # Source vertex
                for j in range(self.vertices):  # Destination vertex
                    if distance[i][k] + distance[k][j] < distance[i][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]

        # Check for negative weight cycles
        for i in range(self.vertices):
            if distance[i][i] < 0:
                print("Error: Graph contains a negative weight cycle.")
                return None

        # Display the shortest distance matrix
        print("Shortest distance matrix (Floyd-Warshall):")
        for row in distance:
            print(row)
        return distance

    def prim_mst(self):
        """Prim's algorithm to find the Minimum Spanning Tree (MST)."""
        # Start with vertex 0
        mst_set = [False] * self.vertices  # Track vertices included in MST
        key = [float('inf')] * self.vertices  # Key values to pick minimum weight edge
        parent = [-1] * self.vertices  # Array to store constructed MST

        # Priority queue to store (key, vertex)
        pq = [(0, 0)]  # (key, vertex) -> Start with vertex 0 with key 0
        key[0] = 0

        while pq:
            current_key, u = heapq.heappop(pq)

            if mst_set[u]:
                continue

            # Include the current vertex in MST
            mst_set[u] = True

            # Update key values and parent for adjacent vertices
            for v in range(self.vertices):
                if self.graph[u][v] != 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    heapq.heappush(pq, (key[v], v))

        # Print the MST
        print("Edges in the Minimum Spanning Tree (MST):")
        total_weight = 0
        for i in range(1, self.vertices):
            if parent[i] != -1:
                print(f"({parent[i]} - {i}) with weight {self.graph[i][parent[i]]}")
                total_weight += self.graph[i][parent[i]]

        print(f"Total weight of MST: {total_weight}")


# Example usage
g = GraphAdjMatrix(5)  # Create a graph with 5 initial vertices

# Add directed edges with weights
g.add_edge(0, 1, 3)
g.add_edge(0, 4, 2)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 5)
g.add_edge(1, 4, 2)
g.add_edge(2, 3, 2)
g.add_edge(3, 4, 4)

print("Adjacency Matrix Representation:")
g.display()

# Run Dijkstra's algorithm from vertex 0
start_vertex = 0
distances = g.dijkstra(start_vertex)

# Output the shortest distances from the start vertex
print(f"\nShortest distances from vertex {start_vertex}:")
for i in range(len(distances)):
    print(f"Vertex {i}: {distances[i]}")

# Run Floyd-Warshall algorithm
g.floyd_warshall()


# Perform BFS
start_vertex = 0
print(f"\nBFS starting from vertex {start_vertex}: {g.bfs(start_vertex)}")

print("\nDFS Traversal starting from vertex 0:")
g.dfs(0)

# Add a new vertex
g.add_vertex()
print("\nAfter adding a new vertex:")
g.display()

# Remove an edge
g.remove_edge(1, 3)
print("\nAfter removing edge 1 -> 3:")
g.display()

# Remove a vertex
g.remove_vertex(4)
print("\nAfter removing vertex 4:")
g.display()

# Get in-degree and out-degree
vertex = 1
print(f"\nIn-degree of vertex {vertex}: {g.get_in_degree(vertex)}")
print(f"Out-degree of vertex {vertex}: {g.get_out_degree(vertex)}")


# # Example usage
# g = GraphAdjMatrix(6)  # Create a graph with 6 vertices (DAG)

# # Add edges for a directed acyclic graph (DAG)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 3)
# g.add_edge(1, 4)
# g.add_edge(2, 4)
# g.add_edge(3, 5)
# g.add_edge(4, 5)
# # g.add_edge(5, 4)

# print("Adjacency Matrix Representation:")
# g.display()

# # Perform topological sort
# g.topological_sort()