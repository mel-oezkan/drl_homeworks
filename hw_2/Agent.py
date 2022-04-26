import numpy as np


class Agent:
    def __init__(self, width, height, n_actions, learning_rate=0.1):
        self.q_table = np.random.rand(width, height, n_actions)
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

    def n_sarsa(self, world, n_steps, gamma):

        # remember pos and first action
        base_pos = world.pos
        base_state = world.world

        td_estimate = 0
        for step in range(n_steps):

            new_action = self.choose_action(world.pos)
            _, reward, end = world.step(new_action)

            # delta = r + GAMMA Q(s', a') - Q(s,a)
            td_estimate += (gamma ** step) * reward
          
            if step == 0:
                base_action = new_action

            if end:
                break

        # add q-table estimate
        last_action = self.choose_action(world.pos)
        last_pos = world.pos

        td_estimate += self.q_table[last_pos[0], last_pos[1], last_action]
        td_estimate -= self.q_table[base_pos[0], base_pos[1], base_action]

        # Q_new(s,a) ← Q_old(s,a) + alpha[R + y*Q(s',a') - Q(s,a)]
        self.q_table[
            base_pos[0],
            base_pos[1],
            base_action
        ] += self.learning_rate * td_estimate

        world.world = base_state
        return base_action
