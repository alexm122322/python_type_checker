import unittest

# from test.example import method_test
from type_checker.typing_exception import TypingException
from type_checker.type_checker_decorator import check_type


@check_type
def method_test(name: str, age: int, sex) -> bool:
    return True


class TestTypeChecker(unittest.TestCase):

    def test_is_type_match(self):
        self.assertEqual(method_test('vana', 14, 21), True)
        self.assertEqual(method_test('vana', 14, 'man'), True)
        self.assertEqual(method_test('vana', 14, sex=21), True)
        self.assertEqual(method_test('vana', 14, sex=[]), True)
        self.assertEqual(method_test('vana', age=14, sex=21), True)
        self.assertEqual(method_test(name='vana', age=14, sex={}), True)
        self.assertEqual(method_test(name='vana', age=14, sex='woman'), True)
        self.assertEqual(method_test(name='vana', age=14, sex=(1, 'df')), True)
        self.assertEqual(method_test(name=None, age=14, sex=(1, 'df')), True)

    def test_is_type_mismatch(self):
        try:
            method_test('vana', '21', 21)
        except Exception as ex:
            self.assertIsInstance(ex, TypingException)

        try:
            method_test([], 21, sex='men')
        except Exception as ex:
            self.assertIsInstance(ex, TypingException)

        try:
            method_test({}, 21, sex='men')
        except Exception as ex:
            self.assertIsInstance(ex, TypingException)

        try:
            method_test('vana', age='21', sex='men')
        except Exception as ex:
            self.assertIsInstance(ex, TypingException)

        try:
            method_test(name=21, age='21', sex='men')
        except Exception as ex:
            self.assertIsInstance(ex, TypingException)

        try:
            method_test(name='Nick', age=[], sex='men')
        except Exception as ex:
            self.assertIsInstance(ex, TypingException)

    def test_typing_exception_message(self):
        try:
            method_test(name='Nick', age=[], sex='men')
        except TypingException as ex:
            self.assertEqual(
                ex.message, "Arg 'age' expects int type, but actually is list type!")


if __name__ == '__main__':
    unittest.main()
