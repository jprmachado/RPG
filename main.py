from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell ("Fire", 10, 100, "black")
thunder = Spell ("Thunder", 10, 100, "black")
blizzard = Spell ("Blizzard", 10, 100, "black")
quake = Spell ("Quake", 20, 200, "black")
meteor = Spell ("Meteor", 14, 140, "black")

# Create White Magic
cure = Spell ("Cure", 12, 120, "white")
cura = Spell ("Cura", 18, 200, "white")


# Create Items
potion = Item("Potion", "potion", "Heals for 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals for 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals for 500 HP", 500)
elixir = Item("Elixer", "elixer", "Fully restores HP/MP for one party member", 9999)
hielixir = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_items = [{"item": potion,"quantity": 15}, {"item": hipotion,"quantity": 5},
                {"item": superpotion,"quantity": 5},{"item": elixir,"quantity": 5},
                {"item": hielixir,"quantity": 5}, {"item": grenade,"quantity": 5}]

player_spells = [fire, thunder, blizzard, quake, meteor, cure, cura]

#Instantiate People
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!!!" + bcolors.ENDC)

while running:
    print("=======================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for ", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int (input("Choose magic : ")) -1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        cost = spell.cost

        current_mp = player.get_mp()
        if spell.cost > current_mp:
            print(bcolors.FAIL+"\n Not enough MP"+ bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(spell.dmg) + " points of damage " + bcolors.ENDC)

    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item:")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for" + str(item.prop) + "HP" + bcolors.ENDC)
        elif item.type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " deals " + str(item.prop) + " points of damage " + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked for ", enemy_dmg )

    print("----------------------------")
    print("Enemy HP:"+bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your HP:"+bcolors.OKGREEN + str(player.get_hp())+"/"+str(player.get_max_hp())+ bcolors.ENDC+ "\n")
    print("Your MP:" + bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win"+ bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.WARNING + "Your has defeated you!" + bcolors.ENDC)
        running = False

