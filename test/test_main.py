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

        city1 = data[0].cities
        optimal1 = data[0].optimal

        city2 = data[1].cities
        optimal2 = data[1].optimal
        
        self.assertEqual(len(city1), 4)
        self.assertEqual(optimal1, 14)
        self.assertEqual(len(city2), 10)
        self.assertEqual(optimal2, 35.06889373058871)

    def test_evaluate_solution(self):
        data = main.read_data('./data.in')
        evaluation = main.evaluate_solution(data[0].cities, [0,1,2,3])
        self.assertEqual(evaluation, data[0].optimal)

    def test_generate_2_sorted_random(self):
        data = main.read_data('./data.in')
        i, j = main.generate_2_sorted_random(data[0].cities)
        self.assertTrue(i < j)

    def test_inverse_solution(self):
        data = [7,6,5,4,3,2,1]
        i, j = 2, 5
        new_data = main.inverse_solution(data, i, j)
        self.assertEqual(new_data, [7,6,3,4,5,2,1])
    
    def test_insert_solution(self):
        data = [7,6,5,4,3,2,1]
        i, j = 2, 5
        new_data = main.insert_solution(data, i, j)
        self.assertEqual(new_data, [7,6,4,3,5,2,1])

    def test_swap_solution(self):
        data = [7,6,5,4,3,2,1]
        i, j = 2, 5
        new_data = main.swap_solution(data, i, j)
        self.assertEqual(new_data, [7,6,2,4,3,5,1])

if __name__ == '__main__':
    unittest.main()