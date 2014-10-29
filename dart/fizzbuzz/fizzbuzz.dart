library fizzbuzz;

class FizzBuzz {
  int num;
  String output;

  int get() {
    if (num % 3 == 0) {
      return "fizz";
    } else if (num % 5 == 0) {
      return "buzz";
    } else {
      return num;
    }
}

  set(int n) => num = n;
}
