---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/train-and-evaluate-models.html
---

# Train and evaluate models
<a name="train-and-evaluate-models"></a>

Training your model involves the vehicle learning optimal driving behaviors through trial and error in a simulated environment. Your vehicle uses its front-mounted camera to capture environmental states and responds with actions (speed and steering combinations). Your model is a neural network function that maps these observations to expected rewards, with training focused on maximizing cumulative rewards.

The reward function defines the criteria for optimal behavior. A simple example might give 0 points for staying on track, -1 for going off track, and \+1 for finishing. More sophisticated reward functions can encourage faster driving by rewarding smaller steering corrections at higher speeds, or penalizing aggressive turns that might cause the vehicle to leave the track.

Training occurs through repeated episodes from start to finish, where the agent learns by maximizing expected cumulative rewards. DeepRacer on AWS supports **Proximal Policy Optimization (PPO)** and **Soft Actor Critic (SAC)** algorithms, integrated with SageMaker AI and TensorFlow frameworks.

Model training is inherently iterative. Since it’s difficult to define perfect reward functions initially and hyperparameters require tuning, start with simple reward functions and progressively enhance them. Use the clone feature to build upon previous models, systematically adjusting variables and hyperparameters until results converge.

Evaluation is essential before deploying to physical vehicles. The simulator provides metrics on track completion rates, lap times, and performance comparisons via leaderboards, helping you assess model effectiveness before real-world deployment.

## Training for time trial races
<a name="training-for-time-trial"></a>

Start with time trials if you’re new to DeepRacer on AWS or the physical vehicle. This provides a gentle introduction to reward functions, agents, and environments. Your goal: train a model to stay on track and complete laps quickly, then deploy it to your physical DeepRacer for testing.

Begin by creating a model with the default configuration (single front-facing camera, default reward function). Starting with defaults helps establish fundamentals before advancing to complex configurations.

 **Training progression:**

1.  **Initial training**: Use a simple track with regular shapes and minimal sharp turns. Train for 30 minutes with the default reward function, then evaluate to confirm the agent completes laps.

1.  **Speed optimization**: Study reward function parameters and modify your reward function to incentivize faster driving. Extend training to 1-2 hours, comparing reward graphs to track improvement.

1.  **Action space tuning**: Read about action space and increase top speed (e.g., 1 m/s) by creating a new model. Higher speeds improve lap times but increase training complexity as agents may overshoot curves. Consider reducing granularities and refining reward functions to accelerate convergence.

1.  **Generalization testing**: Progress to complex tracks, repeating steps 1-3. Evaluate models on different tracks to test generalization capabilities.

1.  *(Optional)* Experiment with hyperparameter variations and analyze training logs for optimization insights.

## Training a model for object avoidance races
<a name="training-for-object-avoidance"></a>

After training for time trials, move on to object avoidance—training models to complete fast laps while avoiding track obstacles. This challenge requires longer convergence times due to increased complexity.

 **Obstacle placement options:**
+  **Fixed locations**: Obstacles remain stationary throughout training. Easier convergence but risk of overfitting.
+  **Random locations**: Obstacles change positions between episodes. Harder convergence but better generalization for real-world transfer.

Start with fixed locations to understand behaviors before tackling random placement. Simulator obstacles match AWS DeepRacer packaging dimensions (9.5" × 15.25" × 10.5"), simplifying real-world transfer.

 **Training progression:**

1.  **Fixed obstacle training**: Use default agent or customize sensors/action space. Limit speed to <0.8 m/s with 1-2 speed levels. Train 3 hours with 2 fixed objects on your target track (e.g., AWS DeepRacer Smile Speedway). Evaluate and monitor reward convergence.

1.  **Reward optimization**: Study reward function parameters and experiment with reward function variations. Increase obstacles to 4, adjusting functions, speeds, or obstacle counts as needed until no significant improvement occurs.

1.  **Random obstacle training**: Progress to stereo camera or LiDAR combinations (expect longer training). Use low top speed (e.g., 2 m/s) and shallow neural networks for faster convergence.

1.  **Advanced training**: Train 4 hours with 4 randomly placed objects on simple tracks. If unsuccessful, modify reward functions, try different sensors, extend training time, or clone existing models to leverage prior learning.

1.  *(Optional)* Experiment with higher speeds, more obstacles, and different sensor combinations to optimize performance.
