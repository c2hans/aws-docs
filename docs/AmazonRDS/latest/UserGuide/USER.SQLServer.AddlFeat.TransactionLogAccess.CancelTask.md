---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.TransactionLogAccess.CancelTask.html
---

# Canceling a task
<a name="USER.SQLServer.AddlFeat.TransactionLogAccess.CancelTask"></a>

To cancel a running task, call the `rds_cancel_task` stored procedure.

**Example usage:**

```
exec msdb.dbo.rds_cancel_task @task_id=ID_number;
```

The following parameter is required:
+ `@task_id` – The ID of the task to cancel. You can view the task ID by calling the `rds_task_status` stored procedure.

For more information on viewing and canceling running tasks, see [Importing and exporting SQL Server databases using native backup and restore](SQLServer.Procedural.Importing.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
