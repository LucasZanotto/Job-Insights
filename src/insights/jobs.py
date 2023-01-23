from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:

    with open(path) as jobs_file:
        jobs_list = csv.DictReader(jobs_file)
        jobs_list1 = []
        for jobs in jobs_list:
            jobs_list1.append(jobs)
        return jobs_list1


# read("data/jobs.csv")


def get_unique_job_types(path: str) -> List[str]:
    with open(path) as jobs_file:
        jobs_list = csv.DictReader(jobs_file)
        jobs_add = []
        for jobs in jobs_list:
            # list = frozenset(jobs["job_type"])
            jobs_add.append(jobs["job_type"])
            job_set_unique = set(jobs_add)
        print(job_set_unique)

        return job_set_unique

    return jobs
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


get_unique_job_types("data/jobs.csv")


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    get_unique_job_types("data/jobs.csv")
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
