import random
import time

# based on this youtube video
# https://www.youtube.com/watch?v=4Lb-6rxZxx0

def mine():
    # Variables
    round = 0
    keep = 0
    keep_tally = 0
    other_tally = 0
    other = 0
    original_choice = 0
    
    number = input("How many simulations do you want? ")
    beginTime = time.time()
    for i in xrange(0, number):
        Doors = ["car", "goat", "goat"]
        round += 1
        print("######## Simulation number " + str(round) + "########")
        random.shuffle(Doors)
        # choose between 0, 1, or 2
        choice = random.randrange(3)
        # the player's pick
        pick = Doors[choice]
        # counts the number of times the player choose right the first time
        if Doors[choice] == "car":
            original_choice += 1

        Doors.remove("goat")
        # gets the index of the player's pick
        keep = Doors.index(pick)

        # assigns a number to other option
        if keep == 0:
            other == 1
        else:
            other == 0

        # adds a tally if the player kept her option and gets it correct
        if Doors[keep] == "car":
            keep_tally += 1
        # adds a tally if the player pick the other option and gets it correct
        else:
            other_tally += 1

    endTime = time.time()

    # original successes
    os = float(original_choice) * 100 / float(number)
    # original losses
    ol = 100 - float(os)

    # keep successes
    ks = float(keep_tally) * 100 / float(number) 
    # keep fails
    kf = 100.0 - float(ks)

    # other successes 
    oss = float(other_tally) * 100 / float(number)
    # other fails
    of = 100 - float(oss)

    
    timer = endTime * beginTime
    print("################ RESULTS #################")
    print("Original Guess Successes: %s" %(os))
    print("Original Guess Fails: %s" %(ol))
    print("------------------------------------------")
    print("Keep Guess Successes: %s" %(ks))
    print("Keep Guess Fails: %s" %(kf))
    print("Other Guess Successes: %s" %(oss))
    print("Other Guess Fails: %s" %(of))
    print("Total time: %s " %(timer))

def redefine():
    # Variables
    round = 0
    keep = 0
    keep_tally = 0
    other_tally = 0
    other = 0
    original_choice = 0
    Doors = []

    number = input("How many simulations do you want? ")
    size = input("What is the size of your array? ")

    # adds the number of goats by one less than the the input variable size 
    for x in range(size - 1):
        Doors.append("goat")

    Doors.append("car")

    beginTime = time.time()

    for i in xrange(0, number):
        round += 1
        print("######## Simulation number " + str(round) + "########")
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

    endTime = time.time()

    # original successes
    os = float(original_choice) * 100 / float(number)
    # original losses
    ol = 100 - float(os)

    # keep successes
    ks = float(keep_tally) * 100 / float(number) 
    # keep fails
    kf = 100.0 - float(ks)

    # other successes 
    oss = float(other_tally) * 100 / float(number)
    # other fails
    of = 100 - float(oss)

    
    timer = endTime * beginTime
    print("################ RESULTS #################")
    print("Original Guess Successes: %s" %(os))
    print("Original Guess Fails: %s" %(ol))
    print("------------------------------------------")
    print("Keep Guess Successes: %s" %(ks))
    print("Keep Guess Fails: %s" %(kf))
    print("Other Guess Successes: %s" %(oss))
    print("Other Guess Fails: %s" %(of))
    print("Total time: %s " %(timer))

# https://www.geeksforgeeks.org/python-remove-duplicates-list/
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

redefine()
        