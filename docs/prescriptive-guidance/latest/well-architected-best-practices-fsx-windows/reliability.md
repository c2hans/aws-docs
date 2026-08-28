---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/well-architected-best-practices-fsx-windows/reliability.html
---

# Reliability pillar
<a name="reliability"></a>

The reliability pillar of the AWS Well-Architected Framework focuses on the ability of workloads to perform their intended functions and recover quickly from failure to meet demands. The following recommendations can help you meet the reliability design principles and architectural best practices for Amazon FSx for Windows File Server.

**Key focus areas**
+ Distributed system design
+ Recovery planning
+ Adapting to changing requirements

## Automatically recover from failure
<a name="automatically-recover-from-failure"></a>
+ Make sure that your IP subnet allocation accounts for expansion and availability.
+ Deploy your Amazon FSx for Windows File Server file system across multiple Availability Zones. For more information, see [Availability and durability: Single-AZ and Multi-AZ file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html) in the Amazon FSx documentation.
+ Replicate your FSx for Windows File Server file system across multiple AWS Regions. For more information, see the AWS blog post [How to replicate Amazon FSx for Windows File Server data across AWS Regions](https://aws.amazon.com/blogs/storage/how-to-replicate-amazon-fsx-file-server-data-across-aws-regions/).
+ Enable shadow copies for your file system so users can view and restore individual files or folders from an earlier snapshot in Windows File Explorer. For more information, see the blog post [Automating shadow copies configuration on Amazon FSx for Windows File Server](https://aws.amazon.com/blogs/storage/enabling-microsoft-shadow-copies-with-amazon-fsx-for-windows-file-server/).

## Test recovery procedures
<a name="test-recovery-procedures"></a>
+ Practice restoring your file systems from backups. For more information, see [Working with backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html) in the Amazon FSx documentation.
+ Test failover on a Multi-AZ file system by modifying throughput.

## Scale horizontally to increase aggregate workload availability, and don't guess capacity
<a name="scale-horizontally-to-increase-aggregate-workload-availability-and-don-t-guess-capacity"></a>
+ Automatically scale storage and throughput capacity for your FSx for Windows File Server file systems based on utilization metrics. For more information, see:
  + [Increasing the storage capacity of an FSx for Windows File Server file system dynamically ](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html#automate-storage-capacity-increase)in the Amazon FSx documentation.
  + [How to modify throughput capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-throughput-capacity.html#increase-throughput-capacity) in the Amazon FSx documentation.
  + [Amazon FSx for Windows File Server - Automatic Storage and Throughput Capacity Scaling](https://www.youtube.com/watch?v=1p0tnll1l14) on the AWS YouTube channel.

## Manage change in automation
<a name="manage-change-in-automation"></a>
+ Apply infrastructure as a code (IaC) to deploy your FSx for Windows File Server file systems. You can use the [Amazon FSx for Windows File Server Quick Start](https://github.com/aws-quickstart/quickstart-fsx-windows-file-server) to implement your file system on AWS.
+ Automate FSx for Windows File Server operational procedures whenever possible. For example, it's a best practice to automate tasks such as [turning on user storage quotas in Track mode and data deduplication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/admin-best-practices-fsxw.html).

## Manage quotas and constraints
<a name="manage-quotas-and-constraints"></a>
+ Monitor and manage FSx for Windows File Server quotas. For more information, watch the [View and manage quotas for AWS services using service quotas](https://www.youtube.com/watch?v=ZTwfIIf35Wc) video on the AWS YouTube channel.
+ Make sure that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover.
+ Accommodate fixed service quotas and constraints through your architecture.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
