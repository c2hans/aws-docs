---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_NotificationConfiguration.html
---

# NotificationConfiguration
<a name="API_NotificationConfiguration"></a>

A container for specifying the notification configuration of the bucket. If this element is empty, notifications are turned off for the bucket.

## Contents
<a name="API_NotificationConfiguration_Contents"></a>

 ** EventBridgeConfiguration **   <a name="AmazonS3-Type-NotificationConfiguration-EventBridgeConfiguration"></a>
Enables delivery of events to Amazon EventBridge.
Type: [EventBridgeConfiguration](API_EventBridgeConfiguration.md) data type
Required: No

 ** LambdaFunctionConfigurations **   <a name="AmazonS3-Type-NotificationConfiguration-LambdaFunctionConfigurations"></a>
Describes the AWS Lambda functions to invoke and the events for which to invoke them.
Type: Array of [LambdaFunctionConfiguration](API_LambdaFunctionConfiguration.md) data types
Required: No

 ** QueueConfigurations **   <a name="AmazonS3-Type-NotificationConfiguration-QueueConfigurations"></a>
The Amazon Simple Queue Service queues to publish messages to and the events for which to publish messages.
Type: Array of [QueueConfiguration](API_QueueConfiguration.md) data types
Required: No

 ** TopicConfigurations **   <a name="AmazonS3-Type-NotificationConfiguration-TopicConfigurations"></a>
The topic to which notifications are sent and the events for which notifications are generated.
Type: Array of [TopicConfiguration](API_TopicConfiguration.md) data types
Required: No

## See Also
<a name="API_NotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/NotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/NotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/NotificationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
