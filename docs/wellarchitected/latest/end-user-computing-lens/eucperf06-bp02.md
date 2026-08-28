---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp02.html
---

# EUCPERF06-BP02 Minimize latency between EUC instances and dependent services
<a name="eucperf06-bp02"></a>

 In most cases, EUC users require connections to resources outside their EUC instances. Common dependencies include web or application servers, database servers, and storage services.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-16"></a>

When possible, deploy these dependencies in the same AWS Region and ideally the same Availability Zone. If the system of record must reside elsewhere, consider deploying caches or replicas. For example, if your Active Directory domain controllers are on your on-premises network, deploy replicas on Amazon EC2.

 When connecting to Amazon S3, use gateway VPC endpoints. For more information on configuring gateway endpoints, see [Gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
