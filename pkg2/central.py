from collections import Counter


def mean(values) -> float:
    """Return the arithmetic mean of a nonempty iterable."""
    values = list(values)
    if not values:
        raise ValueError("mean of empty input")
    return float(sum(values) / len(values))


def median(values) -> float:
    """Return the middle value, averaging the middle pair for even counts."""
    values = list(values)
    if not values:
        raise ValueError("median of empty input")
    values.sort()
    middle = len(values) // 2
    if len(values) % 2:
        return float(values[middle])
    return float((values[middle - 1] + values[middle]) / 2)


def mode(values):
    """Return the most common value, choosing the smallest on a tie."""
    values = list(values)
    if not values:
        raise ValueError("mode of empty input")
    counts = Counter(values)
    highest = max(counts.values())
    return min(value for value, count in counts.items() if count == highest)
