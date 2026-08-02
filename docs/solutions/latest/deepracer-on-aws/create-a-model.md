---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/create-a-model.html
---

# Create a model
<a name="create-a-model"></a>

A model is a reinforcement learning neural network that enables the race car, either virtual or physical, to make real-time driving decisions on its own. The model is created by training the vehicle through trial and error in a simulated environment, where it learns to navigate a track by optimizing for rewards defined in the reward function.

To create a model, find the **Your models** page in the left sidebar and click **Create model** in the upper right corner of the screen. You’ll be brought to a multi-step wizard to help you create the model.

## Model name and environment
<a name="model-name-and-environment"></a>

First, you’ll give your model a **name** and a description (optional).

![AWS DeepRacer Create Model](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_create_model_page1_1.png)

Then, you’ll choose a **race type** to optimize your model for.
+  **Time trial** - aims to go around the track as quickly as possible, while staying on the track.
+  **Object avoidance** - aims to complete the fastest lap while avoiding objects on the track.

![AWS DeepRacer Create Model - Race Type](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_create_model_page1_2.png)

If you select object avoidance, you’ll be presented with additional options that allow you to select the whether you’d like the objects to avoid to be in fixed or random locations, as well as the number of objects to place on the track. If you choose to have the objects placed in a fixed location, you can specify where you’d like them to be placed by selecting:
+  **Lane placement** - whether the object is placed inside or outside of the lane.
+  **Location** - a function of the % distance between the track’s start and finish lines.

Next, you’ll choose the **environment**, or track that your model will be trained on. DeepRacer on AWS comes with a variety of different tracks to choose from. If you plan on entering your model into a competition, it’s best to train your model on the same race track that will be used for that competition. Some tracks offer the option to pick which direction the car will travel (i.e. clockwise or counterclockwise).

Finally, you’ll set the **Minimum evaluation trials** parameter. Minimum evaluation trials determine the number of evaluation laps the simulator runs after each training iteration to measure the model’s current performance. Lower values allow more training iterations to complete within the training time limit. Higher values give a more reliable indication of how the model is progressing. The default is 5, and the minimum is 1.

When you’re ready to move on to the next step, click **Next**.

![AWS DeepRacer Create Model - choose vehicle sensors and hyperparameters](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_create_model_page2_1.png)

## Vehicle sensors and hyperparameters
<a name="vehicle-sensors-and-hyperparameters-2"></a>

### Sensors
<a name="sensors"></a>

#### Front-facing camera
<a name="front-facing-camera"></a>

A single-lens front-facing camera can capture images of the environment in front of the host vehicle, including track borders and shapes. It’s the least expensive sensor and is suitable for handling simpler autonomous driving tasks, such as obstacle-free time trials on well-marked tracks. With proper training, it can avoid stationary obstacles at fixed locations on the track. However, the obstacle location information is built into the trained model and, as a result, the model is likely to be overfitted and may not generalize to other obstacle placements. With stationary objects placed at random locations or other moving vehicles on the track, the model is unlikely to converge.

In the real world, the AWS DeepRacer vehicle comes with a single-lens front-facing camera as the default sensor. The camera has a 120-degree wide angle lens and captures RGB images that are then converted to grayscale images of 160 x 120 pixels at 15 frames per second (fps). These sensor properties are preserved in the simulator to maximize the chance that the trained model transfers well from simulation to the real world.

#### Front-facing stereo camera
<a name="front-facing-stereo-camera"></a>

A stereo camera has two or more lenses that capture images with the same resolution and frequency. Images from both lenses are used to determine the depth of observed objects. The depth information from a stereo camera is valuable for the host vehicle to avoid crashing into obstacles or other vehicles in the front, especially in a more dynamic environment. However, added depth information makes training converge more slowly.

On the AWS DeepRacer physical vehicle, the double-lens stereo camera is constructed by adding another single-lens camera and mounting each camera on the left and right sides of the vehicle. The AWS DeepRacer software synchronizes image captures from both cameras. The captured images are converted into grayscale, stacked, and fed into the neural network for inference. The same mechanism is duplicated in the simulator in order to train the model to generalize well to a real-world environment.

#### LiDAR sensor
<a name="lidar-sensor"></a>

