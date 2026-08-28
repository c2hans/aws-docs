---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/ec2-sql-choosing.html
---

# When to choose Amazon EC2
<a name="ec2-sql-choosing"></a>

Amazon EC2 is a good migration option for your SQL Server database when:
+ You need full control over the database and access to its underlying operating system, database installation, and configuration.
+ You want to administer your database, including backups and recovery, patching the operating system and the database, tuning the operating system and database parameters, managing security, and configuring high availability or replication.
+ You want to use features and options that aren't currently supported by Amazon RDS for SQL Server. For details, see [Features not supported and features with limited support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.FeatureNonSupport) in the Amazon RDS documentation.
+ You need a specific SQL Server version that isn't supported by Amazon RDS. For a list of supported versions and editions, see [SQL Server versions on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.VersionSupport) in the Amazon RDS documentation.
+ Your database size and performance needs exceed the current Amazon RDS for SQL Server offerings. For details, see [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) in the Amazon RDS documentation.
+ You want to avoid automatic software patches that might not be compliant with your applications.
+ You want to bring your own license instead of using the Amazon RDS for SQL Server license-included model.
+ You want to achieve higher IOPS and storage capacity than the current limits. For details, see [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) in the Amazon RDS documentation.

For a list of currently supported SQL Server features and versions on Amazon EC2, see [Choosing between Amazon EC2 and Amazon RDS](comparison.md) later in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
