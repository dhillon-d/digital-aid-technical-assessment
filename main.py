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


def generate_inventory_report():
    return inventory


def generate_donator_report():
    response = {}
    for name in donors:
        personal_donations = {key: value for key, value in donations.items() if value['name'] == name}
        personal_donation_amount_by_type = {type_: sum(entry['amount'] for entry in personal_donations.values() if entry['type'] == type_)
                                            for type_ in set(entry['type'] for entry in personal_donations.values())}
        response[name] = personal_donation_amount_by_type
    return response


# Test

generated_inventory_report = generate_inventory_report()
generated_donator_report = generate_donator_report()

print('DONORS\n', donors)
print('DONATIONS\n', json.dumps(donations, indent=4))
print('DISTRIBUTIONS\n', json.dumps(distribution, indent=4))
print('INVENTORY REPORT\n', json.dumps(generate_inventory_report(), indent=4))
print('DONATOR REPORT\n', json.dumps(generate_donator_report(), indent=4))

print('-----------------------------------------------------------------')


donate('Alice', 'money', 35)
distribute('money', 10)
generated_inventory_report = generate_inventory_report()
generated_donator_report = generate_donator_report()

print('DONORS\n', donors)
print('DONATIONS\n', json.dumps(donations, indent=4))
print('DISTRIBUTIONS\n', json.dumps(distribution, indent=4))
print('INVENTORY REPORT\n', json.dumps(generate_inventory_report(), indent=4))
print('DONATOR REPORT\n', json.dumps(generate_donator_report(), indent=4))
