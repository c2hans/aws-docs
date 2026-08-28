---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.NonPrintableData.html
---

# Reading non-printable UTF-8 character data
<a name="EMRforDynamoDB.CopyingData.NonPrintableData"></a>

To read and write non-printable UTF-8 character data, you can use the `STORED AS SEQUENCEFILE` clause when you create a Hive table. A SequenceFile is a Hadoop binary file format. You need to use Hadoop to read this file. The following example shows how to export data from DynamoDB into Amazon S3. You can use this functionality to handle non-printable UTF-8 encoded characters.

```
1. CREATE EXTERNAL TABLE {{s3_export}}({{a_col string, b_col bigint, c_col array<string>}})
2. STORED AS SEQUENCEFILE
3. LOCATION '{{s3://bucketname/path/subpath/}}';
4.
5. INSERT OVERWRITE TABLE {{s3_export}} SELECT *
6. FROM {{hiveTableName}};
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
