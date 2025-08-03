from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    jobs = []
    for idx, job in enumerate(print_jobs):
        pj = PrintJob(id=job["id"], volume=job["volume"], priority=job["priority"], print_time=job["print_time"])
        jobs.append((idx, pj))
    # Sort by priority then original index
    jobs_sorted = [pj for _, pj in sorted(jobs, key=lambda x: (x[1].priority, x[0]))]
    constraints_obj = PrinterConstraints(max_volume=constraints["max_volume"], max_items=constraints["max_items"])

    assigned = set()
    print_order = []
    total_time = 0

    for i, job in enumerate(jobs_sorted):
        if job.id in assigned:
            continue
        group = [job]
        current_volume = job.volume
        current_items = 1
        assigned.add(job.id)

        for next_job in jobs_sorted[i+1:]:
            if next_job.id in assigned:
                continue
            if current_items + 1 > constraints_obj.max_items:
                continue
            if current_volume + next_job.volume > constraints_obj.max_volume:
                continue
            group.append(next_job)
            current_volume += next_job.volume
            current_items += 1
            assigned.add(next_job.id)

        group_time = max(j.print_time for j in group)
        total_time += group_time
        print_order.extend([j.id for j in group])

    return {
        "print_order": print_order,
        "total_time": total_time
    }

# Testing
def test_printing_optimization():
    # Test 1: Models with the same priority
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    # Тест 2: Models with different priorities
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # lab work
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},  # thesis
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}  # personal project
    ]

    # Тест 3: Exceeding volume constraints
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Test 1 (same priority):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Print order: {result1['print_order']}")
    print(f"Total time: {result1['total_time']} minutes")

    print("\nTest 2 (different priorities):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Print order: {result2['print_order']}")
    print(f"Total time: {result2['total_time']} minutes")

    print("\nTest 3 (exceeding constraints):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Print order: {result3['print_order']}")
    print(f"Total time: {result3['total_time']} minutes")

if __name__ == "__main__":
    test_printing_optimization()