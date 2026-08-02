---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Monitor.html
---

# Monitoring the status of a deployment task
<a name="SSAS.Monitor"></a>

To track the status of your deployment (or download) task, call the `rds_fn_task_status` function. It takes two parameters. The first parameter should always be `NULL` because it doesn't apply to SSAS. The second parameter accepts a task ID.

To see a list of all tasks, set the first parameter to `NULL` and the second parameter to `0`, as shown in the following example.

```
SELECT * FROM msdb.dbo.rds_fn_task_status(NULL,{{0}});
```

To get a specific task, set the first parameter to `NULL` and the second parameter to the task ID, as shown in the following example.

```
SELECT * FROM msdb.dbo.rds_fn_task_status(NULL,{{42}});
```

The `rds_fn_task_status` function returns the following information.

| Output parameter | Description |
| --- | --- |
| `task_id` | The ID of the task. |
| `task_type` | For SSAS, tasks can have the following task types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Monitor.html) |
| `database_name` | Not applicable to SSAS tasks. |
| `% complete` | The progress of the task as a percentage. |
| `duration (mins)` | The amount of time spent on the task, in minutes. |
| `lifecycle` | The status of the task. Possible statuses are the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Monitor.html) |
| `task_info` | Additional information about the task. If an error occurs during processing, this column contains information about the error.<br />For more information, see [Troubleshooting SSAS issues](SSAS.Trouble.md). |
| `last_updated` | The date and time that the task status was last updated. |
| `created_at` | The date and time that the task was created. |
| `S3_object_arn` | Not applicable to SSAS tasks. |
| `overwrite_S3_backup_file` | Not applicable to SSAS tasks. |
| `KMS_master_key_arn` | Not applicable to SSAS tasks. |
| `filepath` | Not applicable to SSAS tasks. |
| `overwrite_file` | Not applicable to SSAS tasks. |
| `task_metadata` | Metadata associated with the SSAS task. |
