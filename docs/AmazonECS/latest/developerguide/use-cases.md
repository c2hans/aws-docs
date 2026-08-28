---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/use-cases.html
---

# Amazon ECS task definition use cases
<a name="use-cases"></a>

Learn more about how to write task definitions for various AWS services and features.

Depending on your workload, there are certain task definition parameters that need to be set. Also for EC2, you have to choose specific instances that are engineered for the workload.

**Topics**
+ [Amazon ECS task definitions for GPU workloads](ecs-gpu.md)
+ [Amazon ECS task definitions for video transcoding workloads](ecs-vt1.md)
+ [Amazon ECS task definitions for AWS Neuron machine learning workloads](ecs-inference.md)
+ [Amazon ECS task definitions for deep learning instances](ecs-dl1.md)
+ [Amazon ECS task definitions for 64-bit ARM workloads](ecs-arm64.md)
+ [Send Amazon ECS logs to CloudWatch](using_awslogs.md)
+ [Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md)
+ [Using non-AWS container images in Amazon ECS](private-auth.md)
+ [Restart individual containers in Amazon ECS tasks with container restart policies](container-restart-policy.md)
+ [Pass sensitive data to an Amazon ECS container](specifying-sensitive-data.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
