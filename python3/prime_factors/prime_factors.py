class PrimeFactors:

    def put(self, num):
        result = []
        divisor = 2

        while num > 1:
            while num % divisor == 0:
                result.append(divisor)
                num //= divisor
            divisor += 1

        return result
