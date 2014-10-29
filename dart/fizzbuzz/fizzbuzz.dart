library fizzbuzz;

class FizzBuzz {
  int num;

  int get() {
    if (num < 3) {
      return num;
    }
    return "fizz";
  }

  set(int n) => num = n;
}
