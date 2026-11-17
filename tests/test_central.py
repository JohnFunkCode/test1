import statistics

import pytest

from pkg2 import central


@pytest.mark.parametrize("values, expected", [([1, 2, 6], 3.0), ([-3.5, -1, 3], -0.5), ([4], 4.0)])
def test_mean(values, expected):
    result = central.mean(values)
    assert result == pytest.approx(expected)
    assert isinstance(result, float)


def test_mean_generator():
    assert central.mean(value for value in [1, 2, 6]) == pytest.approx(3.0)


@pytest.mark.parametrize("values, expected", [([3, 1, 2], 2.0), ([8, 1, 4, 2], 3.0), ([-3.5, 1, -1.5], -1.5), ([4], 4.0)])
def test_median(values, expected):
    original = values.copy()
    result = central.median(values)
    assert result == pytest.approx(expected)
    assert isinstance(result, float)
    assert values == original


def test_median_generator():
    assert central.median(value for value in [8, 1, 4, 2]) == pytest.approx(3.0)


def test_median_empty():
    with pytest.raises(ValueError, match="empty"):
        central.median(iter([]))


@pytest.mark.parametrize("values, expected", [([3, 3, 2, 2, 1], 2), ([3, 1, 2], 1), ([-1.5, 2, -1.5, 2], -1.5), ([4], 4), ([2, 3, 3, 3], 3)])
def test_mode(values, expected):
    assert central.mode(values) == pytest.approx(expected)


def test_mode_generator():
    assert central.mode(value for value in [3, 3, 2, 2, 1]) == 2


def test_mode_empty():
    with pytest.raises(ValueError, match="empty"):
        central.mode(iter([]))


@pytest.mark.parametrize("values", [[3, 1, 3], [-2.5, -2.5, 1, 4], [7]])
def test_matches_statistics_without_mode_ties(values):
    assert central.mean(values) == pytest.approx(statistics.mean(values))
    assert central.median(values) == pytest.approx(statistics.median(values))
    assert central.mode(values) == statistics.mode(values)


def test_mean_empty():
    with pytest.raises(ValueError, match="empty"):
        central.mean(iter([]))
