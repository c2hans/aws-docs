---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/backup_restore-nouns_verbs.html
---

# Back up and restore: concepts
<a name="backup_restore-nouns_verbs"></a>

| Noun | Description | APIs (Verbs) |
| --- | --- | --- |
| Backup retention period | A period of time between 1 and 35 days for which you can perform a point-in-time restore. | `create-db-cluster`<br />`modify-db-cluster`<br />`restore-db-cluster-to-point-in-time` |
| Amazon DocumentDB storage volume | Highly available and highly durable storage volume that replicates data six ways across three Availability Zones. An Amazon DocumentDB cluster is highly durable regardless of the number of instances in the cluster. | `create-db-cluster`<br />`delete-db-cluster` |
| Backup window | Period of time in the day in which automatic snapshots are taken. | `create-db-cluster`<br />`describe-db-cluster`<br />`modify-db-cluster` |
| Automatic snapshot | Daily snapshots that are full backups of cluster and are automatically created by the continuous backup process in Amazon DocumentDB. | `restore-db-cluster-from-snapshot`<br />`describe-db-cluster-snapshot-attributes`<br />`describe-db-cluster-snapshots` |
| Manual snapshot | Snapshots you create manually to retain full backups of a cluster beyond the backup period. | `create-db-cluster-snapshot`<br />`copy-db-cluster-snapshot`<br />`delete-db-cluster-snapshot`<br />`describe-db-cluster-snapshot-attributes`<br />`describe-db-cluster-snapshots`<br />`modify-db-cluster-snapshot-attribute` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
