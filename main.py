import uuid
from datetime import datetime
import json

# Database
donors = {'name': 'bob', 'name': 'jane'}
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
    print('hi')


print(json.dumps(donations, indent=4))