An optional LiDAR sensor uses rotating lasers to send out pulses of light outside the visible spectrum and times how long it takes each pulse to return. The direction of and distance to the objects that a specific pulse hits are recorded as a point in a large 3D map centered around the LiDAR unit.

For example, LiDAR helps detect blind spots of the host vehicle to avoid collisions while the vehicle changes lanes. By combining LiDAR with mono or stereo cameras, you enable the host vehicle to capture sufficient information to take appropriate actions. However, a LiDAR sensor costs more compared to cameras. The neural network must learn how to interpret the LiDAR data. Thus, training will take longer to converge.

On the AWS DeepRacer physical vehicle, a LiDAR sensor is mounted on the rear and tilted down by 6 degrees. It rotates at an angular velocity of 10 rotations per second and has a range of 15cm to 2m. It can detect objects behind and beside the host vehicle as well as tall objects unobstructed by the vehicle parts in the front. The angle and range are chosen to make the LiDAR unit less susceptible to environmental noise.

#### Configuration options
<a name="configuration-options"></a>

You can configure your AWS DeepRacer vehicle with the following combination of the supported sensors:
+  **Front-facing single-lens camera only** - suitable for time trials, as well as obstacle avoidance with objects at fixed locations.
+  **Front-facing stereo camera only** - suitable for obstacle avoidance with objects at fixed or random locations.
+  **Front-facing single-lens camera w/ LiDAR** - suitable for obstacle avoidance.
+  **Front-facing stereo camera w/ LiDAR** - suitable for obstacle avoidance, but probably not the most economical for time trials.

As you add more sensors to make your AWS DeepRacer vehicle transition from time trials to object avoidance, the vehicle collects more data about the environment to feed into the underlying neural network during training. This makes training more challenging because the model is required to handle increased complexities. In the end, your tasks of learning to train models become more demanding.

To learn progressively, you should start training for time trials first before moving on to object avoidance racing.

You should experiment with different sensors on your AWS DeepRacer vehicle to provide it with sufficient capabilities to observe its surroundings for a given race type. The next section describes the supported sensors that can enable the supported types of autonomous racing events.

## Training algorithms and Hyperparameters
<a name="training-algorithms-and-hyperparameters"></a>

![AWS DeepRacer Create Model - Training algorithms and hyperparameters](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_create_model_page_2_2.png)

+  **PPO** - proximal policy optimization - teaches the vehicle by letting it practice driving and gradually improving its skills through small, careful adjustments based on what it just learned, similar to how you might refine your technique after each practice lap.
+  **SAC** - soft actor-critic - allows the vehicle to learn from both its current driving attempts and past experiences, encouraging it to try new approaches while still aiming for the best lap times, making it more flexible but requiring more fine-tuning to get right.

If you select the PPO algorithm, you’ll be asked to provide:
+  **Gradient descent batch size** - how many training examples the model looks at together before updating what it has learned, where looking at more examples at once gives smoother learning but takes longer to process.
+  **Number of epochs** - the number of times the training algorithm passes through and updates the model using the same batch of collected experience data before gathering new experiences. Higher epoch values allow the model to learn more thoroughly from each batch but risk over-fitting to that specific data.
+  **Learning rate** - how quickly the model adjusts its driving strategy based on what it learns, where higher values mean faster learning but risk making the car’s behavior unstable, while lower values mean slower but steadier improvement.
+  **Entropy** - encourages the model to maintain exploration and creativity in its action selection by penalizing overly deterministic behavior, preventing the agent from prematurely settling on repetitive or sub-optimal driving patterns.
+  **Loss type** - determines the function used to calculate prediction errors during training:
  +  **Huber loss** - treats small mistakes gently (helping the model learn smoothly) but doesn’t overreact to occasional big mistakes, making it more forgiving when the training data has some unusual or extreme values.
  +  **Mean squared error** - penalizes bigger mistakes much more than smaller ones, which helps the model focus on avoiding large errors but can sometimes make it too sensitive to unusual data points.
+  **Number of experience episodes between each policy-updating iteration** - specifies how many track runs the vehicle collects and stores as training data before using that batch of experiences to update the model’s neural network weights, balancing data collection efficiency with training frequency.

