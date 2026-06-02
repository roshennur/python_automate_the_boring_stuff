inventory = {'rope':1, 'gold coin':42}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    total = 0
    for i,v in inventory.items():
        print(str(v) + ' ' +str(i))
        total += v
    print('Total number of items: ' + str(total))



def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory


