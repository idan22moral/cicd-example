import example
import unittest


class MathTest(unittest.TestCase):
    def test_mul(self):
        [self.assertEqual(example.mul(a, b), a * b)
         for a in range(10 ** 3) for b in range(10 ** 3)]

    def test_div(self):
        with self.assertRaises(ZeroDivisionError):
            [self.assertEqual(example.div(a, b), a / b)
             for a in range(10 ** 3) for b in range(10 ** 3)]

    def test_sum(self):
        [self.assertEqual(example.sum(a, b), a + b)
         for a in range(10 ** 3) for b in range(10 ** 3)]

    def test_sub(self):
        [self.assertEqual(example.sub(a, b), a - b)
         for a in range(10 ** 3) for b in range(10 ** 3)]

    def test_avg(self):
        [self.assertEqual(example.avg(a, b), (a + b) / 3)
         for a in range(10 ** 3) for b in range(10 ** 3)]


if __name__ == "__main__":
    unittest.main()
