---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/right-size-selection.html
---

# Select the right instance type for Windows workloads
<a name="right-size-selection"></a>

## Overview
<a name="right-size-selection-overview"></a>

A significant distinction between workloads operating in the cloud compared to on-premises environments is the practice of over-provisioning. When purchasing physical hardware for on-premises use, you make a capital expenditure expected to last for a predetermined duration, typically 3–5 years. To accommodate anticipated growth during the hardware's lifespan, the hardware is acquired with more resources than your workload currently requires. Consequently, physical hardware is often over-provisioned well beyond the needs of your actual workload.

Virtual machine (VM) technology emerged as an effective means of utilizing surplus hardware resources. Administrators over-provisioned VMs with vCPUs and RAM, enabling the hypervisor to manage physical resource usage between busy and idle servers by allocating unused resources to each VM. When managing VMs, the vCPU and RAM resources allocated to each VM functioned more as resource governors rather than indicators of actual usage. VM resource over-allocation could easily exceed three times the available compute resources.

[Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) refrains from over-provisioning VMs on the underlying hardware, as it is unnecessary. Cloud computing is an operational expense, not a capital expense, and you only pay for what you use. If your workload requires more resources in the future, provision them when you actually need them, rather than doing so preemptively.

There are hundreds of options for choosing the right [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/). If you plan to migrate a Windows workload to the cloud, AWS offers an [AWS OLA](https://aws.amazon.com/optimization-and-licensing-assessment/) to help you better understand your current workload and provide an example of its performance on AWS. The AWS OLA analysis aims to match the suitable EC2 instance type and size to your actual on-premises usage.

If you already have workloads running on Amazon EC2 and seek cost optimization strategies, this section of the guide helps you identify differences between Amazon EC2 instances and their applicability to typical Windows workloads.

## Cost optimization recommendations
<a name="right-size-selection-recommendations"></a>

To optimize the costs of your EC2 instance types, we recommend that you do the following:
+ Choose the right instance family for your workload
+ Understand price variations between processor architectures
+ Understand price to performance differences across EC2 generations
+ Migrate to newer instances
+ Use burstable instances

### Choose the right instance family for your workload
<a name="choose-the-right-instance-family-for-your-workload.5e2d3050-a3be-51c6-8638-525df9033930"></a>

It's important to choose the right instance family for your workload.

Amazon EC2 instances are divided into these various groups:
+ General purpose
+ Compute optimized
+ Memory optimized
+ Accelerated computing
+ Storage optimized
+ HPC optimized

Most Windows workloads fit into the following categories:
+ General purpose
+ Compute optimized
+ Memory optimized

To simplify this even further, consider a baseline EC2 instance in each category:
+ Compute optimized – C6i
+ General purpose –  M6i
+ Memory optimized – R6i

The previous generation of EC2 instances exhibited minor differences in processor types. For example, C5 compute optimized instances have faster processors than M5 general purpose instances or R5 memory optimized instances. The latest generation of EC2 instances (C6i, M6i, R6i, C6a, M6a, and R6a) all use the same processor across instance families. Since the processor is consistent among the latest generation of instances, the price difference between the instance families now depends more on the amount of RAM. The more RAM an instance has, the more expensive it is.

The following example illustrates the hourly pricing for an Intel-based 4 vCPU instance running in the `us-east-1` Region.

|
|
| Instance | vCPUs | RAM | Hourly price |
| --- |--- |--- |--- |
| c6i.xlarge | 4 | 8 | $0.17 |
| m6i.xlarge | 4 | 16 | $0.19 |
| r6i.xlarge | 4 | 32 | $0.25 |

**Note**
Pricing is based on on-demand hourly pricing in the `us-east-1` Region.

#### Burstable instances
<a name="burstable-instances.52554ae3-9c94-55c7-8fef-b675b7406851"></a>

While it's a best practice in cloud computing to turn off unused compute resources to avoid charges, not all workloads can be switched off and on each time they're needed. Some workloads remain idle for extended periods but must be accessible 24 hours a day.

Burstable instances (T3) offer a way to maintain spiky or low-utilization workloads online all day while still keeping compute costs low. Burstable EC2 instances have a maximum amount of vCPU resources that the instance can use for brief periods. These instances employ a system based on [burstable CPU credits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html#earning-CPU-credits). These credits are accumulated during idle periods throughout the day. Burstable instances offer varying vCPU-to-RAM ratios, making them alternatives to compute optimized instances in some cases and to other general purpose instances in others.

The following example illustrates the hourly pricing for a T3 instance (that is, burstable instance) running in the `us-east-1` Region.

|
|
| Instance | vCPUs | RAM (GB) | Hourly price |
| --- |--- |--- |--- |
| t3.nano | 2 | 0.5 | $0.0052 |
| t3.micro | 2 | 1 | $0.0104 |
| t3.small | 2 | 2 | $0.0208 |
| t3.medium | 2 | 4 | $0.0416 |
| t3.large | 2 | 8 | $0.0832 |
| t3.xlarge | 4 | 16 | $0.1664 |
| t3.2xlarge | 8 | 32 | $0.3328 |

**Note**
Pricing is based on on-demand hourly pricing in the `us-east-1` Region.

### Understand price variations between processor architectures
<a name="understand-price-variations-between-processor-architectures.38e2deba-fa3e-5ef6-b46f-d4d0e1c5becf"></a>

[Intel](https://aws.amazon.com/intel/) processors have been the standard for EC2 instances since their inception. Earlier generations of EC2 instances, such as C5, M5, and R5, don't indicate Intel as the processor architecture (as it was the default). Newer generations of EC2 instances, like C6i, M6i, and R6i, include an "i" to denote the use of an Intel processor.

The change in processor architecture annotation is due to the introduction of additional processor options. The most comparable processor to Intel is [AMD](https://aws.amazon.com/ec2/amd/) (denoted with an "a"). AMD EPYC processors use the same x86 architecture and offer performance similar to Intel processors but at a lower price. As demonstrated in the following pricing examples, AMD EC2 instances provide an approximately 10 percent discount on compute costs compared to their Intel counterparts.

|
|
| Intel instance | Hourly price | AMD instance | Price | % difference |
| --- |--- |--- |--- |--- |
| c6i.xlarge | $0.17 | c6a.xlarge | $0.153 | 10% |
| m6i.xlarge | $0.192 | m6a.xlarge | $0.1728 | 10% |
| r6i.xlarge | $0.252 | r6a.xlarge | $0.2268 | 10% |

**Note**
Pricing is based on on-demand hourly pricing in the `us-east-1` Region.

The third major processor architecture option is [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) (denoted with a "g") on EC2 instances. Designed by AWS, Graviton processors offer the best price performance on Amazon EC2. Not only are current Graviton processors 20 percent cheaper than their Intel counterparts, but they also deliver a 20 percent or greater performance boost. The next generation of Graviton processors is expected to further extend this performance difference, with testing showing an additional 25 percent increase in performance.

Windows Server can't run on Graviton processors, which are based on ARM architecture. In fact, Windows Server operates only on x86 processors. Although you can't achieve a 40 percent price performance boost by using Graviton-based instances for Windows Server, you can still use Graviton processors with specific Microsoft workloads. For example, [newer versions of .NET can run on Linux](net-refactor-linux.md). That means these workloads can use ARM processors and benefit from faster, more affordable Graviton EC2 instances.

The following example illustrates the hourly pricing for a Graviton instance running in the `us-east-1` Region.

|
|
| Intel instance | Hourly price | Graviton instance | Hourly price | % difference |
| --- |--- |--- |--- |--- |
| c6i.xlarge | $0.17 | c6g.xlarge | $0.136 | 20% |
| m6i.xlarge | $0.192 | m6g.xlarge | $0.154 | 20% |
| r6i.xlarge | $0.252 | r6g.xlarge | $0.2016 | 20% |

**Note**
Pricing is based on on-demand hourly pricing in the `us-east-1` Region.

The following chart compares the prices of M series instances.

![M series price comparison](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/82f42f70-6854-466e-a828-609458c082b2.png)

### Understand price performance differences across EC2 generations
<a name="understand-price-performance-differences-across-ec2-generations.89cb41bf-1ed6-525d-af33-0ee92facc55a"></a>

One of the most consistent characteristics of Amazon EC2 is that each new generation offers better price performance than its predecessor. As the following table shows, the price of newer generation EC2 instances decreases with each subsequent release.

|
|
| Compute optimized instance | Hourly price | General purpose instance | Hourly price | Memory optimized instance | Hourly price |
| --- |--- |--- |--- |--- |--- |
| C1.xlarge | $0.52 | M1.xlarge | $0.35 | r1.xlarge | n/a |
| C3.xlarge | $0.21 | M3.xlarge | $0.266 | r3.xlarge | $0.333 |
| C5.xlarge | $0.17 | M5.xlarge | $0.192 | r5.xlarge | $0.252 |

**Note**
Pricing is based on on-demand hourly pricing in the `us-east-1` Region.

The following chart compares the costs of the different generations of C series instances.

![C series price comparison](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/91e37e71-34f7-4afd-ae96-c1106dcb34c2.png)

However, the 6th generation of instances are the same price as the 5th generation, as the following table shows.

|
|
| Compute optimized instance | Hourly price | General purpose instance | Hourly price | Memory optimized instance | Hourly price |
| --- |--- |--- |--- |--- |--- |
| C5.xlarge | $0.17 | M5.xlarge | $0.192 | r5.xlarge | $0.252 |
| C6i.xlarge | $0.17 | M6i.xlarge | $0.192 | r6i.xlarge | $0.252 |

**Note**
Pricing is based on on-demand hourly pricing in the `us-east-1` Region.

Despite having the same cost, the newer generation provides superior price performance due to faster processors, enhanced networking throughput, and increased Amazon Elastic Block Store (Amazon EBS) throughput and IOPS.

One of the most significant price performance improvements is the enhancement of the [X2i instance](https://aws.amazon.com/ec2/instance-types/x2i/). This generation of the instance offers up to 55 percent greater price performance than the previous generation. As the following table shows, the x2iedn demonstrates improvement in every performance aspect (all at the same price as the preceding generation).

|
|
| Instance | Hourly price | vCPUs | RAM | Processor speed | Instance storage | Networking | Amazon EBS throughput | EBS IOPS |
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| x1e.2xlarge | $1.66 | 8 | 244 | 2.3 GHz | 237GB SSD | 10 Gbps | 125 MB/s | 7400 |
| x1iedn.2xlarge | $1.66 | 8 | 256 | 3.5 GHz | 240GB NVMe SSD | 25 Gbps | 2500 MB/s | 65000 |

**Note**
Pricing is based on on-demand hourly pricing in the `us-east-1` Region.

### Example scenarios
<a name="example-scenarios.fb036a7d-d146-52d4-95d3-1949620e9da2"></a>

Consider the example of an analytics company that tracks delivery vehicles and wishes to improve its SQL Server performance. After a MACO SME reviews this company's performance bottlenecks, the company transitions from x1e.2xlarge instances to x2iedn.xlarge instances. The new instance size is smaller, but the enhancements to the x2 instances enable increased SQL Server performance and optimization through the use of Buffer Pool Extensions. This enables the company to downgrade from SQL Server Enterprise edition to SQL Server Standard edition. It also enables the company to reduce its SQL Server licensing from 8 vCPUs to 4 vCPUs.

**Before optimization:**

|
|
| Server | EC2 instance | SQL Server edition | Monthly cost |
| --- |--- |--- |--- |
| ProdDB1 | x1e.2xlarge | Enterprise | $3,918.64 |
| ProdDB2 | x1e.2xlarge | Enterprise | $3,918.64 |
| **Total** |  |  | **$7,837.28** |

**After optimization:**

|
|
| Server | EC2 instance | SQL Server edition | Monthly cost |
| --- |--- |--- |--- |
| ProdDB1 | x2iedn.xlarge | Standard | $1,215.00 |
| ProdDB2 | x2iedn.xlarge | Standard | $1,215.00 |
| **Total** |  |  | **$2,430.00** |

All combined, the change from x1e.2xlarge instances to x2iedn.xlarge instances enables the company in the example scenario to save $5,407 per month on its production database servers. This reduces the total cost of the workload by 69 percent.

**Note**
Pricing is based on on-demand hourly pricing in the `us-east-1` Region.

### Migrate to newer instances
<a name="migrate-to-newer-instances.879ddbb6-cf4c-597a-ba27-00f459ea1318"></a>

Older generations of Amazon EC2 run on the Xen hypervisor, while newer generations operate on the [AWS Nitro System](https://aws.amazon.com/ec2/nitro/). The Nitro System delivers almost all of the compute and memory resources of the host hardware to your instances. This results in improved overall performance. There are special considerations when [migrating from Xen to Nitro-based instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/migrate-to-xen.html). For example, [AWS Windows AMIs](https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/windows-amis.html) are configured with default settings and customizations used by the Microsoft installation media. The customizations include drivers and configurations that support the latest generation instance types ([instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#ec2-nitro-instances)).

If you're launching instances from custom Windows AMIs or from Windows AMIs provided by Amazon that were created before August 2018, we recommend that you complete the steps from [Migrate to latest generation instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/migrating-latest-types.html) in the Amazon EC2 documentation.

### Use burstable instances
<a name="use-burstable-instances.114fbab6-a0c6-5a66-b0d5-fd707b63f89f"></a>

While burstable instances are a good way to save on compute costs, we recommend that you avoid them in the following scenarios:
+ [Minimum specs for Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/hardware-requirements#ram) with the Desktop Experience require 2 GB of RAM. Avoid using t3.micro or t3.nano instances with Windows Server because they lack the minimum amount of RAM.
+ If your workload is spiky but doesn't stay idle long enough to build burst credits, using normal EC2 instances is more efficient than using burstable instances. We recommend [monitoring your CPU credits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-monitoring-cpu-credits.html) to verify this.
+ We recommend that you avoid using burstable instances with SQL Server in most scenarios. The licensing for SQL Server is based on the number of vCPUs assigned to an instance. If SQL Server is idle the majority of the day, you would be paying for SQL licenses that you aren't fully utilizing. In these scenarios, we recommend that you consolidate multiple SQL Server instances onto a larger server.

## Next steps
<a name="right-size-selection-next-steps"></a>

We recommend that you take the following next steps to optimize your costs for Amazon EC2 Windows instances:
+ Use the latest-generation EC2 instance for the best price performance.
+ Use EC2 instances with AMD processors for a ten percent reduction in compute costs.
+ Maximize resource utilization by choosing an EC2 instance type that matches your workload.

The following table shows examples of typical starting points for Windows workloads. Additional options are available, such as instance storage volumes to enhance SQL Server workloads or EC2 instances with much larger vCPU-to-RAM ratios. We recommend that you test your workloads thoroughly and use monitoring tools like AWS Compute Optimizer to help make necessary adjustments.

|
|
| Workload | Typical | Optional |
| --- |--- |--- |
| Active Directory | T3, M6i | R6i |
| File servers | T3, M6i | C6i |
| Web servers | T3, C6i | M6i, R6i |
| SQL Server | R6i | x2iedn, X2iezn |

If you must change your EC2 instance type, the process typically involves just a simple server reboot. For more information, see [Change the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html) in the Amazon EC2 documentation.

Before you change your instance type, we recommend that you consider the following:
+ You must stop your instances backed by Amazon EBS before you can change its instance type. Be sure to plan for downtime while your instance is stopped. Stopping the instance and changing its instance type might take a few minutes, and restarting your instance might take a variable amount of time depending on your application's startup scripts. For more information, see [Stop and start your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html) in the Amazon EC2 documentation.
+ When you stop and start an instance, AWS moves the instance to new hardware. If your instance has a public IPv4 address, AWS releases the address and gives your instance a new public IPv4 address. If you require a public IPv4 address that doesn't change, use an [Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html).
+ You can't change the instance type if [hibernation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html) is enabled on the instance.
+ You can't change the instance type of a [Spot Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html#stopping-a-spot-instance).
+ If your instance is in an Auto Scaling group, Amazon EC2 Auto Scaling marks the stopped instance as unhealthy, and may terminate it and launch a replacement instance. To prevent this, you can suspend the scaling processes for the group while you're changing the instance type. For more information, see [Suspend and resume a process for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html) in the Amazon EC2 Auto Scaling documentation.
+ When you change the instance type of an instance with NVMe instance store volumes, the updated instance might have additional instance store volumes, because all NVMe instance store volumes are available even if they aren't specified in the Amazon Machine Image (AMI) or instance block device mapping. Otherwise, the updated instance has the same number of instance store volumes that you specified when you launched the original instance.

## Additional resources
<a name="right-size-selection-resources"></a>
+ [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/) (AWS documentation)
+ [AWS Optimization and Licensing Assessment](https://aws.amazon.com/optimization-and-licensing-assessment/) (AWS documentation)
