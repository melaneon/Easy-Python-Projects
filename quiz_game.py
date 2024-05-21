print("Welcome to Quiz Game!")

playing = input("Do you want ot play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")

# Q 1
answer = input("What does CPU stand for? ").lower()
score = 0
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Q 2
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Q 3
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Q 4
answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")






