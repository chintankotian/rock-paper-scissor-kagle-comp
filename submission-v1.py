import numpy as np

# Code  symbol
# 0 	Rock
# 1 	Paper
# 2 	Scissors
step_size = 0.99
randomness = 0.3
qTable = np.random.normal(size = (3,3)) # rock,paper,scissor

last_action = 0
last_reward = 0
last_state = 0

def qTableUpdate():
    qTable[last_state][last_action] += step_size * (last_reward - qTable[last_state][last_action])


def getAction(state):
    logits = qTable[state]/qTable[state].sum()
    return np.argmax(logits)
    


def agent(observation, configuration):

    if observation.step > 0:
        last_state = observation.lastOpponentAction
        last_reward = observation.reward
        qTableUpdate()

        last_action = getAction(last_state)
    else:
        last_action = np.random.randint(3) 
    return int(last_action)
    
