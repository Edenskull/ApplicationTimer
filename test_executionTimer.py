import unittest
import executionTimer


class TestExecutionTimer(unittest.TestCase):
    def test_value(self):
        sample = executionTimer.ExecutionTimer()
        sample.start_timer()
        sample.end = sample.start + 15905
        self.assertEqual(sample.elapsed_time(), "4 Heures  25 Minutes  5 Secondes")

    def test_missing_value(self):
        sample = executionTimer.ExecutionTimer()
        self.assertRaises(TypeError, sample.elapsed_time)