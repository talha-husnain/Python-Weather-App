import unittest

class TestWeatherApp(unittest.TestCase):

    # Testing the find_season function
    def test_find_season(self):
        # Testing with valid inputs
        self.assertEqual(find_season("Australia", 1), ("Summer", "summer.png"))
        self.assertEqual(find_season("Canada", 5), ("Spring", "spring.png"))

        # Testing with invalid country
        self.assertEqual(find_season("InvalidCountry", 1), ("Invalid country", ""))

        # Testing with invalid month
        self.assertEqual(find_season("Australia", 13), ("Invalid month", ""))

    # Testing the temperature_comparison function
    def test_temperature_comparison(self):
        # Testing with valid inputs
        self.assertEqual(temperature_comparison("Sydney", 25.0, "Morning"), "Above average temperature (+4.5°C)")
        self.assertEqual(temperature_comparison("London", 10.0, "Evening"), "Within 5 degrees of average temperature")

        # Testing with invalid city
        self.assertEqual(temperature_comparison("InvalidCity", 25.0, "Morning"), "Invalid city")

        # Testing with invalid time of day
        self.assertEqual(temperature_comparison("Sydney", 25.0, "InvalidTime"), "Invalid time of day")

if __name__ == "__main__":
    unittest.main()
