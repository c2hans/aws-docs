---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations.html
---

# Loading streaming data into Amazon OpenSearch Service
<a name="integrations"></a>

You can use OpenSearch Ingestion to directly load [streaming data](http://aws.amazon.com/streaming-data/) into your Amazon OpenSearch Service domain, without needing to use third-party solutions. To send data to OpenSearch Ingestion, you configure your data producers and the service automatically delivers the data to the domain or collection that you specify. To get started with OpenSearch Ingestion, see [Tutorial: Ingesting data into a collection using Amazon OpenSearch Ingestion](osis-serverless-get-started.md).

You can still use other sources to load streaming data, such as Amazon Data Firehose and Amazon CloudWatch Logs, which have built-in support for OpenSearch Service. Others, like Amazon S3, Amazon Kinesis Data Streams, and Amazon DynamoDB, use AWS Lambda functions as event handlers. The Lambda functions respond to new data by processing it and streaming it to your domain.

**Note**
Lambda supports several popular programming languages and is available in most AWS Regions. For more information, see [Getting started with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-app.html) in the *AWS Lambda Developer Guide* and [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#lambda_region) in the *AWS General Reference*.

## Loading streaming data from AWS IoT
<a name="integrations-cloudwatch-iot"></a>

You can send data from AWS IoT using [rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html). To learn more, see the [OpenSearch](https://docs.aws.amazon.com/iot/latest/developerguide/opensearch-rule-action.html) action in the *AWS IoT Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
