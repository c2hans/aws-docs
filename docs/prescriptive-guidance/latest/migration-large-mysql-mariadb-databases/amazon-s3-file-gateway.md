---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/amazon-s3-file-gateway.html
---

# Using Amazon S3 File Gateway to transfer backup files
<a name="amazon-s3-file-gateway"></a>

[Amazon S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/what-is-file-s3.html) connects your on-premises environment to Amazon Simple Storage Service (Amazon S3) through a file interface so that you can store and retrieve Amazon S3 objects by using industry-standard file protocols, such as Network File System (NFS) and Server Message Block (SMB). It is designed to be a cost-effective, scalable solution for storing data in the cloud. Because you can use it to store database backup files, this service can help you migrate large, on-premises databases to the AWS Cloud. For example, you could use Amazon S3 File Gateway and your preferred database backup tool to back up the large MySQL or MariaDB database directly to an Amazon S3 bucket. You can then mount the S3 bucket to the target instance and restore the backup.

The following diagram shows the high-level steps involved when using Amazon S3 File Gateway to transfer the backup file for an on-premises database to an S3 bucket in the AWS Cloud.

![Diagram showing the transfer of a database backup file to the cloud by using Amazon S3 File Gateway.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/images/guide-img/49694e39-c5ff-41ab-af3d-e68e9b6e3ab5/images/3fd3b0d9-2188-4395-be8e-9fa80a366302.png)

The following are the steps for using Amazon S3 File Gateway to transfer a database backup file from an on-premises data center to an S3 bucket in the AWS Cloud:

1. Connect the on-premises data center to the AWS Cloud by using a service such as AWS Direct Connect or AWS Site-to-Site VPN or by using a public internet connection.

1. Create an S3 File Gateway. For instructions, see [Creating your gateway](https://docs.aws.amazon.com/filegateway/latest/files3/create-file-gateway.html).

1. Create an NFS or SMB file share that is hosted by the S3 File Gateway. For instructions, see [Create a file share](https://docs.aws.amazon.com/filegateway/latest/files3/GettingStartedCreateFileShare.html).

1. Mount the NFS or SMB file share on the on-premises server that hosts your MySQL or MariaDB database. For instructions, see [Mount and use your file share](https://docs.aws.amazon.com/filegateway/latest/files3/getting-started-use-fileshare.html).

1. Back up the on-premises MySQL or MariaDB database to the directory where the NFS file share is mounted. You can use any of the backup tools discussed in this guide.

1. Restore the database backup on the target database instance by using any of the approaches discussed in this guide.

## Advantages
<a name="advantages-amazon-s3-file-gateway"></a>
+ By producing database backups directly in the S3 bucket and restoring the backup on the target DB instance directly from the same S3 bucket, you can significantly accelerate the end-to-end migration process.
+ Database backup files are stored durably in Amazon S3, and you choose the lifecycle management policy and S3 storage class.

## Limitations
<a name="limitations-amazon-s3-file-gateway"></a>

The following are limitations when using Amazon S3 File Gateway file shares:
+ The maximum number of file shares per gateway is 50.
+ To prevent read and write conflicts when multiple file shares use the same S3 bucket, you must configure each file share to use a unique prefix name.
+ The maximum size of an individual file is 5 TB, which is the maximum size of any individual object in Amazon S3.
+ The maximum path length is 1024 characters.
+ Windows ACLs are supported only on file shares that are enabled for Active Directory when you use Windows SMB clients to access the file shares.
+ Amazon S3 File Gateway supports a maximum of 10 ACL entries for each file and directory.
+ The root ACL settings of SMB file shares are only on the gateway. These settings are persistent across gateway updates and restarts.

<table>
<tbody>
</tbody>
</table>

## Best practices
<a name="best-practices-amazon-s3-file-gateway"></a>

For more information about the best practices for Amazon S3 File Gateway, see [Best practices](https://docs.aws.amazon.com/filegateway/latest/files3/best-practices.html) in the S3 File Gateway documentation.
