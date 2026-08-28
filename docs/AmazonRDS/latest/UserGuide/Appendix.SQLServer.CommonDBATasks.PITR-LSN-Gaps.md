---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.PITR-LSN-Gaps.html
---

# Troubleshooting point-in-time-recovery failures due to a log sequence number gap
<a name="Appendix.SQLServer.CommonDBATasks.PITR-LSN-Gaps"></a>

When attempting point-in-time-recovery (PITR) in RDS for SQL Server, you might encounter failures due to gaps in log sequence numbers (LSNs). These gaps prevent RDS from restoring your database to the requested time and RDS places your restoring instance in `incompatible-restore` state.

Common causes for this issue are:
+ Manual changes to the database recovery model.
+ Automatic recovery model changes by RDS due to insufficient resources for completing transaction log backups.

To identify LSN gaps in your database, run this query:

```
SELECT * FROM msdb.dbo.rds_fn_list_tlog_backup_metadata({{database_name}})
ORDER BY backup_file_time_utc desc;
```

If you discover an LSN gap, you can:
+ Choose a restore point before the LSN gap.
+ Wait and restore to a point after the next instance backup completes.

To prevent this issue, we recommend you don't manually change the recovery model of your RDS for SQL Server databases, as it interrupts instance durability. We also recommend you choose an instance type with sufficient resources for your workload to ensure regular transaction log backups.

For more information about transaction log management, see [ SQL Server transaction log architecture and management guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide?view=sql-server-ver16) in the Microsoft SQL Server documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
