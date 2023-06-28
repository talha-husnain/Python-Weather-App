import unittest
from unittest.mock import patch
from io import StringIO

class TestWeatherApp(unittest.TestCase):
    # Other tests...

    # Test display_season function
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_season(self, mock_stdout):
        display_season("Autumn", "🍂")
        expected_output = "Season: Autumn\nSymbol: 🍂\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Test display_comparison_result function
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_comparison_result(self, mock_stdout):
        display_comparison_result("Above average temperature (+1.5°C)")
        expected_output = "Comparison Result: Above average temperature (+1.5°C)\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


# Run the tests
if __name__ == '__main__':
    unittest.main()
