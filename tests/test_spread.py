import statistics

import pytest

from pkg2.spread import stdev, value_range, variance


def test_value_range_of_integers():
    assert value_range([2, 8, 4]) == 6


def test_value_range_rejects_empty_input():
    with pytest.raises(ValueError, match="empty"):
        value_range([])


@pytest.mark.parametrize("sample, expected", [(False, 1.25), (True, 5 / 3)])
def test_variance_population_and_sample(sample, expected):
    assert variance([1, 2, 3, 4], sample=sample) == pytest.approx(expected)


@pytest.mark.parametrize("values, sample, message", [([], False, "empty"), ([], True, "empty"), ([5], True, "two")])
def test_variance_rejects_insufficient_values(values, sample, message):
    with pytest.raises(ValueError, match=message):
        variance(values, sample=sample)


@pytest.mark.parametrize("sample, expected", [(False, 1.118033988749895), (True, 1.2909944487358056)])
def test_stdev_population_and_sample(sample, expected):
    assert stdev([1, 2, 3, 4], sample=sample) == pytest.approx(expected)


@pytest.mark.parametrize(
    "values, expected",
    [([1.5, 4.25, 2.0], 2.75), ([-8, -2, -5], 6), ([-3, 4], 7), ([5], 0)],
)
def test_value_range_other_inputs(values, expected):
    assert value_range(values) == pytest.approx(expected)


@pytest.mark.parametrize("function", [value_range, variance, stdev])
def test_functions_reject_empty_generators(function):
    with pytest.raises(ValueError, match="empty"):
        function(iter([]))


@pytest.mark.parametrize("function", [variance, stdev])
def test_single_value_population_is_zero_float(function):
    result = function([5])
    assert result == 0.0
    assert isinstance(result, float)


@pytest.mark.parametrize("function", [variance, stdev])
@pytest.mark.parametrize("values, message", [([], "empty"), ([5], "two")])
def test_sample_rejects_insufficient_values(function, values, message):
    with pytest.raises(ValueError, match=message):
        function(iter(values), sample=True)


@pytest.mark.parametrize(
    "function, kwargs, expected",
    [(value_range, {}, 3), (variance, {}, 1.25),
     (variance, {"sample": True}, 5 / 3),
     (stdev, {}, 1.118033988749895),
     (stdev, {"sample": True}, 1.2909944487358056)],
)
def test_functions_accept_generators(function, kwargs, expected):
    assert function((x for x in [1, 2, 3, 4]), **kwargs) == pytest.approx(expected)


@pytest.mark.parametrize("values", [[1, 2, 3, 4], [1.5, 2.25, 4.75], [-8, -2, -5], [3, 3, 3]])
@pytest.mark.parametrize(
    "function, reference, sample",
    [(variance, statistics.pvariance, False), (variance, statistics.variance, True),
     (stdev, statistics.pstdev, False), (stdev, statistics.stdev, True)],
)
def test_spread_matches_statistics(values, function, reference, sample):
    assert function(values, sample=sample) == pytest.approx(reference(values))
