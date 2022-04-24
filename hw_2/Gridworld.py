"""
Creates a gridworld where the grid can contain different values
possible values:
    - empty tiles: 0 
    - blocked tile: nan
    - reward: [-10, 10]  
"""

import numpy as np

class GridWorld:


    @staticmethod
    def random_pos(width, height):
        return (
            np.random.randint(0, height),
            np.random.randint(0, width)
        )


    def make(self, width, height):
        self.height = height
        self.width = width


        self.world = np.zeros((self.height, self.width))
        self.pos = GridWorld.random_pos(self.height, self.width)

        neg_prob = np.random.randint(0, 4) / 10
        neg_count = width * height * neg_prob

        for _ in range(neg_count):
            pos_y, pos_x = GridWorld.random_pos(width, height)
            self.world[pos_y, pos_x] = np.random.randint(10) * (-1)

        for _ in range(np.random.randint(3, 6)):
            pos_y, pos_x = GridWorld.random_pos(width, height)
            self.world[pos_y, pos_x] = np.nan

        rew_pos = GridWorld.random_pos(width, height)

        self.world[rew_pos] = 10
        self.base_world = self.world

    def reset(self):
        pass

    def step(self, action: tuple):
        pass

    def visualize(self):
        pass
        
