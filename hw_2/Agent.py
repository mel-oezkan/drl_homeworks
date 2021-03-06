import numpy as np


class Agent:
    def __init__(self, world, n_actions, learning_rate=0.1):
        self.world = world
        self.q_table = np.random.rand(world.height, world.width, n_actions)
        self.learning_rate = learning_rate

    def choose_action(self, pos):
        """
        Greedly choose the next action
        :param pos: 2d 
        :type pos: nd.array
        """
        y_pos, x_pos = pos
        possible_actions = self.q_table[y_pos, x_pos, :]
        next_action = np.argmax(possible_actions)
        return next_action


    def update_q(self, base_pos, base_action, td_est):
        """Update the q-value at base_pos-base_action based on the td_estimate"""
        self.q_table[
            base_pos[0],
            base_pos[1],
            base_action
        ] += self.learning_rate * (td_est - self.q_table[base_pos[0], base_pos[1], base_action])


    def n_sarsa(self, pos, n_steps, gamma):
        """Apply n_steps-sarsa to provided pos."""
        # remember pos and first action
        base_pos = pos
        # intialize variable td_estimate to sum results up
        td_estimate = 0
        for step in range(n_steps):
            # choose action
            new_action = self.choose_action(pos)
            pos, reward, terminated = self.world.step(pos, new_action)
            # add the total reward of n steps
            td_estimate += (gamma ** step) * reward
            # remeber first action
            if step == 0:
                base_action = new_action
            # if a terminal state is reached immediately update the q-value
            if terminated:
                self.update_q(base_pos, base_action, td_estimate)
                break
        else:
            # choose action
            last_action = self.choose_action(pos)
            # add q-table estimate to td_estimate
            td_estimate += (gamma ** (step + 1)) * self.q_table[pos[0], pos[1], last_action]
            self.update_q(base_pos, base_action, td_estimate)

        return base_action
