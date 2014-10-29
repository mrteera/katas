import 'package:unittest/unittest.dart';
import 'fizzbuzz.dart';

main() {
 test('one should return one', () {
  var fizzbuzz = new FizzBuzz();
  expect(fizzbuzz.get(), 1);
  });
}
