# TASK 1 - 3D Printer Queue Optimiser

Greedy scheduler that batches print jobs by priority within volume/item limits.  
Batch time = max `print_time` in the group. Higher priority (1 = highest) jobs start first.

**Input:**  
- `print_jobs`: list of `{"id", "volume", "priority", "print_time"}`  
- `constraints`: `{"max_volume", "max_items"}`

**Output:**  
```json
{
  "print_order": [...],
  "total_time": N
}

**Tests:**
Run the built-in test function to validate same/mixed priorities and constraint handling.

Requires: Python 3.7+ (optional: mypy for static type checks)
