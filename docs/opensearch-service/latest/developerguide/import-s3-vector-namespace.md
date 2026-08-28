---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/import-s3-vector-namespace.html
---

# Import Amazon S3 vector namespace to OpenSearch Service vector engine
<a name="import-s3-vector-namespace"></a>

Analyzing your vector data with OpenSearch Service requires a one-time OpenSearch Service collection and IAM permission setup.

**To import Amazon S3 vector namespace to OpenSearch Service vector engine**

1. In the **Source** section, configure the Amazon S3 vector index:

   1. For **Amazon S3 vector index ARN**, enter the ARN of your Amazon S3 vector index.
**Note**
Must be in format arn:aws:iam::account-id:vector-bucket-name/\*:index

1. In the **Service access** section, configure OpenSearch Service authorization:

   1. For **Choose a method to authorize OpenSearch Service**, select one of the following:
      + **Create and use a new service role**
      + **Use an existing service role**

   1. For **Service role name**, enter a name for the service role.
**Note**
Service role name must be 1 to 64 characters. Valid characters are a-z, A-Z, 0-9, and periods (.).

   1. Choose **View permission details** to review the required permissions.

1. Expand **Additional settings - optional** to configure advanced options if needed.

1. In the **Import steps** section, configure the following automation options:
   + **Automate OpenSearch Service vector collection creation** - OpenSearch Service collections are used to store vector data. Serverless compute capacity is measured in OpenSearch Service Compute Units (OCUs), by default the Max OCU capacity is 50.
   + **Automate IAM role creation for service access** - This role is used by OpenSearch Service to read the Amazon S3 vector index and write to the OpenSearch Service collection.
   + **Automate OpenSearch Service ingestion pipeline creation** - OpenSearch Service ingestion pipelines are used to ingest data. An Amazon S3 bucket is created as a best practice to capture and store failed events in an Amazon S3 bucket Dead Letter Queue (DLQ), enabling easy access for troubleshooting and analysis.

1. Choose **Import** to start the import process, or choose **Cancel** to exit without importing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
