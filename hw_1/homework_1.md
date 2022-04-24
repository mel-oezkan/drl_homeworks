# Homework 1

## Task 1 
Markov Decision Process (S, A, P_a, R_a)

States: the positions of the specific chess figures with an identifier on the board

Actions: all possible moves each figure of the agent can take

Probabilistic State Dynamics: probability to reach a certain chess board state when choosing an action and respective reaction of the oponent.

Reward Dynamic an actions reward is defined by the number of points a killed figure has (pawn 1, knight 3, bishop 3, rook 5…)
The rewards gained when killing a figure correspond to the figure’s points (pawn 1, knight 3, bishop 3, rook 5…). Lossing a figure results in a penalization by the respective figure-value. Since killing the king ends the game, the king has a much higher value.

Policy: Take any action that maximizes the probalbilty of winning (that results in the highest reward)

## Task 2
Markov Decision Process (S, A, P_a, R_a)

States: 
There are 8 states: the coordinates of the lander in x & y, its linear velocities in x & y, its angle, its angular velocity, and two booleans that represent whether each leg is in contact with the ground or not.

Actions: There are four discrete actions available: do nothing, fire left orientation engine, fire main engine, fire right orientation engine.

Probability: Due to the dynamics of the environment it is not deterministic what the next state will be. Thus we have to predict what the next state would be

Reward: Reward for moving from the top of the screen to the landing pad and coming to rest is about 100-140 points. If the lander moves away from the landing pad, it loses reward. If the lander crashes, it receives an additional -100 points. If it comes to rest, it receives an additional +100 points. Each leg with ground contact is +10 points. Firing the main engine is -0.3 points each frame. Firing the side engine is -0.03 points each frame. Solved is 200 points.

Policy: Take the shortest path to land the lunar lander on the flag

## Task 3 
reward function: the reward function defines how good or bad a specific state is for the agent. High reward means a good state, low reward means a bad state for the agent. In chess taking the queen might result in a high reward or in the lunar lander problem landing the lander is rewarded. And since these rewards are not always known. We thus have to somehow predict what the reward would be.

state ransition function: For deterministic environments the state transition is trivial. But when the environment beceomes non-deterministic the transtion to the next state becomes unclear. Why introduce the state transition probabilty. E.g. in a chess game we dont know the next move of the opponent why we have to guess what the next move would have been.
