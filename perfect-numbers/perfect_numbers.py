def classify(number):
    if number <= 0:
        raise ValueError("Please provide number higher than zero")
    factors = [i for i in range(1, number) if number % i == 0]
    if sum(factors) == number:
        return "perfect"
    if sum(factors) > number:
        return "abundant"
    if sum(factors) < number:
        return "deficient"

