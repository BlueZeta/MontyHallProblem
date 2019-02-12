import random
import time
from matplotlib import pyplot as plt

# based on this youtube video
# https://www.youtube.com/watch?v=4Lb-6rxZxx0

def main():
    # Variables
    round = 0
    keep = 0
    keep_tally = 0
    other_tally = 0
    other = 0
    original_choice = 0
    Doors = []

    # other choice percentage
    something = []
    # number of simulations
    anything = []
    # kept choice percentage
    nothing = []
    # original choice percentage
    nothing = []

    number = input("How many simulations do you want? ")
    size = input("What is the size of your array? ")

    beginTime = time.time()

    # goes through the number of simulations
    for y in range(1, number):

        # adds the number of goats by one less than the the input variable size 
        for x in range(size - 1):
            Doors.append("goat")

        Doors.append("car")

        # Number of Tests
        for i in xrange(0, y):
            round += 1
            # print("######## Test number " + str(round) + "########")
            random.shuffle(Doors)
            # randomly chooses a number to pick from
            choice = random.randrange(size)
            # the player's pick
            pick = Doors[choice]
            # counts the number of times the player choose right the first time
            if Doors[choice] == "car":
                original_choice += 1

            # remove duplicates except for one car and one goat
            newDoors = Remove(Doors)
            # gets the index of the player's pick
            keep = newDoors.index(pick)

            # assigns a number to other option
            if keep == 0:
                other == 1
            else:
                other == 0

            # adds a tally if the player kept her option and gets it correct
            if newDoors[keep] == "car":
                keep_tally += 1
            # adds a tally if the player pick the other option and gets it correct
            else:
                other_tally += 1

        # original successes
        os = float(original_choice) * 100 / float(y)
        # original losses
        ol = 100 - float(os)

        # keep successes
        ks = float(keep_tally) * 100 / float(y) 
        # keep fails
        kf = 100.0 - float(ks)

        # other successes 
        oss = float(other_tally) * 100 / float(y)
        # other fails
        of = 100 - float(oss)

        # print("################ RESULTS #################")
        # print("Original Guess Successes: %s" %(os))
        # print("Original Guess Fails: %s" %(ol))
        # print("------------------------------------------")
        # print("Keep Guess Successes: %s" %(ks))
        # print("Keep Guess Fails: %s" %(kf))
        # print("Other Guess Successes: %s" %(oss))
        # print("Other Guess Fails: %s" %(of))

        # add data to arrays
        something.append(oss)
        anything.append(y)
        nothing.append(ks)

        # reset
        other_tally = 0
        keep_tally = 0
        original_choice = 0

    # https://stackoverflow.com/questions/27779677/how-to-format-elapsed-time-from-seconds-to-hours-minutes-seconds-and-milliseco
    endTime = time.time()
    timer = endTime - beginTime
    hours = timer//3600
    timer = timer - 3600*hours
    minutes = timer //60
    seconds = timer - 60*minutes
    print("Timer - %d:%d:%d" %(hours, minutes, seconds))

    # plotting stuff
    plt.plot(anything, something)
    plt.plot(nothing)
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
