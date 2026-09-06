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
