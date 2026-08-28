---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.ReadReplicas.Troubleshooting.html
---

# Troubleshooting a SQL Server read replica problem
<a name="SQLServer.ReadReplicas.Troubleshooting"></a>

You can monitor replication lag in Amazon CloudWatch by viewing the Amazon RDS `ReplicaLag` metric. For information about replication lag time, see [Monitoring read replication](USER_ReadRepl.Monitoring.md).

If replication lag is too long, you can use the following query to get information about the lag.

```
SELECT AR.{{replica_server_name}}
     , DB_NAME (ARS.database_id) '{{database_name}}'
     , AR.availability_mode_desc
     , ARS.synchronization_health_desc
     , ARS.last_hardened_lsn
     , ARS.last_redone_lsn
     , ARS.secondary_lag_seconds
FROM sys.dm_hadr_database_replica_states ARS
INNER JOIN sys.availability_replicas AR ON ARS.replica_id = AR.{{replica_id}}
--WHERE DB_NAME(ARS.database_id) = '{{database_name}}'
ORDER BY AR.{{replica_server_name}};
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
