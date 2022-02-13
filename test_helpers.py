from datetime import datetime, timedelta, timezone
from .helpers import compare_timestamps


def test_compare_timestamps_valid():
    current_time = datetime.now(timezone.utc)
    mock_db_query_time = current_time - timedelta(minutes=3)

    result = compare_timestamps(query_time=current_time, db_time=mock_db_query_time)
    assert result


def test_compare_timestamps_invalid():
    current_time = datetime.now(timezone.utc)
    mock_db_query_time = current_time - timedelta(minutes=6)

    result = compare_timestamps(query_time=current_time, db_time=mock_db_query_time)
    assert not result
