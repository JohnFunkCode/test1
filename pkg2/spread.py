import math


def value_range(values):
    """Return the difference between the largest and smallest values."""
    values = list(values)
    return max(values) - min(values)


def variance(values, sample=False) -> float:
    """Return population variance, or sample variance when requested."""
    values = list(values)
    if not values:
        raise ValueError("variance requires non-empty input")
    if sample and len(values) < 2:
        raise ValueError("sample variance requires at least two values")
    mean = sum(values) / len(values)
    divisor = len(values) - 1 if sample else len(values)
    return sum((value - mean) ** 2 for value in values) / divisor


def stdev(values, sample=False) -> float:
    """Return population standard deviation, or sample standard deviation."""
    values = list(values)
    return math.sqrt(variance(values, sample))
