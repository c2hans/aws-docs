---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Serverless.Limitations.html
---

# AWS DMS Serverless limitations
<a name="CHAP_Serverless.Limitations"></a>

AWS DMS Serverless has the following limitations:
+ You can only modify an AWS DMS replication configuration that is in the `CREATED`, `STOPPED`, `FAILED`, or `FAILED_PROVISION` states. For details about which settings you can change under which conditions, see [Modifying AWS DMS serverless replications](CHAP_Serverless.Components.md#CHAP_Serverless.modify).
+ You can only delete an AWS DMS replication configuration that is in the `STOPPED`, or `FAILED` states.
+ Unlike replication instances, AWS DMS Serverless replications do not have a public IP address for management tasks. You manage serverless replications using the console.
+ This release of AWS DMS serverless does not support all the source and target endpoint types that AWS DMS standard supports. For a list of supported engine types, see [AWS DMS Serverless components](CHAP_Serverless.Components.md).
+ Serverless replications need to access dependencies by using VPC endpoints. You must use VPC endpoints to access the following endpoint types:
  + Amazon Amazon S3
  + Amazon Kinesis
  + AWS Secrets Manager
  + Amazon DynamoDB
  + Amazon Redshift
  + Amazon OpenSearch Service

  For information about setting up VPC endpoints, see [Configuring VPC endpoints for AWS DMS](CHAP_VPC_Endpoints.md).
+ AWS DMS serverless does not support views.
+ AWS DMS Serverless does not support SSL connections for DB2 endpoints.
+ AWS DMS Serverless does not support setting custom CDC start points.
+ When a replication task is in deprovisioned state, the metadata related to the table and the replication statistics are lost.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
