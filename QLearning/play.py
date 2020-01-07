import gym
from Agents import QAgent
import numpy as np
from crawler_env import CrawlingRobotEnv

##Todo: Build a robot that can learn to crawl 
env=CrawlingRobotEnv(render=True)
agent=QAgent(env,gamma=0.9)
current_state=env.reset()
total_rewards=0
i=0
while i<90000:
    ##step 1:take an action
    action=agent.choose_action(current_state)
      ##perform the action in the environment
    next_state,reward,done,info=env.step(action) 
    current_state=next_state
    total_rewards +=reward
    
    ##step 2:learn from experience
    agent.learn(current_state,action,reward,next_state)
    
    if i%5000==0:  #evaluation
        print("Average reward in last 5000 steps :",total_rewards/i)
        if total_rewards/i>1.3:
            break
        
        
env=CrawlingRobotEnv(render=True)
current_state=env.reset()
total_rewards=0
agent.eps=0
i=0
while i<90000:
    ##step 1:take an action
    action=agent.choose_action(current_state)
      ##perform the action in the environment
    next_state,reward,done,info=env.step(action) 
    current_state=next_state
    total_rewards +=reward
    
    ##step 2:learn from experience
    agent.learn(current_state,action,reward,next_state)
    
    if i%5000==0:  #evaluation
        print("Average reward in last 5000 steps :",total_rewards/i)
        if total_rewards/i>1.3:
            break