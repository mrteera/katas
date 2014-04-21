class romanNumerals:
    def from_num(self, input_num):
        output = ""
        ten_pos = 0 + int(input_num / 10)
        sing_num = 0 + input_num % 10
        if ten_pos % 5 <= 3 and ten_pos != 0:
            output = 'X'
        elif sing_num % 5 == 0:
            output = 'V'
        elif sing_num % 5 == 4:
            output = 'IV'
        elif sing_num % 5 <= 3:
            output = 'I' * input_num
        return output
