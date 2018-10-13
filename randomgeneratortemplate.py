from random import randint, choice

listname = ['get', 'the', 'heck']
dictname = { 
            'item1': 'this is item 1',
            'item2': 'this is item 2',
            'item3': 'this is item 3',
            }

def pull_randomd():
    result1, result2 = choice(list(dictname.items()))
    print('\n' + result1 + ': ' + result2 + '\n')


def pull_randoml():
    result = randint(0, len(listname))
    result = int(result)
    print('\n' + listname[result - 1] + '\n')

while True:
    doit = input('Would you like to pick a random item? (y/n)\n>')
    if doit.lower() == 'y':
        pull_randomd()
        continue
    elif doit.lower() == 'n':
        break
    elif doit.lower() == 'fuck off':
        print('Rude!')
        continue
    else:
        print('Excuse me?')
        continue

