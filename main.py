import copy
import timeit

from player import *
import csv

# Referenced Corey Schafer's tutorial to parse in python
# https://www.youtube.com/watch?v=q5uM4VKywbA
# reads the csv file, filtering user preferences and appending players to the list of players
def parse(player_list, ms_player_list, qs_player_list, min_height, age_min, age_max, player_foot, sub_position, position, max_price):
    with open('players.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            id_num = line[0]
            name = line[1]
            prev_season = line[2]
            birth_country = line[3]
            citizenship = line[4]
            age = line[5]
            age = int(age)
            sub_pos = line[6]
            pos = line[7]
            foot = line[8]
            player_height = line[9]
            player_height = int(player_height)
            value = line[10]
            value = int(value)
            curr_club = line[11]
            if value > max_price:
                continue
            if min_height != -1 and player_height < min_height:
                continue
            if age_min != -1 and age < age_min:
                continue
            if age_max != -1 and age > age_max:
                continue
            if player_foot!=-1:
                if player_foot==1 and foot!="left":
                    continue
                if player_foot==2 and foot!="right":
                    continue
            if sub_position!=-1:
                if sub_position==1 and sub_pos!="Right Winger":
                    continue
                if sub_position==2 and sub_pos!="Left Winger":
                    continue
                if sub_position==3 and sub_pos!="Right Midfield":
                    continue
                if sub_position==4 and sub_pos!="Left Midfield":
                    continue
                if sub_position==5 and sub_pos!="Right-Back":
                    continue
                if sub_position==6 and sub_pos!="Left-Back":
                    continue
                if sub_position==7 and sub_pos!="Goalkeeper":
                    continue
                if sub_position==8 and sub_pos!="Central Midfield":
                    continue
                if sub_position==9 and sub_pos!="Centre-Back":
                    continue
                if sub_position==10 and sub_pos!="Centre-Forward":
                    continue
                if sub_position==11 and sub_pos!="Defensive Midfield":
                    continue
                if sub_position==12 and sub_pos!="Attacking Midfield":
                    continue
            if position!=-1:
                if position==1 and pos!="Attack":
                    continue
                if position==2 and pos!="Defender":
                    continue
                if position==3 and pos!="Midfield":
                    continue
                if position==4 and pos!="Goalkeeper":
                    continue
            # appending to a list in python is amortized O(1)
            player_list.append(
                Player(name, birth_country, citizenship, sub_pos, pos, value, curr_club, id_num, foot, prev_season, player_height,
                       age))
            ms_player_list.append(
                Player(name, birth_country, citizenship, sub_pos, pos, value, curr_club, id_num, foot, prev_season,
                       player_height,
                       age))
            qs_player_list.append(
                Player(name, birth_country, citizenship, sub_pos, pos, value, curr_club, id_num, foot, prev_season,
                       player_height,
                       age))


# adapted pseudocode from following tutorial to write the merge function: https://www.youtube.com/watch?v=TzeBrDU-JaY
def mergeSort(unsortedList):
    if len(unsortedList) > 1:
        middle = len(unsortedList) // 2
        left_portion = unsortedList[:middle]
        right_portion = unsortedList[middle:]
        
        mergeSort(left_portion)
        mergeSort(right_portion)

        i = j = k = 0
        numInLeft = len(left_portion)
        numInRight = len(right_portion)
        while i < numInLeft and j < numInRight:
            if left_portion[i].highestValue < right_portion[j].highestValue:
                unsortedList[k] = left_portion[i]
                i = i + 1
            else:
                unsortedList[k] = right_portion[j]
                j = j + 1
            k = k + 1
        while i < numInLeft:
            unsortedList[k] = left_portion[i]
            i = i + 1
            k = k + 1
        while j < numInRight:
            unsortedList[k] = right_portion[j]
            j = j + 1
            k = k + 1


# adapted pseudocode from following tutorial to write the quick function: https://www.youtube.com/watch?v=7h1s2SojIRw
def quickSort(unsortedList):
    def quick(array, first_index, second_index):
        if first_index < second_index:
            pivot = array[second_index].highestValue
            i = first_index - 1
            for j in range(first_index, second_index):
                if array[j].highestValue < pivot:
                    i = i + 1
                    array[i], array[j] = array[j], array[i]

            array[i + 1], array[second_index] = array[second_index], array[i + 1]
            pivot_index = i + 1
            quick(array, first_index, pivot_index - 1)
            quick(array, pivot_index + 1, second_index)

    quick(unsortedList, 0, len(unsortedList) - 1)

if __name__ == '__main__':
    # players is the list that holds all the player values
    players = []

    # initializing the lists to be passed into sorting functions
    msPlayers = []
    qsPlayers = []

    # sets initial values for preference variables
    height = -1
    minAge = -1
    maxAge = -1
    footNum = -1
    subNum = -1
    posNum = -1

    # initializes the timer variables for the merge and quick sort functions
    qstime = 0
    mstime = 0

    print("---------------------------------------------")
    print("Welcome to the Football Club Transfer Market!")
    print("---------------------------------------------")
    print()
    print("We hear you are looking for a new player!")

    # prompts the user for a budget for the player and validates input
    while True:
        try:
            budget = int(input("Please provide your budget for the player: "))
            if budget < 0:
                raise ValueError
            break
        except ValueError:
            print()
            print("~WARNING: Please enter a positive integer~")

    # checks if user has preference for the player's height and validates input
    print()
    print("Do you have a height preference for your player?")
    while True:
        try:
            heightPref = int(input("Please enter 1 if YES or 0 if NO: "))
            if heightPref != 0 and heightPref != 1:
                raise ValueError
            break
        except ValueError as error:
            print()
            print("~WARNING: Please type 1 or 0~")

    if heightPref == 1:
        print()
        while True:
            try:
                height = int(input("Please enter the minimum height (in cm) you expect your player to be: "))
                if height < 0:
                    raise ValueError
                break
            except:
                print()
                print("~WARNING: Please type a positive integer")

    # checks if user has a maximum age preference for the player and validates input
    print()
    print("Do you have a maximum age preference for your player?")
    while True:
        try:
            maxAgePref = int(input("Please enter 1 if YES or 0 if NO: "))
            if maxAgePref != 0 and maxAgePref != 1:
                raise ValueError
            break
        except ValueError as error:
            print()
            print("~WARNING: Please type 1 or 0~")

    if maxAgePref == 1:
        print()
        while True:
            try:
                maxAge = int(input("Please enter the maximum age you expect your player to be: "))
                if maxAge < 0:
                    raise ValueError
                break
            except:
                print()
                print("~WARNING: Please type a positive integer")

    # checks if user has a minimum age preference for the player and validates input
    print()
    print("Do you have a minimum age preference for your player?")
    while True:
        try:
            minAgePref = int(input("Please enter 1 if YES or 0 if NO: "))
            if minAgePref != 0 and minAgePref != 1:
                raise ValueError
            break
        except ValueError as error:
            print()
            print("~WARNING: Please type 1 or 0~")

    if minAgePref == 1:
        print()
        while True:
            try:
                minAge = int(input("Please enter the minimum age you expect your player to be: "))
                if minAge < 0:
                    raise ValueError
                break
            except:
                print()
                print("~WARNING: Please type a positive integer")

    # checks if user has a preference for the player's dominant foot and validates input
    # left-dominant: 1 || right-dominant: 2
    print()
    print("Do you have a preference for the player's dominant foot?")
    while True:
        try:
            footPref = int(input("Please enter 1 if YES or 0 if NO: "))
            if footPref != 0 and footPref != 1:
                raise ValueError
            break
        except ValueError as error:
            print()
            print("~WARNING: Please type 1 or 0~")

    if footPref == 1:
        print()
        while True:
            try:
                footNum = int(input("If you prefer left-dominant enter 1 or for right-dominant enter 2: "))
                if footNum != 1 and footNum != 2:
                    raise ValueError
                break
            except:
                print()
                print("~WARNING: Please type a positive integer")

    # checks if user has a preference for the player's sub position
    # Right Winger: 1 || Left Winger: 2 || Right Midfield: 3 || Left Midfield: 4 || Right-Back: 5 || Left-Back: 6
    # Goalkeeper: 7 || Central Midfield: 8 || Centre-Back: 9 || Centre-Forward: 10 || Defensive Midfield: 11
    # Attacking Midfield: 12
    print()
    print("Do you have a preference for the player's sub position?")
    while True:
        try:
            subPref = int(input("Please enter 1 if YES or 0 if NO: "))
            if subPref != 0 and subPref != 1:
                raise ValueError
            break
        except ValueError as error:
            print()
            print("~WARNING: Please type 1 or 0~")

    if subPref == 1:
        print()
        while True:
            try:
                subNum = int(input(
                    "If you prefer Right Winger enter 1, Left Winger enter 2, Right Midfield enter 3, Left Midfield "
                    "enter 4, Right-Back enter 5, Left-Back enter 6, Goalkeeper enter 7, Central Midfield enter 8, "
                    "Centre-Back enter 9, Centre-Forward enter 10, Defensive Midfield enter 11, Attacking Midfield "
                    "enter 12: "))
                if subNum < 1 and subNum > 12:
                    raise ValueError
                break
            except:
                print()
                print("~WARNING: Please type a positive integer")

    # checks if user has a preference for player's position
    # Attack: 1 || Defender: 2 || Midfield: 3 || Goalkeeper: 4
    print()
    print("Do you have a preference for the player's position?")
    while True:
        try:
            posPref = int(input("Please enter 1 if YES or 0 if NO: "))
            if posPref != 0 and posPref != 1:
                raise ValueError
            break
        except ValueError as error:
            print()
            print("~WARNING: Please type 1 or 0~")

    if posPref == 1:
        print()
        while True:
            try:
                posNum = int(
                    input("If you prefer Attack enter 1, Defender enter 2, Midfield enter 3, Goalkeeper enter 4: "))
                if posNum < 1 and posNum > 4:
                    raise ValueError
                break
            except:
                print()
                print("~WARNING: Please type a positive integer")

    # create the list of players based on user's preferences
    parse(players, msPlayers, qsPlayers, height, minAge, maxAge, footNum, subNum, posNum, budget)

    mstime = timeit.timeit(stmt='mergeSort(msPlayers)', setup='pass', number=1, globals=globals())
    qstime = timeit.timeit(stmt='quickSort(qsPlayers)', setup='pass', number=1, globals=globals())
    print()
    print("---------------------------------------------------------")
    print("Listed below are the players that meet your criteria:")
    print("---------------------------------------------------------")
    print(
        f"(It took {qstime} seconds to sort the list of players in order of ascending maximum market value using Quick Sort)")
    print(
        f"(It took {mstime} seconds to sort the list of players in order of ascending maximum market value using Merge Sort)")

    # prints the sorted list of players
    print()
    for player in msPlayers:
        print("Player Cost: ", player.highestValue, " | Name: ", player.name, " | ID: ", player.id, " | Age: ", player.age, " | Position: ", player.position, " | Sub-Position: ", player.subPosition, " | Foot: ", player.foot, " | Height: ", player.height, " | Country of Birth: ", player.birthCountry, " | Country of Citizenship: ", player.citizenship, " | Last Season: ", player.prevSeason)
