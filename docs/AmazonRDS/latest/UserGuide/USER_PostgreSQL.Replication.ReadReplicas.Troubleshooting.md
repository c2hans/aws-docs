---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.ReadReplicas.Troubleshooting.html
---

# Troubleshooting for RDS for PostgreSQL read replica
<a name="USER_PostgreSQL.Replication.ReadReplicas.Troubleshooting"></a>

Following, you can find troubleshooting ideas for some common RDS for PostgreSQL read replica issues.

**Terminate the query that causes the read replica lag**
Transactions either in active or idle in transaction state that are running for a long time in the database might interfere with the WAL replication process, thereby increasing the replication lag. Therefore, be sure to monitor the runtime of these transactions with the PostgreSQL `pg_stat_activity` view.
Run a query on the primary instance similar to the following to find the process ID (PID) of the query that's running for a long time:

```
SELECT datname, pid,usename, client_addr, backend_start,
xact_start, current_timestamp - xact_start AS xact_runtime, state,
backend_xmin FROM pg_stat_activity WHERE state='active';
```

```
SELECT now() - state_change as idle_in_transaction_duration, now() - xact_start as xact_duration,*
FROM  pg_stat_activity
WHERE state  = 'idle in transaction'
AND   xact_start is not null
ORDER BY 1 DESC;
```
After identifying the PID of the query, you can choose to end the query.
Run a query on the primary instance similar to the following to terminate the query that's running for a long time:

```
SELECT pg_terminate_backend(PID);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
