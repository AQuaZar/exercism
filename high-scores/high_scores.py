def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    result = []
    if len(scores) >= 3:
        size = 3
    else:
        size = len(scores)
    for _ in range(size):
        result.append(max(scores))
        scores.remove(max(scores))
    return result
