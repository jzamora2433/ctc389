#Josue Zamora
#lab 8

replay = "yes"

while replay == "yes":


    name= input("Hey, what is your name? ")
    print (name, "our three quaterbacks just got hurt, playoffs berth is on the line, we need you to come in and be our quaterback, here is the playbook,2-minutes left on the clock, which will you choose:")
    print ("----------------------")
    print("option 1: Jet Sweep- hand off to the moving reciever")
    print("option 2: Hail Mary- deep throw hoping someone on your team catches it")
    print("option 3: Running back hand off- give the ball to your running back")
    print ("----------------------")

    option = int(input("please input the number play you choose: "))

    if option == 1:
        print("good call we just got a first down, but the clock is running")
        print("please pick a new play")
        print("1 = Short pass to the left")
        print("2 = Short pass down the middle")
        print("3 = Short pass to the right")
        choice = int(input())

        if (choice == 1):
            print("ouch, you didnt see that defensive end coming you just got sacked and fumbled the ball")
        elif (choice == 2):
            print("oh no interception")
        elif (choice == 3):
            print("good pass, ready for the next play")
            print("we have momentum, lets keep it up, pick the next play")
            print("1: 10 and out to tight end")
            print("2: hand off to running back")
            print("3: quick slant pass to outside reciever")
            choice = int(input())

        if (choice == 1):
            print("lets go!!! first down and clock is stopped")
            print(" pick the next play")
            print("1: take a shot, throw it to the deep reciever")
            print("2: short pass to tight end on the left")
            print("3: hand off to running back")
            choice = int(input())

            if (choice == 1):
                print("aww interception, game over")
            elif (choice == 2):
                print("oh no interception by the defensive end, game over")
            elif (choice == 3):
                print("bad handoff, fumble, game over")


        elif (choice == 2):
            print("fumble, other team recovered")
        elif (choice == 3):
            print("first down, but that clock is running")
            print("pick the next play")
            print("1: take a shot deep ball")
            print("2: QB keep, lets see how fast you are")
            print("3: short pass to running back")
            choice = int(input())

            if (choice == 1):
                print("interception, other team ran it back for a touchdown")
            elif (choice == 2):
                print("oh man your a lot faster than i thought, and smart of you to run out of bounds to stop the clock")
                print("5 seconds left, 5 yards out lets finish this")
                print("1: Trick play")
                print("2: kick the field goal, lets try and go to overtime")
                print("3: passing play, find the open guy")
                choice = int(input())

                if (choice == 1):
                    print("You son of a gun you did it, Touchdown! Touchdown!! Touchdown!!!! We just won the game")
                elif (choice == 2):
                    print("oh no wide right, game over")
                elif (choice == 3):
                    print("oh we were so close, pass deflected game over")
            elif (choice == 3):
                print("he cant catch the ball, he tipped it and now the defender has it, game over")


    elif option == 2:
        print("interception, game over")

    elif option == 3:
        print("nice call, running back got us 3 yards")
        print("please pick a new play")
        print("1 = Short pass to the left")
        print("2 = Short pass down the middle")
        print("3 = Short pass to the right")
        choice = int(input())
    
        if (choice == 1):
            print("ouch, you didnt see that defensive end coming you just got sacked and fumbled the ball")
        elif (choice == 2):
            print("oh no interception")
        elif (choice == 3):
            print("good pass, ready for the next play")

            print("we have momentum, lets keep it up, pick the next play")
            print("1: 10 and out to tight end")
            print("2: hand off to running back")
            print("3: quick slant pass to outside reciever")
            choice = int(input())

        if (choice == 1):
            print("lets go!!! first down and clock is stopped")
            print("pick the next play")
            print("1: take a shot deep ball")
            print("2: QB keep, lets see how fast you are")
            print("3: short pass to running back")
            choice = int(input())

            if (choice == 1):
                print("interception, other team ran it back for a touchdown")
            elif (choice == 2):
                print("oh man you didnt make it out the pocket, sack game over")
            elif (choice == 3):
                print("he cant catch the ball, he tipped it and now the defender has it, game over")


        elif (choice == 2):
            print("fumble, other team recovered")
        elif (choice == 3):
            print("first down, but that clock is running")
            print("pick the next play")
            print("1: take a shot deep ball")
            print("2: QB keep, lets see how fast you are")
            print("3: short pass to running back")
            choice = int(input())

            if (choice == 1):
                print("interception, other team ran it back for a touchdown")
            elif (choice == 2):
                print("oh man your a lot faster than i thought, and smart of you to run out of bounds to stop the clock")
                print("5 seconds left, 5 yards out lets finish this")
                print("1: Trick play")
                print("2: kick the field goal, lets try and go to overtime")
                print("3: passing play, find the open guy")
                choice = int(input())

                if (choice == 1):
                    print("You were so close, fumble on the double exchange, game over")
                elif (choice == 2):
                    print("oh no wide right, game over")
                elif (choice == 3):
                    print("oh we were so close, pass deflected game over")
            elif (choice == 3):
                print("he cant catch the ball, he tipped it and now the defender has it, game over")


            elif (choice == 3):
                print("he cant catch the ball, he tipped it and now the defender has it, game over")

                print("5 seconds left, 5 yards out lets finish this")
                print("1: Trick play")
                print("2: kick the field goal, lets try and go to overtime")
                print("3: passing play, find the open guy")
                choice = int(input())

            if (choice == 1):
                print("You son of a gun you did it, Touchdown! Touchdown!! Touchdown!!!! We just won the game")
            elif (choice == 2):
                print("oh no wide right, game over")
            elif (choice == 3):
                print("oh we were so close, pass deflected game over")
        elif (choice == 3):
            print("he cant catch the ball, he tipped it and now the defender has it, game over")


replay = input("Would you like to play again, please type yes or no")

print("Thank you for playing")

