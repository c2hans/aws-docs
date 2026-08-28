---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-datanodes.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Data Nodes
<a name="dp-concepts-datanodes"></a>

In AWS Data Pipeline, a data node defines the location and type of data that a pipeline activity uses as input or output. AWS Data Pipeline supports the following types of data nodes:

[DynamoDBDataNode](dp-object-dynamodbdatanode.md)
A DynamoDB table that contains data for [HiveActivity](dp-object-hiveactivity.md) or [EmrActivity](dp-object-emractivity.md) to use.

[SqlDataNode](dp-object-sqldatanode.md)
An SQL table and database query that represent data for a pipeline activity to use.
Previously, MySqlDataNode was used. Use SqlDataNode instead.

[RedshiftDataNode](dp-object-redshiftdatanode.md)
An Amazon Redshift table that contains data for [RedshiftCopyActivity](dp-object-redshiftcopyactivity.md) to use.

[S3DataNode](dp-object-s3datanode.md)
An Amazon S3 location that contains one or more files for a pipeline activity to use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
