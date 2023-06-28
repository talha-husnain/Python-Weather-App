import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path

# Path to images folder
IMAGES_PATH = Path("ISEimages")

def find_season(country, season_type, month):
    seasons = {
        "Australia": {
            "Meteorological": {
                12: ("Summer", "summer.png"),
                1: ("Summer", "summer.png"),
                2: ("Summer", "summer.png"),
                3: ("Autumn", "autumn.png"),
                4: ("Autumn", "autumn.png"),
                5: ("Autumn", "autumn.png"),
                6: ("Winter", "winter.png"),
                7: ("Winter", "winter.png"),
                8: ("Winter", "winter.png"),
                9: ("Spring", "spring.png"),
                10: ("Spring", "spring.png"),
                11: ("Spring", "spring.png"),
            },
            "Noongar": {
                12: ("Birak", "birak.png"),
                1: ("Bunuru", "bunuru.png"),
                2: ("Bunuru", "bunuru.png"),
                3: ("Djeran", "djeran.png"),
                4: ("Djeran", "djeran.png"),
                5: ("Makuru", "makuru.png"),
                6: ("Makuru", "makuru.png"),
                7: ("Makuru", "makuru.png"),
                8: ("Djilba", "djilba.png"),
                9: ("Djilba", "djilba.png"),
                10: ("Kambarang", "kambarang.png"),
                11: ("Kambarang", "kambarang.png"),
            },
        },
        "Canada": {
            "Meteorological": {
            12: ("Winter", "winter.png"),
            1: ("Winter", "winter.png"),
            2: ("Winter", "winter.png"),
            3: ("Spring", "spring.png"),
            4: ("Spring", "spring.png"),
            5: ("Spring", "spring.png"),
            6: ("Summer", "summer.png"),
            7: ("Summer", "summer.png"),
            8: ("Summer", "summer.png"),
            9: ("Autumn", "autumn.png"),
            10: ("Autumn", "autumn.png"),
            11: ("Autumn", "autumn.png"),
            }
        },
        # Add more countries and their seasons with images as needed
    }

    # Handle invalid inputs
    if country not in seasons:
        return "Invalid country", ""
    if season_type not in seasons[country]:
        return "Invalid season type", ""
    if month < 1 or month > 12:
        return "Invalid month", ""

    # Determine the season and image
    season, image = seasons[country][season_type].get(month, ("", ""))

    return season, image

def temperature_comparison(city, temperature, time_of_day):
    average_temperatures = {
        "Sydney": {
            "Morning": 20.5,
            "Evening": 18.2
        },
        "London": {
            "Morning": 12.8,
            "Evening": 10.3
        },
        # Add more cities and their average temperatures for morning and evening as needed
    }

    # Handle invalid inputs
    if city not in average_temperatures:
        return "Invalid city"
    if time_of_day not in ["Morning", "Evening"]:
        return "Invalid time of day"

    # Get the average temperature based on the given city and time of day
    average_temperature = average_temperatures[city][time_of_day]

    # Compare the given temperature with the average temperature
    temperature_difference = temperature - average_temperature

    # Determine the comparison result and return the appropriate message
    if temperature_difference > 5:
        return f"Above average temperature (+{temperature_difference:.1f}°C)"
    elif temperature_difference < -5:
        return f"Below average temperature ({temperature_difference:.1f}°C)"
    else:
        return "Within 5 degrees of average temperature"


def display_season(season, image):
    print(f"Season: {season}")
    # Load and display the image
    img = mpimg.imread(IMAGES_PATH / image)
    imgplot = plt.imshow(img)
    plt.show()

def display_comparison_result(result):
    print(f"Comparison Result: {result}")

# Collect user input
country = input("Please enter the country: ")
if country.lower() == 'australia':
    season_type = input("Please enter the type of season (Meteorological or Noongar): ")
else:
    season_type = "Meteorological"  # default to meteorological for other countries
month = int(input("Please enter the month as a number (1-12): "))
city = input("Please enter the city: ")
temperature = float(input("Please enter the temperature: "))
time_of_day = input("Please enter the time of day (Morning or Evening): ")

# Find the season
season, image = find_season(country, season_type, month)

# Display the season
display_season(season, image)

# Compare the temperature
comparison_result = temperature_comparison(city, temperature, time_of_day)

# Display the comparison result
display_comparison_result(comparison_result)
