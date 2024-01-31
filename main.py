import uuid
from datetime import datetime
import json

# Database
donors = {'bob', 'jane'}
donations = {str(uuid.uuid4()): {'name': 'bob', 'type': 'money', 'amount': 10,
                                 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
             str(uuid.uuid4()): {'name': 'jane', 'type': 'money', 'amount': 5,
                                 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
             str(uuid.uuid4()): {'name': 'bob', 'type': 'clothes', 'amount': 2,
                                 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
             str(uuid.uuid4()): {'name': 'bob', 'type': 'money', 'amount': 20,
                                 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}
distribution = {str(uuid.uuid4()): {'type': 'clothes', 'amount': 1,
                                    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}
inventory = {'money': 35, 'clothes': 1, 'food': 0}

# Database API


def donate(name, type, amount):
    # add donor if they don't exist
    if name not in donors:
        donors.add(name)
    # add record to donations table
    donations[str(uuid.uuid4())] = {'name': name, 'type': type, 'amount': amount,
                                    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    # update inventory
    if type in inventory:
        inventory[type] += amount
    else:
        inventory[type] = amount

    return True


def distribute(type, amount):
    # check if type exists in inventory
    if type not in inventory:
        return False
    # check if enough amount of type exists to distribute
    if inventory[type] < amount:
        return False
    # update inventory
    inventory[type] -= amount

    return True


# Test

# print('DONORS\n', donors)
# print('DONATIONS\n', json.dumps(donations, indent=4))
# print('DISTRIBUTIONS\n', json.dumps(distribution, indent=4))
# print('INVENTORY\n', json.dumps(inventory, indent=4))

# donate('Alice', 'money', 35)
# distribute('money', 10)

# print('DONORS\n', donors)
# print('DONATIONS\n', json.dumps(donations, indent=4))
# print('DISTRIBUTIONS\n', json.dumps(distribution, indent=4))
# print('INVENTORY\n', json.dumps(inventory, indent=4))
