"""
Creates a gridworld where the grid can contain different values
possible values:
    - empty tiles: 0 
    - blocked tile: nan
    - reward: [-10, 10]  
"""

import numpy as np


class GridWorld:
    def __init__(self, width, height, proportion_negative=0.4):
        self.width = width
        self.height = height
        # intialize world
        self.create_world(proportion_negative)


    def random_pos(self):
        return (
            np.random.randint(0, self.height),
            np.random.randint(0, self.width)
        )


    def create_world(self, proportion_negative):
        # intialize world
        self.world = np.zeros((self.height, self.width))
        # add goal spot (positive reward)
        self.world[self.random_pos()] = 10
        # add walkable spots (negative reward)
        while np.sum(self.world < 0) < np.floor(proportion_negative * self.world.size):
            rpos = self.random_pos()
            if self.world[rpos] == 0:
                self.world[rpos] = -1
        # add unaccessible spots (nan)
        self.world[self.world == 0] = np.nan


    def reset(self):
        self.make()


    def step(self, pos: tuple, action: tuple):
        """
        Accepts 4 different values
        - up, down, right, left

        Returns the respective reward and new state
        """

        curr_y, curr_x = pos
      
        if action == 0: # up
            new_pos = curr_y - 1, curr_x
        elif action == 1: # down
            new_pos = curr_y + 1, curr_x
        elif action == 2: #'right'
            new_pos = curr_y, curr_x + 1
        elif action == 3: # 'left'
            new_pos = curr_y, curr_x - 1
        
        # check if in bounds 
        bound_x = new_pos[0] >= 0 and new_pos[0] <= (self.width -1)
        bound_y = new_pos[1] >= 0 and new_pos[1] <= (self.height -1)
        if not (bound_x and bound_y):
          return pos, 0, False

        # check if field is blocked
        if np.isnan(self.world[new_pos]):
            return pos, 0, False
          
        # get the reward
        reward = self.world[new_pos]
        return new_pos, reward, reward > 0


    def visualize(self, pos):
        canvas = np.zeros_like(self.world)
        pos_mask = self.world > 0
        neg_mask = self.world < 0

        block_mask = self.world == np.nan
        neutral_mask = self.world == 0

        canvas[pos_mask] = 1
        canvas[neg_mask] = 2
        canvas[block_mask] = 3
        canvas[neutral_mask] = 4

        canvas[pos] = 5
        return canvas
