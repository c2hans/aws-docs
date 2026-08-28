---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-load.cancel.html
---

# Canceling data loading
<a name="limitless-load.cancel"></a>

To cancel a data loading job, call the `rds_aurora.limitless_data_load_cancel` stored procedure, with the job ID as the input parameter. You call this stored procedure from the same database in the DB shard group where the specific data loading job was started. For example:

```
CALL rds_aurora.limitless_data_load_cancel(12345);

INFO: limitless data load job with id 12345 is canceling without rollback.
```

You can't cancel a data loading job that doesn't exist or isn't running in the same DB shard group.

The Aurora PostgreSQL Limitless Database data loading utility leaves loaded data in the destination tables without rollback, as the response shows. If you don’t want to keep the loaded data, we recommend truncating the destination tables.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
