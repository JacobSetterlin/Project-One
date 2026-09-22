"""
Planet Information
Jacob Setterlin

This program is used to find provide the user with the information of a planet 
they want to know about.

Last Updated: 9/22/2026"""

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
    print(f"Distance from our sun: {distance_from_sun}")
    print(f"The atmosphere of {name} is made of {atmosphere}.")
    print(f"The surface of {name} is {surface}")

available_planets = ["Mercury",
                     "Venus",
                     "Earth",
                     "Mars",
                     "Jupiter",
                     "Saturn",
                     "Uranus",
                     "Neptune"]

print("What planet would you like to learn about?")
print("Available Planets:")
for planet in available_planets:
    print(planet)
line_break()