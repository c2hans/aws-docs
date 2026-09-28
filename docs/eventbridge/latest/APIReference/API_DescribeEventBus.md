---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEventBus.html
---

# DescribeEventBus
<a name="API_DescribeEventBus"></a>

Displays details about an event bus in your account. This can include the external AWS accounts that are permitted to write events to your default event bus, and the associated policy. For custom event buses and partner event buses, it displays the name, ARN, policy, state, and creation time.

 To enable your account to receive events from other accounts on its default event bus, use [PutPermission](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPermission.html).

For more information about partner event buses, see [CreateEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventBus.html).

## Request Syntax
<a name="API_DescribeEventBus_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEventBus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DescribeEventBus_RequestSyntax) **   <a name="eventbridge-DescribeEventBus-request-Name"></a>
The name or ARN of the event bus to show details for. If you omit this, the default event bus is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(arn:aws[\w-]*:events:[a-z]+-[a-z]+-[\w-]+:[0-9]{12}:event-bus\/)?[/\.\-_A-Za-z0-9]+`
Required: No

## Response Syntax
<a name="API_DescribeEventBus_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "CreationTime": number,
   "DeadLetterConfig": {
      "Arn": "string"
   },
   "Description": "string",
   "KmsKeyIdentifier": "string",
   "LastModifiedTime": number,
   "LogConfig": {
      "IncludeDetail": "string",
      "Level": "string"
   },
   "ManagedBy": "string",
   "Name": "string",
   "Policy": "string"
}
```

## Response Elements
<a name="API_DescribeEventBus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeEventBus_ResponseSyntax) **   <a name="eventbridge-DescribeEventBus-response-Arn"></a>
The Amazon Resource Name (ARN) of the account permitted to write events to the current account.
Type: String

 ** [CreationTime](#API_DescribeEventBus_ResponseSyntax) **   <a name="eventbridge-DescribeEventBus-response-CreationTime"></a>
The time the event bus was created.
Type: Timestamp

 ** [DeadLetterConfig](#API_DescribeEventBus_ResponseSyntax) **   <a name="eventbridge-DescribeEventBus-response-DeadLetterConfig"></a>
Configuration details of the Amazon SQS queue for EventBridge to use as a dead-letter queue (DLQ).
For more information, see [Using dead-letter queues to process undelivered events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-event-delivery.html#eb-rule-dlq) in the *EventBridge User Guide*.
Type: [DeadLetterConfig](API_DeadLetterConfig.md) object

 ** [Description](#API_DescribeEventBus_ResponseSyntax) **   <a name="eventbridge-DescribeEventBus-response-Description"></a>
The event bus description.
Type: String
Length Constraints: Maximum length of 512.

 ** [KmsKeyIdentifier](#API_DescribeEventBus_ResponseSyntax) **   <a name="eventbridge-DescribeEventBus-response-KmsKeyIdentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use to encrypt events on this event bus, if one has been specified.
For more information, see [Data encryption in EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption.html) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[a-zA-Z0-9_\-/:]*$`

 ** [LastModifiedTime](#API_DescribeEventBus_ResponseSyntax) **   <a name="eventbridge-DescribeEventBus-response-LastModifiedTime"></a>
The time the event bus was last modified.
Type: Timestamp

 ** [LogConfig](#API_DescribeEventBus_ResponseSyntax) **   <a name="eventbridge-DescribeEventBus-response-LogConfig"></a>
The logging configuration settings for the event bus.
For more information, see [Configuring logs for event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html) in the *EventBridge User Guide*.
Type: [LogConfig](API_LogConfig.md) object

 ** [ManagedBy](#API_DescribeEventBus_ResponseSyntax) **   <a name="eventbridge-DescribeEventBus-response-ManagedBy"></a>
If the event bus was created on behalf of your account by an AWS service, this field displays the principal name of the service that created the event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [Name](#API_DescribeEventBus_ResponseSyntax) **   <a name="eventbridge-DescribeEventBus-response-Name"></a>
The name of the event bus. Currently, this is always `default`.
Type: String

 ** [Policy](#API_DescribeEventBus_ResponseSyntax) **   <a name="eventbridge-DescribeEventBus-response-Policy"></a>
The policy that enables the external account to send events to your account.
Type: String

## Errors
<a name="API_DescribeEventBus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEventBus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DescribeEventBus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DescribeEventBus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DescribeEventBus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DescribeEventBus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DescribeEventBus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DescribeEventBus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DescribeEventBus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DescribeEventBus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DescribeEventBus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DescribeEventBus)
