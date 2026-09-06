---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/right-ec2-instance.html
---

# Select the right EC2 instance for SQL Server workloads
<a name="right-ec2-instance"></a>

|
|
| Important: Before you read this section, we recommend that you first read the [Understand SQL Server licensing](sql-server-licensing.md) and [Select the right instance type for Windows workloads](right-size-selection.md) sections of this guide. |
| --- |

## Overview
<a name="right-ec2-instance-overview"></a>

Microsoft SQL Server has been running on Amazon Elastic Compute Cloud (Amazon EC2) instances for over 15 years. AWS has taken that experience and used it to help develop Amazon EC2 instances to fit SQL Server workloads running from minimal specifications all the way to high performance, multi-Region clusters.

Choosing the correct EC2 instance for SQL Server is largely dependent on your workload. Understanding how SQL Server is licensed, how it uses memory, and how SQL Server features align with Amazon EC2 offerings can help guide you to the best EC2 instance for your application.

This section addresses a variety of SQL Server workloads and how they can be paired with certain EC2 instances to keep your licensing and compute costs to a minimum.

## Cost comparison
<a name="right-ec2-instance-cost-comparison"></a>

Amazon EC2 enables you to Bring Your Own License (BYOL) or pay as you go with Windows Server and SQL Server licensing. For pay-as-you-go licensing, the licensing costs for the Windows Server and SQL Server licenses are baked into the hourly cost of the EC2 instance. For example, you can have different AMIs with different prices. The price of the AMI is contingent on the SQL Server edition that the AMI runs on.

