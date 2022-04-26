"""
Creates a gridworld where the grid can contain different values
possible values:
    - empty tiles: 0 
    - blocked tile: nan
    - reward: [-10, 10]  
"""

import numpy as np
import matplotlib.pyplot as plt


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

        # Create thr world
        self.world = np.zeros((self.height, self.width))
        self.pos = GridWorld.random_pos(self.height, self.width)

        neg_prob = np.random.randint(0, 4) / 10
        neg_count = int(width * height * neg_prob)

        # neg rewards
        for _ in range(neg_count):
            pos_y, pos_x = GridWorld.random_pos(width, height)
            self.world[pos_y, pos_x] = np.random.randint(10) * (-1)

        # blocked states
        for _ in range(np.random.randint(3, 6)):
            pos_y, pos_x = GridWorld.random_pos(width, height)
            self.world[pos_y, pos_x] = np.nan

        # infal state
        rew_pos = GridWorld.random_pos(width, height)
        self.world[rew_pos] = 10

        # remember base world for reset
        self.base_world = self.world
        self.start_pos = self.pos

    def reset(self):
        self.make()

    def step(self, action: tuple):
        """
        Accepts 4 different values
        - up, down, right, left

        Returns the respective reward and new state
        """

        curr_y, curr_x = self.pos
        #new_y, new_x = curr_y + action[0], curr_x + action[1]

        if action == 'up':
            self.pos = (max(curr_x - 1, 0), curr_x)
        elif action == 'down':
            self.pos = (min(curr_x + 1, self.height-1), curr_x)
        elif action == 'right':
            self.pos = (curr_y, max(curr_x+1, self.width-1))
        elif action == 'left':
            self.pos = (curr_y, min(curr_x-1, 0))

        # get the reward
        reward = self.world[self.pos[0], self.pos[1]]
        return self.pos, reward, reward > 0

    def visualize(self):

        canvas = np.zeros_like(self.world)
        pos_mask = self.world > 0
        neg_mask = self.world < 0

        block_mask = self.world == np.nan
        neutral_mask = self.world == 0

        canvas[pos_mask] = 1
        canvas[neg_mask] = 2
        canvas[block_mask] = 3
        canvas[neutral_mask] = 4

        canvas[self.pos[0], self.pos[1]] = 5

        plt.imshow(canvas), plt.axis('off')
        plt.legend()
        plt.show()
