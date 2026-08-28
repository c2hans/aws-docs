---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.SQLRef.html
---

# MariaDB on Amazon RDS SQL reference
<a name="Appendix.MariaDB.SQLRef"></a>

Following, you can find descriptions of system stored procedures that are available for Amazon RDS instances running the MariaDB DB engine.

You can use the system stored procedures that are available for MySQL DB instances and MariaDB DB instances. These stored procedures are documented at [RDS for MySQL stored procedure reference](Appendix.MySQL.SQLRef.md). MariaDB DB instances support all of the stored procedures, except for `mysql.rds_start_replication_until` and `mysql.rds_start_replication_until_gtid`.

Additionally, the following system stored procedures are supported only for Amazon RDS DB instances running MariaDB:
+ [mysql.rds\_replica\_status](mysql_rds_replica_status.md)
+ [mysql.rds\_set\_external\_master\_gtid](mysql_rds_set_external_master_gtid.md)
+ [mysql.rds\_kill\_query\_id](mysql_rds_kill_query_id.md)
+ [mysql.rds\_execute\_operation](mysql_rds_execute_operation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
