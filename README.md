# TASK 1 - 3D Printer Queue Optimiser

Greedy scheduler that batches print jobs by priority within volume/item limits.  
Jobs are grouped into batches where each batch respects the volume and item constraints.  
Batch execution time equals the maximum `print_time` within that batch.  
Higher priority jobs (1 = highest priority) are scheduled first.

## Algorithm

1. Sort jobs by priority (ascending, so 1 comes first)
2. For each priority level, create batches respecting constraints
3. Within each batch, execution time = max(print_time) of all jobs in batch
4. Return ordered list of job IDs and total execution time

**Input:**

- `print_jobs`: list of `{"id", "volume", "priority", "print_time"}`
- `constraints`: `{"max_volume", "max_items"}`

**Output:**

```json
{
  "print_order": ["job_id_1", "job_id_2", ...],
  "total_time": 150
}
```

## Example Usage

```python
from goit_algo2_hw_02_task1 import optimize_printing

jobs = [
    {"id": "A", "volume": 50, "priority": 1, "print_time": 30},
    {"id": "B", "volume": 30, "priority": 2, "print_time": 20}
]
constraints = {"max_volume": 100, "max_items": 5}

result = optimize_printing(jobs, constraints)
print(result)  # {"print_order": ["A", "B"], "total_time": 50}
```

**Tests:**
Run the built-in test function to validate same/mixed priorities and constraint handling.

**Requirements:** Python 3.7+ (optional: mypy for static type checks)

# TASK 2 - Optimal Rod Cutting for Maximum Profit

Greedy-free dynamic solution to the rod cutting problem. Implements two DP approaches:

- **Memoization (top-down)**
- **Tabulation (bottom-up)**

## Overview

Given a rod length and a list of prices (`prices[i]` is price for length `i+1`), compute:

- Maximum profit
- Cutting strategy (list of segment lengths)
- Number of cuts

## Input

```python
length = 5
prices = [2, 5, 7, 8, 10]
```

Output (example)
json
Copy
Edit
{
"max_profit": 12,
"cuts": [2,2,1], # or [1,2,2] depending on method
"number_of_cuts": 2
}
Usage
Call the two functions:

python
Copy
Edit
from your_module import rod_cutting_memo, rod_cutting_table

memo = rod_cutting_memo(5, [2,5,7,8,10])
table = rod_cutting_table(5, [2,5,7,8,10])
print(memo, table)
Run built-in tests:

bash
Copy
Edit
python your_script.py
Functions
rod_cutting_memo(length: int, prices: List[int]) -> Dict
Top-down DP with memoization.

rod_cutting_table(length: int, prices: List[int]) -> Dict
Bottom-up tabulation.

Each returns:

max_profit: int

cuts: List[int]

number_of_cuts: int

Expected Test Cases
Base case (e.g., length=5): profit 12, cuts [1,2,2] or [2,2,1]

No cut optimal

All unit cuts

Requirements
Python 3.7+
(Optional) use mypy or linters for type hints.
