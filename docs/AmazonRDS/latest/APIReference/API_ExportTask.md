---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ExportTask.html
---

# ExportTask
<a name="API_ExportTask"></a>

Contains the details of a snapshot or cluster export to Amazon S3.

This data type is used as a response element in the `DescribeExportTasks` operation.

## Contents
<a name="API_ExportTask_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ExportOnly.member.N **
The data exported from the snapshot or cluster.
Valid Values:
+  `database` - Export all the data from a specified database.
+  `database.table` *table-name* - Export a table of the snapshot or cluster. This format is valid only for RDS for MySQL, RDS for MariaDB, and Aurora MySQL.
+  `database.schema` *schema-name* - Export a database schema of the snapshot or cluster. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.
+  `database.schema.table` *table-name* - Export a table of the database schema. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.
Type: Array of strings
Required: No

 ** ExportTaskIdentifier **
A unique identifier for the snapshot or cluster export task. This ID isn't an identifier for the Amazon S3 bucket where the data is exported.
Type: String
Required: No

 ** FailureCause **
The reason the export failed, if it failed.
Type: String
Required: No

 ** IamRoleArn **
The name of the IAM role that is used to write to Amazon S3 when exporting a snapshot or cluster.
Type: String
Required: No

 ** KmsKeyId **
The key identifier of the AWS KMS key that is used to encrypt the data when it's exported to Amazon S3. The KMS key identifier is its key ARN, key ID, alias ARN, or alias name. The IAM role used for the export must have encryption and decryption permissions to use this KMS key.
Type: String
Required: No

 ** PercentProgress **
The progress of the snapshot or cluster export task as a percentage.
Type: Integer
Required: No

 ** S3Bucket **
The Amazon S3 bucket where the snapshot or cluster is exported to.
Type: String
Required: No

 ** S3Prefix **
The Amazon S3 bucket prefix that is the file name and path of the exported data.
Type: String
Required: No

 ** SnapshotTime **
The time when the snapshot was created.
Type: Timestamp
Required: No

 ** SourceArn **
The Amazon Resource Name (ARN) of the snapshot or cluster exported to Amazon S3.
Type: String
Required: No

 ** SourceType **
The type of source for the export.
Type: String
Valid Values: `SNAPSHOT | CLUSTER`
Required: No

 ** Status **
The progress status of the export task. The status can be one of the following:
+  `CANCELED`
+  `CANCELING`
+  `COMPLETE`
+  `FAILED`
+  `IN_PROGRESS`
+  `STARTING`
Type: String
Required: No

 ** TaskEndTime **
The time when the snapshot or cluster export task ended.
Type: Timestamp
Required: No

 ** TaskStartTime **
The time when the snapshot or cluster export task started.
Type: Timestamp
Required: No

 ** TotalExtractedDataInGB **
The total amount of data exported, in gigabytes.
Type: Integer
Required: No

 ** WarningMessage **
A warning about the snapshot or cluster export task.
Type: String
Required: No

## See Also
<a name="API_ExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ExportTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
