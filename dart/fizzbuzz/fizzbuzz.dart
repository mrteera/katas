library fizzbuzz;

class FizzBuzz {
  int num;
  String output = '';

  int get() {
    if (num % 3 == 0) {
      output = output + 'fizz';
    }
    if (num % 5 == 0) {
      output = output + 'buzz';
    } else if (num % 3 != 0) {
      num = num.toString();
      output = num;
    }
    return output;
}

  set(int n) => num = n;

  clear() => output = '';
}
