from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "industry") == 1346
    assert count_ocurrences("data/jobs.csv", "10") == 1988
    assert count_ocurrences("data/jobs.csv", "") == 10343600
