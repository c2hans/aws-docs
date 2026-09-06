---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/audit.html
---

# Step 8. Audit backup configuration
<a name="audit"></a>

To ensure that the backup program is performing as it should and to identify and correct any anomalies from backup processes, audit the compliance of AWS Backup policies against defined controls such as defined backup frequency. To find and investigate backup operations or resources that are not compliant with your business requirements, continuously and automatically track your backup activity and generate automatic reports.

[AWS Backup Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html) provides built-in, customizable compliance controls that align with your business compliance and regulatory requirements. You can use [prebuilt and customizable](https://docs.aws.amazon.com/aws-backup/latest/devguide/choosing-controls.html) controls as audit frameworks to evaluate your AWS Backup practices. The controls include:
+ Backup resources protected by backup plans
+ Backup plan minimum frequency and minimum retention
+ Backup recovery point encrypted
+ Backup recovery point manual deletion
+ Backup recovery point minimum retention
+ Cross-Region copy
+ Cross-account copy
+ Backup Vault Lock

For infrastructure as-code (IaC) automation, you can use [AWS Backup Audit Manager with AWS CloudFormation](https://docs.aws.amazon.com/aws-backup/latest/devguide/bam-cfn-integration.html).

[AWS Security Hub](https://aws.amazon.com/security-hub/) provides you with a comprehensive view of your security state in AWS. It also helps you check your environment against security best practices and industry standards such as [AWS Foundational Security Best Practices controls](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html). If you use Security Hub within your cloud environment, we recommend you enable the AWS Foundational Security Best Practices standard, because it includes detective controls that can help with securing backups in AWS. Most of the detective controls in AWS Backup Audit Manager and Security Hub are also available as [AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html).
