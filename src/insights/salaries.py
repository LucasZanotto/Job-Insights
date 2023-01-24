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
        return job["max_salary"] >= int(salary) >= job["min_salary"] 
    except (ValueError, KeyError, TypeError):
        raise ValueError
        
    # job_max = str(job["max_salary"]).isnumeric()
    # job_min = str(job["min_salary"]).isnumeric()
    # if int(job["min_salary"]) > int(job["max_salary"]):
    #     raise ValueError
    # elif job_max is False and job_min is False:
    #     raise ValueError
    # elif str(salary).isnumeric() is False:
    #     raise ValueError
    # elif (
    #     job["min_salary"] is None and job["max_salary"] is None
    # ):
    #     raise ValueError
    # elif job["max_salary"] >= int(salary) >= job["min_salary"]:
    #     return True
    # return False


if __name__ == "__main__":
    # print(get_max_salary("data/jobs.csv"))
    # print(get_min_salary("data/jobs.csv"))
    print(matches_salary_range([{"max_salary": 0, "min_salary": 10}], 0))


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
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
