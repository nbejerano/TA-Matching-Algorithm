# Sequential 
# Agents are processed one at a time in the order they are input. 
# The agent that is inputted looks through the other available 
# people in the list and if there is a direct possible swap it is made. 
# Once a swap is made the two people are removed from the graph

class Agent:
    def __init__(self, id):
        self.id = id
        self.preferences = []
        self.owned_shift = None

    def set_preferences(self, preferences):
        self.preferences = preferences

    def set_owned_shift(self, shift):
        self.owned_shift = shift

def sequentialMatching(agents, shifts, agentPreferences, initialOwnership):
    # Initialize
    agent_dict = {a: Agent(a) for a in agents}
    for agent, prefs in agentPreferences.items():
        agent_dict[agent].set_preferences(prefs)
    for shift, owners in initialOwnership.items():
        for owner in owners:
            agent_dict[owner].set_owned_shift(shift)
    
    seen = {}  # map of agents that have been processed but not matched
    allocation = {}  # final allocation of agents with new shifts if swapped

    for agent_id, agent in agent_dict.items():
        if agent_id in allocation:
            continue

        for preferred_shift in agent.preferences:
            if preferred_shift in initialOwnership:
                for owner in initialOwnership[preferred_shift]:
                    if owner != agent_id and owner not in allocation:
                        owner_agent = agent_dict[owner]
                        if agent.owned_shift in owner_agent.preferences:
                            # Found swap
                            allocation[agent_id] = preferred_shift
                            allocation[owner] = agent.owned_shift
                            break
                if agent_id in allocation:
                    break
        
        if agent_id not in allocation:
            seen[agent_id] = agent

    # mark unswapped agents as None
    unmatched_agents = set(seen.keys())
    for agent_id in unmatched_agents:
        allocation[agent_id] = None

    return allocation
