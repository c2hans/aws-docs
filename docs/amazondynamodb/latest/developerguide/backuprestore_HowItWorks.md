---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorks.html
---

# Using on-demand DynamoDB backup and restore
<a name="backuprestore_HowItWorks"></a>

Amazon DynamoDB supports stand-alone on-demand backup and restore features. Those features are available to you independent of whether you use AWS Backup.

You can use the DynamoDB on-demand backup capability to create full backups of your tables for long-term retention and archival for regulatory compliance needs. You can back up and restore your table data anytime with a single click on the AWS Management Console or with a single API call. Backup and restore actions run with zero impact on table performance or availability.

You can create table backups using the console, the AWS Command Line Interface (AWS CLI), or the DynamoDB API. For more information, see [Backing up a DynamoDB table](Backup.Tutorial.md).

For information about restoring a table from a backup, see [Restoring a DynamoDB table from a backup](Restore.Tutorial.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
