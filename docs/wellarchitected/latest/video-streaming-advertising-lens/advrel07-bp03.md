---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel07-bp03.html
---

# ADVREL07-BP03 Back up data in multiple locations with consideration for your regulatory or legal requirements
<a name="advrel07-bp03"></a>

 Back up data in multiple locations, and consider how consumer privacy laws may impact your data replication and storage plans.

## Implementation guidance
<a name="implementation-guidance-33"></a>

 Select AWS Regions for backup locations that satisfy your legal and business requirements. Consider how consumer privacy laws may impact your ability to replicate data which could contain personal data. Be aware of how countries where your workload operates regulate advertising and related data, and seek legal consultation when you are unsure of how regulations might apply to your workload. Use your understanding of those regulations to select AWS services and Regions. Seek legal counsel when in doubt.

## Key AWS services
<a name="key-aws-services-19"></a>
+  [AWS Backup](https://aws.amazon.com/backup/)
+  [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)

## Resources
<a name="resources-28"></a>
+  [Cloud security guidance](https://www.ncsc.gov.uk/collection/cloud)
+  [Protecting your data with backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html)
+  [Amazon DynamoDB now helps you meet regulatory compliance and business continuity requirements through enhanced backup features in AWS Backup](https://aws.amazon.com/about-aws/whats-new/2021/11/amazon-dynamodb-requirements-aws-backup/index.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
