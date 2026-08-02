---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-oracle-database-homogeneous-migration/optimize.html
---

# Phase 4: Operate and optimize
<a name="optimize"></a>

After you move your database to AWS, follow AWS best practices for monitoring, alerting, backups, and license management. If you rehosted Oracle Database on Amazon EC2, you are responsible for setting up monitoring, alerting, backups, high availability, and disaster recovery solutions. If you migrated to Amazon RDS for Oracle, many of these configurations are managed by Amazon RDS, and you can set them up on the AWS Management Console.

For monitoring and alerting, you can use the following tools:
+ [Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
+ [Amazon Performance Insights](https://aws.amazon.com/rds/performance-insights/)
+ [Amazon DevOps Guru](https://aws.amazon.com/devops-guru/)
+ [Oracle Enterprise Manager (OEM) integration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.OEM.html)
+ Third-party monitoring tools

To back up databases on Amazon EC2, see the following blog posts:
+ [Using AWS Backup and Oracle RMAN for backup/restore of Oracle databases on Amazon EC2: Part 1](https://aws.amazon.com/blogs/architecture/using-aws-backup-and-oracle-rman-for-backup-restore-of-oracle-databases-on-amazon-ec2-part-1/)
+ [Using AWS Backup and Oracle RMAN for backup/restore of Oracle databases on Amazon EC2: Part 2](https://aws.amazon.com/blogs/architecture/using-aws-backup-and-oracle-rman-for-backup-restore-of-oracle-databases-on-amazon-ec2-part-2/)

To manage database licenses, see [AWS License Manager](https://aws.amazon.com/license-manager/).

To make sure that Amazon EC2 is patched frequently and to review the database patching schedule, use [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html).
