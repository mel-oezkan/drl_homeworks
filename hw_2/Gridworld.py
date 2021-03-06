"""
Creates a gridworld where the grid can contain different values
possible values:
    - blocked tile: nan
    - reward: [-1, 10]
"""

import numpy as np
import matplotlib.pyplot as plt


class GridWorld:
    def __init__(self, width, height, proportion_negative=0.3, undeterministic=True):
        self.width = width
        self.height = height
        # intialize world
        while True:
            self.create_world(proportion_negative)
            if self.check_world_legal():
                break
        self.state_transition_prob = np.ones((height, width, 4))
        if undeterministic:
            self.state_transition_prob -= np.random.rand(height, width, 4) * 0.3


    def random_pos(self):
        """Create a random position"""
        return (
            np.random.randint(0, self.height),
            np.random.randint(0, self.width)
        )


    def create_world(self, proportion_negative):
        """Create reward matrix."""
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
    

    def check_world_legal(self):
        """Apply flood fill to check if all the walkaboe spots are connected"""
        world_copy = np.copy(self.world)
        while True:
            start_pos = self.random_pos()
            if not np.isnan(self.world[start_pos]):
                break
        # floodfill counts the number of accessible spots
        self.c = 0
        self.fill4(*start_pos, world_copy)
        if self.c < np.count_nonzero(np.isnan(self.world) == 0):
            return False
        return True


    def reset(self):
        """Create new World."""
        self.create_world()
    

    def fill4(self, x, y, world_copy):
        """Recursive floodfill algorithm, for every accessbile spot, add 1 to counter"""
        if self.legal_pos((y, x), world=world_copy):
            world_copy[y, x] = np.nan
            self.fill4(x, y + 1, world_copy)  # unten
            self.fill4(x, y - 1, world_copy)  # oben
            self.fill4(x + 1, y, world_copy)  # rechts
            self.fill4(x - 1, y, world_copy)  # links
            self.c += 1


    def legal_pos(self, pos: tuple, world=None):
        """Check if a position is not out of bounds or a blocked state."""
        if world is None: world = self.world
        # check if in bounds 
        bound_x = pos[1] >= 0 and pos[1] <= (self.width -1)
        bound_y = pos[0] >= 0 and pos[0] <= (self.height -1)
        if not (bound_x and bound_y):
            return False
        # check if field is blocked
        if np.isnan(world[pos]):
            return False
        return True


    def step(self, pos: tuple, action: int):
        """
        Accepts 4 different values
        - up, down, right, left

        Returns the respective reward and new state
        """
        curr_y, curr_x = pos
        # change action with certain probability (if world is deterministic nothing will be changed)
        if np.random.rand() > self.state_transition_prob[curr_y, curr_x, action]:
            while True:
                new_action = np.random.randint(0, 4)
                if new_action != action:
                    action = new_action
                    break
        if action == 0: # up
            new_pos = curr_y - 1, curr_x
        elif action == 1: #'left'
            new_pos = curr_y, curr_x - 1
        elif action == 2: # down
            new_pos = curr_y + 1, curr_x
        elif action == 3: # 'right'
            new_pos = curr_y, curr_x + 1
        
        # check if legal move
        if not self.legal_pos(new_pos):
            return pos, self.world[pos], False
          
        # get the reward
        reward = self.world[new_pos]
        return new_pos, reward, reward > 0


    def create_canvas(self, pos):
        """Create canvas matrix for visualisation."""
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
    

    def init_visualisation(self, pos, agent):
        """Initialize plot and vector arrows simbolizing smallest to biggest q-values."""
        self.agent = agent
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.img = self.ax.imshow(self.create_canvas(pos))
        self.quivers = []
        q_table_sort = np.argsort(np.argsort(self.agent.q_table))
        for qi in range(4):
            a = 2 * np.pi * (qi + 1) / 4
            # sin(a) = y/h
            # cos(a) = x/h
            x, y = np.arange(0, self.width), np.arange(0, self.height)
            xx, yy = np.meshgrid(x,y)
            u = q_table_sort[:, :, qi] * np.round(np.cos(a))
            v = q_table_sort[:, :, qi] * np.round(np.sin(a))
            self.quivers.append(self.ax.quiver(xx, yy, u, v, color='red'))
    
    
    def visualization_step(self, pos):
        """Update step for plot."""
        canvas = self.create_canvas(pos)
        self.img.set_data(canvas)
        q_table_sort = np.argsort(np.argsort(self.agent.q_table))
        for qi in range(4):
            a = 2 * np.pi * (qi + 1) / 4
            # sin(a) = y/h
            # cos(a) = x/h
            u = q_table_sort[:, :, qi] * np.cos(a)
            v = q_table_sort[:, :, qi] * np.sin(a)
            self.quivers[qi].set_UVC(u, v)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

