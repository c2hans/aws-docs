---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting-using-x-ray.html
---

# Troubleshooting Amazon Simple Queue Service queues using AWS X-Ray
<a name="sqs-troubleshooting-using-x-ray"></a>

AWS X-Ray collects data about requests that your application serves and lets you view and filter data to identify potential issues and opportunities for optimization. For any traced request to your application, you can see detailed information about the request, the response, and the calls that your application makes to downstream AWS resources, microservices, databases and HTTP web APIs.

To send AWS X-Ray trace headers through Amazon SQS, you can do one of the following:
+ Use the `X-Amzn-Trace-Id` [tracing header](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-tracingheader).
+ Use the `AWSTraceHeader` [message system attribute](sqs-message-metadata.md#sqs-message-system-attributes).

To collect data on errors and latency, you must instrument the [`AmazonSQS`](https://docs.aws.amazon.com/sdk-for-java/latest/reference/index.html?com/amazonaws/services/sqs/AmazonSQSClient.html) client using the [AWS X-Ray SDK](https://docs.aws.amazon.com/xray-sdk-for-java/latest/javadoc/index.html).

You can use the AWS X-Ray console to view the map of connections between Amazon SQS and other services that your application uses. You can also use the console to view metrics such as average latency and failure rates. For more information, see [Amazon SQS and AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-sqs.html) in the *AWS X-Ray Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
