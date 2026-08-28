---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sql-server-rds-sql-server-replication.html
---

# Migrate SQL Server database with AWS DMS ongoing replication
<a name="chap-manageddatabases.sql-server-rds-sql-server-replication"></a>

After you complete the full load, set up ongoing replication using AWS DMS to keep the source and target databases synchronized. To configure the ongoing replication task, open the AWS DMS console. On the **Create database migration task** page, follow these three steps.
+ For **Migration type**, select **Replicate ongoing changes**.
+ Under **CDC start mode for source transactions**, select **Specify a log sequence number**.
+ Under **System change number**, enter the SQL Server log sequence number that you captured during the full load.

For more information, see [Continuous replication tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
