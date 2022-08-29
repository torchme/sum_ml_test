"""
Kartushov Danil

Third case Unit-test
"""
import time
import unittest
from user_input.solution import normalized_discounted_cumulative_gain
from main import normalized_discounted_cumulative_gain as ndcg

class TestNormDicsCumGain(unittest.TestCase):
    """
    Unit-Test Normalized Discounted Cumulative Gain
    """
    def test_nans(self):
        """
        Test Normalized Discounted Cumulative Gain with list of None
        """
        list_nuns = [None, None, None, None]
        self.assertNotEqual(normalized_discounted_cumulative_gain(list_nuns), normalized_discounted_cumulative_gain(list_nuns))

    def test_outliers(self):
        """
        Test Normalized Discounted Cumulative Gain with outlier in ranks
        """
        list_outliers = [3, 2, 1, 0, 999]
        self.assertEqual(normalized_discounted_cumulative_gain(list_outliers), ndcg(list_outliers))

    def test_hyperparams_first(self):
        """
        Test Normalized Discounted Cumulative Gain with K more then size list of ranks
        """
        list_ranks = [3, 2, 1, 0, 0]
        with self.assertRaises(ValueError):
            normalized_discounted_cumulative_gain(list_ranks, k=6)
    
    def test_hyperparams_second(self):
        """
        Test Normalized Discounted Cumulative Gain with another methods
        """
        list_ranks = [3, 2, 1, 0, 0]
        with self.assertRaises(ValueError):
            normalized_discounted_cumulative_gain(list_ranks, method=3)

    def test_zero(self):
        """
        Test cumulative gain with zero
        """
        with self.assertRaises(TypeError):
            normalized_discounted_cumulative_gain(0)

    def test_correct_answer_first(self):
        """
        Test cumulative with correct answers
        """
        list_ranks = [3,2,3,0,1,2]
        self.assertEqual(normalized_discounted_cumulative_gain(list_ranks), ndcg(list_ranks))

    def test_correct_answer_second(self):
        """
        Test cumulative with correct answers
        """
        list_ranks = [0,0,0,0,0,0,0,1]
        self.assertEqual(normalized_discounted_cumulative_gain(list_ranks), ndcg(list_ranks))

    def test_correct_answer_third(self):
        """
        Test cumulative with correct answers
        """
        list_ranks = [3,2,3,0,1,2]
        self.assertEqual(normalized_discounted_cumulative_gain(list_ranks, k=3), ndcg(list_ranks, k=3))

    def test_correct_answer_four(self):
        """
        Test cumulative with correct answers
        """
        list_ranks = [3,2,3,0,1,2]
        self.assertEqual(normalized_discounted_cumulative_gain(list_ranks, method=1), ndcg(list_ranks, method=1))

    def test_speed(self):
        """
        Test code speed
        """
        list_ranks = [3,2,3,0,1,2]
        start_time_student_code = time.monotonic()
        normalized_discounted_cumulative_gain(list_ranks, k=3)
        end_time_student_code  = time.monotonic() - start_time_student_code 

        start_time_our_sol = time.monotonic()
        ndcg(list_ranks, k=3)
        end_time_our_sol  = time.monotonic() - start_time_our_sol
        self.assertGreaterEqual(end_time_student_code, end_time_our_sol*0.8)

def get_test_third_case():
    """
    Unit-test third case
    """
    unittest.main()

if __name__ == '__main__':
    get_test_third_case()