If you select the SAC algorithm, you’ll be asked to provide:
+  **Gradient descent batch size** - how many training examples the model looks at together before updating what it has learned, where looking at more examples at once gives smoother learning but takes longer to process.
+  **Learning rate** - how quickly the model adjusts its driving strategy based on what it learns, where higher values mean faster learning but risk making the car’s behavior unstable, while lower values mean slower but steadier improvement.
+  **SAC alpha value** - controls how much the model balances between trying new driving approaches versus sticking with strategies it already knows work well, helping prevent the car from getting stuck doing the same thing over and over.
+  **Discount factor** - determines how much the model cares about rewards it might get in the future versus rewards it gets right now, where higher values make the car think more about long-term success (like completing the whole lap) rather than just immediate gains.
+  **Loss type** - determines the function used to calculate prediction errors during training:
  +  **Huber loss** - treats small mistakes gently (helping the model learn smoothly) but doesn’t overreact to occasional big mistakes, making it more forgiving when the training data has some unusual or extreme values.
  +  **Mean squared error** - penalizes bigger mistakes much more than smaller ones, which helps the model focus on avoiding large errors but can sometimes make it too sensitive to unusual data points.

When you’re ready to move on to the next step, click **Next**.

## Action space
<a name="action-space"></a>

![AWS DeepRacer Create Model - Action Space](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_create_model_page_3_1.png)

![AWS DeepRacer Create Model - Action Space](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_create_model_page_3_2.png)

In reinforcement learning, the **action space** is the complete set of choices available to the vehicle as it drives around the track. In the DeepRacer on AWS console, you can train your car using either a continuous action space or a discrete action space.

 **Continuous action spaces**

In a continuous action space, the car learns to pick the best speed and steering angle from a range of values you set (i.e. choosing any speed between 1 and 4 meters per second, rather than just picking from fixed options like "slow," "medium," or "fast"). Giving the model a range of values to choose from provides more flexibility and can lead to smoother, more optimized driving, but it also means the car needs more training time to figure out which combinations of speed and steering work best for different parts of the track.

On this page, you’ll start by defining the **left steering angle** and **right steering angle**. This determines how sharply the vehicle can turn its wheels. Smaller angles allow only gentle turns suitable for straighter sections, while larger angles enable the sharp turns needed for tight corners. Setting the right steering angle range is crucial because too narrow means the car can’t navigate sharp curves and will drive off track, while too wide causes unnecessary zig-zagging that slows lap times.

Next, you’ll select the **minimum speed** and **maximum speed**, which determines how fast the vehicle moves around the track. Lower speeds provide more control and stability through corners but result in slower lap times, while higher speeds can complete laps faster but make it harder for the car to stay on track through turns. Setting the right speed range is important because too slow means the car will never achieve competitive lap times even if it stays on track, while too fast can cause the car to overshoot corners and drive off the track before it can react.

 **Discrete action spaces**

A discrete action space means the car chooses from a fixed menu of specific driving options rather than picking any value it wants. You define exactly which steering-and-speed combinations are available (for example, five steering angles like sharp left, slight left, straight, slight right, and sharp right, each paired with three different speeds), and during training, the model learns which of these specific combinations work best for different parts of the track. This approach makes training simpler and faster because the car has fewer choices to evaluate, but it also means the driving behavior is limited to only the combinations you’ve predefined rather than being able to fine-tune to any possible steering angle and speed.

On this page, you’ll start by defining the **steering angle granularity**, which is the number of different steering angle options available to the car between its minimum and maximum turning angles, where higher granularity means more steering choices (like having 7 different turn angles instead of just 3), giving the car finer control but requiring more training time to learn which option works best. Then, you’ll select the **maximum steering angle** you would like your car to have, between 1 and 30 degrees.

Next, you’ll select your **speed granularity**, which is the number of different speed options available to the car between its minimum and maximum speeds, where higher granularity means more speed choices (like having 5 different speeds instead of just 2), allowing the car to fine-tune its velocity for different track sections but requiring more training time to learn the optimal speed for each situation. You’ll also select the **maximum speed** for the car.

