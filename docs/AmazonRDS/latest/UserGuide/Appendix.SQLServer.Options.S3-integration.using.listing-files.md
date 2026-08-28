---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.using.listing-files.html
---

# Listing files on the RDS DB instance
<a name="Appendix.SQLServer.Options.S3-integration.using.listing-files"></a>

To list the files available on the DB instance, use both a stored procedure and a function. First, run the following stored procedure to gather file details from the files in `D:\S3\`.

```
exec msdb.dbo.rds_gather_file_details;
```

The stored procedure returns the ID of the task. Like other tasks, this stored procedure runs asynchronously. As soon as the status of the task is `SUCCESS`, you can use the task ID in the `rds_fn_list_file_details` function to list the existing files and directories in D:\\S3\\, as shown following.

```
SELECT * FROM msdb.dbo.rds_fn_list_file_details({{TASK_ID}});
```

The `rds_fn_list_file_details` function returns a table with the following columns.

| Output parameter | Description |
| --- | --- |
| filepath | Absolute path of the file (for example, D:\\S3\\mydata.csv) |
| size\_in\_bytes | File size (in bytes) |
| last\_modified\_utc | Last modification date and time in UTC format |
| is\_directory | Option that indicates whether the item is a directory (true/false) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
