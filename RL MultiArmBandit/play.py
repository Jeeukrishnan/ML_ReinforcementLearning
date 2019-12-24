import numpy as np
import random
from environment import Environment
from agents import RandomAgent
from agents import ValueApproxAgent

#casino will have 5 arms
env=Environment(5)
agent=RandomAgent(env.action_space)

total_rewards=0



agent = ValueApproxAgent(env.action_space)  

total_rewards=0

for i in range(1000):
    action=agent.choose_action() 
    reward=env.try_arm(action)
    print (action)
    agent.learn(action,reward)
    total_rewards +=reward
    
print(total_rewards)  