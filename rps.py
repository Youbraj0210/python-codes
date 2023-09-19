import random



outcomes = [['D','W','L'],
            ['L','D','W'],
            ['W','L','D']]


play = True
while(play):
    want_to_play = int(input("Do you want to play Rock, papers, sicsros if yes enter 1 if no enter 0: "))
    if want_to_play==1:
        play=True
    else:
        play=False
        print("the game has ended")
        break
    comp = random.randint(0,2)
    player = int(input("Enter 0 for rock 1 for paper and 2 for Sicsor: "))

    choice = ''
    if comp == 0:
        choice = "Rock"
    elif comp == 1:
        choice = "Paper"
    else:
        choice = "Sicsor"

    if outcomes[comp][player] == 'D':
        print(f'computer chose {choice} and you had a Draw')
    elif outcomes[comp][player] == 'W':
        print(f'computer chose {choice} and you had a Win')
    else:
        print(f'computer chose {choice} and you had a Loss')

