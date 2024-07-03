#Task 1: Code Correction Below is a piece of Python code with incorrect indentation. 
# Your task is to correct it.
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

#Task 2: Your Mood Today Ask the user how they feel today. 
# If they say "happy", print "That's great to hear!", and if they say "sad", print "I hope your day gets better!". 
# Ensure your if statement is properly indented. 

mood = input("How are you feeling today?")

if mood == "happy":
    print("That's great to hear!")
if mood == "sad": # wasn't sure if it was better to do if or else, as there's numerous possible inputs
    print ("I hope your day gets better!")
