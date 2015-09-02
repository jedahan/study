class unnamed_graph:
    adj = []
    def edge(self, fro, to):
        if fro > to:
            temp = fro
            fro = to
            to = temp
        if len(self.adj) <= fro:
            self.adj.append(set())
        self.adj[fro].add(to)

    def __str__(self):
        s = ""
        for node,edges in enumerate(self.adj):
            for edge in edges:
                s = s + "{} -> {}\n".format(node, edge)

        return s

class graph:
    adj = {}
    vertices = {}
    directed = False
    def edge(self, fro, to):
        if not self.vertices.has_key(fro): self.vertices[fro] = {}
        if not self.vertices.has_key(to): self.vertices[to] = {}
        if not self.adj.has_key(fro): self.adj[fro] = []
        if not to in self.adj[fro]: self.adj[fro].append(to)
        if not self.directed:
            if not self.adj.has_key(to): self.adj[to] = []
            if not to in self.adj[to]: self.adj[to].append(fro)

    def __str__(self):
        s = ""
        for node in self.adj:
            for edge in self.adj[node]:
                s = s + "{} -- {}\n".format(node, edge)

        return s

def breadth_first_search(G, start):
    for _,v in G.vertices.viewitems():
        v["color"] = "white"
        v["distance"] = float("inf")
        v["pi"] = None
    queue = [start]
    item = G.vertices[start]
    item["color"] = "gray"
    item["distance"] = 0
    item["parent"] = None
    while len(queue) > 0:
        u = queue.pop()
        for v in G.adj[u]:
            fro = G.vertices[u]
            to = G.vertices[v]
            if to["color"] == "white":
                queue.append(v)
                to["color"] = "gray"
                to["distance"] = fro["distance"] + 1
                to["parent"] = fro
                print("{} away from {}".format(to["distance"],v) )
        fro["color"] = "black"

welp = graph()
print(welp)
welp.edge("v","r")
welp.edge("r","s")
welp.edge("s","w")
welp.edge("w","t")
welp.edge("w","x")
welp.edge("t","x")
welp.edge("x","u")
welp.edge("x","y")
welp.edge("t","u")
welp.edge("y","u")
print(welp)
breadth_first_search(welp,"s")
