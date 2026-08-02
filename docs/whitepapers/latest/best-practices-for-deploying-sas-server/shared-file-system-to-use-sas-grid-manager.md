---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/shared-file-system-to-use-sas-grid-manager.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Shared file system to use SAS Grid Manager or SAS Viya
<a name="shared-file-system-to-use-sas-grid-manager"></a>

 SAS Grid Manager and SAS Viya require a shared file system for the permanent files being shared by all the SAS Grid compute nodes. The following options have been tested with SAS Grid manager on AWS:
+  Amazon FSx for Lustre — Provides a high-performance file system optimized for fast processing of workloads such as machine learning and high performance computing. These workloads commonly require data to be presented through a fast and scalable file system interface and typically have data sets stored on long-term data stores like S3.

 AWS sets up the Lustre file system with mount options *noatime* and *flock*. SAS prefers flock parameter and the mount options must be properly implemented for FSx for Lustre.

 FSx does not allow dynamic expansion for the size of the Lustre file system. If a larger size is required then a new system must to be setup, and data must be copied to the new file system.
+  Amazon Elastic File System (Amazon EFS) — Amazon EFS supports network file system version 4 protocol and allows multiple Amazon EC2 instances to interact with EFS. However, the maximum throughput I/O is 500 MB per second per instance. For more information on limits, refer to the [EFS documentation](https://docs.aws.amazon.com/efs/latest/ug/limits.html#limits-efs-resources-per-account-per-region).

 Multiple EFS file systems per instance are required to overcome this I/O throughput limitation in addition to a single NIC per AWS EC2 instance. These file systems cannot be striped together. These file systems have a total of 512 hard locks for any particular file across all users and instances connected to this system.
