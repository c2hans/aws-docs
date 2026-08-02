---
source_url: https://docs.aws.amazon.com/whitepapers/latest/patterns-for-ingesting-saas-data-into-aws-data-lakes/importexport-using-files.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Import/Export using files
<a name="importexport-using-files"></a>

 Many SaaS applications allow data to be exported into files. You can use any of the file transfer mechanisms listed below to move such files into Amazon S3 for further processing:

 [AWS DataSync](https://aws.amazon.com/datasync/) is a secure, online service that automates and accelerates the process of moving data between on premises and AWS storage services. DataSync can copy data between Network File System (NFS) shares, Server Message Block (SMB) shares, Hadoop Distributed File Systems (HDFS), self-managed object storage, AWS Snowcone, Amazon S3 buckets, Amazon Elastic File System (Amazon EFS) file systems, Amazon FSx for Windows File Server file systems, and Amazon FSx for Lustre file systems.

 [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/) securely scales your recurring business-to-business file transfers to Amazon S3 and Amazon EFS using SFTP, FTPS, and FTP protocols.

 You can also write your own scripts using [AWS Command Line Interface (CLI)](https://aws.amazon.com/cli/) or [AWS SDK](https://aws.amazon.com/tools/) to transfer the exported files over to Amazon S3 at a regular interval.
