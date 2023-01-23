from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    with open(path) as jobs_file:
        jobs_list = csv.DictReader(jobs_file)
        jobs_add = []
        for jobs in jobs_list:
            if len(jobs) > 0:
                jobs_add.append(jobs["industry"])
                job_set_unique = set(jobs_add)
        return job_set_unique

    return jobs
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    raise NotImplementedError


get_unique_industries("data/jobs.csv")


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
