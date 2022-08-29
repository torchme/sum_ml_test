"""
Kartushov Danil

Four case Unit-test
"""
import time
import unittest
from user_input.solution import average_ndcg_across_users
from main import average_ndcg_across_users as andcgau

class TestANDCG(unittest.TestCase):
    """
    Unit-Test Avarage Discounted Cumulative Gain
    """
    def test_nans(self):
        """
        Test Avarage Discounted Cumulative Gain with list of None
        """
        list_nuns = [[None, None, None, None]]
        self.assertNotEqual(average_ndcg_across_users(list_nuns), average_ndcg_across_users(list_nuns))

    def test_outliers(self):
        """
        Test Avarage Discounted Cumulative Gain with outlier in ranks
        """
        list_outliers = [[3, 2, 1, 0, 999], [3, 999, 1, 0, 0], [3, 2, 1, 0, -2], [0, 1, 0, 1, 2, 3, 3, 1, 0], [3, 2, 1, 1, 2, 0, 1, 1, 1]]
        self.assertEqual(average_ndcg_across_users(list_outliers), andcgau(list_outliers))

    def test_zero(self):
        """
        Test Avarage Discounted Cumulative Gain with zero
        """
        with self.assertRaises(TypeError):
            average_ndcg_across_users(0)

    def test_correct_answer_first(self):
        """
        Test Avarage Discounted Cumulative Gain with correct answers
        """
        list_ranks = [[3, 3, 2, 2, 1, 1, 0, 0, 0], [3, 2, 1, 1, 2, 0, 1, 1, 1], [0, 1, 0, 1, 2, 3, 3, 1, 0]]
        self.assertEqual(average_ndcg_across_users(list_ranks), andcgau(list_ranks))

    def test_correct_answer_second(self):
        """
        Test Avarage Discounted Cumulative Gain with correct answers
        """
        list_ranks = [[0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0], [0,0,0,0,0,0,1,0]]
        self.assertEqual(average_ndcg_across_users(list_ranks), andcgau(list_ranks))

    def test_correct_answer_third(self):
        """
        Test Avarage Discounted Cumulative Gain with correct answers
        """
        #hyperparams k
        list_ranks = [[3, 3, 2, 2, 1, 1, 0, 0, 0], [3, 2, 1, 1, 2, 0, 1, 1, 1], [0, 1, 0, 1, 2, 3, 3, 1, 0]]
        self.assertEqual(average_ndcg_across_users(list_ranks, k=4), andcgau(list_ranks, k=4))

    def test_correct_answer_four(self):
        """
        Test Avarage Discounted Cumulative Gain with correct answers
        """
        #hyperparams method
        list_ranks = [[3, 3, 2, 2, 1, 1, 0, 0, 0], [3, 2, 1, 1, 2, 0, 1, 1, 1], [0, 1, 0, 1, 2, 3, 3, 1, 0]]
        self.assertEqual(average_ndcg_across_users(list_ranks, method=1), andcgau(list_ranks, method=1))

    def test_speed(self):
        """
        Test code speed
        """
        list_ranks = [[3, 3, 2, 2, 1, 1, 0, 0, 0], [3, 2, 1, 1, 2, 0, 1, 1, 1], [0, 1, 0, 1, 2, 3, 3, 1, 0]]
        start_time_student_code = time.monotonic()
        average_ndcg_across_users(list_ranks, k=3)
        end_time_student_code  = time.monotonic() - start_time_student_code 

        start_time_our_sol = time.monotonic()
        andcgau(list_ranks, k=3)
        end_time_our_sol  = time.monotonic() - start_time_our_sol
        self.assertGreaterEqual(end_time_student_code, end_time_our_sol*0.8)

def get_test_four_case():
    """
    Unit-test four case
    """
    unittest.main()

if __name__ == '__main__':
    get_test_four_case()