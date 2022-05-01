from Agent import Agent
from Gridworld import GridWorld

import numpy as np
import time


HEIGHT, WIDTH = 5, 5
EPISODES = 100
MAX_STEPS = 20
GAMMA = 0.99
N_SARSA_STEPS = 4


if __name__ == '__main__':
    print("Always press [ENTER] to proceed.")
    # intialize world
    world = GridWorld(WIDTH, HEIGHT, proportion_negative=0.6)
    # intialize agend
    agent = Agent(world, 4)
    # intilize fixed starting position
    while True:
        base_pos = world.random_pos()
        if not np.isnan(world.world[base_pos]) and world.world[base_pos] < 0:
            terminal = False
            break
    # intilize visulisation
    world.init_visualisation(base_pos, agent)
    for eps in range(EPISODES):
        pos = base_pos
        # for all steps of the episode
        step = 0
        world.visualization_step(pos)
        input("Start new Epoch")
        while True:
            print("Episode:", eps, "Step:", step)
            # calculate td-estimate and get next action
            action = agent.n_sarsa(pos, N_SARSA_STEPS, GAMMA)
            # take action
            pos, reward, terminal = world.step(pos, action)
            # visualize
            if True:
                world.visualization_step(pos)
            if terminal or step > MAX_STEPS:
                if terminal:
                    terminal = False
                    input("REACHED TERMINAL")
                    time.sleep(1.5)
                break

            #world.check_world_legal()
            input("Next Step")
            # increment counter
            step += 1