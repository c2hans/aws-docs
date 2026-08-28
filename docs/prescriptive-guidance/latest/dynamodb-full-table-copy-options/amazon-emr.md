---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/amazon-emr.html
---

# Using Amazon EMR
<a name="amazon-emr"></a>

This solution uses EMR clusters behind the scenes for the job. The EMR clusters in the source account read from the source Amazon DynamoDB table and write to a destination S3 bucket. The target EMR clusters read from the destination S3 bucket and write to the target DynamoDB table.

To replicate DynamoDB tables using this approach, EMR clusters configured with Apache Hive must be launched in both the source and target accounts. Both EMR clusters must be configured with read/write permissions for the destination S3 bucket.

## Advantages
<a name="advantages.ce417b34-299a-5f10-9295-d569c1c7cafa"></a>
+ The solution provides more options for customization and provides more control over the data migration process.

## Drawbacks
<a name="drawbacks.4b20f720-6915-5a68-beba-c307a9a7d9fe"></a>
+ The process is more involved, because it requires running Hive queries on the source and the target and creating an external table on the S3 location to contain the data.
+ It requires setting up the clusters and terminating them after the completion of the job.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
