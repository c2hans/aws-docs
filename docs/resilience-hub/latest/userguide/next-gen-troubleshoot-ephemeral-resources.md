---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-ephemeral-resources.html
---

# EC2 instances or ECS tasks not appearing as billable resources
<a name="next-gen-troubleshoot-ephemeral-resources"></a>

When a parent resource (such as an Auto Scaling group, ECS service, or EKS deployment) manages an EC2 instance, ECS task, EKS pod, or network interface, Next generation Resilience Hub classifies that resource as *ephemeral*. Ephemeral resources are transient. The parent resource replaces them automatically through lifecycle events. Next generation Resilience Hub assesses them through their parent, not independently.

The following resource types are ephemeral when managed by a parent:

| Resource type | Example parent |
| --- | --- |
| `AWS::EC2::Instance` | Auto Scaling group or EKS node group |
| `AWS::ECS::Task` | ECS service |
| `AWS::EKS::Pod` | EKS deployment or replica set |
| `AWS::EC2::NetworkInterface` | EC2 instance managed by Auto Scaling |

Standalone instances of these types (not managed by a parent) remain billable.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
