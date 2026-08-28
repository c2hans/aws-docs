---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Restore.html
---

# Restoring an SSAS database
<a name="SSAS.Restore"></a>

Use the following stored procedure to restore an SSAS database from a backup.

You can't restore a database if there is an existing SSAS database with the same name. The stored procedure for restoring doesn't support encrypted backup files.

```
exec msdb.dbo.rds_msbi_task
@task_type='SSAS_RESTORE_DB',
@database_name='{{mynewssasdb}}',
@file_path='D:\S3\{{ssas_db_backup}}.abf';
```

The following parameters are required:
+ `@task_type` – The type of the MSBI task, in this case `SSAS_RESTORE_DB`.
+ `@database_name` – The name of the new SSAS database that you're restoring to.
+ `@file_path` – The path to the SSAS backup file.

## Restoring a DB instance to a specified time
<a name="SSAS.PITR"></a>

Point-in-time recovery (PITR) doesn't apply to SSAS databases. If you do PITR, only the SSAS data in the last snapshot before the requested time is available on the restored instance.

**To have up-to-date SSAS databases on a restored DB instance**

1. Back up your SSAS databases to the `D:\S3` folder on the source instance.

1. Transfer the backup files to the S3 bucket.

1. Transfer the backup files from the S3 bucket to the `D:\S3` folder on the restored instance.

1. Run the stored procedure to restore the SSAS databases onto the restored instance.

   You can also reprocess the SSAS project to restore the databases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
