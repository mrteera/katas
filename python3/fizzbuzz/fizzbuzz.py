class FizzBuzz:

    def set_num(self, num):
        self.num = num

    def get(self):
        return "fizz" * (not self.num % 3) + "buzz" * (not self.num % 5) or \
               str(self.num)
