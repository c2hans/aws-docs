---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/ebs-volume-types.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon EBS volume types
<a name="ebs-volume-types"></a>

## General purpose SSD volumes
<a name="general-purpose-ssd-volumes"></a>

 General purpose SSD (`gp2` and `gp3`) volumes are backed by solid-state drives (SSDs). These storge options balance price and performance for a wide variety of database workloads. Both `gp2` and `gp3` volumes provide single-digit millisecond latency and 99.8 percent to 99.9 percent volume durability with an annual failure rate (AFR) no higher than 0.2 percent, which translates to a maximum of two volume failures per 1,000 running volumes over a one-year period.

### `gp2`
<a name="gp2"></a>

 The general purpose SSD (`gp2`) volume offers balanced price and performance. To maximize the performance of the `gp2` volume, you need to know how the burst capability works. The size of the `gp2` volume determines the baseline performance level of the volume and how quickly it can accumulate [I/O credits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#IOcredit). Depending on the volume size, baseline performance ranges between a minimum of 100 IOPS up to a maximum of 16,000 IOPS per volume. Volumes earn I/O credits at the baseline performance rate of 3 IOPS/GiB of volume size. The larger the volume size, the higher the baseline performance and the faster I/O credits accumulate. Refer to [General purpose SSD volumes (`gp2`)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#EBSVolumeTypes_gp2) for more information related to I/O characteristics and burstable performance of `gp2` volumes.

### `gp3`
<a name="gp3"></a>

 These volumes deliver a consistent baseline rate of 3,000 IOPS and 125 MiB/s, included with the price of storage. You can provision additional IOPS (up to 16,000) and throughput (up to 1,000 MiB/s) for an additional cost. The maximum ratio of Provisioned IOPS to provisioned volume size is 500 IOPS per GiB. The maximum ratio of provisioned throughput to Provisioned IOPS is .25 MiB/s per IOPS. The following volume configurations support provisioning either maximum IOPS or maximum throughput:
+  **32 GiB or larger:** 500 IOPS/GiB x 32 GiB = 16,000 IOPS
+  **8 GiB or larger and 4,000 IOPS or higher:** 4,000 IOPS x 0.25 MiB/s/IOPS = 1,000 MiB/s

 In addition to change the volume type, size and provisioned throughput (for `gp3` only); you can also use RAID 0 to stripe multiple `gp2` or `gp3` volumes together to achieve greater I/O performance. The I/O is striped across volumes in the RAID 0 configuration. The throughput of your PostgreSQL database also rises with the addition of an extra volume. The read/write transfer rate, or throughput, is calculated by multiplying the I/O block size by the IOPS rate that is carried out on the disk. Since the performance of the stripe is only as good as the lowest performing volume in the set, AWS advises adding the same volume size to the stripe set. Think about RAID 0's failure tolerance as well as a single volume loss results in a total loss of data for the array. If possible, use RAID 0 in a PostgreSQL primary/secondary environment where data is already replicated in multiple secondary nodes.

## Provisioned IOPS SSD volumes
<a name="provisioned-iops-ssd-volumes"></a>

 [Provisioned IOPS SSD](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#EBSVolumeTypes_piops) (`io1`, `io2`, `io2` Block Express) volumes are designed to meet the needs of I/O-intensive workloads, particularly database workloads that are sensitive to storage performance and consistency. Provisioned IOPS SSD volumes use a consistent IOPS rate, which you specify when you create the volume. Amazon EBS delivers the provisioned performance 99.9 percent of the time.
+  `io1` volumes are designed to provide 99.8 to 99.9 percent volume durability with an annual failure rate (AFR) no higher than 0.2 percent, which translates to a maximum of two volume failures per 1,000 running volumes over a one-year period.
+  `io2`  and `io2` Block Express volumes are designed to provide 99.999 percent volume durability with an AFR no higher than 0.001 percent, which translates to a single volume failure per 100,000 running volumes over a one-year period.

 Provisioned IOPS SSD `io1` and `io2` volumes are available for all Amazon EC2 instance types. Provisioned IOPS SSD `io2` volumes attached to `c6in`, `c7g`, `m6in`, `m6idn`, `r5b`, `r6in`, `r6idn`, `trn1`, `x2idn`, and `x2iedn` instances run on Amazon EBS Block Express.

Provisioned IOPS SSD volumes can range in size from 4 GiB to 16 TiB, and you can provision from 100 IOPS up to 64,000 IOPS per volume. You can achieve up to 64,000 IOPS only on [Instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances).  This provides dedicated throughput between Amazon EBS volume and Amazon EC2 instance. On other instance families you can achieve performance up to 32,000 IOPS. The maximum ratio of provisioned IOPS to requested volume size (in GiB) is 50:1 for `io1` volumes, and 500:1 for `io2` volumes.

 `io2` Block Express volumes is the next generation of Amazon EBS storage server architecture. It has been built for the purpose of meeting the performance requirements of the most demanding I/O intensive applications that run on Nitro-based Amazon EC2 instances. You can provision IOPS up to 256,000, with an IOPS:GiB ratio of 1,000:1. Maximum IOPS can be provisioned with volumes 256 GiB in size and larger (1,000 IOPS × 256 GiB = 256,000 IOPS) while volume throughput can go up to 4,000 MiB/s.
