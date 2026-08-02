---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/high-availability.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# High availability
<a name="high-availability"></a>

 Depending on the need for high availability (HA), a process should be placed in a new instance in case that the existing instance fails. This failover practice is a benefit of running SAS application on AWS.

 For SAS Grid Manager customers, a shared file system, such as Intel Lustre or IBM Spectrum Scale, will remain operational if one of the nodes associated with the shared file system terminates unexpectedly. However, any data associated with the node will not be available until the node is restored. Only one copy of the data is stored by default and it is possible to enable replication of the data to two or three copied across the

 shared file system from the nodes in the system, especially with FSx Lustre, which is backed up into Amazon S3.

 If customers would like to implement redundancy mechanisms, they must decide the downtime SLAs that they are willing to accept, and based on those choices, implement a pilot light, cold start, warm-standby, or active-active setup. With any of the above HA options, customers must mirror SAS deployment, SAS Files, and data store to the appropriate Region/Availability Zone for HA. At minimum, it is expected that customer builds for cold starts with data stores and deployment files are backed up to S3 in separate production accounts. For more information, refer to the option for single host SAS 9.4 on AWS with backups to Amazon Glacier.
