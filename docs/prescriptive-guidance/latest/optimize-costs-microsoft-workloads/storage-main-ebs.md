---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-main-ebs.html
---

# Amazon EBS
<a name="storage-main-ebs"></a>

Amazon Elastic Block Store (Amazon EBS) is a fully managed block storage service that enables you to store persistent block-level storage volumes that you can use with Amazon Elastic Compute Cloud (Amazon EC2) instances. You can take advantage of several features in Amazon EBS to effectively manage and optimize your storage resources for Windows workloads in the cloud. For example, you can use Amazon EBS to provision the exact amount of IOPS and throughput that you require for your workload, select from a range of volume types to match your workload requirements, and use tools to identify and eliminate wasted storage resources. This granular control over storage performance and usage helps you optimize your storage resources while avoiding unnecessary costs.

This section covers the following topics:
+ [Migrate Amazon EBS volumes from gp2 to gp3](ebs-migrate-gp2-gp3.md)
+ [Modify Amazon EBS snapshots](ebs-migrate-ebs-snapshots.md)
+ [Delete unattached Amazon EBS volumes](ebs-delete-ebs-volumes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
