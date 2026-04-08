from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from sesion_4.time_utils import calculate_duration, is_valid_shift


@pytest.mark.parametrize(
    ("start", "end", "expected_minutes"),
    [
        ("09:00", "10:00", 60),
        ("08:15", "09:00", 45),
        ("14:00", "14:30", 30),
        ("00:00", "00:00", 0),
        ("9:00", "10:00", 60),
    ],
)
def test_calculate_duration_returns_minutes_for_same_day_valid_times(
    start: str, end: str, expected_minutes: int
) -> None:
    # Arrange

    # Act
    result = calculate_duration(start, end)

    # Assert
    assert result == expected_minutes


@pytest.mark.parametrize(
    ("start", "end", "expected_minutes"),
    [
        ("23:30", "00:15", 45),
        ("22:00", "06:00", 480),
        ("23:59", "00:00", 1),
        ("18:00", "09:00", 900),
    ],
)
def test_calculate_duration_handles_shifts_that_cross_midnight(
    start: str, end: str, expected_minutes: int
) -> None:
    # Arrange

    # Act
    result = calculate_duration(start, end)

    # Assert
    assert result == expected_minutes


@pytest.mark.parametrize(
    ("start", "end"),
    [
        ("18:00", "09:00"),
        ("23:30", "00:15"),
        ("23:59", "00:00"),
    ],
)
def test_calculate_duration_does_not_return_negative_minutes_for_overnight_shifts(
    start: str, end: str
) -> None:
    # Arrange

    # Act
    result = calculate_duration(start, end)

    # Assert
    assert result >= 0


@pytest.mark.parametrize(
    ("start", "end"),
    [
        ("24:00", "10:00"),
        ("09:60", "10:00"),
        ("09:00", "ab:cd"),
        ("xx:yy", "10:00"),
        ("", "10:00"),
        ("12-00", "13:00"),
    ],
)
def test_calculate_duration_returns_minus_one_for_invalid_time_inputs(
    start: str, end: str
) -> None:
    # Arrange

    # Act
    result = calculate_duration(start, end)

    # Assert
    assert result == -1


@pytest.mark.parametrize(
    ("start", "end"),
    [
        ("09:00", "09:30"),
        ("09:00", "17:00"),
        ("12:15", "16:15"),
        ("23:30", "00:00"),
        ("23:30", "00:15"),
        ("22:00", "06:00"),
    ],
)
def test_is_valid_shift_returns_true_for_durations_within_allowed_range(
    start: str, end: str
) -> None:
    # Arrange

    # Act
    result = is_valid_shift(start, end)

    # Assert
    assert result is True


@pytest.mark.parametrize(
    ("start", "end"),
    [
        ("09:00", "09:29"),
        ("09:00", "17:01"),
        ("09:00", "09:00"),
        ("18:00", "09:00"),
    ],
)
def test_is_valid_shift_returns_false_for_durations_outside_allowed_range(
    start: str, end: str
) -> None:
    # Arrange

    # Act
    result = is_valid_shift(start, end)

    # Assert
    assert result is False


@pytest.mark.parametrize(
    ("start", "end"),
    [
        ("24:00", "10:00"),
        ("09:00", "24:30"),
        ("invalid", "10:00"),
        ("09:61", "10:00"),
    ],
)
def test_is_valid_shift_returns_false_for_invalid_time_inputs(
    start: str, end: str
) -> None:
    # Arrange

    # Act
    result = is_valid_shift(start, end)

    # Assert
    assert result is False
