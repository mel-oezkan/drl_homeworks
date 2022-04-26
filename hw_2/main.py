from Agent import Agent
from Gridworld import GridWorld

EPISODE_STEPS = 1_000
GAMMA = 0.95

if __name__ == '__main__':
    world = GridWorld()
    state = world.make(10, 10)

    agent = Agent(10, 10, 4)

    ep_count = 0
    total_reward = 0
    for eps in range(EPISODE_STEPS):

        if eps % 10:
            print("Current episode: ", eps)

        # generate action
        base_action = None
        base_state = None
        td_estimate = 0

        # convert into agent function
        action = agent.n_sarsa(world, 4, GAMMA)

        # take action
        state, reward, end = world.step(action)

        ep_count += 1
        total_reward += reward

        if reward:
            print(f"Agent finished in {ep_count} steps.")
            print(f"Total reward: {total_reward}.")

            break
