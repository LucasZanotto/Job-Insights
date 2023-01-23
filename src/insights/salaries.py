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


if __name__ == "__main__":
    print(get_max_salary("data/jobs.csv"))
    print(get_min_salary("data/jobs.csv"))


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
