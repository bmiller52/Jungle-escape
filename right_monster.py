import random
import sys

from right_player import Player

class Monster:

    def __init__(self):
        self.player_hp = [100]

    def brown_spider(self):

        player = Player()

        spider_hp = random.randint(15, 25)
        spider_attack = [random.randint(5, 10)]
        spider_xp = random.randint(10, 15)

        current_spider_health = []
        current_spider_health.append(spider_hp)

        both_attack_health = []
        both_attack_health.append(player.player_attack)

        print('----------------------------------------------------------------------')
        print("You've encountered a brown spider. He's not very spooky. Health: {}. |").format(spider_hp)
        print('----------------------------------------------------------------------')

        while True:
            print(' ')
            print("The brown spider has {} HP left and {} attack points. ").format(current_spider_health[0], spider_attack[0])
            print('Your attack is {} and health is {}.').format(player.player_attack, self.player_hp[0])
            print('=======================================================')
            print(' ')
            attack_input = raw_input('Would you like to [Z]Attack or [X]Run Away ').lower()

            if self.player_hp < [1]:
                print('-------------------------------------------------------')
                print('OH NO! The monster killed you! Better luck next time. |')
                print('-------------------------------------------------------')
                sys.exit()

            elif attack_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()

            elif attack_input == 'x':
                ratio_run = [random.choice(range(1, 5))]

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The monster killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif ratio_run == [1] or ratio_run == [2] or ratio_run == [3]:
                    print('OH NO! When you were trying to run away, the spider caught you.')
                    print(' ')
                    sys.exit()
                else:
                    print('Why did you run away you coward?')
                    print(' ')
                    break

            elif attack_input == 'z':
                attack_subtraction = current_spider_health[0] - both_attack_health[0]
                current_spider_health.pop()
                current_spider_health.append(attack_subtraction)

                spider_attacking_chance = [random.choice(range(1, 6))]

                blue = spider_attacking_chance

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The monster killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif current_spider_health < [1]:
                    print('--------------------------------')
                    print('Great job! The spider is dead. |')
                    print('--------------------------------')
                    break


                elif blue == [1] or blue == [2] or blue == [3]:
                    spider_attack_sub = self.player_hp[0] - spider_attack[0]
                    self.player_hp.pop()
                    self.player_hp.append(spider_attack_sub)

                    print('--------------------------------------------------------')
                    print('The spider block your attack and did a counter attack! |')
                    print('--------------------------------------------------------')

                    if self.player_hp < [1]:
                        print('-------------------------------------------------------')
                        print('OH NO! The monster killed you! Better luck next time. |')
                        print('-------------------------------------------------------')
                        sys.exit()

                    elif attack_input == 'q':
                        print('Thanks for playing!')
                        print(' ')
                        sys.exit()

                else:
                    print('Tha\'s not a valid answer')
                    print(' ')
                    continue

    def poisonous_spider(self):
        player = Player()

        spider_hp = random.randint(20,30)
        spider_xp = random.randint(20,25)
        spider_attack = [random.randint(10,15)]

        current_spider_health = []
        current_spider_health.append(spider_hp)

        both_attack_health = []
        both_attack_health.append(player.player_attack)

        print('----------------------------------------------------------------------')
        print("You've encountered a poisonous spider. He's a pesky one. Health: {}. |").format(spider_hp)
        print('----------------------------------------------------------------------')

        while True:
            print(' ')
            print("The poisonous spider has {} HP left and {} attack points. ").format(current_spider_health[0], spider_attack[0])
            print('Your attack is {} and health is {}.').format(player.player_attack, self.player_hp[0])
            print('=======================================================')
            print(' ')
            attack_input = raw_input('Would you like to [Z]Attack or [X]Run Away ').lower()

            if self.player_hp < [1]:
                print('-------------------------------------------------------')
                print('OH NO! The monster killed you! Better luck next time. |')
                print('-------------------------------------------------------')
                sys.exit()

            elif attack_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()

            elif attack_input == 'x':
                ratio_run = [random.choice(range(1, 5))]

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The monster killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif ratio_run == [1] or ratio_run == [2] or ratio_run == [3]:
                    print('OH NO! When you were trying to run away, the spider caught you.')
                    print(' ')
                    sys.exit()
                else:
                    print('Why did you run away you coward?')
                    print(' ')
                    break

            elif attack_input == 'z':
                attack_subtraction = current_spider_health[0] - both_attack_health[0]
                current_spider_health.pop()
                current_spider_health.append(attack_subtraction)

                spider_attacking_chance = [random.choice(range(1, 6))]

                blue = spider_attacking_chance

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The monster killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif current_spider_health < [1]:
                    print('--------------------------------')
                    print('Great job! The spider is dead. |')
                    print('--------------------------------')
                    break


                elif blue == [1] or blue == [2] or blue == [3]:
                    spider_attack_sub = self.player_hp[0] - spider_attack[0]
                    self.player_hp.pop()
                    self.player_hp.append(spider_attack_sub)

                    print('--------------------------------------------------------')
                    print('The spider block your attack and did a counter attack! |')
                    print('--------------------------------------------------------')

                    if self.player_hp < [1]:
                        print('-------------------------------------------------------')
                        print('OH NO! The monster killed you! Better luck next time. |')
                        print('-------------------------------------------------------')
                        sys.exit()

                    elif attack_input == 'q':
                        print('Thanks for playing!')
                        print(' ')
                        sys.exit()

                else:
                    print('Tha\'s not a valid answer')
                    print(' ')
                    continue

    def black_widow_spider(self):
        player = Player()

        spider_hp = random.randint(25,35)
        spider_xp = random.randint(20,35)
        spider_attack = [random.randint(20,25)]

        current_spider_health = []
        current_spider_health.append(spider_hp)

        both_attack_health = []
        both_attack_health.append(player.player_attack)

        print('---------------------------------------------------------------------------------------------------------')
        print("You've encountered a Black Widow Spider spider. Your knees are trembling. He's a pesky one. Health: {}. |").format(spider_hp)
        print('---------------------------------------------------------------------------------------------------------')

        while True:
            print(' ')
            print("The Black Widow Spider spider has {} HP left and {} attack points. ").format(current_spider_health[0], spider_attack[0])
            print('Your attack is {} and health is {}.').format(player.player_attack, self.player_hp[0])
            print('=======================================================')
            print(' ')
            attack_input = raw_input('Would you like to [Z]Attack or [X]Run Away ').lower()

            if self.player_hp < [1]:
                print('-------------------------------------------------------')
                print('OH NO! The monster killed you! Better luck next time. |')
                print('-------------------------------------------------------')
                sys.exit()

            elif attack_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()

            elif attack_input == 'x':
                ratio_run = [random.choice(range(1, 5))]

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The monster killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif ratio_run == [1] or ratio_run == [2] or ratio_run == [3]:
                    print('OH NO! When you were trying to run away, the spider caught you.')
                    print(' ')
                    sys.exit()
                else:
                    print('Why did you run away you coward?')
                    print(' ')
                    break

            elif attack_input == 'z':
                attack_subtraction = current_spider_health[0] - both_attack_health[0]
                current_spider_health.pop()
                current_spider_health.append(attack_subtraction)

                spider_attacking_chance = [random.choice(range(1, 6))]

                blue = spider_attacking_chance

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The monster killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif current_spider_health < [1]:
                    print('--------------------------------')
                    print('Great job! The spider is dead. |')
                    print('--------------------------------')
                    break


                elif blue == [1] or blue == [2] or blue == [3]:
                    spider_attack_sub = self.player_hp[0] - spider_attack[0]
                    self.player_hp.pop()
                    self.player_hp.append(spider_attack_sub)

                    print('--------------------------------------------------------')
                    print('The spider block your attack and did a counter attack! |')
                    print('--------------------------------------------------------')

                    if self.player_hp < [1]:
                        print('-------------------------------------------------------')
                        print('OH NO! The monster killed you! Better luck next time. |')
                        print('-------------------------------------------------------')
                        sys.exit()

                    elif attack_input == 'q':
                        print('Thanks for playing!')
                        print(' ')
                        sys.exit()

                else:
                    print('Tha\'s not a valid answer')
                    print(' ')
                    continue

    def dart_frog(self):
        player = Player()

        spider_hp = random.randint(45,60)
        spider_xp = random.randint(30,40)
        spider_attack = [random.randint(30,40)]

        current_spider_health = []
        current_spider_health.append(spider_hp)

        both_attack_health = []
        both_attack_health.append(player.player_attack)

        print('-----------------------------------------------------------------------------------------------------------------------')
        print("You've just run into the Golden Dart Frog, one of the deadliest animals on the planet. Death is imminent. Health: {}. |").format(spider_hp)
        print('-----------------------------------------------------------------------------------------------------------------------')

        while True:
            print(' ')
            print("The Golden Dart Frog spider has {} HP left and {} attack points. ").format(current_spider_health[0], spider_attack[0])
            print('Your attack is {} and health is {}.').format(player.player_attack, self.player_hp[0])
            print('=======================================================')
            print(' ')
            attack_input = raw_input('Would you like to [Z]Attack or [X]Run Away ').lower()

            if self.player_hp < [1]:
                print('-------------------------------------------------------')
                print('OH NO! The monster killed you! Better luck next time. |')
                print('-------------------------------------------------------')
                sys.exit()

            elif attack_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()

            elif attack_input == 'x':
                ratio_run = [random.choice(range(1, 5))]

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The monster killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif ratio_run == [1] or ratio_run == [2] or ratio_run == [3]:
                    print('OH NO! When you were trying to run away, the spider caught you.')
                    print(' ')
                    sys.exit()
                else:
                    print('Why did you run away you coward?')
                    print(' ')
                    break

            elif attack_input == 'z':
                attack_subtraction = current_spider_health[0] - both_attack_health[0]
                current_spider_health.pop()
                current_spider_health.append(attack_subtraction)

                spider_attacking_chance = [random.choice(range(1, 6))]

                blue = spider_attacking_chance

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The monster killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif current_spider_health < [1]:
                    print('-----------------------------------')
                    print('Great job! The dart frog is dead. |')
                    print('-----------------------------------')
                    break


                elif blue == [1] or blue == [2] or blue == [3]:
                    spider_attack_sub = self.player_hp[0] - spider_attack[0]
                    self.player_hp.pop()
                    self.player_hp.append(spider_attack_sub)

                    print('--------------------------------------------------------')
                    print('The monster block your attack and did a counter attack! |')
                    print('--------------------------------------------------------')

                    if self.player_hp < [1]:
                        print('-------------------------------------------------------')
                        print('OH NO! The monster killed you! Better luck next time. |')
                        print('-------------------------------------------------------')
                        sys.exit()

                    elif attack_input == 'q':
                        print('Thanks for playing!')
                        print(' ')
                        sys.exit()

                else:
                    print('Tha\'s not a valid answer')
                    print(' ')
                    continue

    def angry_native(self):

        player = Player()

        spider_hp = random.randint(20, 25)
        spider_attack = [random.randint(20, 25)]
        spider_xp = random.randint(10, 15)

        current_spider_health = []
        current_spider_health.append(spider_hp)

        both_attack_health = []
        both_attack_health.append(player.player_attack)

        print('-----------------------------------------------------------------------------------')
        print("You've encountered an angry jungle native. He must be very protective. Health: {} |").format(spider_hp)
        print('-----------------------------------------------------------------------------------')

        while True:
            print(' ')
            print("The angry native has {} HP left before he gives up on you and {} attack points. ").format(current_spider_health[0], spider_attack[0])
            print('Your attack is {} and health is {}.').format(player.player_attack, self.player_hp[0])
            print('=======================================================')
            print(' ')
            attack_input = raw_input('Would you like to [Z]Attack or [X]Run Away ').lower()

            if self.player_hp < [1]:
                print('-------------------------------------------------------')
                print('OH NO! The native killed you! Better luck next time. |')
                print('-------------------------------------------------------')
                sys.exit()

            elif attack_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()

            elif attack_input == 'x':
                ratio_run = [random.choice(range(1, 5))]

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The native killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif ratio_run == [1] or ratio_run == [2] or ratio_run == [3]:
                    print('OH NO! When you were trying to run away, the native caught you.')
                    print(' ')
                    sys.exit()
                else:
                    print('Why did you run away you coward?')
                    print(' ')
                    break

            elif attack_input == 'z':
                attack_subtraction = current_spider_health[0] - both_attack_health[0]
                current_spider_health.pop()
                current_spider_health.append(attack_subtraction)

                spider_attacking_chance = [random.choice(range(1, 6))]

                blue = spider_attacking_chance

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The native killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif current_spider_health < [1]:
                    print('--------------------------------')
                    print('Great job! The native is dead. |')
                    print('--------------------------------')
                    break


                elif blue == [1] or blue == [2] or blue == [3]:
                    spider_attack_sub = self.player_hp[0] - spider_attack[0]
                    self.player_hp.pop()
                    self.player_hp.append(spider_attack_sub)

                    print('--------------------------------------------------------')
                    print('The native block your attack and did a counter attack! |')
                    print('--------------------------------------------------------')

                    if self.player_hp < [1]:
                        print('-------------------------------------------------------')
                        print('OH NO! The native killed you! Better luck next time. |')
                        print('-------------------------------------------------------')
                        sys.exit()

                    elif attack_input == 'q':
                        print('Thanks for playing!')
                        print(' ')
                        sys.exit()

                else:
                    print('Tha\'s not a valid answer')
                    print(' ')
                    continue

    def very_angry_native(self):

        player = Player()

        spider_hp = random.randint(25, 35)
        spider_attack = [random.randint(25, 35)]
        spider_xp = random.randint(13, 20)

        current_spider_health = []
        current_spider_health.append(spider_hp)

        both_attack_health = []
        both_attack_health.append(player.player_attack)

        print('----------------------------------------------------------------------------------------------')
        print("You've encountered a very angry jungle native. He must not like your hair color. Health: {}. |").format(spider_hp)
        print('----------------------------------------------------------------------------------------------')

        while True:
            print(' ')
            print("The very angry native has {} HP left before he gives up on you and {} attack points. ").format(current_spider_health[0], spider_attack[0])
            print('Your attack is {} and health is {}.').format(player.player_attack, self.player_hp[0])
            print('=======================================================')
            print(' ')
            attack_input = raw_input('Would you like to [Z]Attack or [X]Run Away ').lower()

            if self.player_hp < [1]:
                print('-------------------------------------------------------')
                print('OH NO! The native killed you! Better luck next time. |')
                print('-------------------------------------------------------')
                sys.exit()

            elif attack_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()

            elif attack_input == 'x':
                ratio_run = [random.choice(range(1, 5))]

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The native killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif ratio_run == [1] or ratio_run == [2] or ratio_run == [3]:
                    print('OH NO! When you were trying to run away, the native caught you.')
                    print(' ')
                    sys.exit()
                else:
                    print('Why did you run away you coward?')
                    print(' ')
                    break

            elif attack_input == 'z':
                attack_subtraction = current_spider_health[0] - both_attack_health[0]
                current_spider_health.pop()
                current_spider_health.append(attack_subtraction)

                spider_attacking_chance = [random.choice(range(1, 6))]

                blue = spider_attacking_chance

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The native killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif current_spider_health < [1]:
                    print('--------------------------------')
                    print('Great job! The native is dead. |')
                    print('--------------------------------')
                    break


                elif blue == [1] or blue == [2] or blue == [3]:
                    spider_attack_sub = self.player_hp[0] - spider_attack[0]
                    self.player_hp.pop()
                    self.player_hp.append(spider_attack_sub)

                    print('--------------------------------------------------------')
                    print('The native block your attack and did a counter attack! |')
                    print('--------------------------------------------------------')

                    if self.player_hp < [1]:
                        print('-------------------------------------------------------')
                        print('OH NO! The native killed you! Better luck next time. |')
                        print('-------------------------------------------------------')
                        sys.exit()

                    elif attack_input == 'q':
                        print('Thanks for playing!')
                        print(' ')
                        sys.exit()

                else:
                    print('Tha\'s not a valid answer')
                    print(' ')
                    continue

    def enraged_native(self):

        player = Player()

        spider_hp = random.randint(35, 45)
        spider_attack = [random.randint(30, 40)]
        spider_xp = random.randint(18, 25)

        current_spider_health = []
        current_spider_health.append(spider_hp)

        both_attack_health = []
        both_attack_health.append(player.player_attack)

        print('--------------------------------------------------------------------------------------')
        print("You've encountered an enranged jungle native. He must not like your face. Health: {}.|").format(spider_hp)
        print('--------------------------------------------------------------------------------------')

        while True:
            print(' ')
            print("The enranged native has {} HP left before he gives up on you and {} attack points. ").format(current_spider_health[0], spider_attack[0])
            print('Your attack is {} and health is {}.').format(player.player_attack, self.player_hp[0])
            print('=======================================================')
            print(' ')
            attack_input = raw_input('Would you like to [Z]Attack or [X]Run Away ').lower()

            if self.player_hp < [1]:
                print('-------------------------------------------------------')
                print('OH NO! The native killed you! Better luck next time. |')
                print('-------------------------------------------------------')
                sys.exit()

            elif attack_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()

            elif attack_input == 'x':
                ratio_run = [random.choice(range(1, 5))]

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The native killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif ratio_run == [1] or ratio_run == [2] or ratio_run == [3]:
                    print('OH NO! When you were trying to run away, the native caught you.')
                    print(' ')
                    sys.exit()
                else:
                    print('Why did you run away you coward?')
                    print(' ')
                    break

            elif attack_input == 'z':
                attack_subtraction = current_spider_health[0] - both_attack_health[0]
                current_spider_health.pop()
                current_spider_health.append(attack_subtraction)

                spider_attacking_chance = [random.choice(range(1, 6))]

                blue = spider_attacking_chance

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The native killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif current_spider_health < [1]:
                    print('--------------------------------')
                    print('Great job! The native is dead. |')
                    print('--------------------------------')
                    break


                elif blue == [1] or blue == [2] or blue == [3]:
                    spider_attack_sub = self.player_hp[0] - spider_attack[0]
                    self.player_hp.pop()
                    self.player_hp.append(spider_attack_sub)

                    print('--------------------------------------------------------')
                    print('The native block your attack and did a counter attack! |')
                    print('--------------------------------------------------------')

                    if self.player_hp < [1]:
                        print('-------------------------------------------------------')
                        print('OH NO! The native killed you! Better luck next time. |')
                        print('-------------------------------------------------------')
                        sys.exit()

                    elif attack_input == 'q':
                        print('Thanks for playing!')
                        print(' ')
                        sys.exit()

                else:
                    print('Tha\'s not a valid answer')
                    print(' ')
                    continue

    def snake(self):

        player = Player()

        snake_color = ['green', 'brown', 'blue']

        snake_color_choice = random.choice(snake_color)
        spider_hp = random.randint(15, 25)
        spider_attack = [random.randint(1, 10)]
        spider_xp = random.randint(10, 15)

        current_spider_health = []
        current_spider_health.append(spider_hp)

        both_attack_health = []
        both_attack_health.append(player.player_attack)

        print('--------------------------------------------------------------------------------------')
        print("You've encountered a cute little {} jungle snake. It really is adorable. Health: {}. |").format(snake_color_choice, spider_hp)
        print('--------------------------------------------------------------------------------------')

        while True:
            print(' ')
            print("The {} snake has {} HP left and {} attack points. ").format(snake_color_choice, current_spider_health[0], spider_attack[0])
            print('Your attack is {} and health is {}.').format(player.player_attack, self.player_hp[0])
            print('=======================================================')
            print(' ')
            attack_input = raw_input('Would you like to [Z]Attack or [X]Run Away ').lower()

            if self.player_hp < [1]:
                print('-------------------------------------------------------')
                print('OH NO! The snake killed you! Better luck next time. |')
                print('-------------------------------------------------------')
                sys.exit()

            elif attack_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()

            elif attack_input == 'x':
                ratio_run = [random.choice(range(1, 5))]

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The snake killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif ratio_run == [1] or ratio_run == [2] or ratio_run == [3]:
                    print('OH NO! When you were trying to run away, the spider caught you.')
                    print(' ')
                    sys.exit()
                else:
                    print('Why did you run away you coward?')
                    print(' ')
                    break

            elif attack_input == 'z':
                attack_subtraction = current_spider_health[0] - both_attack_health[0]
                current_spider_health.pop()
                current_spider_health.append(attack_subtraction)

                spider_attacking_chance = [random.choice(range(1, 6))]

                blue = spider_attacking_chance

                if self.player_hp < [1]:
                    print('-------------------------------------------------------')
                    print('OH NO! The snake killed you! Better luck next time. |')
                    print('-------------------------------------------------------')
                    sys.exit()

                elif current_spider_health < [1]:
                    print('--------------------------------')
                    print('Great job! The snake is dead. |')
                    print('--------------------------------')
                    break


                elif blue == [1] or blue == [2] or blue == [3]:
                    spider_attack_sub = self.player_hp[0] - spider_attack[0]
                    self.player_hp.pop()
                    self.player_hp.append(spider_attack_sub)

                    print('--------------------------------------------------------')
                    print('The snake block your attack and did a counter attack! |')
                    print('--------------------------------------------------------')

                    if self.player_hp < [1]:
                        print('-------------------------------------------------------')
                        print('OH NO! The snake killed you! Better luck next time. |')
                        print('-------------------------------------------------------')
                        sys.exit()

                    elif attack_input == 'q':
                        print('Thanks for playing!')
                        print(' ')
                        sys.exit()

                else:
                    print('Tha\'s not a valid answer')
                    print(' ')
                    continue
