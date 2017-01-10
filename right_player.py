import random
import sys

class Player:

    def __init__(self):
        self.player_movement = [0]
        self.player_attack = random.randint(15, 20)

        '''if self.player_hp > 40:
            global player_attack
            self.pick_player_attack = random.randint(15,20)
            self.player_attack.append(self.pick_player_attack)

        if self.player_hp < 40:
            global player_attack
            self.pick_player_attack = random.randint(20,25)
            self.player_attack.append(self.pick_player_attack)'''

        self.player_xp = [0]

    player_name = raw_input("Choose your daring adventurer's name. ")

    while True:
        player_gender = raw_input("Are you a lady adventurer or a gentleman adventurer? Type F for lady, M for gentleman. ").upper()
        print(' ')

        if player_gender == 'F':
            while True:
                print ("What is {}'s hair color? You can choose black, brown, blonde, red, orange, green, yellow, blue, or purple.").format(player_name)
                female_hair = raw_input("> ").lower()

                if female_hair == 'blue' or female_hair == 'red' or female_hair == 'purple' or female_hair == 'yellow' or female_hair == 'orange' or female_hair == 'green':
                    print ("Your bright color choice of hair will make you stand out among the natives of the jungle. Unfortunately for you, this will increase your chances at being detected by unfriendly foes.")
                    print (" ")
                    break

                elif female_hair == 'black' or female_hair == 'brown' or female_hair == 'blonde':
                    print ("Good choice!")
                    print (" ")
                    break
                else:
                    print ("That's not a valid color!")
                    continue

            while True:
                print ("Will {} take a frying pan, knife, or pepperspray on her adventure? ").format(player_name)
                female_weapon = raw_input("> ").lower()

                if female_weapon == 'frying pan':
                    print ("The best defense.")
                    print(" ")
                    break
                elif female_weapon == 'knife':
                    print ("So violent wow.")
                    print (" ")
                    break
                elif female_weapon == 'pepperspray':
                    print ("Good choice! You're really with the times!")
                    print (" ")
                    break
                else:
                    print ("That's not a valid weapon!")
                    continue

            break

        if player_gender == 'M':
            while True:
                print ("What is {}'s hair color? You can choose black, brown, blond, red, orange, green, yellow, blue, or purple. ").format(player_name)
                male_hair = raw_input("> ").lower()

                if male_hair == 'blue' or male_hair == 'red' or male_hair == 'green' or male_hair == 'purple' or male_hair == 'yellow' or male_hair == 'orange':
                    print("Your bright color choice of hair will make you stand out among the natives of the jungle. Unfortunately for you, this will increase your chances at being detected by unfriendly foes.")
                    print(" ")
                    break
                elif male_hair == 'brown' or male_hair == 'black' or male_hair == 'blond':
                    print ("Good choice!")
                    print(" ")
                    break
                else:
                    print ("That's not a valid color!")
                    continue

            while True:
                print ("Will {} take an axe, shotgun, or slingshot on his adventure? ").format(player_name)
                male_weapon = raw_input("> ").lower()

                if male_weapon == 'axe':
                    print ("Well done! Chopping down trees will be SUPER helpful...")
                    print(" ")
                    break
                elif male_weapon == 'shotgun':
                    print("Super modern wow")
                    print(" ")
                    break
                elif male_weapon == 'slingshot':
                    print("What is this, David and Goliath?")
                    print(" ")
                    break
                else:
                    print("That's not a valid weapon!")
                    continue
            break

        else:
            print('That is not a valid answer!')
            continue
