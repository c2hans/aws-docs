---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/configuring-cloud-watch-with-an-ec2-launch-type.html
---

# Configuring CloudWatch with an EC2 launch type
<a name="configuring-cloud-watch-with-an-ec2-launch-type"></a>

With an EC2 launch type, you provision an Amazon ECS cluster of EC2 instances that use the CloudWatch agent for logging and monitoring. An Amazon ECS optimized AMI comes pre-installed with the [Amazon ECS container agent](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_agent.html) and provides CloudWatch metrics for the Amazon ECS cluster.

These default metrics are included in the cost of Amazon ECS, but the default configuration for Amazon

ECS doesn't monitor log files or additional metrics (for example, free disk space). You can use the AWS Management Console to provision an Amazon ECS cluster with the EC2 launch type, this creates an AWS CloudFormation stack that deploys an Amazon EC2 Auto Scaling group with a launch configuration. However, this approach means that you can't choose a custom AMI or customize the launch configuration with different settings or additional boot up scripts.

To monitor additional logs and metrics, you must install the CloudWatch agent on your Amazon ECS container instances. You can use the installation approach for EC2 instances from the Installing the CloudWatch agent using Systems Manager Distributor and State Manager (p. 20) section of this guide. However, the Amazon ECS AMI doesn't include the required Systems Manager agent. You should use a custom launch configuration with a user data script that installs the Systems Manager agent when you create your Amazon ECS cluster. This allows your container instances to register with Systems Manager and apply the State Manager associations to install, configure, and update the CloudWatch agent. When State Manager runs and updates your CloudWatch agent configuration, it also applies your standardized systems-level CloudWatch configuration for Amazon EC2. You can also store standardized CloudWatch configurations for Amazon ECS in the S3 bucket for your CloudWatch configuration and automatically apply them with State Manager.

You should make sure that the IAM role or instance profile applied to your Amazon ECS container instances includes the required CloudWatchAgentServerPolicy and

AmazonSSMManagedInstanceCore policies. You can use the [ecs\_cluster\_with\_cloudwatch\_linux.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/examples/ecs/ecs_cluster_with_cloudwatch_linux.yaml)

AWS CloudFormation template to provision Linux-based Amazon ECS clusters. This template creates an Amazon ECS cluster with a custom launch configuration that installs Systems Manager and deploys a custom CloudWatch configuration to monitor log files specific to Amazon ECS.

You should capture the following logs for your Amazon ECS container instances, as well as your standard EC2 instance logs:
+ **Amazon ECS agent startup output** – /var/log/ecs/ecs-init.log
+ **Amazon ECS agent output** – /var/log/ecs/ecs-agent.log
+ **IAM credential provider requests log** – /var/log/ecs/audit.log

For more information about output level, formatting, and additional configuration options, see [Amazon ECS log file locations](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logs.html) in the Amazon ECS documentation.

## Important: Agent installation or configuration is not required for the Fargate launch type because you don't run or manage EC2 container instances.
<a name="important--agent-installation-or-configuration-is-not-required-for-the-fargate-launch-type-because-you-don-t-run-or-manage-ec2-container-instances..e0e87727-3c6a-51a1-b2cc-4c32ff7b50b6"></a>

Amazon ECS container instances should use the latest Amazon ECS optimized AMIs and container agent. AWS stores public Systems Manager Parameter Store parameters with Amazon ECS optimized AMI information, including the AMI ID. You can retrieve the latest most recently optimized AMI from the Parameter Store by using the [ Parameter Store parameter format](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/retrieve-ecs-optimized_AMI.html) for Amazon ECS optimized AMIs. You can refer to the public Parameter Store parameter that references the most recent AMI or a specific AMI release in your AWS CloudFormation templates.

AWS provides the same Parameter Store parameters in each supported Region. This means that AWS CloudFormation templates referencing these parameters can be reused across Regions and accounts without the AMI to be updated. You can control the deployment of newer Amazon ECS AMIs to your organization by referring to a specific release, which helps you prevent the use of a new Amazon ECS optimized AMI until you test it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
