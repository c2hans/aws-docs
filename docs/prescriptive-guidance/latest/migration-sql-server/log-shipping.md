---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/log-shipping.html
---

# Log shipping
<a name="log-shipping"></a>

You can use log shipping to send transaction log backups from your primary, on-premises SQL Server database to one or more secondary (warm standby) SQL Server databases that are deployed on Amazon EC2 instances or Amazon RDS for SQL Server DB instances in the AWS Cloud. To set up log shipping on Amazon RDS for SQL Server, you have to use your own custom scripts.

In this scenario, you configure a warm standby SQL Server database on an Amazon EC2 instance or Amazon RDS for SQL Server DB instance, and send transaction log backups asynchronously between your on-premises database and the warm standby server in the AWS Cloud. The transaction log backups are then applied to the warm standby database. When all the logs have been applied, you can perform a manual failover and cut over to the cloud.

This option supports all versions and editions of SQL Server. After you have migrated the database to the AWS Cloud, you can add a secondary replica by using an Always On availability group for high availability and resiliency purposes.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/images/guide-img/aa3b9357-4901-48ca-9fc9-a997d21ade3e/images/e19f3ec5-7e60-44c5-ba6c-a05e580958de.png)

For more information about using this method to achieve high availability, data protection, and disaster recovery for your SQL Server databases on Amazon EC2, see [Log shipping](ec2-sql-ha.md#ec2-log-shipping) in the *Amazon EC2 for SQL Server* section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
