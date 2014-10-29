import 'package:unittest/unittest.dart';
import 'fizzbuzz.dart';

main() {
 var fizzbuzz = new FizzBuzz();

 test('one should return one', () {
    fizzbuzz.set(1);
    expect(fizzbuzz.get(), 1);
  });

  test('two should return two', () {
    fizzbuzz.set(2);
    expect(fizzbuzz.get(), 2);
  });
}
