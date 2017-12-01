from unittest import TestCase

from lesson_2.tasks import functions as f


class FunctionsTest(TestCase):
    def test_get_min(self):
        result = f.get_min(1, 34)
        self.assertEqual(result, 1)

    def test_get_min_without_arguments(self):
        self.assertRaises(TypeError, f.get_min_without_arguments)

    def test_get_min_with_one_argument(self):
        result = f.get_min_with_one_argument(123)
        self.assertEqual(result, 123)

    def test_get_min_with_one_or_more_arguments(self):
        first = 124
        array = [1123, 1421, 12]
        result = f.get_min_with_one_or_more_arguments(first, *array)
        self.assertEqual(12, result)

    def test_get_min_bounded(self):
        kwargs = {
            'low': 0,
            'high': 127
        }
        result = f.get_min_bounded([-54, 45, 23], **kwargs)
        self.assertEqual(0, result)

    def test_make_min(self):
        bounded_min = f.make_min(low=0, high=255)
        self.assertEqual(True, callable(bounded_min))

        if callable(bounded_min):
            result = bounded_min(-5, 12, 13)
            self.assertEqual(0, result)
