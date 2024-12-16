import matplotlib.pyplot as plt
import numpy as np

def generate_graphs(results, overall_stats):
    test_case_numbers = [f"TC {i+1}" for i in range(len(results))]
    
    ttc_top_choice = [result['ttc']['top_choice_percentage'] for result in results]
    random_top_choice = [result['random']['top_choice_percentage'] for result in results]
    sequential_top_choice = [result['sequential']['top_choice_percentage'] for result in results]
    
    ttc_matched = [result['ttc']['matched_percentage'] for result in results]
    random_matched = [result['random']['matched_percentage'] for result in results]
    sequential_matched = [result['sequential']['matched_percentage'] for result in results]
    
    ttc_avg_rank = [result['ttc']['average_preference_rank'] for result in results]
    random_avg_rank = [result['random']['average_preference_rank'] for result in results]
    sequential_avg_rank = [result['sequential']['average_preference_rank'] for result in results]
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    x = np.arange(len(test_case_numbers))
    
    # Plot % Agents Receiving Their Top Choice
    axes[0, 0].bar(x - 0.2, ttc_top_choice, 0.2, label='TTC')
    axes[0, 0].bar(x, random_top_choice, 0.2, label='Random')
    axes[0, 0].bar(x + 0.2, sequential_top_choice, 0.2, label='Sequential')
    axes[0, 0].set_xticks(x)
    axes[0, 0].set_xticklabels(test_case_numbers, rotation=45, ha="right")
    axes[0, 0].set_title('Percentage of Agents Receiving Their Top Choice')
    axes[0, 0].legend()
    
    # Plot % Agents Matched
    axes[0, 1].bar(x - 0.2, ttc_matched, 0.2, label='TTC')
    axes[0, 1].bar(x, random_matched, 0.2, label='Random')
    axes[0, 1].bar(x + 0.2, sequential_matched, 0.2, label='Sequential')
    axes[0, 1].set_xticks(x)
    axes[0, 1].set_xticklabels(test_case_numbers, rotation=45, ha="right")
    axes[0, 1].set_title('Percentage of Agents Matched')
    axes[0, 1].legend()
    
    # Plot Average Preference Rank of Matched Agents
    axes[1, 0].bar(x - 0.2, ttc_avg_rank, 0.2, label='TTC')
    axes[1, 0].bar(x, random_avg_rank, 0.2, label='Random')
    axes[1, 0].bar(x + 0.2, sequential_avg_rank, 0.2, label='Sequential')
    axes[1, 0].set_xticks(x)
    axes[1, 0].set_xticklabels(test_case_numbers, rotation=45, ha="right")
    axes[1, 0].set_title('Average Preference Rank of Matched Agents')
    axes[1, 0].legend()

    # Plot Overall Statistics
    categories = ['Top Choice %', '% Matched', 'Avg Rank']
    overall_labels = ['TTC', 'Random', 'Sequential']
    
    overall_data = [
        [overall_stats['ttc']['top_choice_percentage'], overall_stats['random']['top_choice_percentage'], overall_stats['sequential']['top_choice_percentage']],
        [overall_stats['ttc']['matched_percentage'], overall_stats['random']['matched_percentage'], overall_stats['sequential']['matched_percentage']],
        [overall_stats['ttc']['average_preference_rank'], overall_stats['random']['average_preference_rank'], overall_stats['sequential']['average_preference_rank']]
    ]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.arange(len(categories))
    width = 0.25

    rects1 = ax.bar(x - width, overall_data[0], width, label=overall_labels[0])
    rects2 = ax.bar(x, overall_data[1], width, label=overall_labels[1])
    rects3 = ax.bar(x + width, overall_data[2], width, label=overall_labels[2])

    # lables & titles
    ax.set_ylabel('Scores')
    ax.set_title('Overall Statistics by Algorithm')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()

    plt.tight_layout()
    plt.show()
