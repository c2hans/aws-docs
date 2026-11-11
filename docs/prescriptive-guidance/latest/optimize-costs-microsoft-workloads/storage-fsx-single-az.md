---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-fsx-single-az.html
---

# Use a single Availability Zone
<a name="storage-fsx-single-az"></a>

## Overview
<a name="storage-fsx-single-az-overview"></a>

This section explains when it's more beneficial to use a single Availability Zone implementation of [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html). It covers scenarios where moving to a single Availability Zone reduces costs, while still enabling you to use Amazon FSx for Windows File Server as your managed file storage service. We recommend using Multi-AZ file systems for most production workloads. Single-AZ deployment is designed as a cost-efficient solution for workloads that have replication built into the application layer or have relaxed availability and recovery point objective (RPO) needs.

## Cost impact
<a name="storage-fsx-single-az-cost"></a>

A single Availability Zone file system offers an approximately 40 percent cost reduction compared to a multiple Availability Zone implementation. With a multiple Availability Zone file system, you pay $0.230 per GB-month in SSD and $0.025 per GB-month in HDD compared to $0.130 per GB-month for SSD and $0.013 per GB-month for HDD on a single Availability Zone file system. You can see a comparison of costs and create your own estimates by using the [AWS Pricing Calculator](https://calculator.aws/#/).

For a 10 TB file system, you pay approximately $1,200 per month for multiple Availability Zones or $680 per month for a single Availability Zone. This [example](https://calculator.aws/#/estimate?id=3339ba60d065a76ecfcaa1770450214534941c8f) uses a 10 TB FSx for Windows File Server file system with SSD and assumes estimated deduplication savings of 50 percent. Overall, a single Availability Zone has a lower cost of entry but comes with a few caveats. The next section covers these caveats.

## Cost optimization recommendations
<a name="storage-fsx-single-az-rec"></a>

### Single Availability Zone deployments
<a name="single-availability-zone-deployments.b51a8385-7895-584e-9796-4ddca26d5a6b"></a>

To make sure that a single Availability Zone is the right fit, consider your own internal service level agreements (SLAs) for the data that you store on FSx for Windows File Server. This entails understanding whether you have SLAs to provide to your customers (internal and external) and whether the availability for an Amazon FSx single Availability Zone will still allow you to meet those SLAs. FSx for Windows File Server with a single Availability Zone has an SLA uptime commitment of 99.5 percent. The SLA for Amazon FSx for multiple Availability Zones is 99.99 percent. For mission-critical workloads, we recommend that you use multiple Availability Zones over a single Availability Zone, even at additional cost.

Single Availability Zone deployments are well suited for workloads such as backups for SQL Server databases. They can provide low-cost storage with a hard disk drive (HDD) tier, while still providing you with consistent uptime. If you require a higher level of availability for a production workload, such as highly available SQL Server instances or production application access, then a single Availability Zone isn't the right fit for your workloads. For backups, non-production testing, and development environments, an Amazon FSx single Availability Zone implementation can reduce your operational costs.

One use case where an Amazon FSx single Availability Zone file system works well is a production situation where multiple Amazon FSx single Availability Zone file systems serve as the per-server storage in a highly available SQL Server cluster that uses Always On availability groups. For more information, see the [Optimizing cost for your high availability SQL Server deployments on AWS](https://aws.amazon.com/blogs/storage/optimizing-cost-for-your-high-availability-sql-server-deployments-on-aws/) post on the AWS Storage Blog.

### Multi-Region replication
<a name="multi-region-replication.95dcf801-1b8c-5f34-869a-55c4e3dc6165"></a>

If you use a single Availability Zone file system, you can potentially reduce costs by using multi-Region replication with Amazon FSx. You can deploy [Single-AZ file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html) that support usage with native Microsoft Distributed File System Replication (DFS-R). DFS-R can automatically replicate data across Regions and multiple sites. For more information about configuring DFS-R using Amazon FSx, see [Using Microsoft Distributed File System Replication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/additional-info.html#using-dfsr) in the Amazon FSx documentation.

Another alternative for multi-Region cost savings is using AWS Storage Gateway. This enables you to implement an [Amazon FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html) in another Region for multi-Region access of Amazon FSx. For more information, see the [AWS Storage Gateway](storage-main-storage-gateway.md) section of this guide.

If you work across Regions, consider the data transfer cost for cross-Region data traffic. Traffic that moves across Regions incurs a charge of $0.02 per GB. If your data changes frequently and at high volumes, this charge adds to your overall cost. For [example](https://calculator.aws/#/estimate), 1 TB of data transfer costs approximately $20.48.

### Maintenance window
<a name="maintenance-window.62d43ab7-2d8a-5f71-b2e0-b3e5bd401211"></a>

The maintenance window is a key consideration if you're using a single Availability Zone with Amazon FSx. During the maintenance window, the Amazon FSx file system is unavailable for roughly 20 minutes because of routine software patching for the underlying Windows Server. If you use the file system for overnight backups, schedule the Amazon FSx maintenance window so that it doesn't overlap with your backup. You can adjust the [maintenance window](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/maintenance-windows.html) after you create your Amazon FSx file system.

## Additional resources
<a name="storage-fsx-single-az-resources"></a>
+ [Availability and durability: Single-AZ and Multi-AZ file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html#deployment-type-features-summary) (Amazon FSx documentation)
+ [Amazon FSx for Windows File Server Pricing](https://aws.amazon.com/fsx/windows/pricing/) (AWS website)
