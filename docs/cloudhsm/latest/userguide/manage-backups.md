---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-backups.html
---

# Cluster backups in AWS CloudHSM
<a name="manage-backups"></a>

 AWS CloudHSM makes periodic backups of your cluster at least once every 24 hours. Each backup contains encrypted copies of the following data:
+ Users (COs, CUs, and AUs)
+ Key material and certificates
+ Hardware security module (HSM) configuration and policies

 You can't instruct the service to make backups, but you can take certain actions that force the service to create a backup. The service makes a backup when you perform any of the following actions:
+ Activate a cluster
+ Add an HSM to an active cluster
+ Remove an HSM from an active cluster

AWS CloudHSM deletes backups based on the backup retention policy you set when you create clusters. For information about managing backup retention policy, see [Configure backup retention](manage-backup-retention.md).

**Topics**
+ [Working with backups](backups-using.md)
+ [Delete backups](delete-restore-backup.md)
+ [Restore backups](restore-backup.md)
+ [Configure backup retention](manage-backup-retention.md)
+ [Copying backups across Regions](copy-backup-to-region.md)
+ [Working with shared backups](sharing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
