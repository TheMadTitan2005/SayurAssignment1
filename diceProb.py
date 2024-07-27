import random
points = 0
count = 0
while(points < 50):  
    dice = random.randint(1,6)
    count += 1
    print(f"The number rolled is : {dice}")
    if(dice % 2 == 0):
        points += 2
    else:
        print("Jump")
print(f"Player wins in {count} steps with {points} points")


        
