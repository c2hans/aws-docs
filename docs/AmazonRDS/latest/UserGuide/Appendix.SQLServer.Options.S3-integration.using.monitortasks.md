---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.using.monitortasks.html
---

# Monitoring the status of a file transfer task
<a name="Appendix.SQLServer.Options.S3-integration.using.monitortasks"></a>

To track the status of your S3 integration task, call the `rds_fn_task_status` function. It takes two parameters. The first parameter should always be `NULL` because it doesn't apply to S3 integration. The second parameter accepts a task ID.

To see a list of all tasks, set the first parameter to `NULL` and the second parameter to `0`, as shown in the following example.

```
SELECT * FROM msdb.dbo.rds_fn_task_status(NULL,{{0}});
```

To get a specific task, set the first parameter to `NULL` and the second parameter to the task ID, as shown in the following example.

```
SELECT * FROM msdb.dbo.rds_fn_task_status(NULL,{{42}});
```

The `rds_fn_task_status` function returns the following information.

|  Output parameter  |  Description  |
| --- | --- |
| `task_id` | The ID of the task. |
| `task_type` | For S3 integration, tasks can have the following task types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.using.monitortasks.html) |
| `database_name` | Not applicable to S3 integration tasks. |
| `% complete` | The progress of the task as a percentage. |
| `duration(mins)` | The amount of time spent on the task, in minutes. |
| `lifecycle` | The status of the task. Possible statuses are the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.using.monitortasks.html) |
| `task_info` | Additional information about the task. If an error occurs during processing, this column contains information about the error.  |
| `last_updated` | The date and time that the task status was last updated.  |
| `created_at` | The date and time that the task was created. |
| `S3_object_arn` | The ARN of the S3 object downloaded from or uploaded to. |
| `overwrite_S3_backup_file` | Not applicable to S3 integration tasks. |
| `KMS_master_key_arn` | Not applicable to S3 integration tasks. |
| `filepath` | The file path on the RDS DB instance. |
| `overwrite_file` | An option that indicates if an existing file is overwritten. |
| `task_metadata` | Not applicable to S3 integration tasks. |