In the **Action list**, you’ll see a list of actions, steering angles, and speeds populated based on your selections thus far. You can toggle the Advanced configuration switch to fine tune each action or add/remove actions as desired.

When you’re ready to move on to the next step, click **Next**.

## Vehicle shell
<a name="vehicle-shell"></a>

On this page, you’ll select a **vehicle shell**, which has no performance impact and is cosmetic only. This will be what you see navigating around the track in training, evaluations, and races. You can pick different types of shells and different colors for those shells.

When you’re ready to move on to the next step, click **Next**.

![AWS DeepRacer Create Model - vehicle shell](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_create_model_page_4.png)

## Reward function
<a name="reward-function"></a>

The reward function describes immediate feedback (as a score for reward or penalty) when the vehicle take an action to move from a given position on the track to a new position. Its purpose is to encourage the vehicle to make moves along the track to reach its destination quickly. The model training process will attempt to find a policy which maximizes the average total reward the vehicle experiences.

In the editor, you can see a selection of sample reward functions by clicking **Reward function examples**. Reward functions are defined as Python code, and you can validate your code at any point by clicking **Validate**. Alternatively, if you would like to reset the code that’s in the editor to the default code, you can click **Reset**.

Once you have your reward function defined, you will be asked to set a stop condition. This is the condition for your model training to stop. To avoid run-away jobs, you can limit the length of a job to within a maximum time period (**Maximum time**).

The training will stop when the specified criteria is met. When your model has stopped training, you will be able to clone your model to start training again using new parameters.

When you’re ready to proceed, click **Train your model**.

![AWS DeepRacer Create Model - reward function](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_create_model_page_5.png)

### Input parameters
<a name="input-parameters"></a>

The AWS DeepRacer reward function takes a dictionary object as the input.

```
def reward_function(params) :

    reward = ...

    return float(reward)
```

The `params` dictionary object contains the following key-value pairs:

```
{
    "all_wheels_on_track": Boolean,        # flag to indicate if the agent is on the track
    "x": float,                            # agent's x-coordinate in meters
    "y": float,                            # agent's y-coordinate in meters
    "closest_objects": [int, int],         # zero-based indices of the two closest objects to the agent's current position of (x, y).
    "closest_waypoints": [int, int],       # indices of the two nearest waypoints.
    "distance_from_center": float,         # distance in meters from the track center
    "is_crashed": Boolean,                 # Boolean flag to indicate whether the agent has crashed.
    "is_left_of_center": Boolean,          # Flag to indicate if the agent is on the left side to the track center or not.
    "is_offtrack": Boolean,                # Boolean flag to indicate whether the agent has gone off track.
    "is_reversed": Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    "heading": float,                      # agent's yaw in degrees
    "objects_distance": [float, ],         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
    "objects_heading": [float, ],          # list of the objects' headings in degrees between -180 and 180.
    "objects_left_of_center": [Boolean, ], # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    "objects_location": [(float, float),], # list of object locations [(x,y), ...].
    "objects_speed": [float, ],            # list of the objects' speeds in meters per second.
    "progress": float,                     # percentage of track completed
    "speed": float,                        # agent's speed in meters per second (m/s)
    "steering_angle": float,               # agent's steering angle in degrees
    "steps": int,                          # number steps completed
    "track_length": float,                 # track length in meters.
    "track_width": float,                  # width of the track
    "waypoints": [(float, float), ]        # list of (x,y) as milestones along the track center

}
```

A more detailed technical reference of the input parameters is as follows.

#### all\_wheels\_on\_track
<a name="all_wheels_on_track"></a>

 **Type:** `Boolean`

 **Range:** `(True:False)`

A `Boolean` flag to indicate whether the agent is on-track or off-track. It’s off-track (`False`) if any of its wheels are outside of the track borders. It’s on-track (`True`) if all of the wheels are inside the two track borders. The following illustration shows that the agent is on-track.

![Image showing agent being on-track](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/all-wheels-on-track-001.png)

The following illustration shows that the agent is off-track.

![Image showing agent being off-track](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/all-wheels-on-track-002.png)

 **Example:** *A reward function using the `all_wheels_on_track` parameter*

