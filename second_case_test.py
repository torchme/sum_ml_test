"""
Kartushov Danil

Second case Unit-test
"""
import time
import unittest
from user_input.solution import discounted_cumulative_gain
from user_input.solution import ideal_discounted_cumulative_gain
from main import discounted_cumulative_gain as dcg
from main import ideal_discounted_cumulative_gain as idcg


class TestDicsCumGain(unittest.TestCase):
    """
    Unit-Test Discounted Cumulative Gain
    """
    def test_nans(self):
        """
        Test Discounted Cumulative Gain with list of None
        """
        list_nuns = [None, None, None, None]
        self.assertNotEqual(discounted_cumulative_gain(list_nuns), discounted_cumulative_gain(list_nuns))

    def test_outliers(self):
        """
        Test Discounted Cumulative Gain with outlier in ranks
        """
        list_outliers = [3, 2, 1, 0, 999]
        self.assertEqual(discounted_cumulative_gain(list_outliers), dcg(list_outliers))

    def test_hyperparams_first(self):
        """
        Test Discounted Cumulative Gain with K more then size list of ranks
        """
        list_ranks = [3, 2, 1, 0, 0]
        with self.assertRaises(ValueError):
            discounted_cumulative_gain(list_ranks, k=6)

    def test_hyperparams_second(self):
        """
        Test Discounted Cumulative Gain with another methods
        """
        list_ranks = [3, 2, 1, 0, 0]
        with self.assertRaises(ValueError):
            discounted_cumulative_gain(list_ranks, method=3)

    def test_zero(self):
        """
        Test Discounted Cumulative Gain with zero
        """
        with self.assertRaises(TypeError):
            discounted_cumulative_gain(0)

    def test_correct_answer_first(self):
        """
        Test Discounted Cumulative Gain with correct answers
        """
        list_ranks = [3,2,3,0,1,2]
        self.assertEqual(discounted_cumulative_gain(list_ranks), dcg(list_ranks))

    def test_correct_answer_second(self):
        """
        Test Discounted Cumulative Gain with correct answers
        """
        list_ranks = [0,0,0,0,0,0,0,0]
        self.assertEqual(discounted_cumulative_gain(list_ranks), dcg(list_ranks))

    def test_correct_answer_third(self):
        """
        Test Discounted Cumulative Gain with correct answers
        """
        list_ranks = [3,2,3,0,1,2]
        self.assertEqual(discounted_cumulative_gain(list_ranks, k=3), dcg(list_ranks, k=3))

    def test_correct_answer_four(self):
        """
        Test Discounted Cumulative Gain with correct answers
        """
        list_ranks = [3,2,3,0,1,2]
        self.assertEqual(discounted_cumulative_gain(list_ranks, method=1), dcg(list_ranks, method=1))

    def test_speed(self):
        """
        Test code speed
        """
        list_ranks = [3,2,3,0,1,2]
        start_time_student_code = time.monotonic()
        discounted_cumulative_gain(list_ranks, k=3)
        end_time_student_code  = time.monotonic() - start_time_student_code 

        start_time_our_sol = time.monotonic()
        dcg(list_ranks, k=3)
        end_time_our_sol  = time.monotonic() - start_time_our_sol
        self.assertGreaterEqual(end_time_student_code, end_time_our_sol)

class TestIdealDicsCumGain(unittest.TestCase):
    """
    Unit-Test Ideal Discounted Cumulative Gain
    """
    def test_nans(self):
        """
        Test Ideal Discounted Cumulative Gain with list of None
        """
        list_nuns = [None, None, None, None]
        self.assertNotEqual(ideal_discounted_cumulative_gain(list_nuns), ideal_discounted_cumulative_gain(list_nuns))

    def test_outliers(self):
        """
        Test Ideal Discounted Cumulative Gain with outlier in ranks
        """
        list_outliers = [3, 2, 1, 0, 999]
        self.assertEqual(ideal_discounted_cumulative_gain(list_outliers), idcg(list_outliers))

    def test_hyperparams_first(self):
        """
        Test Ideal Discounted Cumulative Gain with K more then size list of ranks
        """
        list_ranks = [3, 2, 1, 0, 0]
        with self.assertRaises(ValueError):
            ideal_discounted_cumulative_gain(list_ranks, k=6)

    def test_hyperparams_second(self):
        """
        Test Ideal Discounted Cumulative Gain with another methods
        """
        list_ranks = [3, 2, 1, 0, 0]
        with self.assertRaises(ValueError):
            ideal_discounted_cumulative_gain(list_ranks, method=3)

    def test_zero(self):
        """
        Test Ideal Discounted Cumulative Gain with zero
        """
        with self.assertRaises(TypeError):
            ideal_discounted_cumulative_gain(0)

    def test_correct_answer_first(self):
        """
        Test Ideal Discounted Cumulative Gain correct answers
        """
        list_ranks = [3,2,3,0,1,2]
        self.assertEqual(ideal_discounted_cumulative_gain(list_ranks), idcg(list_ranks))

    def test_correct_answer_second(self):
        """
        Test Ideal Discounted Cumulative Gain with correct answers
        """
        list_ranks = [0,0,0,0,0,0,0,0]
        self.assertEqual(ideal_discounted_cumulative_gain(list_ranks), idcg(list_ranks))

    def test_correct_answer_third(self):
        """
        Test Ideal Discounted Cumulative Gain with correct answers
        """
        list_ranks = [3,2,3,0,1,2]
        self.assertEqual(ideal_discounted_cumulative_gain(list_ranks, k=3), idcg(list_ranks, k=3))

    def test_correct_answer_four(self):
        """
        Test Ideal Discounted Cumulative Gain with correct answers
        """
        list_ranks = [3,2,3,0,1,2]
        self.assertEqual(ideal_discounted_cumulative_gain(list_ranks, method=1), idcg(list_ranks, method=1))

    def test_speed(self):
        """
        Test code speed
        """
        list_ranks = [3,2,3,0,1,2]
        start_time_student_code = time.monotonic()
        ideal_discounted_cumulative_gain(list_ranks, k=3)
        end_time_student_code  = time.monotonic() - start_time_student_code 

        start_time_our_sol = time.monotonic()
        idcg(list_ranks, k=3)
        end_time_our_sol  = time.monotonic() - start_time_our_sol
        self.assertGreaterEqual(end_time_student_code, end_time_our_sol*0.8)

def get_test_second_case():
    """
    Unit-test second case
    """
    unittest.main()

if __name__ == '__main__':
    get_test_second_case()