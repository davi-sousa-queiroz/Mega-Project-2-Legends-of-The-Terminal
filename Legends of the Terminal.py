# ---------------------- I M P O R T S -------------------------
import random
import time
# ---------------  G A M E   V A R I A B L E S  -----------------
game_title = 'LEGENDS OF THE TERMINAL'
player = {"name": "Hero1234",
          'HP': 100,
          'ATK': 10,
          'Aether': 0,
          'MAX_HP': 100}
inventory = {
             'slime balls': 0,
             'green crystals': 0,
             'ancient bones': 0,
             'venom bottles': 0,
             'shiny silks': 0,
             'magic teeth': 0,
             'ancient coins': 0,
             'gold bars': 0,
             'royal vests': 0,
             'royal robes': 0,
             'katanas': 0,
             'legendary katanas': 0,
             'Sacred pistols': 0,
             'dragons breath': 0,
             'toy cars': 0,
             'wooden swords': 0,
             'fashionable clothes': 0,
             'chests': 0,
             'diamonds': 0,
             'crowns': 0,
             'golden necklaces': 0,
             'royal armor': 0,
             'ancient relics': 0,
             'dragon eggs': 0,
             'phoenix feather': 0,
             'ancient crown of kings': 0,
             'dragon hearts': 0,
             'celestial crystals': 0
}
enemies = [
    {'name': 'slime', "HP": 30, "ATK": 5,},
    {'name': 'goblin', "HP": 40, "ATK": 7},
    {'name': 'skeleton', "HP": 50, "ATK": 10},
    {'name': 'snake', "HP": 60, "ATK": 12},
    {'name': 'spider', "HP": 70, "ATK": 15},
    {'name': 'bear', "HP": 80, "ATK": 20},
    {'name': 'bandit', "HP": 90, "ATK": 30},
    {'name': 'bandit leader', "HP": 100, "ATK": 40},
    {'name': 'soldier', "HP": 110, "ATK": 50},
    {'name': 'soldier leader', "HP": 120, "ATK": 60},]
bosses = [
    {'name': 'samurai', "HP": 300, "ATK": 25},
    {'name': 'samurai leader', "HP": 500, "ATK": 30},
    {'name': 'sherif', "HP": 750, "ATK": 50},
    {'name': 'Aroura The Dragon 🐉', "HP": 1000, "ATK": 100}
]
materials = ['slime balls',
             'green crystals',
             'ancient bones',
             'venom bottles',
             'shiny silks',
             'magic teeth',
             'ancient coins',
             'gold bars',
             'royal vests',
             'royal robes',
             'katanas',
             'legendary katanas',
             'Sacred pistols',
             'dragons breath']
items = ['toy cars',
         'wooden swords',
         'fashionable clothes',
         'chests',
         'diamonds',
         'crowns',
         'golden necklaces',
         'royal armor',
         'ancient relics',
         'dragon eggs',
         'phoenix feather',
         'ancient crown of kings',
         'dragon hearts',
         'celestial crystals']
characters = {
    "Knight": {"HP": 120, "ATK": 15},
    "Mage": {"HP": 50, "ATK": 30},
    "Archer": {"HP": 25, "ATK": 60},
}
main_menu = ["1. Explore 🗺️",
             "2. Fight Boss 🐉⚔️",
             "3. Inventory 🎒",
             '4. Upgrade ⬆️',
             "5. Shop 💰",
             "6. Sell 🤑",
             '7. Rest 😴',
             '8. Show Stats 📊',
             '9. (coming soon)',
             '10. Drop item 🫳',
             'q. Quit 💨']
item_prices = {
    'toy cars' : 5,
    'wooden swords' : 20,
    'fashionable clothes' : 50,
    'chests' : 100,
    'diamonds' : 500,
    'crowns' : 1000,
    'golden necklaces' : 2500,
    'royal armor' : 5000,
    'ancient relics' : 10000,
    'dragon eggs': 25000,
    'phoenix feather' : 50000,
    'dragon hearts' : 100000,
    'celestial crystals' : 1000000
}
item_rarity = {
    'toy cars' : 'Common',
    'wooden swords' : 'Common',
    'fashionable clothes' : 'Common',
    'chests' : 'Uncommon',
    'diamonds' : 'Uncommon',
    'crowns' : 'Uncommon',
    'golden necklaces' : 'Rare',
    'royal armor' : 'Rare',
    'ancient relics' : 'Rare',
    'dragon eggs' : 'Epic',
    'phoenix feather' : 'Epic',
    'dragon hearts' : 'Legendary',
    'celestial crystals' : 'Legendary',
}
# --------------------- F U N C T I O N S ------------------------
# ---- INTRO AND MENU SYSTEM ------
def welcome():
    print('=======================')
    print(game_title)
    print('=======================')
    time.sleep(2)
    print('')
    print('Welcome, adventurer.')
    time.sleep(2)
    print('')
    print('The world is filled with dangerous creatures,')
    print('ancient treasures, and powerful relics waiting')
    print('to be discovered.')
    time.sleep(6.5)
    print('')
    print('Explore the land, defeat enemies,')
    print('collect materials, and grow stronger.')
    time.sleep(4.5)
    print('')
    print('Survive the world, master the battle.')
    time.sleep(2)
    print('')
