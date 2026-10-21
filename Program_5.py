from dataclasses import dataclass
from typing import List


@dataclass
class Job:
    id: int
    deadline: int
    profit: int


def job_scheduling(jobs: List[Job]) -> List[int]:
    if any(job.deadline < 0 for job in jobs):
        raise ValueError("Deadlines cannot be negative")

    # Consider only jobs that can earn positive profit
    jobs = [job for job in jobs if job.deadline > 0
            and job.profit > 0]

    if not jobs:
        return []

    # Sort jobs by decreasing profit
    jobs.sort(key=lambda job: job.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)

    # Each index represents a time slot
    slots = [None] * (max_deadline + 1)

    for job in jobs:
        # Find the latest available slot before the deadline
        for slot in range(
            min(job.deadline, max_deadline), 0, -1
        ):
            if slots[slot] is None:
                slots[slot] = job.id
                break

    # Return scheduled job IDs in chronological order
    return [job_id for job_id in slots[1:]
            if job_id is not None]


# Example
jobs = [
    Job(1, 2, 100),
    Job(2, 1, 19),
    Job(3, 2, 27),
    Job(4, 1, 25),
    Job(5, 3, 15)
]

sequence = job_scheduling(jobs)

print("Optimal job sequence:", sequence)

# Calculate total profit
job_profit = {job.id: job.profit for job in jobs}
total_profit = sum(job_profit[job_id] for job_id in sequence)

print("Maximum profit:", total_profit)
