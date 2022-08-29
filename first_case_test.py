"""
Kartushov Danil

First case Unit-test
"""
import time
import unittest
from user_input.solution import cumulative_gain
from main import cumulative_gain as cg

class TestCumGain(unittest.TestCase):
    """
    Unit-Test Cumulative Gain
    """
    def test_nans(self):
        """
        Test cumulative gain with list of None
        """
        list_nuns = [None, None, None, None]
        self.assertNotEqual(cumulative_gain(list_nuns), cumulative_gain(list_nuns))

    def test_outliers(self):
        """
        Test cumulative gain with outlier in ranks
        """
        list_outliers = [3, 2, 1, 0, 999]
        self.assertEqual(cumulative_gain(list_outliers), cg(list_outliers))

    def test_hyperparams(self):
        """
        Test cumulative gain with K more then size list of ranks
        """
        list_ranks = [3, 2, 1, 0, 0]
        with self.assertRaises(ValueError):
            cumulative_gain(list_ranks, k=6)

    def test_zero(self):
        """
        Test cumulative gain with zero
        """
        with self.assertRaises(TypeError):
            cumulative_gain(0)

    def test_correct_answer_first(self):
        """
        Test cumulative gain with correct answers
        """
        list_ranks = [3,2,3,0,1,2]
        self.assertEqual(cumulative_gain(list_ranks), 11)

    def test_correct_answer_second(self):
        """
        Test cumulative gain with zeros
        """
        list_ranks = [0,0,0,0,0,0,0,0]
        self.assertEqual(cumulative_gain(list_ranks), 0)

    def test_correct_answer_third(self):
        """
        Test cumulative with correct answers and hyperparametr
        """
        list_ranks = [3,2,3,0,1,2]
        self.assertEqual(cumulative_gain(list_ranks, k=3), 8)

    def test_speed(self):
        """
        Test code speed
        """
        list_ranks = [3,2,3,0,1,2]
        start_time_student_code = time.monotonic()
        cumulative_gain(list_ranks, k=3)
        end_time_student_code  = time.monotonic() - start_time_student_code 

        start_time_our_sol = time.monotonic()
        cg(list_ranks, k=3)
        end_time_our_sol  = time.monotonic() - start_time_our_sol
        self.assertGreaterEqual(end_time_student_code, end_time_our_sol*0.8)

def get_test_first_case():
    """
    Unit-test first case
    """
    unittest.main()

if __name__ == '__main__':
    get_test_first_case()