Windows Server and SQL Server pricing isn't itemized. You won't find itemized pricing on tools like the [AWS Pricing Calculator](https://calculator.aws/). If you select different combinations of license-included offerings, the licensing costs can be deduced, as the following table shows.

|
|
| EC2 instance | AMI | Compute price | Windows license price | SQL license price | Total price |
| --- |--- |--- |--- |--- |--- |
| r5.xlarge | Linux (compute pricing) | $183.96 | - | - | $183.96 |
| r5.xlarge | Linux \+ SQL Developer | $183.96 | $0 | $0 | $183.96 |
| r5.xlarge | Windows Server (LI) | $183.96 | $134.32 | - | $318.28 |
| r5.xlarge | Windows \+ SQL Developer | $183.96 | $134.32 | $0 | $318.28 |
| r5.xlarge | Windows \+ SQL Web (LI) | $183.96 | $134.32 | $49.64 | $367.92 |
| r5.xlarge | Windows \+ SQL Standard (LI) | $183.96 | $134.32 | $350.4 | $668.68 |
| r5.xlarge | Windows \+ SQL Enterprise (LI) | $183.96 | $134.32 | $1095 | $1413.28 |

|
|
| Note: Pricing in the preceding table is based on the on-demand pricing in the `us-east-1` Region. |
| --- |

The most cost-effective method for running SQL Server is to stay at a lower-level edition until you need a feature from a higher-level edition. For more information, see the [Compare SQL Server editions](sql-server-editions.md) section of this guide. Upgrading from SQL Server Web edition to SQL Server Standard edition is over seven times the SQL Server licensing cost and over three times the cost of moving from Standard edition to Enterprise edition. The disparity in licensing costs is a major factor to consider and is explored in the rest of this section.

## Cost optimization scenario
<a name="right-ec2-instance-opt-scenario"></a>

Consider an example scenario where an analytics company tracking delivery vehicles is seeking to improve its SQL Server performance. After a MACO expert reviews the company's performance bottlenecks, the company transitions from x1e.2xlarge instances to x2iedn.xlarge instances. Although the instance size is smaller, the enhancements to the x2 instances improve SQL Server performance and optimization by using buffer pool extensions. This allowed the company to downgrade from SQL Server Enterprise edition to SQL Server Standard edition and reduce its SQL Server licensing from 8 vCPUs to 4 vCPUs.

Before optimization:

|
|
| Server | EC2 instance | SQL Server edition            | Monthly cost |
| --- |--- |--- |--- |
| ProdDB1 | x1e.2xlarge | Enterprise | $3,918.64 |
| ProdDB2 | x1e.2xlarge | Enterprise | $3,918.64 |
| **Total** | ** ** | ** ** | **$7,837.28** |

After optimization:

|
|
| Server | EC2 instance | SQL Server edition            | Monthly cost |
| --- |--- |--- |--- |
| ProdDB1 | x2iedn.xlarge | Standard | $1,215.00 |
| ProdDB2 | x2iedn.xlarge | Standard | $1,215.00 |
| **Total** | ** ** | ** ** | **$2,430.00** |

The combined changes from x1e.2xlarge instances to x2iedn.xlarge instances enabled the example customer to save $5,407 per month on their production database servers. This reduced the total cost of the workload by 69 percent.

|
|
| Note: Pricing in the preceding table is based on the on-demand pricing in the `us-east-1` Region. |
| --- |

## Cost optimization recommendations
<a name="right-ec2-instance-opt-rec"></a>

### Memory optimized instances
<a name="memory-optimized-instances.a80e552f-cfa8-533a-9ee2-b0b9ebf8a78e"></a>

One of the most important aspects of SQL Server is understanding its reliance on memory. SQL Server attempts to use all available RAM not being used by the operating system (up to 2 TB for a default installation). It does this for performance reasons. Working with data in memory is much more performant than having to constantly pull data from disk, make changes, and then write it back to the disk. Instead, SQL Server attempts to load as much data from the attached databases as possible and keeps that data in RAM. Changes made to the data happen in memory and are hardened to disk at a later time.

|
|
| Note: For a detailed explanation of how SQL Server writes changes, see [Writing Pages](https://learn.microsoft.com/en-us/sql/relational-databases/writing-pages?view=sql-server-ver16) in the Microsoft documentation. |
| --- |

Since SQL Server performs better with larger amounts of RAM, we typically recommend starting with [Amazon EC2 memory optimized](https://aws.amazon.com/ec2/instance-types/#Memory_Optimized) instance types. Memory optimized instances are versatile and offer a variety of different options. The R family has a 1-to-8 vCPU-to-RAM ratio and has options for Intel processors, AMD processors, enhanced networking, enhanced EBS performance, instance storage, and enhanced processor speed. For memory-heavy workloads, there's also an X family that combines many of the same options and extends the vCPU-to-RAM ratio to 1-to-32. Due to the versatility of memory optimized instances, you can apply them to SQL Server workloads of all shapes and sizes.

### Workloads below minimal resources (less than 4 vCPUs)
<a name="workloads-below-minimal-resources--less-than-4-vcpus-.b04a70f7-7a23-5f84-83a2-e3711e978ce2"></a>

Although some use cases work well with burstable (T3) instances, we recommend that you generally avoid using burstable instances for SQL Server workloads. The licensing for SQL Server is based on the number of vCPUs assigned to an instance. If SQL Server is idle the majority of the day and is acquiring burst credits, you pay for SQL licenses which you aren't fully utilizing. In addition, SQL Server has a minimum license requirement of 4 cores per server. This means if you have a SQL Server workload that doesn't require 4 vCPUs worth of compute power, you're paying SQL Server licensing which you aren't using. In these scenarios, it would be best to [consolidate multiple SQL Server instances](consolidate-instances.md) onto a larger server.

### Workloads using minimal resources (less than 64 GB RAM)
<a name="workloads-using-minimal-resources--less-than-64-gb-ram-.838d6693-1e56-5492-aaeb-8c4a2ac55932"></a>

Many SQL Server workloads under 64 GB RAM don't prioritize high performance or high availability. For these types of workloads, SQL Server Web edition might be a good fit if the application is covered under Microsoft's licensing restrictions.

|
|
| Important: SQL Server Web edition has a restricted use case based on Microsoft's licensing terms. SQL Server Web edition may be used only to support public and internet accessible webpages, websites, web applications, and web services. It may not be used to support line-of-business applications (for example, customer relationship management, enterprise resource management, and other similar applications). |
| --- |

SQL Server Web edition scales up to 32 vCPUs and 64 GB RAM and is 86 percent less expensive than SQL Server Standard edition. For low resource workloads, using an AMD memory optimized instance like the r6a, which has a 10 percent less expensive compute price than its Intel counterpart, is also a good way to keep compute and SQL licensing costs to a minimum.

### Workloads with average resources (less than 128 GB RAM)
<a name="workloads-with-average-resources--less-than-128-gb-ram-.0f38ca12-21a9-560e-8ea4-40fc735bbb8a"></a>

SQL Server Standard edition is used on the majority of SQL Server workloads up to 128 GB RAM. SQL Server Standard edition is 65–75 percent less expensive than SQL Server Enterprise edition and can scale up to 48 vCPUs and 128 GB RAM. Since the 128 GB RAM limitation is typically hit before the 48 vCPU limitation, it's the focus of most customers who want to avoid upgrading to SQL Server Enterprise edition.

SQL Server has a feature called the [buffer pool extension](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/buffer-pool-extension?view=sql-server-ver16). This feature enables SQL Server to use a portion of a disk to act as an extension of RAM. The buffer pool extension works well when combined with ultra-fast storage, like the NVMe SSDs used in [Amazon EC2 instance storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html). Amazon EC2 instances containing instance storage are denoted with a "d" in the instance name (for example, r5d, r6id, and x2iedn).

Buffer pool extensions are not a replacement for normal RAM. However, if you require more than 128 GB of RAM, you can use buffer pool extensions with EC2 instances like the r6id.4xlarge and x2iedn.xlarge to delay an upgrade to Enterprise edition licensing.

### High performance workloads (more than 128 GB RAM)
<a name="high-performance-workloads--more-than-128-gb-ram-.56695383-0ef5-5afd-ab3f-2d0a7bf5e719"></a>

SQL Server workloads requiring high performance are challenging for cost optimization because of their reliance on a lot of resources. However, understanding the differences in EC2 instances can prevent you from making the wrong choice.

The following table shows a variety of memory optimized EC2 instances and their performance limits.

|  |
| --- |
|   | r5b | r6idn | r7iz | x2iedn | x2iezn |
| --- |--- |--- |--- |--- |--- |
| **Processor** | 3.1 GHz<br />2nd Generation Intel Xeon Processor | 3.5 GHz<br />3rd Generation Intel Xeon Processor | 3.9 GHz<br />4th Generation Intel Xeon Scalable Processor | 3.5 GHz<br />3rd Generation Intel Xeon Processor | 4.5 GHz<br />2nd Generation Intel Xeon Processor |
| **CPU:RAM ratio** | 1:8 | 1:8 | 1:8 | 1:32 | 1:32 |
| **Max vCPU** | 96 | 128 | 128 | 128 | 48 |
| **Max RAM** | 768 GB | 1,024 GB | 1,024 GB | 4,096 GB | 1,536 GB |
| **Instance storage** | – | NVMe SSD<br />(4x 1900 GB) | – | NVMe SSD<br />(2x 1900 GB) | – |
| **io2 Block Express** | Supported | Supported | Supported | Supported | – |
| **Max EBS IOPS** | 260,000 | 350,000 | 160,000 | 260,000 | 80,000 |
| **Max EBS throughput** | 60 Gbps | 80 Gbps | 40 Gbps | 80 Gbps | 19 Gbps |
| **Max network bandwidth** | 25 Gbps | 200 Gbps | 50 Gbps | 100 Gbps | 100 Gbps |

Each instance is used for a different purpose. Understanding your SQL Server workload can help you choose the instance type that's best for you.

Details on attributes:
+ **r5b** – The "b" attribute in r5b means this instance type is focused on high EBS performance. In the fifth generation of memory optimized instances, the r5b was the preferred choice. It was the first instance type to utilize io2 Block Express volumes and reach maximum storage IOPS of 260,000. The r5b instance type is still a cost-effective alternative for high EBS performance needs.
+ **r6idn** – The sixth generation of memory optimized instances offered considerable improvements over the previous generation. The EBS performance enhancements from the r5b are taken a step further with the r6idn, bumping up the maximum IOPS to 350,000. The r6idn also has an instance store volume for tempdb and buffer pool extensions to further increase SQL Server performance.
+ **x2iedn** – The x2iedn is similar to the r6idn. It offers similar levels of enhanced EBS, enhanced networking, and NVMe SSD instance storage, but with a 1:32 vCPU-to-RAM ratio for high memory workloads and low CPU quantity (lower SQL Server licensing costs).
+ **x2iezn** – The "z" attribute in x2iezn indicates this instance type is focused on high processor performance. The Cascade Lake processor has an all-core turbo frequency up to 4.5 GHz. We recommend that you use this EC2 instance, coupled with a 1:32 vCPU-to-RAM ratio, in a scenario where you want to keep vCPU quantity low. This, in turn, can keep SQL Server licensing costs low.
+ **r7iz** – The "z" attribute in r7iz indicates this instance type is focused on high processor performance. The Sapphire rapids processor has an all-core turbo frequency up to 3.9 GHz. Like the x2iezn instances, the r7iz prioritizes high frequency processor performance but with a 1:8 vCPU-to-RAM ratio.

## Additional resources
<a name="right-ec2-instance-resources"></a>
+ [General purpose Amazon EC2 instances](https://aws.amazon.com/ec2/instance-types/) (AWS documentation)
+ [Comparison tool](https://instances.vantage.sh/) (Vantage)
+ [Licensing – SQL Server](https://aws.amazon.com/windows/faq/#licensing-sql) (AWS documentation)
