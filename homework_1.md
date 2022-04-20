# Homework 1

## Task1
Markov Decision Process (S, A, P_a, R_a)

States: the positions of the specific chess figures with an identifier on the board

Actions: all possible moves each figure of the agent can take

Probabilistic State Dynamics: probability to reach a certain chess board state when choosing an action and respective reaction of the oponent.

Reward Dynamic an actions reward is defined by the number of points a killed figure has (pawn 1, knight 3, bishop 3, rook 5…)
The rewards gained when killing a figure correspond to the figure’s points (pawn 1, knight 3, bishop 3, rook 5…). Lossing a figure results in a penalization by the respective figure-value. Since killing the king ends the game, the king has a much higher value.

Policy: Take any action that maximizes the probalbilty of winning (that results in the highest reward)


## Task2
