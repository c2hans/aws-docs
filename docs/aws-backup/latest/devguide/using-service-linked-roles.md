---
source_url: https://docs.aws.amazon.com/aws-backup/latest/devguide/using-service-linked-roles.html
---

# Using service-linked roles for AWS Backup
<a name="using-service-linked-roles"></a>

AWS Backup uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#id_roles_terms-and-concepts). A service-linked role is a unique type of IAM role that is linked directly to AWS Backup. Service-linked roles are predefined by AWS Backup and include all the permissions that the service requires to call other AWS services on your behalf.

**Topics**
+ [Using roles to back up and copy](using-service-linked-roles-AWSServiceRoleForBackup.md)
+ [Using roles for AWS Backup Audit Manager](using-service-linked-roles-AWSServiceRoleForBackupReports.md)
+ [Using roles for restore testing](using-service-linked-roles-AWSServiceRoleForBackupRestoreTesting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
