import unittest
import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        # Исправлена проверка ожидаемого значения
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)  # Вернёт элемент со значением 2
        self.assertEqual(arrs.get([], 0, "test"), "test")  # Вернёт значение по умолчанию

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
