---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html
---

# Partitions
<a name="partitions"></a>

 AWS groups Regions into [partitions](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html). Every Region is in exactly one partition, and each partition has one or more Regions. Partitions have independent instances of AWS Identity and Access Management (IAM) and provide a hard boundary between Regions in different partitions. AWS commercial Regions are in the `aws` partition, Regions in China are in the `aws-cn` partition, and AWS GovCloud Regions are in the `aws-us-gov` partition. Some AWS services are designed to provide cross-Region functionality, such as [Amazon S3 Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario) or [AWS Transit Gateway Inter-Region peering](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html). These types of capabilities are only supported between Regions in the same partition. You cannot use IAM credentials from one partition to interact with resources in a different partition.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
