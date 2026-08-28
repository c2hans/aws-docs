---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/cpu.html
---

# Adjust CPU settings
<a name="cpu"></a>

The default CPU settings on a SQL Server database allow processes to consume all available resources to complete their tasks. This configuration can starve EnterpriseOne processes on the CPU resources they require, causing performance issues and timeouts. To mitigate this issue, you can adjust the maximum degree of parallelism and cost threshold settings.

## Adjust MAXDOP
<a name="maxdop"></a>

By default, the maximum degree of parallelism (MAXDOP) is set to unlimited (0). Setting MAXDOP to a value of 1 disables parallelism and forces queries to run single-threaded. A value other than 0 or 1 sets the maximum number of parallel threads (vCPUs) that a single query can use.

To set the appropriate value for MAXDOP, consider the following:
+ If you're running SQL Server Enterprise edition, you can use Resource Governor to control CPU allocation. However, because SQL Server Standard edition is typically more cost-effective, many EnterpriseOne installations cannot use Resource Governor.
+ Most EnterpriseOne processes are short DML operations and do not use parallelism. However, many third-party applications benefit from parallelism and might experience performance degradation when parallelism is reduced or disabled.
+ You can set a smaller MAXDOP value to limit the ability of any single process to saturate the system.

We recommend that you set the MAXDOP value, at most, to half the number of the vCPUs available in the instance. The minimum MAXDOP value would be 1, which disables parallelism entirely. The following query disables parallelism by setting MAXDOP to 1, but you can adjust the script to set it to any other MAXDOP value.

|
|
| Note    The scripts in this guide use `JDE_Prist920` as the EnterpriseOne database name. To use the scripts, update the database name to reflect your database. |
| --- |

```
USE JDE_Prist920;
GO
EXEC sp_configure 'show advanced options', 1;
GO
RECONFIGURE WITH OVERRIDE;
GO
EXEC sp_configure 'max degree of parallelism', 1;
GO
RECONFIGURE WITH OVERRIDE;
GO
```

## Adjust the cost threshold for parallelism
<a name="cost-threshold"></a>

If you enable parallelism by setting MAXDOP to a value greater than 1, set the cost threshold for parallelism to 50 or higher to limit the number of EnterpriseOne queries that are considered for parallelism. You can use the following script to set the value.If parallelism is enabled by setting maxDOP to a value greater than 1, set the "cost threshold for parallelism" to 50 or higher to limit the number of E1 queries are are considered for parallelism. The following script can be used to set the value.

```
EXEC sp_configure 'show advanced options', 1 ;
GO
RECONFIGURE
GO
EXEC sp_configure 'cost threshold for parallelism', 50 ;
GO
RECONFIGURE
GO
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
