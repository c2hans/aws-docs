---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-managing-on-aws/backup-compare.html
---

# Backup option comparison
<a name="backup-compare"></a>

We completed performance benchmark testing on the approaches covered in this guide. The tests were performed with an r5d.8xlarge instance and 1TB SQL Server database as the source. The source system was configured according to best practices, and the source database contained four data files (250 GB each) and one log file (50 GB) spread across separate GP3 volumes. The SQL Server native BACKUP command included writing to 10 backup files, using compression to optimize backup performance and reduce the amount of data sent across the network and written to the target. In all test cases, the source database or target backup option, storage performance was the bottleneck.

There is an almost endless variety of possible configurations for these types of test. We took care to optimize for performance, cost, scalability, and real-world use cases. The backup target options with details and performance are included in the following table.

|
|
| Backup options | Run duration | Backup rate |
| --- |--- |--- |
| Native backup to local EBS volume st1 HDD<br />2 TB st1 500 IOPS 500 MiB/s | 00:30:46 | 554.7 Mbps |
| Native backup to FSx for Windows File Server <br />HDD 10 TB at 512 Mbps throughput | 00:20:58 | 814.0 Mbps |
| Native backup to Amazon S3 File Gateway<br />m6i.4xlarge (16 vCPU, 64 GB) with 2 TB gp3 | 00:23:20 | 731.5 Mbps |
| VSS-enabled EBS snapshot | 00:00:53 | Not applicable (snapshot) |
| AWS Backup AMI | 00:08:00 | Not applicable (snapshot) |

Based on our testing, native SQL Server database backups to FSx for Windows File Server is the fastest option, while backups to Storage Gateway and locally attached EBS volumes are more cost-efficient with slower performance. For server-level backups (AMI), AWS Backup should be used for optimal performance, cost, and manageability.
