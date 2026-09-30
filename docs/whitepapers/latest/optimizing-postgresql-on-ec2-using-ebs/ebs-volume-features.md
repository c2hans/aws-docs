---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/ebs-volume-features.html
---

# Amazon EBS volume features
<a name="ebs-volume-features"></a>

## Amazon EBS monitoring
<a name="ebs-monitoring"></a>

 Amazon EC2 allows different types of metrics and logs to be collected, viewed, and analyzed. The metrics deal with the Amazon EC2 instance, storage, network and application level. Amazon EBS automatically sends data points to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) for one-minute intervals at no charge. Amazon CloudWatch metrics are statistical data to view, analyze, and set alarms on the operational behavior of storage volumes. The Amazon EBS metrics can be viewed by selecting the monitoring tab of the volume in the Amazon EC2 console. For more information about the Amazon EBS metrics collected by CloudWatch, refer to the [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html).

## Amazon EBS durability and availability
<a name="ebs-durability-and-availability"></a>

 [Amazon EBS general purpose volumes](https://aws.amazon.com/ebs/features/) are designed for reliability with a 0.1 percent to 0.2 percent annual failure rate (AFR) compared to the typical 2 percent of commodity disk drives. These storage volumes are backed by multiple physical drives for redundancy that is replicated within an Availability Zone to protect database workload from component failure. Amazon EBS also offers a higher durability volume (io2), that is designed to provide 99.999% durability with an annual failure rate (AFR) of 0.001%, where failure refers to a complete or partial loss of the volume. For example, if you have 100,000 Amazon EBS io2 volumes running for one year, you should expect only one io2 volume to experience a failure. This makes io2 ideal for business-critical PostgreSQL applications. For more details, see the [Amazon EBS Service Level Agreement.](https://aws.amazon.com/ebs/sla/)

## Amazon EBS snapshots
<a name="ebs-snapshots"></a>

 Amazon EBS snapshots back up the data on Amazon EBS volumes by taking point-in-time snapshots to Amazon Simple Storage Service (Amazon S3) which is designed for 99.999999999% (11 nines) of durability. Apart from providing backup, other reasons for creating Amazon EBS snapshots include:
+  **Set up a non-production or test environment** — You can share the Amazon EBS snapshot to duplicate the installation of PostgreSQL in different environments. You can also share Amazon EBS snapshots among different AWS accounts within the same AWS Region. For example, you can restore a snapshot of your PostgreSQL database that's in a production environment to a test environment to duplicate and troubleshoot production issues.
+  **Disaster recovery** — Amazon EBS's ability to copy snapshots across AWS Regions makes it easier to use multiple AWS Regions for geographical expansion, data center migration and disaster recovery. Amazon EBS Snapshots can be copied from one AWS Region to another for site disaster recovery.
+  **Meet compliance and regulatory obligations -** Certain industries require periodic archival of key data including PostgreSQL databases. Amazon EBS Snapshots enable you to use Amazon EBS Snapshots archive which is a lower storage cost tier that stores a full copy of your point-in-time Amazon EBS Snapshots, and can be restored as needed.

 In addition, you can also use [Data Lifecycle Manager (DLM)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html) which provides a mechanism to automate creation, retention, archival and deletion of Amazon EBS Snapshots. This facilitates simple and automated way to manage backup of PostgreSQL data stored on Amazon EBS volumes. You can define backup and retention schedules for Amazon EBS snapshots by creating lifecycle policies based on tags. With this feature, there are no dependencies to rely on custom scripts to create and manage your backups.

 Also, note that a volume that is restored from a snapshot is lazily loaded in the background, which means that you can start using PostgreSQL database right away. When you perform a query on a PostgreSQL data that has not been downloaded yet, the data will be downloaded from Amazon S3 directly. You also have the option of enabling Amazon EBS fast snapshot restore to create a volume from a snapshot that is fully initialized at creation. For an additional hourly charge, you can enable Fast Snapshot Restore (FSR) capability for low latency access to data restored from snapshots. You can enable FSR on snapshots you own or those shared with you. Amazon EBS volumes restored from FSR-enabled snapshots instantly receive their full performance. Refer to [Amazon EBS fast snapshot restore](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.html) for more information.

## Amazon EBS security
<a name="ebs-security"></a>

 Amazon EBS encryption offers seamless encryption of Amazon EBS data volumes, boot volumes and snapshots, eliminating the need to build and manage a secure key management infrastructure. Amazon EBS supports several security features to use from volume creation to utilization. These features prevent unauthorized access to PostgreSQL databases. You can use tags and resource-level permissions to enforce security on volumes upon creation. These tags are typically used to track resources, control cost, implement compliance protocols, and control access to resources through AWS Identity and Access Management (IAM) policies. Tags can be assigned on Amazon EBS volumes during creation time for efficient volume management. After the volume is created, you can use the IAM [resource-level permissions for Amazon EC2 API actions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html) where only authorized IAM users; or groups who can attach, delete, or detach Amazon EBS volumes to Amazon EC2 instances.

 Protection of data in transit and at rest is crucial in most PostgreSQL implementations. You can use Secure Sockets Layer (SSL) to encrypt the connection from application to PostgreSQL database. To encrypt data at rest, Amazon EBS volumes should have encryption enabled at the time of creation. The new volume gets a unique 256-bit AES key, which is protected by the fully managed [AWS Key Management Service](https://aws.amazon.com/kms/). Amazon EBS snapshots created from the encrypted volumes are automatically encrypted. Encryption operations occur on the servers that host Amazon EC2 instances, ensuring the security of both data-at-rest and data-in-transit between an instance and its attached Amazon EBS storage. The Amazon EBS encryption feature is available on all current generation instance types. For more information on the supported instance types, refer to the [Amazon EBS Encryption documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances).

## Elastic volumes
<a name="elastic-volumes"></a>

 Elastic volumes is a feature that allows you to easily adapt Amazon EBS volumes according to the needs of your application's requirements. The elastic feature of Amazon EBS SSD volumes allows you to dynamically change the size, performance, and type of Amazon EBS volume in a single API call or within the AWS Management Console without any interruption of PostgreSQL operations. This simplifies some of the administration and maintenance activities of PostgreSQL workloads running on [current generation Amazon EC2 instances.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#current-gen-instances)

 You can call the [ModifyVolume](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVolume.html) API to dynamically increase the size of the Amazon EBS volume if the PostgreSQL database is running low on usable storage capacity. Note that decreasing the size of the Amazon EBS volume isn't supported, so AWS recommends not to over-allocate the Amazon EBS volume size any more than necessary to avoid paying for extra resources that you do not use.

 In situations where there is a planned increase in your PostgreSQL utilization, you can either change your volume type or add additional IOPS. The time it takes to complete these changes depends on the size of Amazon EBS volume. The progress of the volume modification can be monitored either through the AWS Management Console or CLI. You can also create CloudWatch Events to send alerts after the changes are complete.

## Amazon EBS–optimized instances
<a name="ebsoptimized-instances"></a>

 Amazon EBS–optimized instances deliver dedicated throughput between Amazon EC2 and Amazon EBS. The dedicated throughput minimizes contention between Amazon EBS I/O and other traffic from Amazon EC2 instance, providing the best performance for PostgreSQL workloads. It is recommended to choose an Amazon EBS–optimized instance that provides more dedicated Amazon EBS throughput than application needs; otherwise, the connection between Amazon EBS and Amazon EC2 can become a performance bottleneck. For more information about the instance types that can be launched as Amazon EBS-Optimized instances, see [Amazon EC2 Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html).
