---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/oracle-dump-files-aws/dump-files-to-amazon-efs.html
---

# Using Amazon EFS to transfer dump files
<a name="dump-files-to-amazon-efs"></a>

Amazon Elastic File System (Amazon EFS) provides serverless, fully elastic file storage for sharing file data without managing capacity or performance. You can transfer files between your Oracle DB instance and your Amazon RDS for Oracle instance. With this approach, you can transfer Oracle Data Pump files between Amazon EFS and your Amazon RDS for Oracle DB instance. You don't need to copy these files locally because Data Pump imports directly from the Amazon EFS file system.

For more information about configuring Amazon EFS to move the Oracle Database dump files between the source and target databases, see the blog post [Integrate Amazon RDS for Oracle with Amazon EFS](https://aws.amazon.com/blogs/database/integrate-amazon-rds-for-oracle-with-amazon-efs/). For information about transferring Oracle Database dump files between the source and target systems, see the [Oracle documentation](https://docs.oracle.com/en/learn/create_nfs_linux/#introduction).

For security best practices when using Amazon EFS, see the [AWS documentation](https://docs.aws.amazon.com/efs/latest/ug/security-considerations.html).

If there is no storage at the source for Oracle database dump files, you can do the following:
+ Add a network attached storage (NAS) device for taking Oracle database dump files. For more information, see the [Oracle documentation](https://docs.oracle.com/cd/E11882_01/install.112/e48357/app_nas.htm#SSDBI1365).
+ Mount an Amazon EFS file system on premises and take Oracle database dump files by using AWS Direct Connect and AWS Virtual Private Network (Site-to-Site VPN). For more information, see the [AWS documentation](https://docs.aws.amazon.com/efs/latest/ug/efs-onpremises.html).
