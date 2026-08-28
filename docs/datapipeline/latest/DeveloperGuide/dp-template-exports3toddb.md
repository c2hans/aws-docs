---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-exports3toddb.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Import DynamoDB backup data from S3
<a name="dp-template-exports3toddb"></a>

The **Import DynamoDB backup data from S3** template schedules an Amazon EMR cluster to load a previously created DynamoDB backup in Amazon S3 to a DynamoDB table. Existing items in the DynamoDB table are updated with those from the backup data and new items are added to the table. This template uses an Amazon EMR cluster, which is sized proportionally to the value of the throughput available to the DynamoDB table. Although you can increase IOPs on a table, this may incur additional costs while importing and exporting. Previously, import used a HiveActivity but now uses native MapReduce.

The template uses the following pipeline objects:
+ [EmrActivity](dp-object-emractivity.md)
+ [EmrCluster](dp-object-emrcluster.md)
+ [DynamoDBDataNode](dp-object-dynamodbdatanode.md)
+ [S3DataNode](dp-object-s3datanode.md)
+ [S3PrefixNotEmpty](dp-object-s3prefixnotempty.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
