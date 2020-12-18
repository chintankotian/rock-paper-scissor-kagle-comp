from kaggle_environments import evaluate, make, utils
env = make("rps", debug=True)
import numpy

def agent(observation, configuration):
    if observation.step > 0:
        return observation.lastOpponentAction
    else:
        return 0

env.reset()
# Play as the first agent against default "random" agent.
data = env.run([ 'submission-v2.py', 'submission-v1.py'])
print(data[-1])
# env.render(mode="ansi", width=500, height=450)

