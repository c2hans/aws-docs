---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables-SameAccount.html
---

# DynamoDB same-account global table
<a name="globaltables-SameAccount"></a>

Same-account global tables automatically replicate your DynamoDB table data across AWS Regions within a single AWS account. Same-account global tables provide the simplest model for running multi-Region applications because all replicas share the same account boundary, ownership, and permissions model. When you choose the AWS Regions for your replica tables, global tables handle all replication automatically. Global tables are available in all Regions where DynamoDB is available.

Same-account global tables provide the following benefits:
+ Replicate DynamoDB table data automatically across your choice of AWS Regions to locate data closer to your users
+ Enable higher application availability during regional isolation or degradation
+ Use built-in conflict resolution so you can focus on your application's business logic
+ When creating a same-account global table, you can choose either [Multi-Region eventual consistency (MREC)](V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes.mrec) or [Multi-Region strong consistency (MRSC)](V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes.mrsc)

**Topics**
+ [How DynamoDB global tables work](V2globaltables_HowItWorks.md)
+ [Tutorials: Creating global tables](V2globaltables.tutorial.md)
+ [DynamoDB global tables security](globaltables-security.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
