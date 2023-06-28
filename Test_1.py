import unittest

class TestWeatherApp(unittest.TestCase):
    # Test find_season function
    def test_find_season(self):
        # Test Case 1: Valid country and month
        self.assertEqual(find_season("Australia", 5), ("Autumn", "🍂"))
        
        # Test Case 2: Invalid country
        self.assertEqual(find_season("NotACountry", 5), ("Invalid country", ""))
        
        # Test Case 3: Invalid month
        self.assertEqual(find_season("Australia", 13), ("Invalid month", ""))

    # Test temperature_comparison function
    def test_temperature_comparison(self):
        # Test Case 1: Valid city, temperature, and time of day
        self.assertEqual(temperature_comparison("Sydney", 22.0, "Morning"), "Above average temperature (+1.5°C)")

        # Test Case 2: Invalid city
        self.assertEqual(temperature_comparison("NotACity", 22.0, "Morning"), "Invalid city")

        # Test Case 3: Invalid time of day
        self.assertEqual(temperature_comparison("Sydney", 22.0, "NotATimeOfDay"), "Invalid time of day")


# Run the tests
if __name__ == '__main__':
    unittest.main()
