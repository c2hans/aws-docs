---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch-type-external.html
---

# External (Amazon ECS Anywhere) for Amazon ECS
<a name="launch-type-external"></a>

Amazon ECS Anywhere provides support for registering an *external instance* such as an on-premises server or virtual machine (VM), to your Amazon ECS cluster. External instances are optimized for running applications that generate outbound traffic or process data. If your application requires inbound traffic, the lack of Elastic Load Balancing support makes running these workloads less efficient. Amazon ECS added a new `EXTERNAL` launch type that you can use to create services or run tasks on your external instances.

The following provides a high-level system architecture overview of Amazon ECS Anywhere. Your on-premises server has both the Amazon ECS agent and the SSM agent installed.

![Diagram showing the architecture of Amazon ECS Anywhere.](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/images/overview-ecsanywhere.png)

For more information, see [Amazon ECS clusters for external instances](ecs-anywhere.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
