import random
import game.py

def rewardNext(gameWin, cards):
    if !gameWin:
        r_val = -1
    else:
        r_val = 1/(22 - (cards + (random.randint(1, 11))))
    return r_val

def rewardStay (gameWin, cards):
    if !gameWin:
        r_val = -1
    else:
        r_val = 1/(22 - cards)
    return r_val

def choose(epsilon, Qnew):
    test = random.randint(1, 100)
    if test < epsilon:
        choice = random.randint(0,1)
        choice = Qnew[choice]
        return choice
    else:
        if Qnew[0] > Qnew[1]:
            choice = Qnew[0]
        else:
            choice = Qnew[1]
        return choice

def Q_algorithm(reward, Qold, cards):
    if cards in Qold.keys:
        qO = Qold[cards]
    else:
        qO = 0
    Qnew[0] = qO + 'learning rate' * (rewardNext + 'discount factor' - qO)
    Qnew[1] = qO + 'learning rate' * (rewardStay + 'discount factor' - qO)
    choice = choose(10, Qnew)
    QOld[cards] = choice

