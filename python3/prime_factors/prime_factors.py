class PrimeFactors:

    def put(self, num):
        result = []
        divisor = 2

        while num > 1:
            result.append(divisor)
            num //= divisor
        return result
