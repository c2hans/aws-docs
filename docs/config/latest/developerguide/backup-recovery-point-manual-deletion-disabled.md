---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/backup-recovery-point-manual-deletion-disabled.html
---

# backup-recovery-point-manual-deletion-disabled
<a name="backup-recovery-point-manual-deletion-disabled"></a>

Checks if a backup vault has an attached resource-based policy which prevents deletion of recovery points. The rule is NON\_COMPLIANT if the Backup Vault does not have resource-based policies or has policies without a suitable 'Deny' statement (statement with backup:DeleteRecoveryPoint, backup:UpdateRecoveryPointLifecycle, and backup:PutBackupVaultAccessPolicy permissions).

**Note**
**Wildcard required for `"Resource"` and `"Principal"` of the Deny statement**
The rule requires that the `"Resource"` and `"Principal"` of the Deny statement must have a wildcard in the [vault access policy](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-a-vault-access-policy.html). Otherwise, the rule returns NON\_COMPLIANT.

**Identifier:** BACKUP\_RECOVERY\_POINT\_MANUAL\_DELETION\_DISABLED

**Resource Types:** AWS::Backup::BackupVault

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

principalArnList (Optional)Type: CSV
Comma-separated list of AWS Identity and Access Management (IAM) Amazon Resource Names (ARNs) for the rule to NOT check.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d251c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
