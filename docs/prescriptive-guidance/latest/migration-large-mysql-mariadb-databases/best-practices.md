---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/best-practices.html
---

# Best practices for migrating large MySQL and MariaDB databases
<a name="best-practices"></a>

In addition to the tool-specific best practices listed for each migration option, review the following general best practices. These best practices apply when migrating large, multi-terabyte MySQL and MariaDB databases, regardless of the tool you select:
+ Make sure that there is sufficient space on the source and destination databases to take and restore the backup.
+ Don't create secondary indexes on the target database instance until the migration is complete. Secondary indexes add additional maintenance overhead during import and can slow down the import process.
+ If you use a multi-threaded approach, choose the right number of threads. For export, we recommend you use one thread for each CPU core. For import, we recommend you use one thread for every two CPU cores.
+ Data dumps are often performed from active database servers that are part of a mission-critical production environment. If the data dump severely affects performance and this isn't acceptable in your environment, consider one of the following:
  + The source server has replicas, you can dump data from one of the replicas.
  + The source server is covered by regular backup procedures:
    + If the backup format is suitable for direct import into the target database, use the backup data as the input for the import process.
    + If the backup format isn't suitable for direct import into the target database, use the backup to provision a temporary database and dump data from it.
  + If replicas and backups aren't available:
    + Perform dumps during off-peak hours, when production traffic is at its lowest.
    + Reduce the concurrency of dump operations so that the server has enough spare capacity to handle production traffic.
+ Create dumps of user-created databases only.
+ Re-create the users on the target database and configure their permissions. For more information, see [Identity and access management for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAM.html), [Identity and access management for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAM.html), or [Identity and access management for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-iam.html).
+ When migrating a large database server that consists of multiple, independent databases, create a separate instance for each database. This helps you manage the database more efficiently and can improve resource provisioning, and the separate compute resources can improve database performance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
