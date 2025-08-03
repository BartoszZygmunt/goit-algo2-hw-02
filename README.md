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
