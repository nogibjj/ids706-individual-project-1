import unittest
from src.lib import read_dataset, generate_summary_statistics


class TestLib(unittest.TestCase):

    def setUp(self):
        # Setup a test dataframe using a subset of your data
        self.data = read_dataset('tests/test.csv')

    def test_read_dataset(self):
        # Test that read_dataset is working correctly
        data = read_dataset('tests/test.csv')
        self.assertIsNotNone(data)

    def test_generate_summary_statistics(self):
        # Test that generate_summary_statistics is working correctly
        summary = generate_summary_statistics(self.data)
        self.assertIn('mean', summary)
        self.assertIn('median', summary)
        self.assertIn('std_dev', summary)


if __name__ == '__main__':
    unittest.main()
