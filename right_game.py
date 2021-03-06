import random
import sys

from right_monster import Monster
from right_player import Player
from right_weather import WEATHER

monsters = Monster()
the_player = Player()
the_weather = WEATHER()

player_coins = [0]

print ("Welcome to the jungle, {}.").format(the_player.player_name)

if Player.player_gender == 'F':
    print ("You have chosen the {} as your weapon.").format(the_player.female_weapon)
    print ("With your {}, you can do {} damage to oncoming foes.").format(the_player.female_weapon, the_player.player_attack)

elif Player.player_gender == 'M':
    print ("You have chosen the {} as your weapon.").format(the_player.male_weapon)
    print ("With your {}, you can do {} damage to oncoming foes.").format(the_player.male_weapon, the_player.player_attack)

print ("Your beginning health status is {}.").format(monsters.player_hp[0])

print ("You start off with {} coins.").format(the_player.player_xp[0])

def current_user_interface():
    print(' ')
    print('You can move (A)Left, (D)Right, or (W)Forward.')
    print('Health: {}').format(monsters.player_hp[0])
    print('Coins: {}').format(player_coins[0])
    strip_weather = ' '.join(the_weather.weather_pick_list)
    print('Weather: {}'.format(strip_weather))
    print('(Q) for Quit -- (H) for Help')
    print('==============================================================')
    print(' ') #Add new stuff to so what the user is facing. If there's a spider or if he just collected a coin ect.
    global user_input
    user_input = raw_input('Which way do you wish to move? ').lower()

def print_help():
    print(' ')
    print('Hey there {}. You have two goals and it\'s to collect coins and escape the jungle.').format(the_player.player_name)
    print('You might run into monsters so watch out. If you do, you will start a battle.')
    print('To win you need to collect 15 coins. These coins are rare so it\'s not going to be easy. ')

current_user_interface()
player_movement = [0]

while True:
    spider_attack_chance = []
    spider_number = random.choice(range(1, 116))
    spider_attack_chance.append(spider_number)

    coin_chance = []
    coin_number = random.choice(range(1, 3))
    coin_chance.append(coin_number)

    if player_coins == [15]:
        print('-----------------------------------------------------------------------------')
        print('You did it! You collect all 15 coins.                                       |')
        print('And now you can afford to by a plane ticket to get out of that crazy jungle |')
        print('-----------------------------------------------------------------------------')
        sys.exit()

    elif player_movement == [5]:
        player_movement = [0]
        the_weather.pick_weather()
        del the_weather.weather_pick_list[0]

    elif user_input == 'a' or user_input == 'd' or user_input == 'w':
        player_movement[0] += 1
        red = spider_attack_chance

        if coin_chance == [1]:
            player_coins[0] += 1

        elif red == [1] or red == [2] or red == [3] or red == [4] or red == [5] or red == [6] or red == [7] or red == [8] or red == [9] or red == [10]:
            if user_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()
            elif user_input == 'h':
                print_help()
            else:
                monsters.brown_spider()

        elif red == [11] or red == [12] or red == [13] or red == [14] or red == [15] or red == [16] or red == [17]:
            if user_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()
            elif user_input == 'h':
                print_help()
            else:
                monsters.poisonous_spider()

        elif red == [18] or red == [19] or red == [20] or red == [21] or red == [21]:
            if user_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()
            else:
                monsters.black_widow_spider()

        elif red == [22] or red == [23] or red == [24] or red == [57] or red == [58]:
            if user_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()
            elif user_input == 'h':
                print_help()
            else:
                monsters.dart_frog()

        elif red == [25] or red == [26] or red == [27] or red == [28] or red == [29] or red == [30] or red == [31] or red == [32] or red == [33] or red == [34]:
            if user_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()
            elif user_input == 'h':
                print_help()
            else:
                monsters.angry_native()

        elif red == [35] or red == [36] or red == [37] or red == [38] or red == [39] or red == [40] or red == [41]:
            if user_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()
            elif user_input == 'h':
                print_help()
            else:
                monsters.very_angry_native()

        elif red == [42] or red == [43] or red == [44] or red == [45] or red == [46]:
            if user_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()
            else:
                monsters.enraged_native()

        elif red == [47] or red == [48] or red == [49] or red == [50] or red == [51] or red == [52] or red == [53] or red == [54] or red == [55] or red == [56]:
            if user_input == 'q':
                print('Thanks for playing!')
                print(' ')
                sys.exit()
            elif user_input == 'h':
                print_help()
            else:
                monsters.snake()

    elif user_input == 'h':
        print_help()

    elif user_input == 'q':
        print('Thanks for playing!')
        print(' ')
        sys.exit()

    else:
        print('-----------------------------')
        print('That\'s not a valid answer! |')
        print('-----------------------------')
        current_user_interface()
        continue

    current_user_interface()
