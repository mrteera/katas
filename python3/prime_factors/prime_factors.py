class PrimeFactors:

    def put(self, num):
        result = []
        while num > 1:
            result.append(2)
            num = num - 1

        return result
