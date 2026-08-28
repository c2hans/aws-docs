---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-fsx-data-sharding.html
---

# Understand data sharding in FSx for Windows File Server
<a name="storage-fsx-data-sharding"></a>

## Overview
<a name="storage-fsx-data-sharding-overview"></a>

FSx for Windows File Server performance is configuration dependent. It's primarily based on storage type, storage capacity, and throughput configuration. The throughput capacity that you select determines the performance resources available for the file server—including the network I/O limits, the CPU and memory, and the disk I/O limits imposed by the file server. The storage capacity and storage type that you select determine the performance resources available for the storage volumes—the disk I/O limits imposed by the storage disks. In addition to performance, the configuration choices also influence the cost. FSx for Windows File Server pricing primarily depends on storage capacity and storage type, throughput capacity, backup, and data transferred.

If you have relatively large file storage and performance requirements, you can benefit from data sharding. Data sharding involves [dividing your file data](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/group-file-systems.html) into smaller datasets (shards) and storing them across different file systems. Applications accessing your data from multiple instances can achieve high levels of performance by reading and writing to these shards in parallel. At the same time, you can still present a unified view under a common namespace to your applications. In addition, it can also help to scale file data storage beyond what each file system supports (64 TB) for large file datasets—up to hundreds of petabytes.

## Cost impact
<a name="storage-fsx-data-sharding-cost"></a>

For large datasets, it's typically more effective to deploy multiple small FSx for Windows File Server file systems, rather than one large SSD share to achieve the same level of performance. Using a combination of FSx for Windows File Server HDD and SSD storage types enables better cost savings, and enables you to match the workload with the best underlying disk subsystem. In the following tables, you can see the difference between a single 17 TB file system and compare it to multiple smaller file systems which add to the same capacity.

**Large SSD file system with multiple workloads**

|
|
| Server name | Cost | Configuration | Region |
| --- |--- |--- |--- |
| Amazon FSx for Windows File Server | $5,716 USD | 17 TB SSD<br />30 percent deduplication<br />256 Mbps<br />17 TB backup | US East (N. Virginia) |

**Partitioned workload using DFSN**

|
|
| Server name | Cost | Configuration | Region | Share |
| --- |--- |--- |--- |--- |
| Amazon FSx for Windows File Server | $1,024 USD | 2 TB SSD<br />20% deduplication<br />128 Mbps<br />2 TB backup<br />Multi-AZ | US East (N. Virginia) | Share 1 |
| Amazon FSx for Windows File Server | $2,132 USD | 5 TB SSD<br />30% deduplication<br />256 Mbps<br />5 TB backup<br />Multi-AZ | US East (N. Virginia) | Share 2 |
| Amazon FSx for Windows File Server | $1,036 USD | 10 TB HDD<br />40% deduplication<br />128 Mbps<br />10 TB backup<br />Multi-AZ | US East (N. Virginia) | Share 3 |
| DFSN Windows EC2 instances | $27 USD | t3a.medium<br />2 vCPUs<br />4 GiB memory | US East (N. Virginia) | DFSN Instances |

The annual cost for a large SSD file system is $68,592. The annual cost of a partitioned workload is $50,640. In this example, a 26 percent savings can be achieved while matching the workload to the appropriate backend storage. For more information about pricing estimation, see the [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=50b7af500c59bdff4c35e57bc9b8c71334cf4232) estimate.

## Cost optimization recommendations
<a name="storage-fsx-data-sharding-rec"></a>

To deploy a data deduplication solution, you must set up a [Microsoft DFS Namespace](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/group-file-systems.html) based on the type of data, I/O size, and I/O access pattern. Each namespace supports up to 50,000 file shares and hundreds of petabytes of storage capacity in aggregate.

It works most efficiently to choose a sharding convention that distributes I/O evenly across all the file systems you plan on using. Monitoring your workload will help with additional optimization or cost reduction. If you need help gauging performance information for the Amazon FSx file system, see [FSx for Windows File Server performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html) in the FSx for Windows File Server documentation.

After you choose a sharding strategy, you can group the file systems for easy access to your shares by using DFS Namespaces. This enables users to see one homogenous file system, when in reality they're accessing a variety of different file systems with purpose-built use cases. It's important to create the shares with a proper naming convention so your end users can easily decipher what workload the shares are designed for. It's also important to label production and non-production shares, so end users don't place files in the wrong file system by mistake.

The following diagram shows how a single DFS Namespace can be used as the access point for multiple Amazon FSx file systems.

![DFN Namespace access point](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/51f1471a-707f-43d9-bd39-7b520f1d295d.png)

Keep in mind the following:
+ You can add existing FSx for Windows File Server shares to a DFS tree.
+ Amazon FSx can't be added to the root of the DFS share path. You have only one subfolder.
+ You must deploy an EC2 instance to serve the DFS namespace configuration.

For more information about DFS-N configuration, see [DFS Namespaces overview](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview) in the Microsoft documentation. For more information about using DFS namespaces, see the [Using DFS Namespaces with Amazon FSx for Windows File Server](https://www.youtube.com/watch?v=s482kj_xMeE) video on YouTube.

## Additional resources
<a name="storage-fsx-data-sharding-resources"></a>
+ [Grouping multiple file systems with DFS Namespaces](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/group-file-systems.html) (Amazon FSx documentation)
+ [Walkthrough 6: Scaling out performance with shards](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/scale-out-performance.html) (Amazon FSx documentation)
+ [Using DFS Namespaces with Amazon FSx for Windows File Server](https://aws-labs.net/images/Resource/Video-FSX-DFSN-v4.pdf) (AWS Labs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
