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
After iterating for 500 episodes with maximum 500 steps each, the final Q-table is shown as below:
| |Forward	|Backward	|Left	|Right	|Up	|Down|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|(0, 0, 0)	|-0.1|	-0.1|	-0.1|	-0.1	|-0.1|	-0.1|
|(0, 0, 1)	|-0.1	|-0.1|	-0.1|	-0.1|	-0.1|	-0.1|
|(0, 0, 2)	|-0.09935|	__-0.05102__|	-0.1|	-0.08214|	-0.09997|	-0.1|
|(0, 0, 3)	|-0.09488|	-0.08872|	-0.1	|__-0.06034__|	-0.1|	-0.09955|
|(0, 1, 0)	|-0.1|	-0.1|	-0.1	|__-0.09590__|	-0.1	|-0.1|
|(0, 1, 1)	|-0.07660	|-0.04360|	-0.09939|	__-0.01872__|	-0.09271|	-0.09754|
|(0, 1, 2)	|__-0.00178__|	-0.04503|	-0.09843	|-0.07037|	-0.08787|	-0.09999|
|(0, 1, 3)	|-0.04703|	-0.09453	|-0.09230|	__-0.03082__|	-0.09817	|-0.06290|
|(0, 2, 0)	|__0.01515__	|-0.09998	|-0.1|	-0.09916|	-0.02125|	-0.1|
|(0, 2, 1)	|-0.04388	|-0.09358	|-0.06127|	__-0.02371__|	-0.06762|	-0.09902|
|(0, 2, 2)	|-0.06350	|-0.09998	|-0.01263	|-0.00171	|__0.10398__	|-0.09961||
|(0, 2, 3)	|-0.06738|	-0.09995|	-0.07476|	__0.26624__|	-0.09844|	-0.07519|
|(0, 3, 0)	|-0.09831	|-0.09659	|-0.1	|__-0.09122__	|-0.09367	|-0.1|
|(0, 3, 1)	|-0.01517	|-0.09796|	-0.00490	|-0.09759|	__0.01328__	|-0.09999|
|(0, 3, 2)	|__0.33853__	|-0.09688	|-0.09375	|-0.01708	|-0.05050	|-0.09375|
|(0, 3, 3)	|__0.52999__|	-0.09961|	-0.09980|	-0.09604|	-0.07500|	-0.07500|
|(1, 0, 0)	|__-0.09998__|	-0.1|	-0.1	|-0.1	|-0.1	|-0.1|
|(1, 0, 1)	|__-0.07980__|	-0.1	|-0.1|	-0.08657|	-0.09998	|-0.09283|
|(1, 0, 2)	|-0.01957	|-0.09994	|-0.09978	|__0.07132__	|-0.05704	|-0.1|
|(1, 0, 3)	|-0.00330|	-0.09980|	-0.09667|	-0.03248|	__0.15711__|	-0.08728|
|(1, 1, 0)	|-0.06886	|-0.09235|	-0.1	|-0.06977	|__-0.06224__|	-0.07360|
|(1, 1, 1)	|-0.06602	|-0.09997	|-0.06543	|__0.08740__	|-0.00843|	-0.09998|
|(1, 1, 2)	|-0.05423	|-0.09012	|-0.09990	|-0.02979	|__0.21069__	|-0.06474|
|(1, 1, 3)	|-0.08123	|-0.02045	|-0.00257|	__0.51067__	|-0.03019	|-0.09459|
|(1, 2, 0)	|__0.01162__	|-0.00664	|-0.1	|-0.03187	|-0.04376|	-0.1|
|(1, 2, 1)	|-0.09557|	-0.09980|	-0.07313|	__0.13636__	|-0.05978|	-0.1|
|(1, 2, 2)	|__0.16391__	|-0.08750|	-0.00320	|-0.09980|	-0.00860|	-0.05000|
|(1, 2, 3)	|-0.08750|	-0.09688	|0|	__0.61297__	|-0.09375|	-0.09375|
|(1, 3, 0)	|-0.07512	|-0.7060|	-0.1	|-0.1|	-0.07368	|__0.07942__|
|(1, 3, 1)	|-0.01080|	-0.09961|	-0.03369|	-0.09844|	__0.29597__	|-0.09980|
|(1, 3, 2)	|-0.07440	|-0.09688	|0.04892	|-0.06511	|__0.33202__	|-0.01015|
|(1, 3, 3)	|__0.69237__	|-0.08108	|-0.05000	|-0.07500|	-0.07500|	0|
|(2, 0, 0)	|-0.1	|-0.08968	|-0.1	|-0.09828|	__-0.07558__|	-0.09995|
|(2, 0, 1)	|-0.09071|	-0.09911	|-0.09540|	__-0.00629__|	-0.02587|	-0.09944|
|(2, 0, 2)	|__0.10817__	|-0.09688	|-0.03688	|-0.09844|	-0.03409	|-0.09156|
|(2, 0, 3)	|-0.07500|	-0.09922|	-0.09375|	-0.03439|	-0.09375	|__0.06103__|
|(2, 1, 0)	|-0.1	|-0.09884	|-0.1	|__-0.04193__	|-0.06294	|-0.1|
|(2, 1, 1)	|-0.01939|	-0.09998|	-0.1	|__0.11316__	|-0.06187|	-0.08458|
|(2, 1, 2)	|-0.04187	|-0.09980	|-0.04987	|0.10081	|__0.24139__	|-0.09844|
|(2, 1, 3)	|-0.02471|	-0.07500|	-0.06883|	__0.50413__|	-0.08750|	-0.07500|
|(2, 2, 0)	|-0.1	|-0.09995	|-0.08245	|__0.08422__	|-0.06044	|-0.1|
|(2, 2, 1)	|-0.09283|	-0.04381|	-0.09844|	__0.28136__	|-0.07666|	-0.09688|
|(2, 2, 2)	|-0.09375	|0	|-0.09688	|-0.05000	|__0.40165__	|-0.09844|
|(2, 2, 3)	|__0.73853__|	-0.07500	|-0.04420	|0.22168|	-0.07500|	0|
|(2, 3, 0)	|-0.09990	|-0.09594	|-0.09375|	-0.09844	|__0.33802__	|-0.09980|
|(2, 3, 1)	|-0.09375|	-0.08676|	0.02677|	-0.03762|	__0.42496__	|-0.08675|
|(2, 3, 2)	|-0.02420	|-0.09375	|-0.04845	|-0.09375|	__0.69758__|	-0.09315|
|(2, 3, 3)	|__0.93637__	|0.13046	|0	|0.56149	|0.50040|	0.25901|
|(3, 0, 0)	|-0.1	|-0.1	|-0.1	|__-0.09145__	|-0.09796	|-0.1|
|(3, 0, 1)|	-0.09998	|-0.09185|	-0.05225	|-0.07914|	__0.14941__|	-0.09980||
|(3, 0, 2)	|__0.05728__	|-0.09844	|-0.07500	|0.27001|	-0.03440|	-0.09375|
|(3, 0, 3)	|-0.07500|	-0.07500	|-0.05000|	__0.54915__|	-0.09375	|-0.08750|
|(3, 1, 0)	|-0.05730	|-0.1	|-0.07273	|-0.02962|	__0.06120__	|-0.1|
|(3, 1, 1)|	-0.09961|	-0.02047	|-0.05660	|__0.31722__|	-0.02972|	-0.09998|
|(3, 1, 2)	|-0.06964	|0.16478	|-0.09375	|-0.02220	|__0.44389__	|-0.05000|
|(3, 1, 3)	|0	|-0.08750	|-0.07500	|__0.68194__	|0.21230	|0.23966|
|(3, 2, 0)	|-0.09875	|-0.09995|	-0.07096|	-0.09844|	__0.09362__	|-0.09922|
|(3, 2, 1)	|-0.02140	|-0.09998	|-0.09752|	__0.57819__	|-0.06018	|-0.09844|
|(3, 2, 2)	|-0.01391|	0.15039|	-0.01391|	-0.05000	|__0.57525__|	-0.09688|
|(3, 2, 3)	|-0.09375	|0.34218|	-0.07500	|__0.88675__	|0.49100	|-0.09375|
|(3, 3, 0)	|-0.09990	|-0.05632|	__0.02246__	|-0.09688|	-0.04139|	-0.03911|
|(3, 3, 1)	|-0.05000|	0.20288	|-0.07982	|-0.08750|	__0.65123__	|-0.09375|
|(3, 3, 2)|	-0.07510	|-0.04988	|-0.06211|	-0.08750	|__0.89534__	|-0.07500|  
  
