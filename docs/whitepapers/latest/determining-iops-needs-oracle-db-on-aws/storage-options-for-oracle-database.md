---
source_url: https://docs.aws.amazon.com/whitepapers/latest/determining-iops-needs-oracle-db-on-aws/storage-options-for-oracle-database.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Storage options for Oracle Database
<a name="storage-options-for-oracle-database"></a>

 For Oracle Database storage on AWS, you must use [Amazon Elastic Block Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) (Amazon EBS) volumes, which offer the consistent, low-latency performance required to run your Oracle Database. Each Amazon EBS volume is automatically replicated within its Availability Zone to protect you from component failure, which provides high availability and durability. Amazon EBS provides these volume types:
+  General Purpose solid state drive (SSD) (`gp2`)
+  General Purpose SSD (`gp3`)
+  Provisioned IOPS SSD (`io1`)
+  Provisioned IOPS SSD (`io2`)
+  Throughput Optimized hard disk drive (HDD) (`st1`)
+  Cold HHD (`sc1`)

 Volume types differ in performance characteristics and cost. For the high and consistent IOPS required for Oracle Database, Amazon EBS General Purpose SSD or Amazon EBS Provisioned IOPS SSD volumes are the best fit.

 For `gp2` volumes, IOPS performance is directly related to the provisioned capacity. `gp2` volumes can deliver a consistent baseline of 3 IOPS/GB up to a maximum of 16,000 IOPS (based on 16 KB/IO) for a 16 TB volume. Input/output (I/O) is included in the price of `gp2` volumes, so you pay only for each gigabyte of storage that you provision. `gp2` volumes also have the ability to burst to 3,000 IOPS per volume, independent of volume size, to meet the periodic spike in performance that most applications need. This is a useful database feature, for which you can predict normal IOPS needs well, but you might still experience an occasional higher spike based on specific workloads.

 Currently, `gp3` is available for Oracle databases running on Amazon EC2. It has the same qualities of `gp2` but also increases the throughput from 250 MiB/s to 1,000 MiB/s.

 `gp2` volumes are sufficient for most Oracle Database workloads. If you need more IOPS and throughput than `gp2` can provide, Provisioned IOPS (PIOPS) is the best choice. `io2` volumes can provide up to 64,000 IOPS per volume for [AWS Nitro](https://aws.amazon.com/ec2/nitro/)-based instances and 32,000 IOPS per volume for other instance families.

 Throughput optimized HDD volumes (`st1`) offer low-cost HDD volume designed for intensive workloads that require less IOPS but high throughput. Oracle databases used for data warehouses and data analytics purposes can use st1 volumes. Any log processing or data staging areas that require high throughput, such as Oracle external tables or external BLOB storage, can use `st1` volumes. `st1` volumes can handle a maximum of 500 IOPS per volume.

 Cold HDD volumes (`sc1`) are suitable for legacy systems that you retain for occasional reference or archive purposes. These systems are accessed less frequently and only a few scans are performed each day on the volume.

 You can create striped volumes (areas of free space on multiple volumes) for more IOPS and larger capacity. The maximum IOPS an EC2 instance can support across all EBS volumes is 260,000. The maximum IOPS an RDS instance can support is 256,000. Use only Amazon EBS-optimized instances with `gp2` and PIOPS. You can use multiple EBS volumes individually for different data files, but striped volumes allow better throughput, balancing, scalability, and burstable performance (for `gp2`).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
