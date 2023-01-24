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
            jobs_add.append(jobs["job_type"])
            job_set_unique = set(jobs_add)

        return job_set_unique

    return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_list = jobs
    jobs_add = []
    for job in jobs_list:
        if job["job_type"] == job_type:
            jobs_add.append(job)

    return jobs_add


if __name__ == "__main__":
    print(get_unique_job_types("data/jobs.csv"))
    print(
        filter_by_job_type(
            [
                {"id": 1, "job_type": "PART_TIME"},
                {"id": 2, "job_type": "PART_TIME"},
                {"id": 3, "job_type": "OTHER"},
                {"id": 4, "job_type": "OTHER"},
                {"id": 5, "job_type": "FULL_TIME"},
                {"id": 6, "job_type": "FULL_TIME"},
                {"id": 7, "job_type": "CONTRACTOR"},
                {"id": 8, "job_type": "CONTRACTOR"},
                {"id": 9, "job_type": "TEMPORARY"},
                {"id": 10, "job_type": "TEMPORARY"},
                {"id": 11, "job_type": "INTERN"},
                {"id": 12, "job_type": "INTERN"},
            ],
            "TEMPORARY",
        )
    )
