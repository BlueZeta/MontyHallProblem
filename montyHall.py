import random
import time
from matplotlib import pyplot as plt

def main():
    # Variables
    keep = 0
    other_tally = 0
    original_tally = 0
    Doors = []

    # other choice percentage
    otherArray = []
    # original choice percentage
    originalArray = []

    number = input("What is the max number of simulations you want? ")
    size = input("What is the size of your array? ")

    # parsing string to integer
    number = int(number)
    size = int(size)

    beginTime = time.time()

    # goes through the number of simulations
    for y in range(1,number):

        # adds the number of goats by one less than the the input variable size 
        for x in range(size - 1):
            Doors.append("goat")
            
        Doors.append("car")

        # Number of Tests
        for i in range(0, y):

            random.shuffle(Doors)

            # randomly chooses a number to pick from
            choice = random.randrange(size)
            # the player's pick
            pick = Doors[choice]

            # remove duplicates except for one car and one goat
            newDoors = Remove(Doors)
            # gets the index of the player's pick
            keep = newDoors.index(pick)

            # adds a tally if the player kept her option and gets it correct
            if newDoors[keep] == "car":
                original_tally += 1
            # adds a tally if the player pick the other option and gets it correct
            else:
                other_tally += 1

        # Original Guess Win Percentage
        originalPercentage = float(original_tally) * 100 / float(y) 

        # Other Guess Win Percentage
        otherPercentage = float(other_tally) * 100 / float(y)

        #print("################ RESULTS #################")
        #print("Original Guess Win Percentage: %s" %(originalPercentage))
        #print("Other Guess Win Percentage: %s" %(otherPercentage))

        # add data to arrays
        originalArray.append(originalPercentage)
        otherArray.append(otherPercentage)

        # reset
        other_tally = 0
        original_tally = 0
        Doors.clear()
    
    endTime = time.time()
    
    # time conversions
    timer = endTime - beginTime
    hours = timer//3600
    timer = timer - 3600*hours
    minutes = timer //60
    seconds = timer - 60*minutes
    print("Timer - %d:%d:%d" %(hours, minutes, seconds))

    # plotting stuff
    plt.plot(otherArray, label = "Other Guess Win Percentage")
    plt.plot(originalArray, label = "Original Guess Win Percentage")
    plt.legend(loc = "upper right")
    plt.xlabel("Number of simulations")
    plt.ylabel("Success rate")
    plt.title("Monty Python Problem")
    plt.show()

# https://www.geeksforgeeks.org/python-remove-duplicates-list/
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

main()        
