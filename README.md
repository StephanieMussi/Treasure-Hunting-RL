# Treasure_Hunting_RL
This project aims to perform treasure hunting in a 3x3x3 grid-world-based environment using Reinforcement Learning.  

## Introduction  
The 3D grid world is shown below:  
<img src = "https://github.com/StephanieMussi/Treasure_Hunting_RL/blob/main/Figures/world.png" width = 300 height = 225>  

As it can be seen, there are 64 states in total, in which (0, 0, 0) is the start state, and (3, 3, 3) is the goal state:  
(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 3),  
(0, 2, 0), (0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 3, 0), (0, 3, 1), (0, 3, 2), (0, 3, 3),  
(1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 0, 3), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 1, 3),  
(1, 2, 0), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 3, 0), (1, 3, 1), (1, 3, 2), (1, 3, 3),  
(2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 0, 3), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 1, 3),  
(2, 2, 0), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 0), (2, 3, 1), (2, 3, 2), (2, 3, 3),  
(3, 0, 0), (3, 0, 1), (3, 0, 2), (3, 0, 3), (3, 1, 0), (3, 1, 1), (3, 1, 2), (3, 1, 3),  
(3, 2, 0), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 3, 0), (3, 3, 1), (3, 3, 2), (3, 3, 3).  

There are 6 actions in the action space, and the meaning of each action is as below:  
|Forward| Backward| Left| Right| Up| Down|
|:-:|:-:|:-:|:-:|:-:|:-:|
|x+1|x-1|y+1|y-1|z+1|z-1|  
  

The agent will take the intended action with a probability of 0.6. Besides, the agent will move in the direction perpendicular to the intended direction with a probability of 0.1 each, as shown below:  
<img src = "https://github.com/StephanieMussi/Treasure_Hunting_RL/blob/main/Figures/trans.png" width = 237 height = 206>  

The agent will receive a reward when arriving at a state. A reward of 1 will be given to the agent only when it reaches the terminal state (3, 3, 3). When arriving at any other state, the agent will receive a reward of -0.1.  

The setting of the world can be found in ["environment.py"](https://github.com/StephanieMussi/Treasure_Hunting_RL/blob/main/environment.py).  


## Method
The __Q-Learning Algorithm__ is used. For the choice of action at each step, the Epsilon-Greedy Policy is applied. This means that with a probability of (1 – ε), the action with highest Q-value is chosen, and with probability ε, a random action is chosen from the action space.  

* Initially, the Q-value for all (s, a) pair is set as 0.
* Then, for each step, the trajectory (s, a, s', r) is obtained, and it is used to update the Q-value with the following formula:  
    Qnew(s, a)  = Qold(s, a) + α(r + γmaxAQold(s', A)  - Qold(s, a))
* For each episode, the total reward is counted. 
* Finally, after iterating for a predefined number of episodes, the final Q-table is obtained, and the optimistic action for each state can be chosen. The graph of episode reward vs. episode number is plotted to visualize the process of Q-Learning.

## Experiment Results
