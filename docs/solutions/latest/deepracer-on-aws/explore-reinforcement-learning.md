---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/explore-reinforcement-learning.html
---

# Explore reinforcement learning
<a name="explore-reinforcement-learning"></a>

Reinforcement learning, especially deep reinforcement learning, has proven effective in solving a wide array of autonomous decision-making problems. It has applications in financial trading, data center cooling, fleet logistics, and autonomous racing, to name a few.

Reinforcement learning has the potential to solve real-world problems. However, it has a steep learning curve because of its extensive technological scope and depth. Real-world experimentation requires that you construct a physical agent, such as an autonomous racing car. It also requires that you secure a physical environment, such as a driving track or public road. The environment can be costly, hazardous, and time-consuming. These requirements go beyond merely understanding reinforcement learning.

To help reduce the learning curve, DeepRacer on AWS simplifies the process in three ways:

1. Offering step-by-step guidance when training and evaluating reinforcement learning models. The guidance includes pre-defined environments, states, and actions, and customizable reward functions.

1. Providing a simulator to emulate interactions between a virtual agent and a virtual environment.

1. Using an AWS DeepRacer vehicle as a physical agent. Use the vehicle to evaluate a trained model in a physical environment. This closely resembles a real-world use case.

If you are a seasoned machine learning practitioner, you will find DeepRacer on AWS a welcome opportunity to build reinforcement learning models for autonomous racing in both virtual and physical environments. To summarize, use DeepRacer on AWS to create reinforcement learning models for autonomous racing with the following steps:

1. Train a custom reinforcement learning model for autonomous racing.

1. Use the simulator to evaluate a model and test autonomous racing in a virtual environment.

1. Deploy a trained model to an AWS DeepRacer to test autonomous racing in a physical environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
