---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/top-recommendations.html
---

# Top recommendations for optimizing costs
<a name="top-recommendations"></a>

## Overview
<a name="top-recommendations-overview"></a>

Cost optimization is one of the pillars of the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc) and it plays a critical role in your cloud migration plans. You will find recommendations for cost optimizations throughout this guide, but this section calls out the highest-impact recommendations. You can implement these recommendations quickly and they will have a significant impact on your organization. These recommendations can help lay the groundwork for your entire cost optimization effort.

## Top recommendations
<a name="top-recommendations-main"></a>

The following table lists the top recommendations for the highest-impact cost optimizations. The "Difficultly to implement" column rates each optimization based on a scale of what's easiest to implement (1) to what's most difficult to implement (5). The "Estimated savings" column shows a percentage-based estimate of how much your organization can save for each recommended optimization.

|
|
| Optimizations | Difficulty to implement | Estimated savings |
| --- |--- |--- |
| [Rightsize Windows workloads by using AWS Compute Optimizer](rightsize.md) | 3 | 25% |
| [Bring licenses for Windows and SQL Server workloads by using Amazon EC2 Dedicated Hosts](byol-ded-hosts.md) | 3 | 30% |
| [Remove SQL Server costs for non-production workloads by using SQL Server Developer Edition](sql-server-dev.md) | 2 | 20% |
| [Optimize SQL Server licensing on AWS](sql-server-licensing.md) | 2 | Up to 50% |
| [Control workloads by using the Instance Scheduler on AWS for Amazon EC2](windows-ec2-schedules.md) | 3 | Up to 40% |
| [Select the right instance type for Windows workloads](right-size-selection.md) | 1 | 10–30% |
| [Refactor to modern .NET and move to Linux](net-refactor-linux.md) | 5 | 10–20% |
| [Optimize EC2 instances for Windows by using Savings Plans](savings-plans.md) | 3 | Up to 20–40% |
| [Migrate Amazon Elastic Block Store (Amazon EBS) volumes from gp2 to gp3 to optimize costs](ebs-migrate-gp2-gp3.md) | 4 | Up to 20% |

**Important**
The estimated savings in the preceding table apply to each individual technical domain, not overall AWS spend within an account. For example, you can implement the Instance Scheduler in a variety of environment types and sizes that can alter the potential savings. The estimates apply specifically to Amazon EC2 instance costs and don't imply any overall savings for other AWS services. These estimates are provided as a gauge, not a guarantee.

MACO experts are available to talk about cost optimizations in more depth. To set up a meeting for a deep dive into your use case, contact your account team or email optimize-microsoft@amazon.com.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
