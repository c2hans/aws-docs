---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.TransactionLogAccess.S3namingConvention.html
---

# Amazon S3 bucket folder and file structure
<a name="USER.SQLServer.AddlFeat.TransactionLogAccess.S3namingConvention"></a>

Transaction log backups have the following standard structure and naming convention within an Amazon S3 bucket:
+ A new folder is created under the `target_s3_arn` path for each database with the naming structure as `{db_id}.{family_guid}`.
+ Within the folder, transaction log backups have a filename structure as `{db_id}.{family_guid}.{rds_backup_seq_id}.{backup_file_epoch}`.
+ You can view the details of `family_guid,db_id,rds_backup_seq_id and backup_file_epoch` with the `rds_fn_list_tlog_backup_metadata`function.

The following example shows the folder and file structure of a set of transaction log backups within an Amazon S3 bucket.

![Amazon S3 bucket structure with access to transaction logs.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/sql_accesstransactionlogs_s3.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
