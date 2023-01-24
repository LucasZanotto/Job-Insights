from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_list = read(path)
    industry_add = set()
    for jobs in jobs_list:
        if len(jobs["industry"]) > 0:
            industry_add.add((jobs["industry"]))
    print(industry_add)
    return industry_add


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobs_list = jobs
    jobs_add = []
    for job in jobs_list:
        if job["industry"] == industry:
            jobs_add.append(job)

    return jobs_add


if __name__ == "__main__":
    # print(get_unique_industries("data/jobs.csv"))
    print(
        filter_by_industry(
            [
                {"id": 1, "industry": "agriculture"},
                {"id": 2, "industry": "agriculture"},
                {"id": 3, "industry": "solar energy"},
                {"id": 4, "industry": "solar energy"},
                {"id": 5, "industry": "bank"},
                {"id": 6, "industry": "bank"},
                {"id": 7, "industry": "mechanical engineering"},
                {"id": 8, "industry": "mechanical engineering"},
                {"id": 9, "industry": "translation"},
                {"id": 10, "industry": "translation"},
                {"id": 11, "industry": "finances"},
                {"id": 12, "industry": "finances"},
            ],
            "agriculture",
        )
    )
