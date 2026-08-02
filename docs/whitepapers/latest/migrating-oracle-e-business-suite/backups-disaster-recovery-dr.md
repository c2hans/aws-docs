---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/backups-disaster-recovery-dr.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Backups and disaster recovery (DR) - Oracle E-Business Suite application and database on AWS
<a name="backups-disaster-recovery-dr"></a>

## Backup and recovery
<a name="backup"></a>

 AWS recommends implementing a robust and reliable backup and recovery procedure as part of customers build on AWS. Backup and restore policies differ between organizations, which is typically dictated based on the RPO and RTO requirements. The following are some of the options available to customers:

![Diagram showing backup architecture options.](http://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/backup-architecture-options.png)

AWS Backup, a fully managed backup and recovery service that integrates with AWS services such as Amazon EC2, Amazon FSx, Amazon EFS, Amazon EBS, and Amazon S3
+  RMAN backup weekly full (level 0)
+  RMAN daily incremental, with block change tracking enabled
+  RMAN \+ OSB > Amazon S3 \+ intelligent tiering > Amazon Glacier
+  Frequent restore testing using "RMAN restore database check logical"
+  AWS managed file and object services (Amazon S3, Amazon EFS, Amazon FSx family, Storage Gateway)
+  Tiering capabilities built into AWS storage services, object, file, and block
+  Backup capabilities, AWS and third-party agent-based tools, such as Commvault, and Veritas.

 [AWS Backup](https://aws.amazon.com/backup/), fully managed backup and recovery service which integrates with AWS services such as Amazon EC2, Amazon FSx Amazon EFS, Amazon EBS, Amazon S3, and many more

 AWS recommends a *belts and braces* approach to backing up Oracle E-Business Suite, as there is benefit in having more than one restore point in the event of a disaster. AWS recommend documenting and testing backups regularly to ensure they are working as expected.

## Disaster recovery (DR)
<a name="disaster-recovery-dr"></a>

There are a number of options for implementing DR for Oracle E-Business Suite on AWS.

[AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) is an alternative to using Oracle native tools for DR, which works at the block level and can achieve a relatively low-cost DR alternative, which can meet extremely low RPO and RTO requirements. This solution simplifies the DR solution for our customers by removing the complexity of configuring, managing and invoking a DR for these highly complexity Oracle E-Business Suite systems.

[Amazon EFS replication](https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html), You can use Amazon EFS replication to create a replica of your application file system in the AWS Region of your preference. When you enable replication on an EFS file system, Amazon EFS automatically and transparently replicates the data and metadata on the source file system to a new destination EFS file system. To manage the process of creating the destination file system and keeping it synced with the source file system, Amazon EFS uses a *replication configuration*.

Amazon EFS automatically keeps the source and destination file systems synchronized.Amazon EFS replication is continual and designed to provide a recovery point objective (RPO) and a recovery time objective (RTO) of minutes. These features should assist you in meeting your compliance and business continuity goals.

[Amazon FSx for NetApp ONTAP supports NetApp SnapMirror](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/migrating-fsx-ontap-snapmirror.html), a replication technology that you can use to replicate data between two ONTAP file systems. You can configure automatic NetApp SnapMirror replication of your application file system to another Amazon FSx for NetApp ONTAP file system in another AWS Region. With SnapMirror, you can configure replication with a recovery point objective (RPO) of as low as five minutes, and a recovery time objective (RTO) in single-digit minutes.

The following architecture represents an Oracle E-Business Suite implementation using Amazon FSx for NetApp ONTAP as the database and application storage layer. The database layer, Region 1, Availability Zone B and Region 2, Availability Zone A are passive, which means the FSx storage (containing the Oracle binaries and data files) is mounted during a failover or switchover operation. This is a potentially efficient way of providing low RPO and RTO with a reduction on licenses. Cloning to lower environments is also fast using SnapClone, which is particularly useful for large multi-terabyte databases, where AWS Snapshot or RMAN restores could take longer.

AWS does not provide licensing advice. We highly recommend that you consult with an Oracle licensing specialist to provide recommendations based on your environment.

![Reference architecture diagram showing Oracle E-Business Suite Architecture – Storage replication with Amazon FSx for NetApp ONTAP.](http://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/ebs-storage-replication.png)

 This architecture could provide the following benefits:
+  Binaries and data files stored on Amazon FSx, potentially saving on licenses
+  Ability to clone environments quickly using [FlexClone](https://aws.amazon.com/fsx/netapp-ontap/features/)
+  Ability to sync to another availability zone using [SnapMirror](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/scheduled-replication.html)
+  Low RPO, RTO, or both
