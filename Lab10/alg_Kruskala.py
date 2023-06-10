class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def kruskal(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = {}

        for u, v, _ in self.graph:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v

        while e < len(parent) - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                parent[x] = y

        minimum_cost = 0
        for u, v, weight in result:
            minimum_cost += weight
            print(f"{u} -- {v} == {weight}")

        print(f"Minimalne koszty = {minimum_cost}")


g = Graph()
g.add_edge('A','B', 4)
g.add_edge('A','G', 8)
g.add_edge('B','C', 8)
g.add_edge('B','G', 11)
g.add_edge('C','E', 2)
g.add_edge('C','D', 7)
g.add_edge('C','I', 4)
g.add_edge('D','F', 9)
g.add_edge('D','I', 14)
g.add_edge('E','G', 7)
g.add_edge('E','H', 6)
g.add_edge('F','I', 10)
g.add_edge('G','H', 1)
g.add_edge('H','I', 2)

g.kruskal()
