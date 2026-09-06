---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/action-space-reward-function.html
---

# Action space and reward function
<a name="action-space-reward-function"></a>

<a name="how-it-works-action-space"></a> **Action space**

In reinforcement learning, the set of all valid actions, or choices, available to an agent as it interacts with an environment is called an action space. In the DeepRacer on AWS console, you can train agents in either a discrete or continuous action space.

 **Discrete action space**

A discrete action space represents all of an agent’s possible actions for each state in a finite set. For DeepRacer, this means that for every incrementally different environmental situation, the agent’s neural network selects a speed and direction for the car based on input from its camera(s) and (optional) LiDAR sensor. The choice is limited to a grouping of predefined steering angle and throttle value combinations.

An AWS DeepRacer vehicle in a discrete action space approaching a turn can choose to accelerate or brake and turn left, right, or go straight. These actions are defined as a combination of steering angle and speed creating a menu of options, 0-9, for the agent. For example, 0 could represent -30 degrees and 0.4 m/s, 1 could represent -30 degrees and 0.8 m/s, 2 could represent -15 degrees and 0.4 m/s, 3 could represent -15 degrees and 0.8 m/s and so on through 9. Negative degrees turn the car right, positive degrees turn the car left and 0 keeps the wheels straight.

The default discrete action space contains the following actions:

<table>
<thead>
  <tr><th colspan="3">Default discrete action space</th></tr>
</thead>
<tbody>
  <tr><td> <b>Action number</b> </td><td> <b>Steering</b> </td><td> <b>Speed</b> </td></tr>
  <tr><td>0</td><td>-30 degrees</td><td>0.4 m/s</td></tr>
  <tr><td>1</td><td>-30 degrees</td><td>0.8 m/s</td></tr>
  <tr><td>2</td><td>-15 degrees</td><td>0.4 m/s</td></tr>
  <tr><td>3</td><td>-15 degrees</td><td>0.8 m/s</td></tr>
  <tr><td>4</td><td>0 degrees</td><td>0.4 m/s</td></tr>
  <tr><td>5</td><td>0 degrees</td><td>0.8 m/s</td></tr>
  <tr><td>6</td><td>15 degrees</td><td>0.4 m/s</td></tr>
  <tr><td>7</td><td>15 degrees</td><td>0.8 m/s</td></tr>
  <tr><td>8</td><td>30 degrees</td><td>0.4 m/s</td></tr>
  <tr><td>9</td><td>30 degrees</td><td>0.8 m/s</td></tr>
</tbody>
</table>

 **Continuous action space**

A continuous action space allows the agent to select an action from a range of values for each state. Just as with a discrete action space, this means for every incrementally different environmental situation, the agent’s neural network selects a speed and direction for the car based on input from its camera(s) and (optional) LiDAR sensor. However, in a continuous action space, you can define the range of options the agent picks its action from.

In this example, the AWS DeepRacer vehicle in a continuous action space approaching a turn can choose a speed from 0.5 m/s to 4 m/s and turn left, right, or go straight by choosing a steering angle from -20 to 20 degrees.

 **Discrete vs. continuous**

The benefit of using a continuous action space is that you can write reward functions that train models to incentivize speed/steering actions at specific points on a track that optimize performance. Picking from a range of actions also creates the potential for smooth changes in speed and steering values that, in a well trained model, may produce better results in real-life conditions.

In the discrete action space setting, limiting an agent’s choices to a finite number of predefined actions puts the onus on you to understand the impact of these actions and define them based on the environment (track, racing format) and your reward functions. However, in a continuous action space setting, the agent learns to pick the optimal speed and steering values from the min/max bounds you provide through training.

Though providing a range of values for the model to pick from seems to be the better option, the agent has to train longer to learn to choose the optimal actions. Success is also dependent upon the reward function definition.

 **Reward function**

As the agent explores the environment, the agent learns a value function. The value function helps your agent judge how good an action taken is, after observing the environment. The value function uses the reward function that you write in the DeepRacer on AWS console to score the action. For example, in the follow the center line sample reward function in the DeepRacer on AWS console, a good action would keep the agent near the center of the track and be scored higher than a bad action, which would move the agent away from the center of the track.

Over time, the value function helps the agent learn policies that increase the total reward. The optimal, or best policy, would balance the amount of time the agent spends exploring the environment with the amount of time it spends exploiting, or making the best use of, what the policy has learned through experience.

In the *Time trial - follow the center line* sample reward function example (see [Reward function examples](create-a-model.md#sample-reward-functions)), the agent first takes random actions to explore the environment, which means it doesn’t do a very good job of staying in the center of the track. Over time, the agent begins to learn which actions keep it near the center line, but if it does this by continuing to take random actions, it will take a long time to learn to stay near the center of the track for the entire lap. So, as the policy begins to learn good actions, the agent begins to use those actions instead of taking random actions. However, if it always uses or exploits the good actions, the agent won’t make any new discoveries, because it’s no longer exploring the environment. This trade-off is often referred to as the exploration vs exploitation problem in RL.

Experiment with the default action spaces and sample reward functions. Once you’ve explored them all, put your knowledge to use by designing your own custom action spaces and custom reward functions.
