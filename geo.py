
import random

# dictionary with countries and their capitals
countries_cities = {
    "Slovenia": "Ljubljana",
    "Austria": "Vienna",
    "Croatia": "Zagreb",
    "Italy": "Rome",
    "Hungary": "Budapest",
    "Belgium": "Brussels",
    "Bulgaria": "Sofia",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Ireland": "Dublin",
    "Latvia": "Riga",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg City",
    "Malta": "Valletta",
    "Netherlands": "Amsterdam",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Slovakia": "Bratislava",
    "Spain": "Madrid",
    "Sweden": "Stockholm"
}

# game logic
def start_quiz():
    country = random.choice(list(countries_cities.keys()))
    capital = countries_cities[country]

    print(f"What is the capital city of {country}?")
    answer = input("Answer: ")

    if answer.lower() == capital.lower():
        print("Correct answer!")
    else:
        print(f"Wrong answer, capital city of {country} is {capital}.")

    user_input = input("Do you want to guess again? (Y/N) ")

    if user_input.upper() == "Y":
        start_quiz()
    else:
        print("Thank you for playing!")

# game call
start_quiz()


