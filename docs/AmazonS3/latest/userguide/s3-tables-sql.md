---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-sql.html
---

# Granting access with SQL semantics
<a name="s3-tables-sql"></a>

You can grant permissions to tables by using SQL semantics in table and table bucket policies. Examples of SQL semantics you can use are `CREATE`, `INSERT`, `DELETE`, `UPDATE`, and `ALTER`. The following table provides a list of API actions associated with SQL semantics that you can use to grant permissions to your users.

S3 Tables partially supports permissions using SQL semantics. For example, the `CreateTable` API only creates an empty table in the table bucket. You need additional permissions such as, `UpdateTableMetadata`, `PutTableData`, and `GetTableMetadataLocation` to be able to set the table schema. These additional permissions also mean that you are also granting the user access to insert rows in the table. If you wish to govern access purely based on SQL semantics, then we recommend using [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) or any third-party solution that is integrated with S3 Tables.

| Table-level activity | IAM actions |
| --- | --- |
| SELECT | s3tables:GetTableData, s3tables:GetTableMetadataLocation |
| CREATE | s3tables:CreateTable, s3tables:UpdateTableMetadataLocation, s3tables:PutTableData, s3tables:GetTableMetadataLocation,  |
| INSERT | s3tables:UpdateTableMetadataLocation, s3tables:PutTableData, s3tables:GetTableMetadataLocation |
| UPDATE | s3tables:UpdateTableMetadataLocation, s3tables:PutTableData, s3tables:GetTableMetadataLocation |
| ALTER,RENAME | s3tables:UpdateTableMetadataLocation, s3tables:PutTableData, s3tables:GetTableMetadataLocation, s3tables:RenameTable  |
| DELETE,DROP | s3tables:DeleteTable, s3tables:UpdateTableMetadataLocation, s3tables:PutTableData, s3tables:GetTableMetadataLocation  |

**Note**
The `s3tables:DeleteTable` permission is required to delete a table from a table bucket. This permission allows you to permanently remove a table and all its associated data and metadata. Use this permission carefully as the delete operation cannot be undone.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
