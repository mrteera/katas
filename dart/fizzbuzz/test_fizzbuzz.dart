import 'package:unittest/unittest.dart';
import 'fizzbuzz.dart';

main() {
 test('one should return one', () {
    var fizzbuzz = new FizzBuzz();
    fizzbuzz.set(1);
    expect(fizzbuzz.get(), 1);
  });

  test('two should return two', () {
    var fizzbuzz = new FizzBuzz();
    fizzbuzz.set(2);
    expect(fizzbuzz.get(), 2);
  });
}
