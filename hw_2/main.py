from Agent import Agent
from Gridworld import GridWorld

EPISODE_STEPS = 100
GAMMA = 0.95

if __name__ == '__main__':
    world = GridWorld()
    state = world.make(10, 10)

    agent = Agent(10, 10, 4)

    ep_count = 0
    total_reward = 0
    for eps in range(EPISODE_STEPS):

        if True: #eps % 10 == 0:
            world.visualize()
            print("Current episode: ", eps)


        # convert into agent function
        action = agent.n_sarsa(world, 2, GAMMA)

        # take action
        print('Action: ', action)
        state, reward, end = world.step(action)

        ep_count += 1
        total_reward += reward

        if end:
            print(f"Agent finished in {ep_count} steps.")
            print(f"Total reward: {total_reward}.")
            break
