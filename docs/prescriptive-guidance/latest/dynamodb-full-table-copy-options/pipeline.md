---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/pipeline.html
---

# Using AWS Data Pipeline
<a name="pipeline"></a>

**Note**
AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

[AWS Data Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html) is a web service that you can use to automate the movement and transformation of data. Using Data Pipeline, you can create a pipeline to export table data from the source account. The exported data is stored in an Amazon Simple Storage Service (Amazon S3) bucket in the target account. The S3 bucket in the target account must be accessible from the source account. To allow this cross-account access, update the access control list (ACL) in the target S3 bucket.

Create another pipeline in the target account (Account-B) to import data from the S3 bucket into the table in the target account.

This was the traditional way to back up DynamoDB tables to Amazon S3 and to restore from Amazon S3 until AWS Glue introduced support for reading from DynamoDB tables natively.

## Advantages
<a name="advantages.60412439-22a2-5f27-8d3b-93335cc0b886"></a>
+ It's a serverless solution.
+ No new code is required.
+ AWS Data Pipeline uses Amazon EMR clusters behind the scenes for the job, so this approach is efficient and can handle large datasets.

## Drawbacks
<a name="drawbacks.0bf8152c-6fc2-58ed-944a-65cd7308a67e"></a>
+ Additional AWS services (Data Pipeline and Amazon S3) are required.
+ The process consumes provisioned throughput on the source table and the target tables involved, so it can affect performance and availability.
+ This approach incurs additional costs, over the cost of DynamoDB read capacity units (RCUs) and write capacity units (WCUs).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
