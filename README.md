## How To Run

- You can either run code in online interpreter or run locally on your machine
  - Online: https://www.online-python.com/
    - Paste code from `main.py` into interpreter and click `run`
  - Locally: https://github.com/pyenv/pyenv
    - Tested on python version 3.8 and up
    - Clone code from repo and run the command `python main.py`

## Design

### Decisions

- Write a command line application because it is quick to write without having to worry about UI
- Only using builtin libraries in Python because I don't have to worry about downloading dependencies, also easier for the end user to run application

### Further Improvements (least to most time)

- Input validation
- type checking
- use an actual relational database
- UI/View

### Data Model

_Donors_
| name |
|------|
_Donations_
| id | name | type | amount | date |
|----|------|------|--------|------|
_Distributions_
| id | type | amount | date |
|----|------|--------|------|
_Inventory_
| type | amount |
|------|--------|
