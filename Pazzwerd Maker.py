
import random 
import string 
print("Welcome to ze pazzwerd pickor")



while True:
    adjectives = ['happy', 'sad', 'sleepy', 'lazy', 'useless', 'slow', 'fast', 'handsome', 'sussy', 'gay', 'epok', 'purple', 'orange', 'green', 'red', 'yellow', 'blue', 'white', 'black', 'grey', 'brave', 'stupid', 'smart',]
    nouns = ['Bastard', 'Dinosoar', 'Human', 'Dragon', 'Gamer', 'Toaster', 'Python', 'Coder', 'DrugDealer', 'Gun', 'Airsofter', 'PowerTool', 'AttackHeli', 'Furry']
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0,100)
    special_char = random.choice(string.punctuation)
    pazzwerd = adjective + noun + str(number) + special_char
    print('Your new randomly generated pazzwerd is... %s' % pazzwerd)

    response = input('Another Pazzwerd? Press Enter for another and n for no more:  ')
    if response == 'n':
        break