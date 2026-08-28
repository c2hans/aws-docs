---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_data_a6.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS04-BP05 Remove unneeded or redundant data
<a name="sus_sus_data_a6"></a>

 Duplicate data only when necessary to minimize total storage consumed. Use backup technologies that deduplicate data at the file and block level. Limit the use of Redundant Array of Independent Drives (RAID) configurations except where required to meet Service Level Agreements (SLAs).

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use mechanisms that can deduplicate data at the block and object level.
+  Use backup technology that can make incremental backups and deduplicate data at the block, file, and object level.
+  Use RAID only when required to meet your SLAs.
+  Centralize log and trace data, deduplicate identical log entries, and establish mechanisms to tune verbosity when needed.
+  Pre-populate caches only where justified.
+  Establish cache monitoring and automation to resize cache accordingly.
+  Remove out-of-date deployments and assets from object stores and edge caches when pushing new versions of your workload.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)
+  [Change log data retention in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention)
+  [Data deduplication on Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-data-dedup.html)
+  [Features of Amazon FSx for ONTAP including data deduplication](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html#features-overview)
+  [Invalidating Files on Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html)
+  [Using AWS Backup to back up and restore Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html)
+  [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
+  [Working with backups on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)

 **Related examples:**
+  [Lab: Optimize Data Pattern Using Amazon Redshift Data Sharing](https://wellarchitectedlabs.com/sustainability/300_labs/300_optimize_data_pattern_using_redshift_data_sharing/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
