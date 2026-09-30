---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-mysql-on-ec2-using-amazon-ebs/ebs-volume-types.html
---

# Amazon EBS volume types
<a name="ebs-volume-types"></a>

## General Purpose SSD volumes
<a name="general-purpose-ssd-volumes"></a>

 General Purpose SSD volumes are designed to provide a balance of price and performance.

 The General Purpose SSD (gp3) volumes offer cost-effective storage that is ideal for a broad range of database workloads. These volumes deliver a consistent baseline rate of 3,000 IOPS and 125 MiB/s, included with the price of storage. You can provision additional IOPS (up to 16,000) and throughput (up to 1,000 MiB/s) for an additional cost. The maximum ratio of Provisioned IOPS to provisioned volume size is 500 IOPS per GiB. The maximum ratio of provisioned throughput to Provisioned IOPS is .25 MiB/s per IOPS. The following volume configurations support provisioning either maximum IOPS or maximum throughput:
+ **32 GiB or larger:** 500 IOPS/GiB x 32 GiB = 16,000 IOPS
+ **8 GiB or larger and 4,000 IOPS or higher:** 4,000 IOPS x 0.25 MiB/s/IOPS = 1,000 MiB/s

The older General Purpose SSD (gp2) volume is also a good option because it also offers balanced price and performance. To maximize the performance of the gp2 volume, you need to know how the [burst bucket](https://aws.amazon.com/blogs/database/understanding-burst-vs-baseline-performance-with-amazon-rds-and-gp2/) works. The size of the gp2 volume determines the baseline performance level of the volume and how quickly it can accumulate [I/O credits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#IOcredit). Depending on the volume size, baseline performance ranges between a minimum of 100 IOPS up to a maximum of 16,000 IOPS. Volumes earn I/O credits at the baseline performance rate of 3 IOPS/GiB of volume size. The larger the volume size, the higher the baseline performance and the faster I/O credits accumulate. Refer to [General Purpose SSD volumes (gp2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#EBSVolumeTypes_gp2) for more information related to I/O characteristics and burstable performance of gp2 volumes.

 In addition to changing the volume type, size, and provisioned throughput (for gp3 only); you can also use RAID 0 to stripe multiple gp2 or gp3 volumes together to achieve greater I/O performance. The RAID 0 configuration distributes the I/O across volumes in a stripe. Adding an additional volume also increases the throughput of your MySQL database. Throughput is the read/write transfer rate, which is the I/O block size multiplied by the IOPS rate performed on the disk. AWS recommends adding the same volume size into the stripe set since the performance of the stripe is limited to the worst performing volume in the set. Also consider fault tolerance in RAID 0. A loss of a single volume results in a complete data loss for the array. If possible, use RAID 0 in a MySQL primary/secondary environment where data is already replicated in multiple secondary nodes.

## Provisioned IOPS SSD (io1) volumes
<a name="provisioned-iops-ssd-io1-volumes"></a>

 [Provisioned IOPS SSD](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#EBSVolumeTypes_piops) (io1, io2, and io2 Block Express) volumes are designed to meet the needs of I/O-intensive workloads, particularly database workloads that are sensitive to storage performance and consistency. Provisioned IOPS SSD volumes use a consistent IOPS rate, which you specify when you create the volume, and Amazon EBS delivers the provisioned performance 99.9 percent of the time.
+  io1 volumes are designed to provide 99.8 to 99.9 percent volume durability with an annual failure rate (AFR) no higher than 0.2 percent, which translates to a maximum of two volume failures per 1,000 running volumes over a one-year period.
+  io2 and io2 Block Express volumes are designed to provide 99.999 percent volume durability with an AFR no higher than 0.001 percent, which translates to a single volume failure per 100,000 running volumes over a one-year period.

 The maximum ratio of Provisioned IOPS to requested volume size (in GiB) is 50:1 for io1 volumes, and 500:1 for io2 volumes. For example, a 100 GiB io1 volume can be provisioned with up to 5,000 IOPS, while a 100 GiB io2 volume can be provisioned with up to 50,000 IOPS.

 [io2 Block Express](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/provisioned-iops.html#io2-block-express) volumes are the next generation of Amazon EBS storage server architecture. They are built to meet the performance requirements of the most demanding I/O-intensive workloads that run on instances built on the Nitro System. With io2 Block Express, you can provision up to 256,000 IOPS per volume, with an IOPS to volume size (in GiB) ratio of 1,000:1, and up to 4,000 MiB/s of throughput.

 To maximize the volume throughput, AWS recommends using an [Amazon EBS–optimized instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html#current) (note that most new Amazon EC2 instances are Amazon EBS–optimized by default, with no extra charge). This provides dedicated throughput between your Amazon EBS volume and Amazon EC2 instance. As instance size and type affects volume throughput, choose an instance that has more channel bandwidth than the maximum throughput of the io1 volume.

 For example, an `r5.12xlarge` instance provides a maximum bandwidth of 9,500 MB/s. Therefore, it can more than handle the 1,187.5 MB/s maximum throughput of the io1 volume. Another approach to increasing io1 throughput is to configure RAID 0 on your Amazon EBS volumes. For more information about RAID configuration, refer to [RAID configuration](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/raid-config.html) in the *Amazon EC2 User Guide*.
