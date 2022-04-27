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
        (height, width) = pos
        possible_actions = self.q_table[height, width, :]

        #print(possible_actions)

        next_action = np.argmax(possible_actions)
        return next_action


    def update_q(self, base_pos, base_action, td_est):
        self.q_table[
            base_pos[0],
            base_pos[1],
            base_action
        ] += self.learning_rate * td_est


    def n_sarsa(self, pos, n_steps, gamma):

        # remember pos and first action
        base_pos = pos

        td_estimate = 0
        for step in range(n_steps):

            new_action = self.choose_action(pos)
            pos, reward, terminated = self.world.step(pos, new_action)

            # delta = r + GAMMA Q(s', a') - Q(s,a)
            td_estimate += (gamma ** step) * reward
          
            if step == 0:
                base_action = new_action

            if terminated:
                self.update_q(base_pos, base_action, td_estimate)
        else:
            last_action = self.choose_action(pos)
            # add q-table estimate to td_estimate
            td_estimate += self.q_table[pos[0], pos[1], last_action]
            td_estimate -= self.q_table[pos[0], pos[1], base_action]
            self.update_q(base_pos, base_action, td_estimate)

        return base_action
