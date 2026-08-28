---
source_url: https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/protecting-data.html
---

# Protecting your Amazon FSx for OpenZFS data
<a name="protecting-data"></a>

Amazon FSx for OpenZFS provides you with the following options to further protect the data stored on your file systems:
+ **Built-in Amazon FSx backups** – Supports your backup retention and compliance needs within Amazon FSx, offering both automatic daily backups and user-initiated backups.
+ **Snapshots** – Enables your users to easily undo file changes and compare file versions by restoring files to previous versions.
+ **On-demand data replication** – Makes it easy to replicate datasets across file systems, within or across AWS Regions and accounts.
+ **AWS Backup** – Creates backups of your FSx for OpenZFS file system that work as part of a centralized and automated backup solution across AWS services in the cloud and on premises.

**Topics**
+ [Protect data with backups](using-backups.md)
+ [Protecting data with snapshots](snapshots-openzfs.md)
+ [Protect data with replication](on-demand-replication.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
