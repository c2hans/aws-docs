---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-sql-server.html
---

# Optimize storage for SQL Server
<a name="storage-sql-server"></a>

## Overview
<a name="storage-sql-server-overview"></a>

This section focuses on cost optimization for [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) (Amazon EBS) SSD storage for SQL Server workloads on EC2 instances.

You have a wide variety of storage options for deploying and running SQL Server workloads on AWS. Choose storage based on purpose, architecture, durability, performance, capacity, and cost. AWS customers running SQL Server workloads typically use a combination of Amazon EBS, NVMe, Amazon FSx, and Amazon Simple Storage Service (Amazon S3) storage.

Amazon EBS is network-attached storage that connects to EC2 instances. You can use it to store and process operating system, application, database, and backup files. Amazon EBS solid state drive (SSD) storage includes General Purpose SSD (gp2 and gp3) and Provisioned IOPS SSD (io1, io2, and io2 Block Express). Consider the following:
+ Some EC2 instances, like r5d, have local NVMe SSDs physically attached to the host instance. These volumes provide block-level storage that's commonly used for SQL Server tempdb or buffer pool extension.
+ Amazon FSx for Windows File Server is a fully managed file storage service, while Amazon FSx for NetApp ONTAP is fully managed shared storage built on the NetApp ONTAP file system. Amazon FSx is often used to run SQL Server workloads in a high availability, SQL Server Failover Clustered Instance (FCI) configuration. This solution hosts SQL Server data and log files, which reduces the Amazon EBS performance requirements on EC2 instances.
+ Amazon S3 is an object storage service designed for scalability, data availability, security, and performance. You can store SQL Server native backup files, AMIs, Amazon EBS snapshots, and application logs in Amazon S3.

## SSD storage types, performance, and cost for Amazon EBS
<a name="ssd-storage-types-performance-and-cost-for-amazon-ebs"></a>

