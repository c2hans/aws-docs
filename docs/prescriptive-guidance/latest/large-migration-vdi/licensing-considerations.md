---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-vdi/licensing-considerations.html
---

# Licensing considerations for large VDI migrations
<a name="licensing-considerations"></a>

When planning a large VDI migration to AWS, validate your licensing agreements for the operating system and software that you plan to use on the target VDI.

If you're planning to use your own license for the operating system, give special consideration to the potential impacts this can have. Under standard terms, Microsoft requires that you deploy Windows on hardware that is dedicated to your organization, such as a dedicated Amazon Elastic Compute Cloud (Amazon EC2) instance. Similar licensing agreements can apply to Microsoft Office or Microsoft 365.

If your organization has customized enterprise licensing agreements, get confirmation from the licensing team. Understanding your licensing agreements is vital to the successful planning of the migration.

Although bringing your own license might be more cost effective from a license perspective, it might not be cost-effective from a compute perspective. If dedicated hosts would be required for compliance with your licensing agreements, we recommend that you conduct a cost-benefit analysis.

For Microsoft operating systems and software, we recommend that you take advantage of an [AWS Optimization and Licensing Assessment (AWS OLA)](https://aws.amazon.com/optimization-and-licensing-assessment/) to assess on-premises or cloud workloads. AWS OLA makes optimized suggestions for the right EC2 instances for your workloads, but it also reviews your Microsoft licensing position. AWS OLA can help you reduce compute and licensing costs.

For more information about Microsoft licensing requirements and how to request a copy of your Microsoft License Statement (MLS), see [Microsoft licensing on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-microsoft-workloads-aws/licensing-microsoft-workloads.html) in AWS Prescriptive Guidance.
