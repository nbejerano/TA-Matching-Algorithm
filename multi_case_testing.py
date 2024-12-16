from graph import *
from to_submit.proper_ttc import *
from to_submit.analysis import *
from to_submit.random_swapping import *
from to_submit.sequential import *
from to_submit.makeGraphs import *

if __name__ == "__main__":
    from unittest import test

    test_cases = [
        {
            "name": "5 Agents with Preferences Over All Other Shifts",
            "agents": {'a', 'b', 'c', 'd', 'e'},
            "shifts": {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
            "initialOwnership": {
                1: ['a'],
                2: ['b'],
                3: ['c'],
                4: ['d'],
                5: ['e']
            },
            "agentPreferences": {
                'a': [2, 3, 4, 5, 6, 7, 8, 9, 10],
                'b': [3, 4, 5, 1, 6, 7, 8, 9, 10],
                'c': [4, 5, 1, 2, 6, 7, 8, 9, 10],
                'd': [5, 1, 2, 3, 6, 7, 8, 9, 10],
                'e': [1, 2, 3, 4, 6, 7, 8, 9, 10]
            }
        },
        {
            "name": "10 Agents Each with Ownership Over a Different Shift",
            "agents": {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'},
            "shifts": {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
            "initialOwnership": {
                1: ['a'],
                2: ['b'],
                3: ['c'],
                4: ['d'],
                5: ['e'],
                6: ['f'],
                7: ['g'],
                8: ['h'],
                9: ['i'],
                10: ['j']
            },
            "agentPreferences": {
                'a': [2, 3, 4, 5],
                'b': [3, 4, 5, 6],
                'c': [4, 5, 6, 7],
                'd': [5, 6, 7, 8],
                'e': [6, 7, 8, 9],
                'f': [7, 8, 9, 10],
                'g': [8, 9, 10, 1],
                'h': [9, 10, 1, 2],
                'i': [10, 1, 2, 3],
                'j': [1, 2, 3, 4]
            }
        },
        {
            "name": "20 Agents with Variable Ownership per Shift and Preference Lists of Size 2",
            "agents": {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'},
            "shifts": {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
            "initialOwnership": {
                1: ['a', 'b'],
                2: ['c', 'd'],
                3: ['e', 'f'],
                4: ['g', 'h'],
                5: ['i', 'j'],
                6: ['k', 'l'],
                7: ['m', 'n'],
                8: ['o', 'p'],
                9: ['q', 'r'],
                10: ['s', 't']
            },
            "agentPreferences": {
                'a': [2, 4],
                'b': [3, 5],
                'c': [1, 6],
                'd': [3, 7],
                'e': [2, 8],
                'f': [4, 9],
                'g': [5, 10],
                'h': [6, 1],
                'i': [7, 2],
                'j': [8, 3],
                'k': [9, 4],
                'l': [10, 5],
                'm': [1, 6],
                'n': [2, 7],
                'o': [3, 8],
                'p': [4, 9],
                'q': [5, 10],
                'r': [6, 1],
                's': [7, 2],
                't': [8, 3]
            }
        },
        {
            "name": "20 Agents with Variable Ownership per Shift and Preference Lists of Size 8",
            "agents": {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'},
            "shifts": {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
            "initialOwnership": {
                1: ['a', 'b'],
                2: ['c', 'd'],
                3: ['e', 'f'],
                4: ['g', 'h'],
                5: ['i', 'j'],
                6: ['k', 'l'],
                7: ['m', 'n'],
                8: ['o', 'p'],
                9: ['q', 'r'],
                10: ['s', 't']
            },
            "agentPreferences": {
                'a': [2, 3, 4, 5, 6, 7, 8, 9],
                'b': [2, 3, 4, 5, 6, 7, 8, 9],
                'c': [1, 3, 4, 5, 6, 7, 8, 10],
                'd': [1, 3, 4, 5, 6, 7, 8, 10],
                'e': [1, 2, 4, 5, 6, 7, 9, 10],
                'f': [1, 2, 4, 5, 6, 7, 9, 10],
                'g': [1, 2, 3, 5, 6, 8, 9, 10],
                'h': [1, 2, 3, 5, 6, 8, 9, 10],
                'i': [1, 2, 3, 4, 6, 7, 9, 10],
                'j': [1, 2, 3, 4, 6, 7, 9, 10],
                'k': [1, 2, 3, 4, 5, 7, 8, 10],
                'l': [1, 2, 3, 4, 5, 7, 8, 10],
                'm': [1, 2, 3, 4, 5, 6, 8, 9],
                'n': [1, 2, 3, 4, 5, 6, 8, 9],
                'o': [1, 2, 3, 4, 5, 6, 7, 10],
                'p': [1, 2, 3, 4, 5, 6, 7, 10],
                'q': [1, 2, 3, 4, 5, 6, 7, 8],
                'r': [1, 2, 3, 4, 5, 6, 7, 8],
                's': [1, 2, 3, 4, 5, 6, 7, 9],
                't': [1, 2, 3, 4, 5, 6, 7, 9]
            }
        },
        {
            "name": "15 Agents with One Shift Owned by 5 Agents",
            "agents": {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'},
            "shifts": {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
            "initialOwnership": {
                1: ['a', 'b', 'c', 'd', 'e'],
                2: ['f'],
                3: ['g'],
                4: ['h'],
                5: ['i'],
                6: ['j'],
                7: ['k'],
                8: ['l'],
                9: ['m'],
                10: ['n', 'o']
            },
            "agentPreferences": {
                'a': [2, 6, 7],
                'b': [3, 6, 8],
                'c': [4, 7, 9],
                'd': [5, 8, 10],
                'e': [6, 9, 2],
                'f': [1, 7, 10],
                'g': [1, 8, 9],
                'h': [1, 2, 6],
                'i': [1, 3, 7],
                'j': [1, 4, 8],
                'k': [1, 5, 9],
                'l': [1, 6, 10],
                'm': [1, 7, 2],
                'n': [1, 8, 3],
                'o': [1, 9, 4]
            }
        }
    ]

    results = []

    # Loop through each test case to run all 3 algorithms on each
    for i, test_case in enumerate(test_cases):
        agents = test_case["agents"]
        shifts = test_case["shifts"]
        initialOwnership = test_case["initialOwnership"]
        agentPreferences = test_case["agentPreferences"]
        test_case_name = test_case["name"]

        results.append(run_all_algorithms(agents, shifts, agentPreferences, initialOwnership, test_case_name))

    # Compute overall statistics
    overall_stats = compute_overall_statistics(results)
    print(overall_stats)
    print("\nOverall Statistics:")
    for algorithm in overall_stats:
        print(f"\n{algorithm.capitalize()} Algorithm:")
        print_stats(overall_stats[algorithm])

    generate_graphs(results, overall_stats)
