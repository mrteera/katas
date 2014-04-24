class PrimeFactor:

    def put(self, num):
        return self.prime_factors(num)

    def prime_factors(self, num):
        result = []
        divisor = 2
        while num > 1:
            while num % divisor == 0:
                result.append(divisor)
                num //= divisor
            divisor += 1
        return result

