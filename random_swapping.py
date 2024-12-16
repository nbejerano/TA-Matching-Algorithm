import random

def randomSwapMatching(agents, shifts, agentPreferences, initialOwnership):
    # Initialize
    allocation = {}
    for shift, owners in initialOwnership.items():
        for owner in owners:
            if owner in agents:
                allocation[owner] = shift

    agent_list = list(agents)

    for _ in range(len(agent_list)):
        # random swaps
        agent1, agent2 = random.sample(agent_list, 2)
        shift1 = allocation.get(agent1, None)
        shift2 = allocation.get(agent2, None)

        if shift1 is not None and shift2 is not None:
            if shift2 in agentPreferences[agent1] and shift1 in agentPreferences[agent2]:
                allocation[agent1], allocation[agent2] = allocation[agent2], allocation[agent1]

    # mark agents that were not switched as None
    for agent in agent_list:
        shift = allocation.get(agent, None)
        if shift is not None and shift not in agentPreferences[agent]:
            allocation[agent] = None  

    return allocation
