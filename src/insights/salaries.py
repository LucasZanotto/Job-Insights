from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    salary_add = set()
    for jobs in jobs_list:
        if jobs["max_salary"].isnumeric():
            salary_add.add(int(jobs["max_salary"]))
    high_salary = max(salary_add)

    return high_salary


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    salary_add = set()
    for jobs in jobs_list:
        if jobs["min_salary"].isnumeric():
            salary_add.add(int(jobs["min_salary"]))
    lower_salary = min(salary_add)

    return lower_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError
        return int(job["max_salary"]) >= int(salary) >= int(job["min_salary"])
    except (ValueError, KeyError, TypeError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_list = jobs
    jobs_add = []
    for job in jobs_list:
        try:
            if matches_salary_range(job, salary):
                jobs_add.append(job)
        except (ValueError):
            continue
    return jobs_add


if __name__ == "__main__":
    # print(get_max_salary("data/jobs.csv"))
    # print(get_min_salary("data/jobs.csv"))
    # print(matches_salary_range([{"max_salary": 0, "min_salary": 10}], 0))
    print(filter_by_salary_range([
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 15000, "min_salary": 0},
        {"max_salary": 1500, "min_salary": 0},
        {"max_salary": -1, "min_salary": 10},
    ], 1000))
