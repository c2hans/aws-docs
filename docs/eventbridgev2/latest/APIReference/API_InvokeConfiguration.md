---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_InvokeConfiguration.html
---

# InvokeConfiguration
<a name="API_InvokeConfiguration"></a>

Configuration for how the subscriber invokes its target.

## Contents
<a name="API_InvokeConfiguration_Contents"></a>

 ** RoleArn **   <a name="eventbridgev2-Type-InvokeConfiguration-RoleArn"></a>
IAM role the service assumes to invoke the target. Must belong to the calling account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:aws(-[a-z0-9]+)*:iam::\d{12}:role\/[\w+=,.@/-]+`
Required: Yes

 ** TargetArn **   <a name="eventbridgev2-Type-InvokeConfiguration-TargetArn"></a>
ARN of the target a subscriber invokes. The resource grammar is service-neutral because target services use different separators and the USI form omits region and account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:aws(-[a-z0-9]+)*:[^\s]+(?![\s\S]).*`
Required: Yes

 ** EventBusV2Parameters **   <a name="eventbridgev2-Type-InvokeConfiguration-EventBusV2Parameters"></a>
Parameters for forwarding events to another EventBridge event bus.
Type: [EventBusV2Parameters](API_EventBusV2Parameters.md) object
Required: No

 ** HttpParameters **   <a name="eventbridgev2-Type-InvokeConfiguration-HttpParameters"></a>
HTTP invocation parameters for subscribers (API Gateway / API Destination). Values are forwarded to the HTTP endpoint.
Type: [HttpParameters](API_HttpParameters.md) object
Required: No

 ** KinesisParameters **   <a name="eventbridgev2-Type-InvokeConfiguration-KinesisParameters"></a>
Kinesis Data Streams invocation parameters for subscribers. Values are forwarded to the Kinesis PutRecords API. All scalar values accept a literal or a JSONata expression (e.g. "{% $events.Data.partitionKey %}").
Type: [KinesisParameters](API_KinesisParameters.md) object
Required: No

 ** LambdaParameters **   <a name="eventbridgev2-Type-InvokeConfiguration-LambdaParameters"></a>
Lambda invocation parameters for subscribers. Values are forwarded to the Lambda Invoke API. Every string member accepts a literal or a JSONata expression (e.g. "{% $events.Data.qualifier %}").
Type: [LambdaParameters](API_LambdaParameters.md) object
Required: No

 ** SnsParameters **   <a name="eventbridgev2-Type-InvokeConfiguration-SnsParameters"></a>
SNS invocation parameters for subscribers. Values are forwarded to the SNS PublishBatch API. All scalar values accept a literal or a JSONata expression (e.g. "{% $events.Data.groupId %}").
Type: [SnsParameters](API_SnsParameters.md) object
Required: No

 ** SqsParameters **   <a name="eventbridgev2-Type-InvokeConfiguration-SqsParameters"></a>
SQS invocation parameters for subscribers. Values are forwarded to the SQS SendMessageBatch API. All scalar values accept a literal or a JSONata expression (e.g. "{% $events.Data.groupId %}").
Type: [SqsParameters](API_SqsParameters.md) object
Required: No

 ** StepFunctionsParameters **   <a name="eventbridgev2-Type-InvokeConfiguration-StepFunctionsParameters"></a>
Step Functions invocation parameters for subscribers. Values are forwarded to the Step Functions StartExecution or StartSyncExecution API. Every string member accepts a literal or a JSONata expression (e.g. "{% $events.Data.executionName %}").
Type: [StepFunctionsParameters](API_StepFunctionsParameters.md) object
Required: No

 ** UniversalTargetParameters **   <a name="eventbridgev2-Type-InvokeConfiguration-UniversalTargetParameters"></a>
Parameters for USI (Universal Service Integration) targets. Used when TargetArn is in the format arn:aws:events:::aws-sdk:{service}:{apiAction}
Type: [UniversalTargetParameters](API_UniversalTargetParameters.md) object
Required: No

## See Also
<a name="API_InvokeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/InvokeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/InvokeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/InvokeConfiguration)
