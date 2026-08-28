---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.Native.Compression.html
---

# Compressing backup files
<a name="SQLServer.Procedural.Importing.Native.Compression"></a>

To save space in your Amazon S3 bucket, you can compress your backup files. For more information about compressing backup files, see [Backup compression](https://msdn.microsoft.com/en-us/library/bb964719.aspx) in the Microsoft documentation.

Compressing your backup files is supported for the following database editions:
+ Microsoft SQL Server Enterprise Edition
+ Microsoft SQL Server Standard Edition

To verify the compression option for your backup files, run the following code:

```
1. exec rdsadmin.dbo.rds_show_configuration 'S3 backup compression';
```

To turn on compression for your backup files, run the following code:

```
1. exec rdsadmin.dbo.rds_set_configuration 'S3 backup compression', 'true';
```

To turn off compression for your backup files, run the following code:

```
1. exec rdsadmin.dbo.rds_set_configuration 'S3 backup compression', 'false';
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
