---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/messaging-and-streaming-layer.html
---

# Messaging and streaming layer
<a name="messaging-and-streaming-layer"></a>

 The messaging layer of your workload manages communications between components. The streaming layer manages real-time analysis and processing of streaming data.

 [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) provides a fully managed messaging service for pub/sub patterns using asynchronous Event Notifications and mobile push notifications for microservices, distributed systems, and serverless applications.

 [Amazon Kinesis](https://aws.amazon.com/kinesis/) makes it easy to collect, process, and analyze real-time streaming data. With [Amazon Kinesis](https://aws.amazon.com/kinesis/), you can run standard SQL, or build entire streaming applications using SQL.

 [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/) captures, transforms, and loads streaming data into [Managed Service for Apache Flink](https://aws.amazon.com/kinesis/data-analytics/), [Amazon S3](https://aws.amazon.com/s3/), [Amazon Redshift](https://aws.amazon.com/redshift/), and [OpenSearch Service](https://aws.amazon.com/opensearch-service/), enabling near real-time analytics with existing business intelligence tools.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
