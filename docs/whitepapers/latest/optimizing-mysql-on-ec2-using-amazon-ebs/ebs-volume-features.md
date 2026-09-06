---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-mysql-on-ec2-using-amazon-ebs/ebs-volume-features.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# EBS volume features
<a name="ebs-volume-features"></a>

## EBS monitoring
<a name="ebs-monitoring"></a>

 Amazon EBS automatically sends data points to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) for one-minute intervals at no charge. Amazon CloudWatch metrics are statistical data that you can use to view, analyze, and set alarms on the operational behavior of your volumes. The EBS metrics can be viewed by selecting the monitoring tab of the volume in the Amazon EC2 console. For more information about the EBS metrics collected by CloudWatch, refer to the [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html).

## EBS durability and availability
<a name="ebs-durability-and-availability"></a>

 Durability in the storage subsystem for MySQL is especially important if you are storing user data, valuable production data, and individual data points. [EBS volumes](https://aws.amazon.com/ebs/features/) are designed for reliability with a 0.1 percent to 0.2 percent annual failure rate (AFR) compared to the typical 4 percent of commodity disk drives. EBS volumes are backed by multiple physical drives for redundancy that is replicated within the Availability Zone to protect your MySQL workload from component failure.

## EBS snapshots
<a name="ebs-snapshots"></a>

 You can perform backups of your entire MySQL database using EBS snapshots. These snapshots are stored in Amazon Simple Storage Service (S3), which is designed for 99.999999999% (11 nines) of durability. To satisfy your recovery point and recovery time objectives, you can [schedule EBS snapshots using Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/TakeScheduledSnapshot.html).

 Apart from providing backup, other reasons for creating EBS snapshots of your MySQL database include:
+  **Set up a non-production or test environment** — You can share the EBS snapshot to duplicate the installation of MySQL in different environments and also share between different AWS accounts within the same Region. For example, you can restore a snapshot of your MySQL database that’s in a production environment to a test environment to duplicate and troubleshoot production issues.
+  **Disaster recovery** — EBS snapshots can be copied from one AWS Region to another for site disaster recovery.

 A volume that is restored from a snapshot loads slowly in the background, which means that you can start using your MySQL database right away. When you perform a query on MySQL that finds a table that has not been downloaded yet, the data will be downloaded from Amazon S3. You also have the option of enabling Amazon EBS fast snapshot restore to create a volume from a snapshot that is fully initialized at creation. Refer to [Amazon EBS fast snapshot restore](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.html) for more information. Best practices for restoring EBS snapshots are discussed in the [*MySQL backups*](mysql-backups.md) section of this whitepaper.

## EBS security
<a name="ebs-security"></a>

 Amazon EBS supports several security features you can use from volume creation to utilization. These features prevent unauthorized access to your MySQL data.

 You can use tags and resource-level permissions to enforce security on your volumes upon creation. Tags are key-value pairs that you can assign to your AWS resources as part of infrastructure management. These tags are typically used to track resources, control cost, implement compliance protocols, and control access to resources through AWS Identity and Access Management (IAM) policies. You can assign tags on EBS volumes during creation time, which allows you to enforce the management of your volume as soon as it is created.

 Additionally, you can have granular control on who can create or delete tags through the IAM resource-level permissions. This granularity of control extends to the `RunInstances` and `CreateVolume` APIs where you can write IAM policies that requires the encryption of the EBS volume upon creation.

 After the volume is created, you can use the IAM [resource-level permissions for Amazon EC2 API actions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html) where you can specify the authorized users or groups who can attach, delete, or detach EBS volumes to EC2 instances.

 Protection of data in transit and at rest is crucial in most MySQL implementations. You can use Secure Sockets Layer (SSL) to encrypt the connection from your application to your MySQL database. To encrypt your data at rest, you can enable volume encryption during creation time. The new volume will get a unique 256-bit AES key, which is protected by the fully managed AWS Key Management Service. EBS snapshots created from the encrypted volumes are automatically encrypted.

 The Amazon EBS encryption feature is available on all current generation instance types. For more information on the supported instance types, refer to the [Amazon EBS Encryption documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances).

## Elastic Volumes
<a name="elastic-volumes"></a>

 The Elastic Volumes feature of EBS SSD volumes allows you to dynamically change the size, performance, and type of EBS volume in a single API call or within the AWS Management Console without any interruption of MySQL operations. This simplifies some of the administration and maintenance activities of MySQL workloads running on [current generation EC2 instances.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#current-gen-instances)

 You can call the [ModifyVolume](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVolume.html) API to dynamically increase the size of the EBS volume if the MySQL database is running low on usable storage capacity. Note that decreasing the size of the EBS volume isn’t supported, so AWS recommends that you do not over-allocate the EBS volume size any more than necessary to avoid paying for extra resources that you do not use.

 In situations where there is a planned increase in your MySQL utilization, you can either change your volume type or add additional IOPS. The time it takes to complete these changes will depend on the size of your MySQL volume. You can monitor the progress of the volume modification either through the AWS Management Console or CLI. You can also create CloudWatch Events to send alerts after the changes are complete.
