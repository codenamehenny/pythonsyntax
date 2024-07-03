#Write a program that prompts the user to input the color of a traffic light 
# (red, yellow, green) and outputs the action a driver should take.

traffic_light_color = input("What's the traffic light color?")
if traffic_light_color == "green":
    print("Go")
elif traffic_light_color == "yellow" or "red":
    print("Come to a stop")