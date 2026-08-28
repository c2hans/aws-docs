---
source_url: https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html
---

# Backup vaults
<a name="vaults"></a>

In AWS Backup, a *backup vault* is a container that stores and organizes your backups.

When creating a backup vault, you must specify the AWS Key Management Service (AWS KMS) encryption key that encrypts some of the backups placed in this vault. Encryption for other backups is managed by their source AWS services. For more information about encryption, see the chart in [Encryption for backups in AWS](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html).

The following sections provide an overview of how to manage your backup vaults in AWS Backup.

**Topics**
+ [Backup vault creation and deletion](create-a-vault.md)
+ [Logically air-gapped vault](logicallyairgappedvault.md)
+ [Vault access policies](create-a-vault-access-policy.md)
+ [AWS Backup Vault Lock](vault-lock.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
