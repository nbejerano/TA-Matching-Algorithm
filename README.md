# Market Design Final Project: TA Shift Swapping Simulation

This project simulates the market for swapping LaIR shifts among Teaching Assistants (TAs) in Stanford's introductory computer science courses (CS106A/B). The project involves designing algorithms, running simulations, and analyzing results to improve the current manual swap system.

## Project Overview
The existing shift-swapping system relies on a Slack channel where TAs manually coordinate swaps. This project proposes an automated system using matching algorithms to optimize the process.

### Key Algorithms Implemented:
1. **Modified Top Trading Cycles (TTC):** Adapts the classic TTC algorithm for shift-swapping, ensuring efficient and strategyproof swaps.
2. **Sequential Algorithm:** Simulates the current manual process for comparison.
3. **Random Algorithm:** Provides a baseline for evaluation by randomly assigning swaps.

### Evaluation Metrics:
- Percentage of agents receiving their top choice.
- Percentage of agents successfully matched.
- Average preference rank of assigned swaps.

### Key Findings:
- The Modified TTC algorithm outperformed the other two algorithms in most scenarios.
- The Sequential Algorithm closely mimicked the current Slack-based system.
- The Random Algorithm consistently performed worst.

## Repository Structure
```
📂 TA-Matching-Algorithm
 ├── analysis.py            # Code for evaluating algorithm performance
 ├── makeGraphs.py         # Code for generating performance graphs
 ├── multi_case_testing.py  # Runs simulations with various test cases
 ├── proper_ttc.py         # Implementation of the Modified TTC Algorithm
 ├── random_swapping.py    # Implementation of the Random Algorithm
 └── sequential.py         # Implementation of the Sequential Algorithm
```

For more detailed project insights, see Final Paper.docx



