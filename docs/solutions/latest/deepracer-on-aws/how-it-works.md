---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/how-it-works.html
---

# How DeepRacer works
<a name="how-it-works"></a>

The AWS DeepRacer vehicle is a 1/18th scale vehicle that can autonomously drive along a track by itself or race against another vehicle. The vehicle can be equipped with various sensors that include a front-facing camera, stereo cameras, radar, or LiDAR. The sensors collect data about the environment the vehicle operates in. Different sensors provide the view at different scales.

DeepRacer on AWS uses reinforcement learning to enable autonomous driving for the AWS DeepRacer vehicle. To achieve this, you train and evaluate a reinforcement learning model in a virtual environment with a simulated track. After the training, you upload the trained model artifacts to your AWS DeepRacer vehicle. You can then set the vehicle for autonomous driving in a physical environment with a real track.

Training a reinforcement learning model can be challenging, especially if you’re new to the field. DeepRacer on AWS simplifies the process by integrating required components together and providing easy-to-follow wizard-like task templates. However, it’s helpful to have a good understanding of the basics of reinforcement learning training implemented in DeepRacer on AWS.

 **Topics**
+  [Reinforcement learning overview](reinforcement-learning-overview.md)
+  [Action space and reward function](action-space-reward-function.md)
+  [Training algorithms](training-algorithms.md)
+  [User workflow](user-workflow.md)
+  [Simulated-to-real performance gaps](simulated-to-real-gaps.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
