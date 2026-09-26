"""
Planet Information
Jacob Setterlin

This program is used to find provide the user with the information of a planet 
they want to know about.

All information comes from NASA unless stated otherwise.

Last Updated: 9/26/2026"""

def line_break():
    """Used to seperate different messages and user input in the console."""
    print("--------------------")

def print_planet_info(name: str, distance_from_sun: int, atmosphere: str, surface: str):
    """
    This function is used to print information about a planet.
    
    Paramaters:
        distance_from_sun:
            The planets distance from our sun measured in
            astronomical units rounded to the nearest integer.
        
        atmosphere:
            The most common gas in the atmosphere.
        
        surface:
            A few words describing what the surface of the planet is like.
            'surface' should be set to 'none' if the planet is a gas giant.
    """

    print(f"{name}:")
    print(f"Distance from our sun: {distance_from_sun} astronomical units.")
    print(f"The atmosphere of {name} is made of {atmosphere}.")
    if surface == "none":
        print(f"{name} is a gas giant.")
    else:
        print(f"The surface of {name} is {surface}.")

    input("Press enter to continue.")

available_planets = ["Mercury",
                     "Venus",
                     "Earth",
                     "Mars",
                     "Jupiter",
                     "Saturn",
                     "Uranus",
                     "Neptune"]

while True:
    print("Enter the name of the planet you want to learn about, or press q to quit.")
    print("Available Planets:")
    for planet in available_planets:
        print(planet)
    line_break()

    user_input = input().lower()
    line_break()

    if user_input == "mercury":
        print_planet_info("Mercury", 0.4, "sodium", "rocky.")

    elif user_input == "venus":
        print_planet_info("venus", 0.72, "carbon dioxide", "rocky with many mountains.")

    elif user_input == "earth":
        print_planet_info("earth", 1, "oxygen", "earth-like.")

    elif user_input == "mars":
        print_planet_info("mars", 1.5, "carbon dioxide", "believed to contain lots of iron.")

    elif user_input == "jupiter":
        print_planet_info("jupiter", 5.2, "ammonia ice", "none")

    #Information about the atmosphere of saturn comes from the European Space Agency.
    elif user_input == "saturn":
        print_planet_info("saturn", 9.5, "hydrogen", "none")

    elif user_input == "uranus":
        print_planet_info("uranus", 19, "hydrogen", "liquidy.")

    elif user_input == "neptune":
        print_planet_info("neptune", 30, "hydrogen", "none")

    elif user_input == "q":
        quit()

    line_break()