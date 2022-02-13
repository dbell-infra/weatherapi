from datetime import datetime


def compare_timestamps(db_time: datetime, query_time: datetime, cache_minutes: int = 5) -> bool:
    """
    :param db_time:
    :param query_time:
    :param cache_minutes:
    :return: Boolean value describing value of cache data
    """
    cache_seconds = 60 * cache_minutes
    result = query_time - db_time
    if result.total_seconds() <= cache_seconds:
        return True
    return False
