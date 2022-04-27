from Agent import Agent
from Gridworld import GridWorld
import matplotlib.pyplot as plt
import time

EPISODE_STEPS = 30
GAMMA = 0.99

if __name__ == '__main__':
    world = GridWorld()
    world.make(10, 10)

    agent = Agent(10, 10, 4)

    ep_count = 0
    total_reward = 0
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    img = ax.imshow(world.visualize())
    for eps in range(EPISODE_STEPS):
        input("Press for next step")
        if True: #eps % 10 == 0:
            canvas = world.visualize()
            img.set_data(canvas)
            fig.canvas.draw()
            fig.canvas.flush_events()
            print("Current episode: ", eps)


        # convert into agent function
        action = agent.n_sarsa(world, 5, GAMMA)

        # take action
        print('Action: ', action)
        _, reward, end = world.step(action)

        ep_count += 1
        total_reward += reward
        if end:
            print(f"Agent finished in {ep_count} steps.")
            print(f"Total reward: {total_reward}.")
            break
