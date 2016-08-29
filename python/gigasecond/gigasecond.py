from datetime import timedelta


def add_gigasecond(strt_time):
    return strt_time + timedelta(seconds=1E9)
