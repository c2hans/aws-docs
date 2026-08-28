---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-switchover.monitoring.html
---

# Monitoring the Oracle Data Guard switchover
<a name="oracle-switchover.monitoring"></a>

To check the status of your instances, use the AWS CLI command `describe-db-instances`. The following command checks the status of the DB instance {{orcl2}}. This database was a standby database before the switchover, but is the new primary database after the switchover.

```
aws rds describe-db-instances \
    --db-instance-identifier {{orcl2}}
```

To confirm that the switchover completed successfully, query `V$DATABASE.OPEN_MODE`. Check that the value for the new primary database is `READ WRITE`.

```
SELECT OPEN_MODE FROM V$DATABASE;
```

To look for switchover-related events, use the AWS CLI command `describe-events`. The following example looks for events on the {{orcl2}} instance.

```
aws rds describe-events \
    --source-identifier {{orcl2}} \
    --source-type db-instance
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
