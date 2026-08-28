---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/logging-and-monitoring-on-amazon-ecs.html
---

# Logging and monitoring on Amazon ECS
<a name="logging-and-monitoring-on-amazon-ecs"></a>

Amazon Elastic Container Service (Amazon ECS) provides [two launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) for running containers and that determine the type of infrastructure that host tasks and services; these launch types are AWS Fargate and Amazon EC2. Both launch types integrate with CloudWatch but configurations and support vary.

The following sections help you understand how to use CloudWatch for logging and monitoring on Amazon ECS.

**Topics**
+ Configuring CloudWatch with an EC2 launch type
+ Amazon ECS container logs for EC2 and Fargate launch types
+ Using custom log routing with FireLens for Amazon ECS
+ Metrics for Amazon ECS

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
