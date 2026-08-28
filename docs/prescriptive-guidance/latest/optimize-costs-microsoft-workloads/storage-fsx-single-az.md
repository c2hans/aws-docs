---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-fsx-single-az.html
---

# Use a single Availability Zone
<a name="storage-fsx-single-az"></a>

## Overview
<a name="storage-fsx-single-az-overview"></a>

This section explains when it's more beneficial to use a single Availability Zone implementation of [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html). It covers scenarios where moving to a single Availability Zone reduces costs, while still enabling you to use Amazon FSx for Windows File Server as your managed file storage service. We recommend that you implement a single Availability Zone for Amazon FSx for production workloads. This can help ensure that you have the redundancy of multiple Availability Zones.

## Cost impact
<a name="storage-fsx-single-az-cost"></a>

A single Availability Zone file system offers an approximately 40 percent cost reduction compared to a multiple Availability Zone implementation. With a multiple Availability Zone file system, you pay $0.230 per GB-month in SSD and $0.025 per GB-month in HDD compared to $0.130 per GB-month for SSD and $0.013 per GB-month for HDD on a single Availability Zone file system. You can see a comparison of costs and create your own estimates by using the [AWS Pricing Calculator](https://calculator.aws/#/).

For a 10 TB file system this can be a difference of paying approximately $1,200 per month for multiple Availability Zones or $680 per month for a single Availability Zone. This [example](https://calculator.aws/#/estimate?id=3339ba60d065a76ecfcaa1770450214534941c8f) uses a 10 TB FSx for Windows File Server file system with SSD. The estimated savings for deduplication is 50 percent. Overall, a single Availability Zone has a lower cost of entry but comes with a few caveats that are covered in the next section.

## Cost optimization recommendations
<a name="storage-fsx-single-az-rec"></a>

### Single Availability Zone deployments
<a name="single-availability-zone-deployments.1e60fda5-56c4-5f09-8966-4421cbef65af"></a>

To make sure that a single Availability Zone is the right fit, take into consideration your own internal SLAs for the data being stored on FSx for Windows File Server. This entails understanding if you have SLAs to provide to your customers (internal and external) and if the three nines of availability for an Amazon FSx single Availability Zone will still allow you to meet those SLAs. FSx for Windows File Server with a single Availability Zone still has an uptime of 99.9 percent. The SLA for Amazon FSx for multiple Availability Zones is greater than 99.99 percent. For mission-critical workloads, we recommend that you use multiple Availability Zones over a single Availability Zone, even at additional cost.

Single Availability Zone deployments are ideal for workloads such as backups for SQL Server databases. They can provide low cost storage with an HDD tier, while still providing you with consistent uptime. If you require a higher level of availability for a production workload, such as highly-available SQL servers or production application access, then a single Availability Zone isn't the right fit for your workloads. For backups, non-production testing, and development environments, an Amazon FSx single Availability Zone implementation can reduce your operational costs.

One use case where an Amazon FSx single Availability Zone file system works well is in a production situation where multiple Amazon FSx single Availability Zone file systems are in use, as the per-server storage in a highly available SQL Server cluster using Always On availability groups. For more information, see the [Optimizing cost for your high availability SQL Server deployments on AWS](https://aws.amazon.com/blogs/storage/optimizing-cost-for-your-high-availability-sql-server-deployments-on-aws/) post on the AWS Storage Blog.

### Multi-Region replication
<a name="multi-region-replication.5e7b8aa1-93e5-5593-90c1-fed46a1bd6e6"></a>

A potential option for reducing costs with a single Availability Zone file system (one where only a single Availability Zone file system works) is if you want to take advantage of a multi-Region replication with Amazon FSx. You can deploy [Single-AZ file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html) that support usage with native Microsoft DFS-R. DFS-R has the capability to automatically replicate data across Regions and multiple sites. For more information about configuring DFS-R using Amazon FSx, see [Using Microsoft Distributed File System Replication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/additional-info.html#using-dfsr) in the Amazon FSx documentation.

Another alternative for multi-Region cost savings is using AWS Storage Gateway. This enables you to implement an [Amazon FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html) in another Region for multi-Region access of Amazon FSx. For more information, see the [AWS Storage Gateway](storage-main-storage-gateway.md) section of this guide.

If you work across Regions, you must consider the data transfer cost for cross-Region data traffic. Traffic moving across Regions incurs a $0.02/Gb charge. So, if you have consistent data change at high volumes, this will add to your overall cost. For [example](https://calculator.aws/#/estimate), 1 TB of data transfer equals approximately $20.48.

### Maintenance window
<a name="maintenance-window.79b7ed99-cef0-5c71-b789-b2e91342c29c"></a>

The maintenance window is a key consideration if you're using a Single Availability Zone with Amazon FSx. During the maintenance window, the Amazon FSx file system is unavailable for roughly 20 minutes, due to routine software patching for the underlying Windows Server. If you're using the file system for overnight backups, adjust the Amazon FSx maintenance window accordingly to avoid interruptions during your backup. You can adjust the [maintenance window](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/maintenance-windows.html) after creating your Amazon FSx file system.

## Additional resources
<a name="storage-fsx-single-az-resources"></a>
+ [Availability and durability: Single-AZ and Multi-AZ file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html#deployment-type-features-summary) (Amazon FSx documentation)
+ [Amazon FSx for Windows File Server Pricing](https://aws.amazon.com/fsx/windows/pricing/) (AWS website)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
