---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dr-standard-edition-amazon-rds/native-transaction-log-backup.html
---

# Native transaction log backup replication
<a name="native-transaction-log-backup"></a>

Amazon RDS for SQL Server takes periodic transaction log backups. It provides [access to transaction log backups](https://aws.amazon.com/about-aws/whats-new/2022/11/amazon-rds-sql-server-supports-access-transaction-log-backups/) in an AWS managed [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket. With this feature, you can access these transaction log backup files and copy them to an S3 bucket in your own account.

This approach provides the cross-Region disaster recovery solution with the lowest recovery point objective (RPO) for Amazon RDS for SQL Server standard editions. An overview of the solution and detailed instructions are explained in the blog post [Implement Amazon RDS for SQL Server Standard edition cross-Region disaster recovery using access to transaction log backups feature](https://aws.amazon.com/blogs/database/implement-amazon-rds-for-sql-server-standard-edition-cross-region-disaster-recovery-using-access-to-transaction-log-backups-feature/).

This solution uses logs copy to provide continuous replication across Regions, so you have minimal RPO. The RPO depends on transaction log generation and network transfer time.

The cost associated with this solution is higher because the Amazon RDS for SQL Server instance in the DR must be up and running all the time. Additionally, you will need a tracking instance of Amazon RDS for SQL Server.

The failover is manual and not transparent to the application. After failover, you must modify the application connection settings or DNS values.