Therefore, any action can be chosen at these states and there is no single best action.

|(0, 0, 0)	|(any)	|(0, 0, 1)	|(any)	|(0, 0, 2)|	Backward|	(0, 0, 3)	|Right|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|(0, 1, 0)	|Right|	(0, 1, 1)	|Right	|(0, 1, 2)|	Forward|	(0, 1, 3)	|Right|
|(0, 2, 0)	|Forward	|(0, 2, 1)	|Right|	(0, 2, 2)|	Up	|(0, 2, 3)|	Right|
|(0, 3, 0)	|Right	|(0, 3, 1)|	Up	|(0, 3, 2)|	Forward	|(0, 3, 3)|	Forward|
|(1, 0, 0)|	Forward	|(1, 0, 1)	|Forward	|(1, 0, 2)	|Right|	(1, 0, 3)|	Up|
|(1, 1, 0)|	Up	|(1, 1, 1)	|Right	|(1, 1, 2)|	Up	|(1, 1, 3)	|Right|
|(1, 2, 0)	|Forward|	(1, 2, 1)|	Right|	(1, 2, 2)|	Forward	|(1, 2, 3)|	Right|
|(1, 3, 0)|	Down|	(1, 3, 1)|	Up	|(1, 3, 2)	|Up	|(1, 3, 3)	|Forward|
|(2, 0, 0)|	Up|	(2, 0, 1)	|Right|	(2, 0, 2)|	Forward|	(2, 0, 3)|	Down|
|(2, 1, 0)|	Right	|(2, 1, 1)|	Right	|(2, 1, 2)|	Up	|(2, 1, 3)	|Right|
|(2, 2, 0)	|Right	|(2, 2, 1)	|Right|	(2, 2, 2)|	Up|	(2, 2, 3)|	Forward|
|(2, 3, 0)	|Up	|(2, 3, 1)	|Up	|(2, 3, 2)|	Up|	(2, 3, 3)	|Forward|
|(3, 0, 0)	|Right	|(3, 0, 1)|	Up	|(3, 0, 2)|	Forward	|(3, 0, 3)	|Right|
|(3, 1, 0)|	Up	|(3, 1, 1)	|Right	|(3, 1, 2)|	Up	|(3, 1, 3)|	Right|
|(3, 2, 0)	|Up	|(3, 2, 1)	|Right	|(3, 2, 2)	|Up	|(3, 2, 3)	|Right|
|(3, 3, 0)	|Left	|(3, 3, 1)	|Up|	(3, 3, 2)	Up|		| | |  

It is observed that the best actions mostly belong to {Forward, Right, Up}. This is because from starting point (0, 0, 0) to ending point (3, 3, 3), all coordinates need to be incremented, which can be accomplished by these 3 actions.  

For the first episode:  
<img src = "https://github.com/StephanieMussi/Treasure_Hunting_RL/blob/main/Figures/first.png" width = 730 height = 30>  
For the last episode:  
<img src = "https://github.com/StephanieMussi/Treasure_Hunting_RL/blob/main/Figures/last.png" width = 730 height = 30>  
In the process of Q-Learning, the number of total steps taken in an episode is decreases and the reward is increased, which means the agent performs better.  

The graph of episode reward vs, episode is shown as below:  
<img src = "https://github.com/StephanieMussi/Treasure_Hunting_RL/blob/main/Figures/graph.png" width = 300 height = 200>  
