import unittest

import main # my main conde

class TestMain(unittest.TestCase):

    def test_evaluate_distance(self):
        a = main.City('a', 0, 0)
        b = main.City('b', 3, 0)
        c = main.City('c', 3, 4)
        d = main.City('d', 0, 4)
        self.assertEqual(main.evaluate_distance(a, a), 0)
        self.assertEqual(main.evaluate_distance(a, b), 3)
        self.assertEqual(main.evaluate_distance(a, c), 5)
        self.assertEqual(main.evaluate_distance(a, d), 4)

    def test_read_data(self):
        data = main.read_data('./data.out')
        self.assertFalse(data)

        data = main.read_data('./data.in')
        self.assertEqual(len(data), 2)

        city1, optimal1 = data[0]
        city2, optimal2 = data[1]
        
        self.assertEqual(len(city1), 4)
        self.assertEqual(optimal1, 14)
        self.assertEqual(len(city2), 10)
        self.assertEqual(optimal2, 100)

if __name__ == '__main__':
    unittest.main()