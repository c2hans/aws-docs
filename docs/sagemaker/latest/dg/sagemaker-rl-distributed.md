---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-rl-distributed.html
---

# Distributed Training with Amazon SageMaker AI RL
<a name="sagemaker-rl-distributed"></a>

Amazon SageMaker AI RL supports multi-core and multi-instance distributed training. Depending on your use case, training and/or environment rollout can be distributed. For example, SageMaker AI RL works for the following distributed scenarios:
+ Single training instance and multiple rollout instances of the same instance type. For an example, see the Neural Network Compression example in the [SageMaker AI examples repository](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/reinforcement_learning).
+ Single trainer instance and multiple rollout instances, where different instance types for training and rollouts. For an example, see the AWS DeepRacer / AWS RoboMaker example in the [SageMaker AI examples repository](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/reinforcement_learning).
+ Single trainer instance that uses multiple cores for rollout. For an example, see the Roboschool example in the [SageMaker AI examples repository](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/reinforcement_learning). This is useful if the simulation environment is light-weight and can run on a single thread.
+ Multiple instances for training and rollouts. For an example, see the Roboschool example in the [SageMaker AI examples repository](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/reinforcement_learning).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
