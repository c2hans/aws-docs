---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/efs-automatic-backups-enabled.html
---

# efs-automatic-backups-enabled
<a name="efs-automatic-backups-enabled"></a>

Checks if an Amazon Elastic File System (Amazon EFS) file system has automatic backups enabled. The rule is NON\_COMPLIANT if `BackupPolicy.Status` is set to DISABLED.

**Identifier:** EFS\_AUTOMATIC\_BACKUPS\_ENABLED

**Resource Types:** AWS::EFS::FileSystem

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d695c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