SSD storage costs for [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) (Amazon EBS) generally increase as durability and performance increase. The storage currently comes in five volume types, each with its own [performance metrics](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html). For a summary of the use cases and characteristics of SSD-backed volumes, see the table in the [Solid state drive (SSD) volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html#vol-type-ssd) section of the Amazon EBS documentation.

You can use Amazon CloudWatch to monitor SSD performance, capture trending data, and set alarms when metrics reach thresholds that you define. If you're running Microsoft SQL Server workloads on AWS, consider enabling [detailed monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-basic-detailed.html) and deploying [CloudWatch custom metrics](https://aws.amazon.com/blogs/database/monitor-your-microsoft-sql-server-using-custom-metrics-with-amazon-cloudwatch-and-aws-systems-manager/) to capture detailed volume performance metrics such as disk latency, IOPS, throughput, disk queue length, and used versus free capacity. You can use these CloudWatch performance metrics to identify under-provisioned and over-provisioned storage and to provide historical data points that help define storage requirements.

SSD storage costs for Amazon EBS also vary based on allocated capacity. The following table compares the different volume types. All of the volume types have 1 TB of capacity and similar performance configurations.

|
|
| Volume type | Max IOPS (16 KiB I/O) | Max throughput (128 KiB I/O) | Price per 1 TB | Percent cost savings |
| --- |--- |--- |--- |--- |
| gp2 | 3,000 | 250 | $102.40 |   |
| gp3 | 3,000 | 250 | $86.92 | 15% |
| io1 | 16,000 | 500 | $1,168 |   |
| io2 | 16,000 | 500 | $1,168 |   |
| gp3 | 16,000 | 500 | $146.92 | 87% |
| io2BX | 16,000 | 4,000 | $1,168 |   |
| gp3 | 16,000 | 1,000 | $181.92 | 84% |

|
|
| Note: The performance and cost metrics in the preceding table are per volume, based on an [estimate](https://calculator.aws/#/estimate?id=b637bb9c21ae8ad62f440e349dd2067de80e76b2) from the AWS Pricing Calculator. An AWS account is required to access the estimate in the AWS Pricing Calculator. |
| --- |

Amazon EBS SSD gp3 volumes balance performance and cost. You can save up to 87 percent if you choose a gp3 volume over io1 or io2 volumes for workloads that require less than 16,000 IOPS and 500 MiBps throughput.

io2 Block Express (io2BX) volumes offer increased performance over regular io2 volumes. At 16,000 IOPS, io1 or io2 volumes provide only 500 MiBps throughput, while you can configure io2BX volumes for up to 4,000 MiBps throughput. Compared to io1 and io2 volumes, io2BX volumes provide more than four times the throughput between 16,000 and 64,000 IOPS, at the same price. You can convert regular io2 volumes to io2BX volumes by attaching them to Amazon EC2 instances that support io2BX. For a list of Amazon EC2 instances that support io2BX, see [Provisioned IOPS SSD volumes](https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html#io2-block-express) in the Amazon EBS documentation. Before you deploy new storage, you can use the [AWS Pricing Calculator](https://calculator.aws/) to estimate your monthly cost and understand the cost impact of trade-offs between durability, performance, and capacity.

## General SSD cost optimization for Amazon EBS
<a name="storage-sql-server-overview-ssd-ebs"></a>

We recommend that you evaluate what you're storing and ensure that you're using the appropriate storage type and class. For example, Amazon S3 provides cost-effective storage, built-in lifecycle policies, and replication options suited for SQL Server backups. SQL Server 2022 can back up directly to Amazon S3, while previous versions of SQL Server rely on native local backups. If you're running older versions of SQL Server, consider backing up to Amazon EBS HDD volumes and then copying the backup to Amazon S3. This solution can save up to 53 percent compared to using gp3 volumes for backups.

The following table shows the price difference for 1 TB of storage on Amazon EBS gp3, Amazon EBS HDD st1, and Amazon S3.

|
|
| Storage type | Capacity | Price per month |
| --- |--- |--- |
| EBS gp3 500 MiBps | 1 TB | $96.92 |
| EBS st1 burst 500 MiBps | $46.08 |  |
| S3 Standard | $23.55 |  |
| S3 Standard (infrequent access) | $12.80 |  |
| S3 Glacier Deep Archive | $1.03 |  |

|
|
| Note: The cost metrics in the preceding table are based on an [estimate](https://calculator.aws/#/estimate?id=ba6032e10a5f8a82807c1e3b7d5a64ceb2cdcbde) in the AWS Pricing Calculator. An AWS account is required to access the estimate in the AWS Pricing Calculator. |
| --- |

We recommend that you consider the following:
+ Enable detailed monitoring and deploy CloudWatch custom metrics to capture your storage performance requirements.
+ Upgrade Amazon EBS storage from gp2 to gp3 to reduce costs, increase flexibility, and improve performance.
+ Upgrade Amazon EBS storage from io1 to io2 for increased durability and performance flexibility.
+ Use io2BX instead of io1 or io2 when possible for increased durability and performance.
+ Consider a mix-and-match approach when choosing storage to help reduce capacity requirements and the cost of high-performance volumes. For example, you could use low-cost gp3 volumes for your root volume (operating system), SQL Server installation, system databases (excluding tempdb), and lower performing user databases. This could help reduce the capacity and cost of an io2 volume, which can be dedicated to high-performance user databases.
+ If you're hosting SQL Server databases on AWS, we recommend that you use multiple SQL Server data files per database. This lets you distribute read/write workloads across multiple volumes, which reduces performance and capacity requirements per volume and helps lower cost.
+ Even if production workloads require higher performing storage, such as io1 or io2/io2BX, consider gp3 volumes for non-production workloads to help reduce costs.
+ Track and trend storage utilization over time to easily identify usage spikes and unexpected costs.
+ Use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) for recommendations on scaling Amazon EBS volumes up or down based on actual utilization.
+ Use the elasticity of AWS to adjust the performance and capacity needs of your SSD volumes for Amazon EBS. Unlike for on-premises environments, you don't need to overprovision storage performance and capacity for future workloads. You can migrate your existing SQL Server workloads onto AWS and adjust performance or capacity as needed, while keeping your databases online.

## Additional resources
<a name="storage-sql-server-resources"></a>
+ [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) (Amazon EBS documentation)
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) (Amazon EBS documentation)
+ [Provisioned IOPS SSD volumes](https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html) (Amazon EBS documentation)
+ [SSD instance store volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) (Amazon EC2 documentation)
+ [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/using_cloudwatch_ebs.html) (Amazon EBS documentation)
+ [Specifications for Amazon EC2 storage optimized instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/so.html) (Amazon EC2 documentation)
+ [Protect your SQL Server workloads using NetApp SnapCenter with Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/storage/using-netapp-snapcenter-with-amazon-fsx-for-netapp-ontap-to-protect-your-sql-server-workloads/) (AWS Storage Blog)
+ [Amazon EC2 FAQ](https://aws.amazon.com/ec2/faqs/) (AWS product page)
