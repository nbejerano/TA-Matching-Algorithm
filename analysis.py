from graph import *
from to_submit.proper_ttc import *
from to_submit.analysis import *
from to_submit.random_swapping import *
from to_submit.sequential import *

def run_all_algorithms(agents, shifts, agentPreferences, initialOwnership, test_case_name):
    print(f"\nRunning {test_case_name}:")
    # Run Top Trading Cycles
    ttc_matching = topTradingCycles(agents, shifts, agentPreferences, initialOwnership)
    ttc_stats = evaluate_matching(agents, shifts, agentPreferences, initialOwnership, ttc_matching)
    print("Analysis of TTC matching: ")
    print_stats(ttc_stats)

    # Run Random Swapping
    random_matching = randomSwapMatching(agents, shifts, agentPreferences, initialOwnership)
    random_stats = evaluate_matching(agents, shifts, agentPreferences, initialOwnership, random_matching)
    print("Analysis of Random matching: ")
    print_stats(random_stats)

    # Run Sequential Matching
    sequential_matching = sequentialMatching(agents, shifts, agentPreferences, initialOwnership)
    sequential_stats = evaluate_matching(agents, shifts, agentPreferences, initialOwnership, sequential_matching)
    print("Analysis of Sequential matching: ")
    print_stats(sequential_stats)

    return {
        "ttc": ttc_stats,
        "random": random_stats,
        "sequential": sequential_stats
    }

def evaluate_matching(agents, shifts, agentPreferences, initialOwnership, allocation):
    total_agents = len(agents)
    matched_agents = len([a for a in allocation if allocation[a] is not None])
    unmatched_agents = total_agents - matched_agents
    top_choice_count = 0
    total_preference_rank = 0

    # Calculate statistics
    for agent, shift in allocation.items():
        if shift is not None:
            preferences = agentPreferences[agent]
            if shift in preferences:
                rank = preferences.index(shift) + 1  
                total_preference_rank += rank
                if rank == 1:
                    top_choice_count += 1
            else:
                print(f"Warning: Shift {shift} is not in the preference list of agent {agent}")

    # Calculate percentages and average rank
    top_choice_percentage = (top_choice_count / total_agents) * 100
    matched_percentage = (matched_agents / total_agents) * 100
    unmatched_percentage = (unmatched_agents / total_agents) * 100
    average_preference_rank = total_preference_rank / matched_agents if matched_agents > 0 else 0

    return {
        "top_choice_percentage": top_choice_percentage,
        "matched_percentage": matched_percentage,
        "unmatched_percentage": unmatched_percentage,
        "average_preference_rank": average_preference_rank
    }

def print_stats(stats):
    print(f"Percentage of agents receiving their top choice: {stats['top_choice_percentage']}%")
    print(f"Percentage of agents matched: {stats['matched_percentage']}%")
    print(f"Percentage of agents left without a match: {stats['unmatched_percentage']}%")
    print(f"Average preference rank of matched agents: {stats['average_preference_rank']}")

def compute_overall_statistics(results):
    overall_stats = {
        "ttc": {
            "top_choice_percentage": 0,
            "matched_percentage": 0,
            "unmatched_percentage": 0,
            "average_preference_rank": 0
        },
        "random": {
            "top_choice_percentage": 0,
            "matched_percentage": 0,
            "unmatched_percentage": 0,
            "average_preference_rank": 0
        },
        "sequential": {
            "top_choice_percentage": 0,
            "matched_percentage": 0,
            "unmatched_percentage": 0,
            "average_preference_rank": 0
        }
    }

    for result in results:
        for algorithm in overall_stats:
            for stat in overall_stats[algorithm]:
                overall_stats[algorithm][stat] += result[algorithm][stat]

    num_cases = len(results)
    for algorithm in overall_stats:
        for stat in overall_stats[algorithm]:
            overall_stats[algorithm][stat] /= num_cases

    return overall_stats