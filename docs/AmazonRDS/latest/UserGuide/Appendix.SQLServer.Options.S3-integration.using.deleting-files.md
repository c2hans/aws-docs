---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.using.deleting-files.html
---

# Deleting files on the RDS DB instance
<a name="Appendix.SQLServer.Options.S3-integration.using.deleting-files"></a>

To delete the files available on the DB instance, use the Amazon RDS stored procedure `msdb.dbo.rds_delete_from_filesystem` with the following parameters.

| Parameter name | Data type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `@rds_file_path` | NVARCHAR | – | Required | The file path of the file to delete. Absolute and relative paths are supported.  |
| `@force_delete` | INT | 0 | Optional | To delete a directory, this flag must be included and set to `1`.<br />`1` = delete a directory<br />This parameter is ignored if you are deleting a file. |

To delete a directory, the `@rds_file_path` must end with a backslash (`\`) and `@force_delete` must be set to `1`.

The following example deletes the file `D:\S3\delete_me.txt`.

```
exec msdb.dbo.rds_delete_from_filesystem
    @rds_file_path='D:\S3\{{delete_me.txt}}';
```

The following example deletes the directory `D:\S3\example_folder\`.

```
exec msdb.dbo.rds_delete_from_filesystem
    @rds_file_path='D:\S3\{{example_folder}}\',
    @force_delete=1;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
