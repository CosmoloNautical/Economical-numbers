def is_economical(number):

    """
    A number is Economical if the quantity of digits of its prime factorization (including exponents greater than 1) is equal to or lower than the digit quantity of the number itself.

    a number is:
    "Equidigital" if the quantity of digits of the prime factorization (including exponents greater than 1) is equal to the quantity of digits of n;
    "Frugal" if the quantity of digits of the prime factorization (including exponents greater than 1) is lower than the quantity of digits of n;
    "Wasteful" if none of the two above conditions is true.
    """

    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    def collapse_factors(factors):
        for factor in factors:
            occurrence = factors.count(factor)
            if occurrence > 1:
                try:
                    while True:
                        factors.remove(factor)
                except ValueError:
                    factors.append(str(factor) + str(occurrence))
        collapsed_factors = ""
        for factor in factors:
            collapsed_factors += str(factor)
        return collapsed_factors

    number_digits = len(str(number))
    factor_digits = len(collapse_factors(prime_factors(number)))
    if factor_digits == number_digits:
        return "Equidigital"
    elif factor_digits < number_digits:
        return "Frugal"
    else:
        return "Wasteful"