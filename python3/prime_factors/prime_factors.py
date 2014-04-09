class PrimeFactors:

    def __init__(self):
        number = 0

    def set_number(self, number):
        self.number = number

    def factor(self, number, list_number):
        if not number % 2:
            number /= 2
            list_number.append(2)
        elif not number %3:
            number /= 3
            list_number.append(3)
        else:
            return self.factor(number, list_number)

    def prime(self):
        if self.number % 2 != 0 and self.number % 3 != 0:
            results = [self.number]
        else:
            results = []
        if self.number == 1:
            return []
        list_number = []
        results = self.factor(self.number, list_number)

#        while self.number % 2 == 0 :
#            results.append(2)
#            self.number /= 2
#        while self.number % 3 == 0:
#            results.append(3)
#            self.number /= 3
        return results

