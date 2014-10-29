import 'package:unittest/unittest.dart';
import 'fizzbuzz.dart';

main() {
 var fizzbuzz = new FizzBuzz();

 test('one should return one', () {
    fizzbuzz.clear();
    fizzbuzz.set(1);
    expect(fizzbuzz.get(), '1');
  });

  test('two should return two', () {
    fizzbuzz.clear();
    fizzbuzz.set(2);
    expect(fizzbuzz.get(), '2');
  });

  test('three should return fizz', () {
    fizzbuzz.clear();
    fizzbuzz.set(3);
    expect(fizzbuzz.get(), "fizz");
  });

  test('five should return buzz', () {
    fizzbuzz.clear();
    fizzbuzz.set(5);
    expect(fizzbuzz.get(), "buzz");
  });

  test('fifteen should return fizzbuzz', () {
    fizzbuzz.clear();
    fizzbuzz.set(15);
    expect(fizzbuzz.get(), "fizzbuzz");
  });
}
