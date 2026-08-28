---
source_url: https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/choosing-between-amazon-rds-amazon-ec2-or-vmware-cloud-on-aws-for-your-oracle-database.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Choosing between Amazon RDS, Amazon EC2, or VMware Cloud on AWS for your Oracle database
<a name="choosing-between-amazon-rds-amazon-ec2-or-vmware-cloud-on-aws-for-your-oracle-database"></a>

 Both Amazon RDS and Amazon EC2 offer different advantages for running Oracle Database. Amazon RDS is easier to set up, manage, and maintain than running Oracle Database on Amazon EC2, and lets you focus on other important tasks, rather than the day-to-day administration of Oracle Database. Alternatively, running Oracle Database on Amazon EC2 gives you more control, flexibility, and choice. Depending on your application and your requirements, you might prefer one over the other.

 If you are migrating multiple Oracle databases to AWS, you will find that some of them are a great fit for Amazon RDS while others are better suited to run directly on Amazon EC2. Many AWS customers run several databases across Amazon RDS, Amazon EC2, and VMware Cloud on AWS for their Oracle Database workloads.

 Amazon RDS might be a better choice for you if:
+  You want to focus on your business and applications, and have AWS take care of the undifferentiated heavy lifting tasks such as provisioning of the database, management of backup and recovery tasks, management of security patches, minor Oracle version upgrades, and storage management.
+  You need a highly available database solution and want to take advantage of the push-button, synchronous Multi-AZ replication offered by Amazon RDS, without having to manually set up and maintain a standby database.
+  You would like to have synchronous replication to a standby instance for high availability for Oracle Database Standard Edition One or Standard Edition Two.
+  You want to pay for the Oracle license as part of the instance cost on an hourly basis instead of making a large upfront investment.
+  Your database size and IOPS needs are less than the RDS Oracle limits. Refer to [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) for the current maximum.
+  You don’t want to manage backups and, most importantly, point-in-time recoveries of your database.
+  You would rather focus on high-level tasks, such as performance tuning and schema optimization, rather than the daily administration of the database.
+  You want to scale the instance type up or down based on your workload patterns without being concerned about licensing and the complexity involved.

 Amazon EC2 might be a better choice for you if:
+  You need full control over the database, including SYS/SYSTEM user access, or you need access at the operating system level.
+  Your database size exceeds the 80% of current maximum database size in Amazon RDS.
+  You need to use Oracle features or options that are not [currently supported by Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html).
+  Your database IOPS needs are higher than the [current IOPS limit](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html).
+  You need a specific Oracle Database version that is not supported by Amazon RDS. For more information, refer to [Oracle Database Editions](https://aws.amazon.com/rds/oracle/features/#Oracle_Database_Editions).

 VMware Cloud on AWS might be a better choice for you if:
+  Your Oracle databases are already running in on-premises data center in vSphere virtualized environments.
+  You need to run Oracle Real Application Clusters (RAC) in the cloud.
+  You have large number of databases and you need faster migration (in order of few hours) to migrate to cloud without any migration team man-hours.
+  You need to preserve the IP addresses of the databases and applications, when migrating to cloud, to avoid any post-migration re-work.
+  You need the performance of NVMe storage in Amazon EC2 bare metal hosts along with data persistence.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
