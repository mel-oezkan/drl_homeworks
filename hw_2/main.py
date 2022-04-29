from Agent import Agent
from Gridworld import GridWorld
import matplotlib.pyplot as plt
import time
import numpy as np

HEIGHT, WIDTH = 5, 5
EPISODES = 100
MAX_STEPS = 20
GAMMA = 0.99

if __name__ == '__main__':
    # intialize world
    world = GridWorld(WIDTH, HEIGHT, proportion_negative=0.8)
    # intialize agend
    agent = Agent(world, 4)
    # intilize fixed starting position
    while True:
        base_pos = world.random_pos()
        if not np.isnan(world.world[base_pos]) and world.world[base_pos] < 0:
            break
    ep_count = 0
    total_reward = 0
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    img = ax.imshow(world.visualize(base_pos))
    quivers = []
    for qi in range(4):
        a = 2 * np.pi * (qi + 1) / 4
        # sin(a) = y/h
        # cos(a) = x/h
        x, y = np.arange(0,WIDTH), np.arange(0,HEIGHT)
        xx, yy = np.meshgrid(x,y)
        u = agent.q_table[:, :, qi] * np.round(np.cos(a))
        v = agent.q_table[:, :, qi] * np.round(np.sin(a))
        quivers.append(ax.quiver(xx, yy, u, v))
    for eps in range(EPISODES):
        pos = base_pos
        # for all steps of the episode
        step = 0
        while True:
            # visualize
            if True:
                canvas = world.visualize(pos)
                img.set_data(canvas)
                for qi in range(4):
                    a = 2 * np.pi * (qi + 1) / 4
                    # sin(a) = y/h
                    # cos(a) = x/h
                    x, y = np.arange(0,WIDTH), np.arange(0,HEIGHT)
                    xx, yy = np.meshgrid(x,y)
                    u = agent.q_table[:, :, qi] * np.cos(a)
                    v = agent.q_table[:, :, qi] * np.sin(a)
                    quivers[qi].set_UVC(u, v)
                fig.canvas.draw()
                fig.canvas.flush_events()
            print("Episode:", eps, "Step:", step)
            input("Next Step")
            # calculate td-estimate and get next action
            action = agent.n_sarsa(pos, 4, GAMMA)
            # take action
            pos, reward, terminal = world.step(pos, action)
            # increment counter
            step += 1
            if terminal or step > MAX_STEPS:
                if terminal:
                    print("REACHED TERMINAL")
                    time.sleep(2)
                break

        ep_count += 1
