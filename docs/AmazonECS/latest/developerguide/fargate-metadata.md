---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-metadata.html
---

# Amazon ECS task metadata available for tasks on Fargate
<a name="fargate-metadata"></a>

Amazon ECS on Fargate provides a method to retrieve various metadata, network metrics, and [Docker stats](https://docs.docker.com/reference/api/engine/latest/#tag/Container/operation/ContainerStats) about your containers and the tasks they are a part of. This is referred to as the *task metadata endpoint*. The following task metadata endpoint versions are available for Amazon ECS on Fargate tasks:
+ Task metadata endpoint version 4 – Available for tasks that use platform version 1.4.0 or later.
+ Task metadata endpoint version 3 – Available for tasks that use platform version 1.1.0 or later.

All containers belonging to tasks that are launched with the `awsvpc` network mode receive a local IPv4 address within a predefined link-local address range. When a container queries the metadata endpoint, the container agent can determine which task the container belongs to based on its unique IP address, and metadata and stats for that task are returned.

**Topics**
+ [Amazon ECS task metadata endpoint version 4 for tasks on Fargate](task-metadata-endpoint-v4-fargate.md)
+ [Amazon ECS task metadata endpoint version 3 for tasks on Fargate](task-metadata-endpoint-v3-fargate.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
