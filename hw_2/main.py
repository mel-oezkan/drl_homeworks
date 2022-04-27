from Agent import Agent
from Gridworld import GridWorld
import matplotlib.pyplot as plt
import time
import numpy as np

HEIGHT, WIDTH = 4,4
EPISODES = 100
MAX_STEPS = 15
GAMMA = 0.99

if __name__ == '__main__':
    # intialize world
    world = GridWorld(WIDTH, HEIGHT, proportion_negative=0.8)
    # intialize agend
    agent = Agent(world, 4)

    ep_count = 0
    total_reward = 0
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    img = ax.imshow(world.visualize((0,0)))
    for eps in range(EPISODES):
        # intilize starting position
        while True:
            pos = world.random_pos()
            print(world.world, pos)
            print("AAAAAA", world.world[pos], not np.isnan(world.world[pos]))
            if not np.isnan(world.world[pos]) and world.world[pos] < 0:
                break
        step = 0
        # for all steps of the episode
        while True:
            print("Step:", step)
            # calculate td-estimate and get next action
            action = agent.n_sarsa(pos, 6, GAMMA)
            # take action
            pos, reward, terminal = world.step(pos, action)
            # increment counter
            step += 1
            if True:
                canvas = world.visualize(pos)
                img.set_data(canvas)
                fig.canvas.draw()
                fig.canvas.flush_events()
                print("Current episode: ", eps)
                input("Press to show next step")
            if terminal or step > MAX_STEPS:
                if terminal:
                    print("REACHED TERMINAL")
                    time.sleep(2)
                    input()
                break

        ep_count += 1
