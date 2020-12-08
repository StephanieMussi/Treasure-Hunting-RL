import argparse
import random
from collections import defaultdict
from matplotlib import pyplot as plt
import math

from environment import TreasureCube


class QLearningAgent(object):
    def __init__(self):
        self.action_space = ['left','right','forward','backward','up','down'] # in TreasureCube
        self.gamma = 0.99
        self.alpha = 0.5
        self.epsilon = 0.01
        self.Q = {}

    def take_action(self, state):
        r = random.random()
        if r < self.epsilon:
            action = random.choice(self.action_space)
        else:
            # get V*(s)
            value = self.get_value_from_Qvalue(state)
            # if all Q(s, a) are 0, use random selection of action
            if value == 0:
                action = random.choice(self.action_space)
            else:
                # choose the action that produces V*(s)
                for a in self.action_space:
                    Qvalue = self.get_Qvalue(state, a)
                    if Qvalue == value:
                        action = a
        return action

    
    def train(self, state, action, next_state, reward):
        # get the maximum value of Qold(St+1, a)
        maxQ = self.get_value_from_Qvalue(next_state)
        # get Qold(St, At)
        oldQ = self.get_Qvalue(state, action)
        # Qnew(St, At) <- Qold(St, At) + α*(Rt+1 + γ*max(Qold(St+1, a)) - Qold(St, At))
        self.Q[(state, action)] = oldQ + self.alpha * (reward + self.gamma * maxQ - oldQ)
    
    
    def get_Qvalue(self, state, action):
        # if Q(s, a) is assigned, return it
        if (state,action) in self.Q:
            return self.Q[(state,action)]
        # else return 0 (default value)
        else:
            return 0
   

    def get_best_action(self, state):
        temp = -100
        for a in self.action_space:
            if (state,a) in self.Q and self.Q[(state,a)] > temp: 
                temp = self.Q[(state,a)]
                best_action = a

        return best_action
    
    
    def get_value_from_Qvalue(self, state):
        value = 0
        # for given state s, find the maximum value of Q(s, a)
        for action in self.action_space:
            QValue = self.get_Qvalue(state, action)
            if QValue > value:
                value = QValue
        return value

def test_cube(max_episode, max_step):
    env = TreasureCube(max_step=max_step)
    agent = QLearningAgent()
    total_episode_reward = []

    for epsisode_num in range(0, max_episode):
        state = env.reset()
        terminate = False
        t = 0 # count of steps
        episode_reward = 0
        while not terminate: # must reach goal state
            action = agent.take_action(state) 
            reward, terminate, next_state = env.step(action) # get reward, is terminate state, new position
            episode_reward += reward # update total reward
            # you can comment the following two lines, if the output is too much
            #env.render() # comment
            #print(f'step: {t}, action: {action}, reward: {reward}') # comment
            t += 1
            agent.train(state, action, next_state, reward)
            state = next_state
        print(f'episode: {epsisode_num}, total_steps: {t} episode reward: {episode_reward}')
        total_episode_reward.append(episode_reward)
    
    d_best_action = dict()
    for (state,action) in sorted (agent.Q) : 
        print(str(state), str(action), '{:10.5f}'.format(agent.Q[(state, action)]))
        best_action = agent.get_best_action(state)
        if state not in d_best_action:
            d_best_action[state] = best_action
    
    for state, action in d_best_action.items():
        print(state, ' : ', action)
        
    
   
    # summarize episode reward
    plt.plot(total_episode_reward)
    plt.ylabel('episode reward')
    plt.xlabel('episode')
    plt.show()





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('--max_episode', type=int, default=500)
    parser.add_argument('--max_step', type=int, default=500)
    args = parser.parse_args()

    test_cube(args.max_episode, args.max_step)