```
def reward_function(params):
    #############################################################################
    '''
    Example of using all_wheels_on_track and speed
    '''

    # Read input variables
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']

    # Set the speed threshold based your action space
    SPEED_THRESHOLD = 1.0

    if not all_wheels_on_track:
        # Penalize if the car goes off track
        reward = 1e-3
    elif speed < SPEED_THRESHOLD:
        # Penalize if the car goes too slow
        reward = 0.5
    else:
        # High reward if the car stays on track and goes fast
        reward = 1.0

    return float(reward)
```

#### closest\_waypoints
<a name="closest_waypoints"></a>

 **Type:** `[int, int]`

 **Range:** `[(0:Max-1),(1:Max-1)]`

The zero-based indices of the two neighboring `waypoints` closest to the agent’s current position of `(x, y)`. The distance is measured by the Euclidean distance from the center of the agent. The first element refers to the closest waypoint behind the agent and the second element refers the closest waypoint in front of the agent. `Max` is the length of the waypoints list. In the illustration shown in [waypoints](#waypoints), the `closest_waypoints` would be `[16, 17]`.

 **Example:** A reward function using the `closest_waypoints` parameter.

The following example reward function demonstrates how to use `waypoints` and `closest_waypoints` as well as `heading` to calculate immediate rewards.

DeepRacer on AWS supports the following libraries: `math`, `random`, `NumPy`, `SciPy`, and `Shapely`. To use one, add an import statement above your function definition for the library you would like to use.

```
# Place import statement outside of function (supported libraries: math, random, numpy, scipy, and shapely)
# Example imports of available libraries
#
# import math
# import random
# import numpy
# import scipy
# import shapely

import math

def reward_function(params):
    ###############################################################################
    '''
    Example of using waypoints and heading to make the car point in the right direction
    '''

    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    # Initialize the reward with typical value
    reward = 1.0

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    return float(reward)
```

#### closest\_objects
<a name="closest_objects"></a>

 **Type:** `[int, int]`

 **Range:** `[(0:len(objects_location)-1), (0:len(objects_location)-1)]`

The zero-based indices of the two closest objects to the agent’s current position of (x, y). The first index refers to the closest object behind the agent, and the second index refers to the closest object in front of the agent. If there is only one object, both indices are 0.

#### distance\_from\_center
<a name="distance_from_center"></a>

 **Type:** `float`

 **Range:** `0:~track_width/2`

Displacement, in meters, between the agent center and the track center. The observable maximum displacement occurs when any of the agent’s wheels are outside a track border and, depending on the width of the track border, can be slightly smaller or larger than half the `track_width`.

![Image showing vehicle distance from center](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/distance-from-center-001.png)

 **Example:** *A reward function using the `distance_from_center` parameter*

```
def reward_function(params):
    #################################################################################
    '''
    Example of using distance from the center
    '''

    # Read input variable
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Penalize if the car is too far away from the center
    marker_1 = 0.1 * track_width
    marker_2 = 0.5 * track_width

    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    else:
        reward = 1e-3  # likely crashed/ close to off track

    return float(reward)
```

#### heading
<a name="heading"></a>

 **Type:** `float`

 **Range:** `-180:+180`

Heading direction, in degrees, of the agent with respect to the x-axis of the coordinate system.

![Image showing vehicle heading](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/heading-001.png)

 **Example:** See the [closest\_waypoints](#closest_waypoints) reward function for an example that uses the `heading` parameter.

#### is\_crashed
<a name="is_crashed"></a>

 **Type:** `Boolean`

 **Range:** `(True:False)`

A Boolean flag to indicate whether the agent has crashed into another object (`True`) or not (`False`) as a termination status.

#### is\_left\_of\_center
<a name="is_left_of_center"></a>

 **Type:** `Boolean`

 **Range:** `(True:False)`

A Boolean flag to indicate if the agent is on the left side to the track center (`True`) or on the right side (`False`).

#### is\_offtrack
<a name="is_offtrack"></a>

 **Type:** `Boolean`

 **Range:** `(True:False)`

A Boolean flag to indicate whether the agent has off track (`True`) or not (`False`) as a termination status.

#### is\_reversed
<a name="is_reversed"></a>

 **Type:** `Boolean`

 **Range:** `(True:False)`

A Boolean flag to indicate if the agent is driving on clock-wise (`True`) or counter clock-wise (`False`).

It’s used when you enable direction change for each episode.

#### objects\_distance
<a name="objects_distance"></a>

 **Type:** `[float, … ]`

 **Range:** `[(0:track_length), … ]`

A list of the distances between objects in the environment in relation to the starting line. The ith element measures the distance in meters between the ith object and the starting line along the track center line.

 **Note:** abs \| (var1) - (var2)\| = how close the car is to an object, WHEN var1 = ["objects\_distance"][index] and var2 = params["progress"]\*params["track\_length"]

To get an index of the closest object in front of the vehicle and the closest object behind the vehicle, use the `closest_objects` parameter.

#### objects\_heading
<a name="objects_heading"></a>

 **Type:** `[float, … ]`

 **Range:** `[(-180:180), … ]`

List of the headings of objects in degrees. The ith element measures the heading of the ith object. For stationary objects, their headings are 0. For a bot vehicle, the corresponding element’s value is the vehicle’s heading angle.

#### objects\_left\_of\_center
<a name="objects_left_of_center"></a>

 **Type:** `[Boolean, … ]`

 **Range:** `[True|False, … ]`

List of Boolean flags. The ith element value indicates whether the ith object is to the left (`True`) or right (`False`) side of the track center.

#### objects\_location
<a name="objects_location"></a>

 **Type:** `[(x,y), … ]`

 **Range:** `[(0:N,0:N), … ]`

List of all object locations, each location is a tuple of [[(x, y)]](#xy).

The size of the list equals the number of objects on the track. Note the object could be the stationary obstacles, moving bot vehicles.

#### objects\_speed
<a name="objects_speed"></a>

 **Type:** `[float, … ]`

 **Range:** `[[(0:12.0), … ], … ]`

List of speeds (meters per second) for the objects on the track. For stationary objects, their speeds are 0. For a bot vehicle, the value is the speed you set in training.

#### progress
<a name="progress"></a>

 **Type:** `float`

 **Range:** `0:100`

Percentage of track completed.

 **Example:** See the [steps](#steps) example for a reward function that uses the `progress` parameter.

#### speed
<a name="speed"></a>

 **Type:** `float`

 **Range:** `0.0:5.0`

The observed speed of the agent, in meters per second (m/s).

![Image showing agent speed](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/speed-001.png)

 **Example:** See the [all\_wheels\_on\_track](#all_wheels_on_track) example for a reward function that uses the `progress` parameter.

#### steering\_angle
<a name="steering_angle"></a>

 **Type:** `float`

 **Range:** `-30:30`

Steering angle, in degrees, of the front wheels from the center line of the agent. The negative sign (-) means steering to the right and the positive (\+) sign means steering to the left. The agent center line is not necessarily parallel with the track center line as is shown in the following illustration.

![Image showing agent steering angle](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/steering-angle-001.png)

 **Example:** *A reward function using the `steering_angle` parameter*

```
def reward_function(params):
    '''
    Example of using steering angle
    '''

    # Read input variable
    abs_steering = abs(params['steering_angle']) # We don't care whether it is left or right steering

    # Initialize the reward with typical value
    reward = 1.0

    # Penalize if car steer too much to prevent zigzag
    ABS_STEERING_THRESHOLD = 20.0
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)
```

#### steps
<a name="steps"></a>

 **Type:** `int`

 **Range:** `0:Nstep`

Number of steps completed. A step corresponds to an action taken by the agent following the current policy.

 **Example:** *A reward function using the `steps` parameter*

```
def reward_function(params):
    #############################################################################
    '''
    Example of using steps and progress
    '''

    # Read input variable
    steps = params['steps']
    progress = params['progress']

    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 300

    # Initialize the reward with typical value
    reward = 1.0

    # Give additional reward if the car pass every 100 steps faster than expected
    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward += 10.0

    return float(reward)
```

#### track\_length
<a name="track_length"></a>

 **Type:** `float`

 **Range:** `[0:Lmax]`

The track length in meters. `Lmax` is track-dependent.

#### track\_width
<a name="track_width"></a>

 **Type:** `float`

 **Range:** `0:Dtrack`

Track width in meters.

![Image showing track width](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/track-width-001.png)

 **Example:** *A reward function using the `track_width` parameter*

```
def reward_function(params):
    #############################################################################
    '''
    Example of using track width
    '''

    # Read input variable
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate the distance from each border
    distance_from_border = 0.5 * track_width - distance_from_center

    # Reward higher if the car stays inside the track borders
    if distance_from_border >= 0.05:
        reward = 1.0
    else:
        reward = 1e-3 # Low reward if too close to the border or goes off the track

    return float(reward)
```

#### x, y
<a name="xy"></a>

 **Type:** `float`

 **Range:** `0:N`

Location, in meters, of the agent center along the x and y axes, of the simulated environment containing the track. The origin is at the lower-left corner of the simulated environment.

![Image showing x-y coordinates of agent on track](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer-reward-function-input-x-y.png)

#### waypoints
<a name="waypoints"></a>

 **Type:** `list` of `[float, float]`

 **Range:** ` `

An ordered list of track-dependent `Max` milestones along the track center. For a looped track, the first and last waypoints are the same. For a straight or other non-looped track, the first and last waypoints are different.

![Image showing waypoints on track](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer-reward-function-input-waypoints.png)

### Sample reward functions
<a name="sample-reward-functions"></a>

 **Example 1: Follow the center line in time trials**

This example determines how far away the agent is from the center line, and gives higher reward if it is closer to the center of the track, encouraging the agent to closely follow the center line.

```
def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 3 markers that are increasingly further away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    return reward
```

 **Example 2: Stay inside the two borders in time trials**

This example simply gives high rewards if the agent stays inside the borders, and lets the agent figure out the best path to finish a lap. It’s easy to program and understand, but likely takes longer to converge.

```
def reward_function(params):
    '''
    Example of rewarding the agent to stay inside the two borders of the track
    '''

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the car is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0

    # Always return a float value
    return reward
```

 **Example 3: Prevent zig-zag in time trials**

This example incentivizes the agent to follow the center line but penalizes with lower reward if it steers too much, which helps prevent zig-zag behavior. The agent learns to drive smoothly in the simulator and likely keeps the same behavior when deployed to the physical vehicle.

```
def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle

    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)
```

 **Example 4: Stay in one lane without crashing into stationary obstacles or moving vehicles**

This reward function rewards the agent for staying inside the track’s borders and penalizes the agent for getting too close to objects in front of it. The agent can move from lane to lane to avoid crashes. The total reward is a weighted sum of the reward and penalty. The example gives more weight to the penalty in effort to avoid crashes. Experiment with different averaging weights to train for different behavior outcomes.

```
import math
def reward_function(params):
    '''
    Example of rewarding the agent to stay inside two borders
    and penalizing getting too close to the objects in front
    '''
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    objects_location = params['objects_location']
    agent_x = params['x']
    agent_y = params['y']
    _, next_object_index = params['closest_objects']
    objects_left_of_center = params['objects_left_of_center']
    is_left_of_center = params['is_left_of_center']

    # Initialize reward with a small number but not zero
    # because zero means off-track or crashed
    reward = 1e-3

    # Reward if the agent stays inside the two borders of the track
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward_lane = 1.0
    else:
        reward_lane = 1e-3

    # Penalize if the agent is too close to the next object
    reward_avoid = 1.0

    # Distance to the next object
    next_object_loc = objects_location[next_object_index]
    distance_closest_object = math.sqrt((agent_x - next_object_loc[0])**2 + (agent_y - next_object_loc[1])**2)

    # Decide if the agent and the next object is on the same lane
    is_same_lane = objects_left_of_center[next_object_index] == is_left_of_center
    if is_same_lane:
        if 0.5 <= distance_closest_object < 0.8:
            reward_avoid *= 0.5
        elif 0.3 <= distance_closest_object < 0.5:
            reward_avoid *= 0.2
        elif distance_closest_object < 0.3:
            reward_avoid = 1e-3  # Likely crashed

    # Calculate reward by putting different weights on
    # the two aspects above
    reward += 1.0 * reward_lane + 4.0 * reward_avoid
    return reward
```
