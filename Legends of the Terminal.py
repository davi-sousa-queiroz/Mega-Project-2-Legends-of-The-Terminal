# ---------------------- I M P O R T S -------------------------
import random
import time
# ---------------  G A M E   V A R I A B L E S  -----------------
game_title = 'LEGENDS OF THE TERMINAL'
player = {"name": "Hero1234",
          'HP': 100,
          'ATK': 10,
          'Aether': 0}
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
    {'name': 'soldier leader', "HP": 120, "ATK": 60},
    {'name': 'samurai', "HP": 300, "ATK": 25},
    {'name': 'samurai leader', "HP": 500, "ATK": 30},
    {'name': 'sherif', "HP": 750, "ATK": 50},
    {'name': 'Aroura The Dragon 🐉', "HP": 1000, "ATK": 100}]
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
             '9. Use Item 🫴',
             '10. Drop item 🫳',
             'q. Quit 💨']
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
# ------ EXPLORATION SYSTEM --------
def explore():
    pass
# ------------ COMBAT --------------
def enemy_encounter():
    pass
def fight_boss():
    pass
# ------------ ENEMIES -------------
def slime():
    pass
def goblin():
    pass
def skeleton():
    pass
def snake():
    pass
def spider():
    pass
def bear():
    pass
def bandit():
    pass
def bandit_leader():
    pass
def soldier():
    pass
def soldier_leader():
    pass
# Bosses
def samurai():
    pass
def samurai_leader():
    pass
def sherif():
    pass
def aroura_the_dragon():
    pass
# --------- TREASURE SYSTEM ----------
def find_treasure():
    pass
def toy_cars():
    pass
def wooden_swords():
    pass
def fashionable_clothes():
    pass
def chests():
    pass
def diamonds():
    pass
def crowns():
    pass
def golden_necklaces():
    pass
def royal_armor():
    pass
def ancient_relics():
    pass
def dragon_eggs():
    pass
def phoenix_feather():
    pass
def ancient_crowns():
    pass
def dragon_hearts():
    pass
def celestial_crystals():
    pass
# ----------- UPGRADES -------------
def upgrade_characters():
    pass
# ------ INVENTORY AND STATS -------
def show_stats():
    pass
def show_inventory():
    pass
# --------- SHOP AND SELL ----------
def shop():
    pass
def sell():
    pass
# ------------ ACTIONS -------------
def use_item():
    pass
def drop_item():
    pass
def rest():
    pass
def quit_game():
    pass
# ---------------------------   L E G E N D S   O F   T H E   T E R M I N A L   ---------------------------------
def main():
    pass
if __name__ == '__main__':
    main()