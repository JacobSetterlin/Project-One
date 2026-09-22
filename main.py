"""
Planet Information
Jacob Setterlin

This program is used to find provide the user with the information of a planet 
they want to know about.

Last Updated: 9/22/2026"""

def line_break():
    """Used to seperate different messages and user input in the console."""
    print("--------------------")

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