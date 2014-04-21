class PrimeFactor:

    def put(self, num):
        return self.prime_factors(num)

    def prime_factors(self, num):
        result = []
        while num > 3 and num % 2 == 0:
            num = num // 2
            result.append(num)
        if num == 1:
            return result
        else:
            result = [num]
        return result

