---
source_url: https://docs.aws.amazon.com/whitepapers/latest/choosing-an-aws-nosql-database/amazon-dynamodb.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon DynamoDB
<a name="amazon-dynamodb"></a>

 [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) is a fully managed NoSQL database service. Some key capabilities of DynamoDB include:
+  **High performance** — Designed to provide single-digit millisecond latency for read and write operations at any scale.
+  **Scalability** — The ability to automatically scale throughput capacity in response to demand, so you can start small and scale as needed.
+  **Flexibility** — Supports both document and key-value data models, and provides rich data types such as lists and maps, making it easy to store any type of data.
+  **Durability** — Provides consistent, single-digit millisecond performance for read and write operations, even in the face of hardware failures.
+  **Global tables** — [DynamoDB global tables](https://aws.amazon.com/dynamodb/global-tables/) provides multi-[Region](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html) data replication which makes it easy to build globally distributed applications.
+  **Integrations** — Integration with other AWS services such as [AWS Lambda](https://aws.amazon.com/lambda/), [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3), [Amazon DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html), and [Amazon Kinesis](https://aws.amazon.com/kinesis/), making it easy to build serverless and data-driven applications. [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) integrates with [Amazon CloudWatch Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) to provide information about the most accessed and throttled items in a table or index. DynamoDB delivers this information to you using CloudWatch Contributor Insights rules, reports, and graphs of report data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
