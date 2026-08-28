---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/aws-backup.html
---

# Using AWS Backup
<a name="aws-backup"></a>

[AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) is a web service that you can use to automate data backups and data protection across AWS services. Using this service, you can configure backup policies and monitor backup activity for your AWS resources in one place. AWS Backup supports cross-Region and cross-account backup and restore of data for Amazon DynamoDB, Amazon Simple Storage Service (Amazon S3), and other AWS services. For cross-account backup and restore of DynamoDB tables, the source and target accounts should be part of an AWS Organizations organization.

You can use backup and restore to copy a DynamoDB database across accounts. At a high level, the following steps are required to copy a DynamoDB table from the source account to the target account, where both the accounts are part of an organization.

1. Turn on the cross-account management feature in AWS Backup for both the accounts.

1. Create new backup vaults in the source and target accounts.

1. Create a new DynamoDB table backup from the source account.

1. After the backup job is completed, copy the backup from the source account to the target account.

1. Restore the backup in the target account.

For more detailed instructions, see the [Copy Amazon DynamoDB tables across accounts using AWS Backup](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-amazon-dynamodb-tables-across-accounts-using-aws-backup.html) pattern. For more information about AWS Backup for DynamoDB, see the [AWS documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorksAWS.html).

## Advantages
<a name="advantages.d7efb1f5-c807-56f9-be52-f1a190f3deaa"></a>
+ The process doesn't not consume DynamoDB read capacity units (RCUs) or write capacity units (WCUs).
+ No new code is required.
+ You can schedule the backup and restore process.

## Drawbacks
<a name="drawbacks.47289583-9670-5da0-9c0d-5d1493d954f8"></a>
+ Both source and target accounts should be part of an AWS Organizations organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
