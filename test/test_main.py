import unittest

import main # my main code

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

        data = main.read_data('./test/data.in')
        self.assertEqual(len(data), 2)

        city1 = data[0].cities
        optimal1 = data[0].optimal

        city2 = data[1].cities
        optimal2 = data[1].optimal
        
        self.assertEqual(len(city1), 4)
        self.assertEqual(optimal1, 14.0)
        self.assertEqual(len(city2), 10)
        self.assertEqual(optimal2, 35.06889373058871)

    def test_evaluate_solution(self):
        data = main.read_data('./test/data.in')
        evaluation = main.evaluate_solution(data[0].cities, [0,1,2,3])
        self.assertEqual(evaluation, data[0].optimal)

    def test_generate_2_random_index(self):
        data = main.read_data('./test/data.in')
        i, j = main.generate_2_random_index(data[0].cities)
        self.assertTrue(i < len(data[0].cities))
        self.assertTrue(j < len(data[0].cities))

    def test_generate_random_probability_r(self):        
        r = main.generate_random_probability_r()
        self.assertTrue(r <= 1)

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

    def test_create_new_solution(self):
        data = main.read_data('./test/data.in')
        cities = data[1].cities
        solution = [0, 1, 7, 9, 5, 4, 8, 6, 2, 3]
        
        i, j = 3, 7
        # inverse_solution = main.inverse_solution(solution, i, j)
        insert_solution = main.insert_solution(solution, i, j)
        # swap_solution = main.swap_solution(solution, i, j)

        """enable line code if want to see the evalation value"""
        # evaluation_inverse = main.evaluate_solution(cities, inverse_solution)
        # evaluation_insert = main.evaluate_solution(cities, insert_solution)
        # evaluation_swap = main.evaluate_solution(cities, swap_solution)

        new_solution = main.create_new_solution(cities, solution, i, j)
        
        # for i=3, j=7, the best solution is insert
        self.assertEqual(new_solution, insert_solution)
    
    def test_calculate_bad_result_acceptance_probability(self):
        probability = main.calculate_bad_result_acceptance_probability(100, 100, 100)
        self.assertEqual(probability, 1)

        probability = main.calculate_bad_result_acceptance_probability(100, -100, -50)
        self.assertGreaterEqual(probability, 0)

    def test_calculate_new_temparature(self):
        old_temarature = 100
        temparature = main.calculate_new_temparature(2, old_temarature, -100, 50)
        self.assertGreater(temparature, old_temarature)

    def test_create_initial_temp(self):
        data = main.read_data('./test/data.in')
        cities = data[1].cities
        temp_list = main.create_initial_temp(cities, 30, initial_acc_probability=0.7)
        self.assertEqual(len(temp_list), 31)


if __name__ == '__main__':
    unittest.main()