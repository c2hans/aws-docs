---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Backup.html
---

# Backing up an SSAS database
<a name="SSAS.Backup"></a>

You can create SSAS database backup files only in the `D:\S3` folder on the DB instance. To move the backup files to your S3 bucket, use Amazon S3.

You can back up an SSAS database as follows:
+ A domain user with the `admin` role for a particular database can use SSMS to back up the database to the `D:\S3` folder.

  For more information, see [Adding a domain user as a database administrator](SSAS.Use.md#SSAS.Admin).
+ You can use the following stored procedure. This stored procedure doesn't support encryption.

  ```
  exec msdb.dbo.rds_msbi_task
  @task_type='SSAS_BACKUP_DB',
  @database_name='{{myssasdb}}',
  @file_path='D:\S3\{{ssas_db_backup}}.abf',
  [@ssas_apply_compression=1],
  [@ssas_overwrite_file=1];
  ```

  The following parameters are required:
  + `@task_type` – The type of the MSBI task, in this case `SSAS_BACKUP_DB`.
  + `@database_name` – The name of the SSAS database that you're backing up.
  + `@file_path` – The path for the SSAS backup file. The `.abf` extension is required.

  The following parameters are optional:
  + `@ssas_apply_compression` – Whether to apply SSAS backup compression. Valid values are 1 (Yes) and 0 (No).
  + `@ssas_overwrite_file` – Whether to overwrite the SSAS backup file. Valid values are 1 (Yes) and 0 (No).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
