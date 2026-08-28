---
source_url: https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-iam.html
---

# Identity and access management in AWS Backup
<a name="backup-iam"></a>

Access to AWS Backup requires credentials. Those credentials must have permissions to access AWS resources, such as an Amazon DynamoDB database or an Amazon EFS file system. Moreover, recovery points created by AWS Backup for some AWS Backup-supported services cannot be deleted using the source service (such as Amazon EFS). You can delete those recovery points using AWS Backup.

The following sections provide details on how you can use [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) and AWS Backup to help secure access to your resources.

**Warning**
AWS Backup uses the same IAM role that you chose when assigning resources to manage your recovery point lifecycle. If you delete or modify that role, AWS Backup cannot manage your recovery point lifecycle. When this occurs, it will attempt to use a service-linked role to manage your lifecycle. In a small percentage of cases, this might also not work, leaving `EXPIRED` recovery points on your storage, which might create unwanted costs. To delete `EXPIRED` recovery points, manually delete them using the procedure in [Deleting backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-backups.html).

**Topics**
+ [Authentication](authentication.md)
+ [Access control](access-control.md)
+ [IAM service roles](iam-service-roles.md)
+ [Managed policies for AWS Backup](security-iam-awsmanpol.md)
+ [Using service-linked roles for AWS Backup](using-service-linked-roles.md)
+ [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
