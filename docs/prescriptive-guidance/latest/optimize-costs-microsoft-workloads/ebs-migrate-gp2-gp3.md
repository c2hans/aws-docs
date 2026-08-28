---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-gp2-gp3.html
---

# Migrate Amazon EBS volumes from gp2 to gp3
<a name="ebs-migrate-gp2-gp3"></a>

## Overview
<a name="ebs-migrate-gp2-gp3-overview"></a>

A solid-state drive (SSD) is the standard storage option for production and high-performance workloads. Amazon EBS offers a [general purpose SSD volume](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html) for mid- to high-performance workloads. The standard across many AWS services (including Amazon EC2) is [gp2](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html#EBSVolumeTypes_gp2), the second generation of these general purpose SSD volumes. The third generation of general purpose SSDs, called [gp3](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html#gp3-ebs-volume-type), was released in December 2020.

The gp3 offering made significant improvements to the performance customization aspects over the previous generation. For Amazon EBS gp2 volumes, the performance is closely coupled with the size of the volume. For every 1 GB of capacity, gp2 volumes get 3 IOPS of performance. That is, a 2,000 GB gp2 volume is capable of 6,000 IOPS. For gp3 volumes, performance can be customized independently from the storage capacity. This enables even small capacity volumes to achieve performance capabilities up to 80,000 IOPS and 2,000 Mb/s throughput.

Another major change with gp3 volumes is the baseline IOPS performance. The gp3 volumes start at 3,000 IOPS. By comparison, gp2 volumes must reach 1 TiB in size before reaching the same performance capability. For Windows Server, which usually has a C: drive much smaller than 1 TiB, upgrading from gp2 to gp3 is a significant performance improvement.

Finally, the price of gp3 volumes is one of the largest improvements compared to gp2 volumes. The gp3 volumes offer enhanced performance capabilities at 20 percent lower cost than gp2 volumes.

## Cost impact
<a name="ebs-migrate-gp2-gp3-cost"></a>

With the ability to scale performance independently from capacity, it's important to understand the pricing aspects of adding additional IOPS and throughput. For gp2 volumes, pricing is based on provisioned capacity at $0.10 per GiB-month. For gp3 volumes, pricing is similar to the high performance [provisioned IOPS SSD volumes](https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html#EBSVolumeTypes_piops), which have one cost for capacity and a separate cost for additional IOPS and throughput.

As noted in the following table, gp3 volumes have a capacity price at $0.08 per GiB-month (20 percent less expensive than gp2) and separate costs for IOPS at $0.005 per provisioned IOPS-month over 3,000 and $0.04 per provisioned MiBs-month over 125 MiBs for throughput.

|  |
| --- |
|  | gp3 | gp2 |
| --- |--- |--- |
| **Volume size** | 1 GiB – 64 TiB | 1 GiB – 16 TiB |
| **Baseline IOPS** | 3,000 | 3 IOPS/GiB (minimum 100 IOPS) to a maximum of 16,000 IOPS<br />Volumes smaller than 1 TiB can burst up to 3,000 IOPS |
| **Max IOPS/volume** | 80,000 | 16,000 |
| **Baseline throughput** | 125 MiBs | Throughput limit is between 128 MiBs – 250 MiBs, depending on volume size |
| **Max throughput/volume** | 2,000 MiBs | 250 MiBs |
| **Price** | $0.08/GiB-month<br />3,000 IOPS free and $0.005/provisioned IOPS-month over 3,000<br />125 MiBs free and $0.04/provisioned MiBs-month over 125 MiBs | $0.10/GiB-month |

|
|
| Important: Even though gp3 volumes have separate costs for capacity and performance, gp3 volumes are always cheaper than gp2 volumes if they're configured at the same performance levels. |
| --- |

The following tables show examples of cost savings that can be achieved by converting gp2 to gp3 volumes at various capacity and performance configurations.

**Example for gp2 configuration**

|
|
| Volume size (GiB) | Max IOPS | Throughput (MiBs) | Cost (USD/month) |
| --- |--- |--- |--- |
| 30 | 3000 | 128 | $3.00 |
| 100 | 3000 | 128 | $10.00 |
| 500 | 3000 | 250 | $50.00 |
| 1000 | 3000 | 250 | $100.00 |
| 2000 | 6000 | 250 | $200.00 |
| 6000 | 16000 | 250 | $600.00 |

**Example for gp3 (baseline) configuration**

|
|
| Max IOPS | Throughput (MiBs) | Cost (USD/month) | Cost reduction (compared to gp2) |
| --- |--- |--- |--- |
| 3000 | 125 | $2.40 | 20% |
| 3000 | 125 | $8.00 | 20% |
| 3000 | 125 | $40.00 | 20% |
| 3000 | 125 | $80.00 | 20% |
| 3000 | 125 | $160.00 | 20% |
| 3000 | 125 | $480.00 | 20% |

**Example for gp3 (gp2 matching) configuration**

|
|
| Max IOPS | Throughput (MiBs) | Cost (USD/month) | Cost reduction (compared to gp2) |
| --- |--- |--- |--- |
| 3000 | 128 | $2.52 | 16% |
| 3000 | 128 | $8.12 | 19% |
| 3000 | 250 | $45.00 | 10% |
| 3000 | 250 | $85.00 | 15% |
| 6000 | 250 | $180.00 | 10% |
| 16000 | 250 | $550.00 | 8% |

For a cost analysis, see the *EBS gp2 to gp3 migration cost savings calculator *section in [Amazon EBS resource](https://aws.amazon.com/ebs/resources/). You can download the calculator and use it to find out how much you can save by migrating your gp2 volumes to gp3.

## Cost optimization recommendations
<a name="ebs-migrate-gp2-gp3-rec"></a>

For instructions on how to complete the migration process, see the [Migrate your Amazon EBS volumes from gp2 to gp3 and save up to 20% on costs](https://aws.amazon.com/blogs/storage/migrate-your-amazon-ebs-volumes-from-gp2-to-gp3-and-save-up-to-20-on-costs/) post on the AWS Storage Blog.

## Additional resources
<a name="ebs-migrate-gp2-gp3-resources"></a>
+ [Migrate your Amazon EBS volumes from gp2 to gp3 and save up to 20% on costs](https://aws.amazon.com/blogs/storage/migrate-your-amazon-ebs-volumes-from-gp2-to-gp3-and-save-up-to-20-on-costs/) (AWS Storage Blog)
+ [Build an AWS Config Custom Rule to Optimize Amazon EBS Volume Types](https://aws.amazon.com/blogs/mt/build-an-aws-config-custom-rule-to-optimize-amazon-ebs-volume-types/) (AWS Cloud Operations & Migrations Blog)
+ [Controlling your AWS costs by deleting unused Amazon EBS volumes](https://aws.amazon.com/blogs/mt/controlling-your-aws-costs-by-deleting-unused-amazon-ebs-volumes/) (AWS Cloud Operations & Migrations Blog)
+ [Amazon EBS Migration Utility](https://github.com/aws-samples/amazon-ebs-migration-utility) (GitHub)
+ [Finding savings from 2020 re:Invent announcements](https://aws.amazon.com/blogs/aws-cloud-financial-management/finding-savings-from-2020-reinvent-announcements/) (AWS Cloud Financial Management)
+ [Cost Optimization Workshop](https://wellarchitectedlabs.com/cost-optimization/) (AWS Well-Architected Labs)
+ [gp2 to gp3 migration cost savings calculator](https://d1.awsstatic.com/product-marketing/Storage/EBS/gp2_gp3_CostOptimizer.dd5eac2187ef7678f4922fcc3d96982992964ba5.xlsx) (download)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
