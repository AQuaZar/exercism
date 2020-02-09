def slices(series, length):
    if len(series) < length or length <= 0:
        raise ValueError("Wrong length value")
    result = [series[i : i + length] for i in range(len(series) - length + 1)]
    return result
