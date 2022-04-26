import numpy as np


class Agent:
  def __init__(self, width, height, n_actions, learning_rate=0.1):
    self.q_table = np.random.rand(width, height, n_actions)
    self.actions = {
      0: (0,1),
      1: (0,-1),
      2: (1,0),
      3: (-1,0)
    }
    self.learning_rate = learning_rate
    
  def choose_action(self, pos):
    """
    Greedly choose the next action
    :param pos: 2d 
    :type pos: nd.array
    """
    (height, width) = pos
    possible_actions = self.q_table[height, width, :]    
    
    next_action = np.argmax(possible_actions)
    return self.actions[next_action]
  
  def n_sarsa(state, world):

    # remember pos and first action
    base_pos = world.pos

    q_sum = 0
    for step in range(n_steps):
      
      new_action = self.choose_action(pos)
      state, reward, end = world.step(action)

      # delta = r + GAMMA Q(s', a') - Q(s,a)
      td_estimate += (GAMMA ** step) * reward
      
      if step == 0:
        base_state = state
        base_action = action
        
    # add q-table estimate 
    last_action = self.choose_action(pos)
    last_pos = world.pos
    
    td_estimate += self.q_table[last_pos[0], last_pos[1], last_action]
    td_estimate -= self.q_table[base_pos[0], base_pos[1], base_action]
    
    # Q_new(s,a) ← Q_old(s,a) + alpha[R + y*Q(s',a') - Q(s,a)]  
    self.q_table[
      base_pos[0], 
      base_pos[1], 
      base_action
    ] += self.learning_rate * td_estimate
  
    world.world = base_pos
    return base_action