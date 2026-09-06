---
source_url: https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/database-storage.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Database storage
<a name="database-storage"></a>

 Most users typically use Amazon EBS for database storage. For some very high-performance architectures, you can use instance storage SSDs, but they should be augmented with Amazon EBS storage for reliable persistence.

 For high and consistent IOPS and database performance, AWS highly recommends using General Purpose (GP2) volumes or Provisioned IOPS (PIOPS) volumes. GP2 and PIOPS volumes are available for both Amazon EC2 and Amazon RDS. Refer to [ Amazon RDS DB instance storage ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) for the latest limits of IOPS per volume for both GP2 and PIOPS volume types. GP2 volumes provide an excellent balance of price and performance for most database needs. When your database requires higher IOPS than what GP2 can provide, PIOPS volumes are the right choice.

 For PIOPS volumes, you specify an IOPS rate when you create the volume, and Amazon EBS delivers within 10% of the Provisioned IOPS performance 99.9% of the time over a given year. The ratio of IOPS provisioned to the volume size requested can be a maximum of 30. For example, to get 3,000 IOPS your volume size should be at least 100 GB.

 Similar to PIOPS volumes, GP2 volumes are also SSD-based, but the IOPS you get from GP2 volumes can vary from a baseline IOPS up to a maximum burstable 3,000 IOPS per volume. This works very well for most database workloads because the IOPS performance needed from the database varies many times during a period of time based on the load size and the number of queries being executed.

 General Purpose (SSD) volume performance is governed by volume size, which dictates the base performance level of the volume and how quickly it accumulates I/O credits. Larger volumes have higher base performance levels and accumulate I/O credits faster.

 I/O credits represent the available bandwidth that your General Purpose (SSD) volume can use to burst large amounts of I/O when more than the base performance is needed. The more credits your volume has for I/O, the more time it can burst beyond its base performance level and the better it performs when more performance is needed.

 Throughput Optimized HDD volumes (st1) offers low-cost HDD volume designed for intensive workloads that require less IOPS but high throughput. Oracle databases used for data warehouses and data analytics purposes can leverage st1 volumes.

Any log processing or data staging areas like Oracle external tables or external BLOB storage that require high throughput can leverage st1 volumes. Throughput optimized (st1) volumes can handle max 500 IOPS per volume.

 Cold HDD volumes (sc1) are suitable for handling legacy systems, which are kept around for occasional reference or archive purposes. These systems are accessed less frequently and a few scans are performed per day on the volume.

 A good approach is to estimate the amount of IOPS consistently needed for your database, and allocate enough GP2 storage to obtain that many IOPS. Any additional IOPS needed for periodic spikes should be covered by the burst performance based on the available credits.

For information about estimation methods you can use to determine the IOPS needs of your Oracle Database, refer to the [Determining the IOPS Needs for Oracle Database on AWS](https://docs.aws.amazon.com/whitepapers/latest/determining-iops-needs-oracle-db-on-aws/determining-iops-needs-oracle-db-on-aws.html) whitepaper.

 The burst duration of a volume is dependent on the size of the volume, the burst IOPS required, and the credit balance when the burst begins. If you notice that your volume performance is frequently limited to the base level (due to an empty I/O credit balance), you should consider using a larger General Purpose (SSD) volume (with a higher base performance level) or switching to a Provisioned IOPS (SSD) volume for workloads that require sustained IOPS performance greater than 10,000 IOPS. For additional details about GP2 volumes, refer to [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html).

 For Amazon RDS, General Purpose (SSD) storage delivers a consistent baseline of 3 IOPS per provisioned GB and provides the ability to burst up to 3,000 IOPS. If you are already using magnetic storage for Amazon RDS, you can convert to General Purpose (SSD) storage, but you will encounter a short availability impact when doing so. Using Provisioned IOPS, you can provision up to the current maximum storage limit and the maximum IOPS per database instance.

Your actual realized IOPS may vary from the amount you provisioned based on your database workload, instance type, and database engine. For more information, refer to [Factors That Affect Realized IOPS Rates in the *Amazon RDS User Guide*](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html).

 For Oracle Database on Amazon EC2, stripe multiple volumes together for more IOPS and larger capacity. You can use multiple Amazon EBS volumes individually for different data files, but striping them together allows better balancing and scalability.

Oracle Automatic Storage Management (ASM) can be used for striping. Keep data files, log files, and binaries on separate Amazon EBS volumes, and take snapshots of log file volumes on a regular basis. Choosing an instance type with local SSD storage allows you to boost the database performance by using Smart Flash Cache (if the operating system is Oracle Linux) and by using local storage for temporary files and table spaces.

 For Oracle Database on VMware Cloud on AWS, vSAN provides necessary virtualized storage striped across the bare metal hosts. vSAN virtualized storage capability can be used in Oracle RAC for high-performance shared storage.

The VMDK (virtual machine disk) files created for Oracle RAC have to be provisioned for eager zero thick and be multi-writer flag enabled. VMware has published a [detailed performance study](https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/whitepaper/solutions/oracle/vmw-oracle-performance-on-the-vmware-cloud-on-aws.pdf) for Oracle databases on VMware Cloud on AWS.
