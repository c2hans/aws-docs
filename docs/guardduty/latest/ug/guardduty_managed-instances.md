---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managed-instances.html
---

# GuardDuty Managed Instances Support
<a name="guardduty_managed-instances"></a>

The following table indicates the support that GuardDuty's various features have for the different types of managed instances.

| Managed Feature Type | [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html) support | [Malware Protection for EC2](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html) support |
| --- | --- | --- |
| [Amazon EKS Auto Mode](https://aws.amazon.com/eks/auto-mode/) | Supported | Supported |
| [Amazon ECS AWS Fargate Managed Instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ManagedInstances.html) | Unsupported | Supported |
| [Lambda Managed Instance](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html) | Unsupported | Unsupported |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
