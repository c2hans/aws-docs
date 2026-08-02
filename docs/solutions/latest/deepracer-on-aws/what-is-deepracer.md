---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/what-is-deepracer.html
---

# What is DeepRacer?
<a name="what-is-deepracer"></a>

AWS DeepRacer is a fully autonomous 1/18th scale race car driven by reinforcement learning. It consists of the following components:

1.  **DeepRacer on AWS**: A customer-deployable machine learning solution for training and evaluating reinforcement learning models in a three-dimensional simulated autonomous-driving environment.

1.  **AWS DeepRacer vehicle**: A 1/18th scale RC car capable of running inference on a trained AWS DeepRacer model for autonomous driving.

<a name="deepracer-on-aws-console"></a> **DeepRacer on AWS**

DeepRacer on AWS is a customer-deployable platform for learning and applying reinforcement learning concepts. You can use the graphical user interface to train a reinforcement learning model and to evaluate the model performance in the AWS DeepRacer simulator. From the console, you can also download a trained model for deployment to your AWS DeepRacer vehicle for autonomous driving in a physical environment.

The DeepRacer on AWS console supports the following features:

1. Create a training job to train a reinforcement learning model with a specified reward function, optimization algorithm, environment, and hyperparameters.

1. Choose a simulated track to train and evaluate a model using SageMaker AI.

1. Clone a trained model to improve training by tuning hyperparameters to optimize your model’s performance.

1. Download a trained model for deployment to your AWS DeepRacer vehicle so it can drive in a physical environment.

1. Submit your model to a virtual race and have its performance ranked against other models in a virtual leaderboard.

When you use DeepRacer on AWS, you are charged based on your usage to train or evaluate and store models.

For details about pricing see the [Cost](cost.md) section.

<a name="deepracer-on-aws-vehicle"></a> **AWS DeepRacer vehicle**

The AWS DeepRacer vehicle is a Wi-Fi enabled, physical vehicle that can drive itself on a physical track by using a reinforcement learning model.

1. You can manually control the vehicle or deploy a model for the vehicle to drive autonomously.

1. The autonomous mode runs inference on the vehicle’s compute module. Inference uses images that are captured from the camera that is mounted on the front.

1. A Wi-Fi connection allows the vehicle to download software. The connection also allows the user to access the device console to operate the vehicle by using a computer or mobile device.

 **Topics**
+  [Explore reinforcement learning](explore-reinforcement-learning.md)
+  [Concepts and terminology](concepts-and-terminology.md)
