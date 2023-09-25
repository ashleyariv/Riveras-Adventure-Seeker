# lib/cli.py

# from helpers import (
#     exit_program,
#     helper_1
# )


# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             helper_1()
#         else:
#             print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. Some useful function")


# if __name__ == "__main__":
#     main()

username = input('Enter adventerous username: ')
print(f'Welcome, {username}! Get ready to play, the rules are as follows:\nYou must choose a path at each prompt\nChoose carefully of it could cost you\nRemember every decision counts, so choose wisely, and have fun!!')

answer = input('Do you wish to continue on this adventure? (y/n): ').lower()

while True:
    if answer == 'n':
        break
    if answer == 'y':
        answer = input("You've just woken up in a strange room. You hear a faint sound coming from upstairs and it sounds like something in distress. You also see what you think are flashlights roaming around outside. Do you follow the sound or the lights? Please Choose (sound/lights): ").lower()
        if answer == 'sound':
            answer = input('You head upstairs toward the sound and find a locked armoire. It sounds like there is a rabid dog inside, do you open it or go back downstairs? Please Choose (open/leave): ').lower()
            if answer == 'leave':
                print('You turn around to go back but fall down the stairs and break your neck.\nTry again next time! Thanks for playing!')
                break
            elif answer == 'open':
                answer = input('A dog greets you with kisses, happy to be saved. Inside the armoire you find a crossbow but no arrows, do you take it or leave it behind? Please Choose (take it/leave it): ').lower()
                if answer == 'take it':
                    answer = input('You head downstairs and lucky for you the dog notices a big hole in the ground, so you step around it. You start calling for help moving towards the lights in the woods and you notice the lights begin to charge at you. It is a very large man looking to harm you but once he is close enough the dog jumps to your rescue and attcks. He successfully protects you but dies in the tussle. Do you go back into the house and hide or do you take the flashlight from the corpse and continue walking through the woods? Please Choose (hide/continue): ').lower()
                    if answer == 'hide':
                        print('You hide inside the house for several hours and eventually a group of cannibals finds you and you die.\nTry again next time! Thanks for playing!')
                        break
                    elif answer == 'continue':
                        answer = input('As you walk through the woods you come across some arrows on the ground that will serve as ammo for your crossbow. Suddenly you hear a motorcycle approaching and you see two ax-wielding men. Now you have a decision to make, do you try to kill these men with your crossbow or do you run back to the house and hide? Please Choose (house/shoot): ').lower()
                        if answer == 'shoot':
                            print('Your crossbow jammed and they killed you.\nTry again next time! Thanks for playing!')
                            break
                        elif answer == 'house':
                            print('You realize the house was the home of your attackers and as you anxiously look around you find a shotgun. When they run inside looking for you, you shoot them with the shotgun.\nNow at ease, you look for something to call for help but instead find dismembered body parts and you relaize these men were cannibals looking for their next meal. You decide to take their motorcycle and ride until you reach civilization. Congrats you have made it through this adventure!')
                            break
                        else:
                            print('Not a valid option, you died.\nThanks for playing!')
                            break
                    else:
                        print('Not a valid option, you died.\nThanks for playing!')
                        break
                elif answer == 'leave it':
                    answer = input('You head downstairs and lucky for you the dog notices a big hole in the ground, so you step around it. You start calling for help moving towards the lights in the woods and you notice the lights begin to charge at you. It is a very large man looking to harm you but once he is close enough the dog jumps to your rescue and attcks. He successfully protects you but dies in the tussle. Do you go back into the house and hide or do you take the flashlight from the corpse and continue walking through the woods? Please Choose (hide/continue): ')
                    if answer == 'hide':
                        print('You hide inside the house for several hours and eventually a group of cannibals finds you and you die.\nTry again next time! Thanks for playing!')
                        break
                    elif answer == 'continue':
                        answer = input('As you walk through the woods you come across some arrows on the ground and you pick them up hoping to use them as defense. Suddenly you hear a motorcycle approaching and you see two ax-wielding men. Now you have a decision to make, do you try to attack these men with your arrows or do you run back to the house and hide? Please Choose (attack/run): ')
                        if answer == 'run':
                            print('You realize the house was the home of your attackers and as you anxiously look around you find a shotgun. When they run inside looking for you, you shoot them with the shotgun.\nNow at ease, you look for something to call for help but instead find dismembered body parts and you relaize these men were cannibals looking for their next meal. You decide to take their motorcycle and ride until you reach civilization. Congrats you have made it through this adventure!')
                            break
                        elif answer == 'attack':
                            print('Your arrows were no match for their axes and they killed you, you lost!\nTry again next time! Thanks for playing!')
                            break
                        else: 
                            print('Not a valid option, you died.\nThanks for playing!')
                            break
                else: 
                    print('Not a valid option, you died.\nThanks for playing!')
                    break
            else: 
                print('Not a valid option, you died.\nThanks for playing!')
                break
        elif answer == 'lights':
            answer = input('You run outside toward the lights and fall into a hole before you could get close to them. Inside the hole you find a small tunnel, do you go through it or stay in place and call for help? Please Choose (tunnel/help): ').lower()
            if answer == 'tunnel':
                answer = input('You crawl inside looking for something and find a flashlight jammed into the wall of the tunnel, do you pull it out or continue without it? Please Choose (pull/continue): ').lower()
                if answer == 'pull':
                    print('You caused the tunnel to collapse in on itself and you died from suffocation!\nTry again next time! Thanks for playing!')
                elif answer == 'continue':
                    print('As you went on your knee hit the flashlight causing the tunnel to become unstable and collapse in on itself, you are now dead.\nTry again next time! Thanks for playing!')
                else:
                    print('Not a valid option, you died.\nThanks for playing!')
            elif answer == 'help':
                print('After yelling for help the lights make their way toward you and find you in the hole. It is a cannibalistic man looking for food and you have just made his day. Sorry but you died, maybe you should have gone upstairs.\nTry again next time! Thanks for playing!')
            else:
                print('Not a valid option, you died.\nThanks for playing!')
        else: 
            print('Not a valid option, you died.\nThanks for playing!')
            break
    else:
        print('Not a valid option, please try again.')
        break