---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/run-bluage-modernized-mainframes/faq.html
---

# FAQ
<a name="faq"></a>

## What performance controls are available for modernized mainframe workloads?
<a name="faq1"></a>

You can adjust the following to fine-tune the performance of your modernized mainframe workload in the AWS Cloud:
+ Adjust the compute resource reservations and limits for the Amazon Elastic Container Service (Amazon ECS) tasks through the task definitions. This controls the memory and CPU resources available to the container.
+ Adjust the Java command line options, such as the maximum heap size and database tuning parameters.
+ Adjust the size of the ephemeral storage available to the container if you need more than the default, which is 20 GiB.
+ Use indexes to optimize queries for Amazon Aurora PostgreSQL-Compatible Edition.

## What are the limitations of the architecture?
<a name="faq2"></a>

The following are the limitations of this architecture:
+ Resource limits apply to Amazon ECS tasks hosted on AWS Fargate. For more information, see [Task resource limits](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html#fargate-resource-limits) in the Amazon ECS documentation*.*
+ The maximum amount of ephemeral storage that can be allocated is 200 GiB. For more information, see [Fargate task storage](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-storage.html) in the Amazon ECS documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