def hero_name():
    name =  input('What is your name adventurer? : ').capitalize()
    player['name'] = name
    time.sleep(0.5)
    print('')
    print(f"Welcome to the terminal {name} the great.")
    time.sleep(2)
    print('')
    print('Do you have what it takes to become a Legend of The Terminal?')
    time.sleep(2)
    print('')
    print('Let\'s find out.')
    time.sleep(2)
    print('')
def menu():
    global main_menu
    for option in main_menu:
        print(option)
        print('')
# ------ EXPLORATION SYSTEM --------
def explore():
    print("\nYou explore the land...")
    time.sleep(1)

    event = random.randint(1,3)

    if event == 1:
        enemy_encounter()

    elif event == 2:
        find_treasure()

    elif event == 3:
        print('Nothing happened.')
# ------------ COMBAT --------------
def enemy_encounter():
    enemy = random.choice(enemies)
    print(f"\nA {enemy['name']}appeared!!")
    combat(enemy)
def fight_boss():
    global player
    boss = random.choice(bosses)

    print(f"\n⚔️ A boss appears: {boss['name']}!")
    print(f'Prepare yourself {player["name"]}')

    combat(boss)
def combat(enemy):
    enemy_hp = enemy["HP"]
    while enemy_hp>0 and player['HP']>0:
        print(f"\n{enemy['name']} HP: {enemy_hp}")
        print(f"{player['name']} HP: {player['HP']}")
        action = input("Attack or Run?  ").lower()

        if action == 'attack':
            enemy_hp-=player['ATK']
            print(f"You hit the {enemy['name']}!")
            if enemy_hp<0:
                print(f"You defeated the {enemy['name']}!")
                reward = random.randint(5,15)
                player['Aether']+=reward
                print(f"You gained {reward} Aether.")
                return
        elif action == 'run':
            print("You escaped!")
            return
# --------- TREASURE SYSTEM ----------
def find_treasure():
    item = random.choice(items)
    rarity = item_rarity.get(item, "common")
    inventory[item] +=1
    print("\n✨ You found treasure!")
    print(f'{rarity} item discovered: {item}!! ')
# ----------- UPGRADES -------------
def upgrade_characters():
    print("\n=== UPGRADE MENU ===")
    print("1. Increase ATK (+5) - cost: 50 Aether")
    print("2. Increase MAX HP (+10) - Cost: 50 Aether")
    choice = input(">  ")
    if player['Aether']<50:
        print("You don't have enough Aether.")
        return
    if choice == '1':
        player['ATK']+=5
        player["Aether"]-=50
        print("Attack increased by 50!")
    elif choice == '2':
        player["MAX_HP"] +=10
        player["Aether"]-=50
        print("Max HP increased by 10!")
    else:
        print("invalid upgrade.")
# ------ INVENTORY AND STATS -------
def show_stats():
    for stat, value in player.items():
        print(f'{stat}: {value}')
def show_inventory():
    print("======INVENTORY======")

    empty = True

    for item, amount in inventory.items():
        if amount > 0:
            print(f"{item} : {amount}")
            empty = False
        if empty:
            print("Your inventory is empty.")
def heal(amount):
    player['HP'] = min(player['HP'] + amount, player["MAX_HP"])
# --------- SHOP AND SELL ----------
def shop():
    print('\n=== SHOP ===')
    for item, price in item_prices.items():
        print(f'{item} - {price} Aether')

    choice = input("\nWhat do you want to buy?  ").lower()
    if choice in item_prices[choice]:
        price = item_prices[choice]
        if player['Aether']>=price:
            player['Aether']-=price
            inventory[choice] += 1

            print(f'You bought {choice}!')

        else:
            print('Not enough Aether!')
    else:
        print('That item is not in the shop!')
def sell():
    pass
# ------------ ACTIONS -------------
def drop_item():
    available_items = []

    for item, amount in inventory.items():
        if amount > 0:
            print(f'{item}: {amount}')
            available_items.append(item)

    if not available_items:
        print('You have nothing to drop adventurer.')
        return

    item_choice = input('What do you want to get rif of? ').lower()

    if item_choice in inventory and inventory[item_choice] > 0:
        inventory[item_choice] -= 1
        print(f'You dropped one "{item_choice}."')
    else:
        print("You don't have that item adventurer.")
def rest():
    print(f'Sweet dreams {player["name"]}.')
    time.sleep(2)
    print('')
    print('Health + 2')
    heal(2)
def quit_game():
    print('')
    print('Goodbye adventurer.')
    time.sleep(1)
    print('')
def game_over():
    global player, inventory
    print('GAME OVER!')
    time.sleep(1)
    print('')
    for keys, value in player.items():
        print(f'{keys}: {value}')
# ---------------------------   L E G E N D S   O F   T H E   T E R M I N A L   ---------------------------------
def main():
        welcome()
        hero_name()
        while True:
            menu()
            choice = input(f'Whats your next move, {player["name"]}? >')
            if choice == '1':
                explore()
            elif choice == '2':
                fight_boss()
            elif choice == '3':
                show_inventory()
            elif choice == '4':
                upgrade_characters()
            elif choice == '5':
                shop()
            elif choice == '6':
                sell()
            elif choice == '7':
                rest()
            elif choice == '8':
                show_stats()
            elif choice == '9':
                continue
            elif choice == '10':
                drop_item()
            elif choice == 'q':
                quit_game()
                game_over()
                break
            else:
                print('That\'s not in the menu adventurer.')
if __name__ == '__main__':
    main()