---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/protecting-data.html
---

# Protecting your data
<a name="protecting-data"></a>

Beyond automatically replicating your file system's data to ensure [high durability](high-availability-AZ.md), with Amazon FSx you also have the following options that you can use to further protect your data:
+ Native Amazon FSx volume backups that support your backup retention and compliance needs within Amazon FSx.
+ Using AWS Backup to implement a centrally managed, automated backup and retention strategy across multiple AWS services.
+ Snapshots that enable your users to easily undo unwanted file changes, by restoring files to previous versions.
+ Use SnapLock to create write once, read many (WORM) storage volumes to prevent file modification or deletion once committed, for a specified retention period.
+ FlexCache volumes offer storage efficient, cost effective, high-performance data replication for read-heavy workloads with data that remains largely unchanged.
+ Use SnapMirror to create scheduled, automatic file system replication to a second file system for data protection and disaster recovery.

**Topics**
+ [Protecting your data with volume backups](using-backups.md)
+ [Protecting your data with snapshots](snapshots-ontap.md)
+ [Protecting your data with Autonomous Ransomware Protection](ARP.md)
+ [Protecting your data with SnapLock](snaplock.md)
+ [Replicating your data with FlexCache](using-flexcache.md)
+ [Replicating your data using NetApp SnapMirror](scheduled-replication.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
