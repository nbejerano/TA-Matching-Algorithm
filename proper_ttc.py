from graph import *

# getAgents: graph, vertex -> set(vertex)
# get the set of agents on a cycle starting at the given vertex
def getAgents(G, cycle, agents):
    if cycle.vertexId in agents:
        cycle = cycle.anyNext()

    startingShift = cycle
    currentVertex = startingShift.anyNext()
    theAgents = set()

    while currentVertex not in theAgents:
        theAgents.add(currentVertex)
        currentVertex = currentVertex.anyNext()
        currentVertex = currentVertex.anyNext()

    return theAgents

# anyCycle: graph -> vertex
# find any vertex involved in a cycle
def anyCycle(G):
    visited = set()
    v = G.anyVertex()

    while v not in visited:
        visited.add(v)
        if len(v.outgoingEdges) == 0:  # Handle vertices with no outgoing edges
            raise ValueError("Vertex with no outgoing edges encountered.")
        v = v.anyNext()

    return v

# find a core matching of agents to shifts
# agents and shifts are unique identifiers for the agents and shifts involved
# agentPreferences is a dictionary with keys being agents and values being
# lists that are permutations of the list of all shifts.
# initialOwnership is a dict {shifts: list of agents}
def topTradingCycles(agents, shifts, agentPreferences, initialOwnership):
    # Filter out shifts with no initial owners
    shifts_with_owners = {h for h in shifts if initialOwnership.get(h)}

    # Adjust preferences to exclude shifts with no owners
    adjustedPreferences = {a: [s for s in prefs if s in shifts_with_owners] for a, prefs in agentPreferences.items()}

    # form initial graph
    agents = set(agents)
    vertexSet = agents | shifts_with_owners
    G = Graph(vertexSet)

    # maps agent to an index of agentPreferences[agent] list
    currentPreferenceIndex = {a: 0 for a in agents}
    def preferredShift(a):
        while currentPreferenceIndex[a] < len(adjustedPreferences[a]) and adjustedPreferences[a][currentPreferenceIndex[a]] not in shifts_with_owners:
            currentPreferenceIndex[a] += 1
        if currentPreferenceIndex[a] < len(adjustedPreferences[a]):
            return adjustedPreferences[a][currentPreferenceIndex[a]]
        else:
            raise ValueError(f"No valid shifts left for agent {a}")

    for a in agents:
        try:
            G.addEdge(a, preferredShift(a))
        except ValueError:
            pass  

    for h, owners in initialOwnership.items():
        if owners:
            for owner in owners:
                G.addEdge(h, owner)

    # iteratively remove cycles
    allocation = {}
    while len(G.vertices) > 0:
        try:
            cycle = anyCycle(G)
        except ValueError as e:
            print(e)
            break
        cycleAgents = getAgents(G, cycle, agents)

        # resolve cycles, assign agents
        for a in cycleAgents:
            h = a.anyNext().vertexId
            allocation[a.vertexId] = h
            G.delete(a)
            G.delete(h)

        for a in agents:
            if a in G.vertices and G[a].outdegree() == 0:
                try:
                    while preferredShift(a) not in G.vertices:
                        currentPreferenceIndex[a] += 1
                    G.addEdge(a, preferredShift(a))
                except ValueError:
                    # No valid shifts left to assign, remove agent and their shift from the graph
                    owned_shifts = [h for h, owners in initialOwnership.items() if a in owners]
                    for shift_to_remove in owned_shifts:
                        if shift_to_remove in G.vertices:
                            G.delete(shift_to_remove)
                            shifts_with_owners.remove(shift_to_remove)
                    if a in G.vertices:
                        G.delete(a)

    print(allocation)
    return allocation

