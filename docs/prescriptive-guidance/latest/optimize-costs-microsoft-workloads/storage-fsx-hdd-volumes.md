---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-fsx-hdd-volumes.html
---

# Understand HDD volume usage in Amazon FSx
<a name="storage-fsx-hdd-volumes"></a>

## Overview
<a name="storage-fsx-hdd-volumes-overview"></a>

Amazon FSx for Windows File Server offers the flexibility to choose throughput independently of file system capacity. Two capacity settings are available: hard disk drive (HDD) and solid state drive (SSD).

The following diagram shows the relationship between throughput and storage settings.

![Relationship between throughput and storage settings](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/6d89270d-872d-40ec-861d-9f7de6e9bcbe.png)

With HDD-based storage, you receive a 12 IOPS baseline with 80 burst disk IOPS (IOPs per TiB of storage) and throughput of 12 Megabytes/second baseline with 80 burst Megabytes/second (per TiB of storage). For example, if your share is 50 TB in size, you get 50 \* 12 = 600 as baseline for both throughput and IOPS.

Amazon FSx for Windows File Server provides 80 burst IOPS. Burst credits are refilled automatically when your utilization is below your baseline rate and are automatically consumed when your utilization is above your baseline rate. For example, if your workload is only utilizing 10 IOPS/TB for an hour (2 IOPS/TB below your baseline rate), you can then utilize 14 IOPS/TB (2 IOPS/TB above your baseline) for the following hour before running out of burst credits again.

For file operations, Amazon FSx for Windows File Server provides consistent sub-millisecond latencies with SSD storage and single-digit millisecond latencies with HDD storage. For all file systems, including those with HDD storage, Amazon FSx for Windows File Server provides a fast (in-memory) cache on the file server, so you can get high performance and sub-millisecond latencies for actively accessed data, irrespective of storage type.

When appropriate, the usage of HDD storage can help to reduce the cost of your overall storage capacity and provide a reliable storage platform for your needs.

## Cost impact
<a name="storage-fsx-hdd-volumes-cost"></a>

Amazon FSx for Windows File Server performance depends on three factors: storage capacity, storage type, and throughput. Network I/O performance and in-memory cache size are solely determined by throughput capacity, while the disk I/O performance is determined by a combination of throughput capacity, storage type, and storage capacity.

While SSD is recommended for I/O intensive workloads, there are a variety of workloads whose needs can be met with HDD performance specs. HDD storage is designed for a broad spectrum of workloads, including home directories, user and departmental shares, and content management systems. For example, if your users only need low-latency access to data supporting current projects, then most of the data you're storing is infrequently accessed.

You can use the [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=24d13161c41a4f947ff78abb2e36c1815c914cb1) to provide a comparison of a 20 TB SSD to an HDD file system in `us-east-1`. As the following table shows, even with no deduplication savings, the cost difference is significant when comparing HDD file systems to SSD file systems.

|
|
| Amazon FSx file system configuration | Monthly costs |
| --- |--- |
| 20 TB multi-AZ SSD (us-east-1) | $4,699.30 |
| 20 TB multi-AZ HDD (us-east-1) | $542.88 |
| **Estimated monthly savings** | **$4,156.42** |

|
|
| Note: For additional FSx for Windows File Server savings, see the [Enable data deduplication in Amazon FSx](storage-fsx-deduplication.md) section of this guide. |
| --- |

By correctly identifying your performance needs, you can select right storage for your workload and reduce your costs.

## Cost optimization recommendations
<a name="storage-fsx-hdd-volumes-rec"></a>

If you decide to use HDD storage, test your file system to ensure it can meet your performance requirements. HDD storage comes at a lower cost relative to SSD storage, but with lower levels of disk throughput and disk IOPS per unit of storage. It might be suitable for general-purpose user shares and home directories with low I/O requirements, large content management systems where data is retrieved infrequently, or datasets with small numbers of large files.

The storage type for an existing file system can't be changed. To convert the storage type for an Amazon FSx for Windows File Server file system, you must back up your existing file system and restore it to a new file system with the desired storage type. If you're looking to convert an existing SSD file system to an HDD file system, be aware that HDD has a much higher minimum capacity of 2 TB.

To restore a backup with a different storage type, do the following:

1. [Back up your existing file system](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html).

1. [Create a new Amazon FSx file system](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started.html) with the HDD storage type.

1. Restore the backup to the new file system with the desired storage type.

1. Verify the new file system has the correct storage type and your data is intact.

Before moving your changes to production, we recommend that you analyze the performance of your Amazon FSx file system and verify the change is acceptable. For more guidance, see the [Optimizing Amazon FSx for Windows File Server performance with new metrics](https://aws.amazon.com/blogs/storage/optimizing-amazon-fsx-for-windows-file-server-performance-with-new-metrics/) post on the AWS Storage Blog.

## Additional resources
<a name="storage-fsx-hdd-volumes-resources"></a>
+ [Optimizing costs with Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/optimize-fsx-costs.html) (Amazon FSx documentation)
