---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventBus.html
---

# CreateEventBus
<a name="API_CreateEventBus"></a>

Creates a new event bus within your account. This can be a custom event bus which you can use to receive events from your custom applications and services, or it can be a partner event bus which can be matched to a partner event source.

## Request Syntax
<a name="API_CreateEventBus_RequestSyntax"></a>

```
{
   "DeadLetterConfig": {
      "Arn": "{{string}}"
   },
   "Description": "{{string}}",
   "EventSourceName": "{{string}}",
   "KmsKeyIdentifier": "{{string}}",
   "LogConfig": {
      "IncludeDetail": "{{string}}",
      "Level": "{{string}}"
   },
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateEventBus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeadLetterConfig](#API_CreateEventBus_RequestSyntax) **   <a name="eventbridge-CreateEventBus-request-DeadLetterConfig"></a>
Configuration details of the Amazon SQS queue for EventBridge to use as a dead-letter queue (DLQ).
For more information, see [Using dead-letter queues to process undelivered events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-event-delivery.html#eb-rule-dlq) in the *EventBridge User Guide*.
Type: [DeadLetterConfig](API_DeadLetterConfig.md) object
Required: No

 ** [Description](#API_CreateEventBus_RequestSyntax) **   <a name="eventbridge-CreateEventBus-request-Description"></a>
The event bus description.
Type: String
Length Constraints: Maximum length of 512.
Required: No

 ** [EventSourceName](#API_CreateEventBus_RequestSyntax) **   <a name="eventbridge-CreateEventBus-request-EventSourceName"></a>
If you are creating a partner event bus, this specifies the partner event source that the new event bus will be matched with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `aws\.partner(/[\.\-_A-Za-z0-9]+){2,}`
Required: No

 ** [KmsKeyIdentifier](#API_CreateEventBus_RequestSyntax) **   <a name="eventbridge-CreateEventBus-request-KmsKeyIdentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt events on this event bus. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.
If you do not specify a customer managed key identifier, EventBridge uses an AWS owned key to encrypt events on the event bus.
For more information, see [Identify and view keys](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html) in the * AWS Key Management Service Developer Guide*.
Schema discovery is not supported for event buses encrypted using a customer managed key. EventBridge returns an error if:
+ You call ` [CreateDiscoverer](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers.html#CreateDiscoverer) ` on an event bus set to use a customer managed key for encryption.
+ You call ` [UpdatedEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdatedEventBus.html) ` to set a customer managed key on an event bus with schema discovery enabled.
To enable schema discovery on an event bus, choose to use an AWS owned key. For more information, see [Encrypting events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-event-bus-cmkey.html) in the *Amazon EventBridge User Guide*.
If you have specified that EventBridge use a customer managed key for encrypting the source event bus, we strongly recommend you also specify a customer managed key for any archives for the event bus as well.
For more information, see [Encrypting archives](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[a-zA-Z0-9_\-/:]*$`
Required: No

 ** [LogConfig](#API_CreateEventBus_RequestSyntax) **   <a name="eventbridge-CreateEventBus-request-LogConfig"></a>
The logging configuration settings for the event bus.
For more information, see [Configuring logs for event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html) in the *EventBridge User Guide*.
Type: [LogConfig](API_LogConfig.md) object
Required: No

 ** [Name](#API_CreateEventBus_RequestSyntax) **   <a name="eventbridge-CreateEventBus-request-Name"></a>
The name of the new event bus.
Custom event bus names can't contain the `/` character, but you can use the `/` character in partner event bus names. In addition, for partner event buses, the name must exactly match the name of the partner event source that this event bus is matched to.
You can't use the name `default` for a custom event bus, as this name is already used for your account's default event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[/\.\-_A-Za-z0-9]+`
Required: Yes

 ** [Tags](#API_CreateEventBus_RequestSyntax) **   <a name="eventbridge-CreateEventBus-request-Tags"></a>
Tags to associate with the event bus.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateEventBus_ResponseSyntax"></a>

```
{
   "DeadLetterConfig": {
      "Arn": "string"
   },
   "Description": "string",
   "EventBusArn": "string",
   "KmsKeyIdentifier": "string",
   "LogConfig": {
      "IncludeDetail": "string",
      "Level": "string"
   }
}
```

## Response Elements
<a name="API_CreateEventBus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeadLetterConfig](#API_CreateEventBus_ResponseSyntax) **   <a name="eventbridge-CreateEventBus-response-DeadLetterConfig"></a>
Configuration details of the Amazon SQS queue for EventBridge to use as a dead-letter queue (DLQ).
For more information, see [Using dead-letter queues to process undelivered events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-event-delivery.html#eb-rule-dlq) in the *EventBridge User Guide*.
Type: [DeadLetterConfig](API_DeadLetterConfig.md) object

 ** [Description](#API_CreateEventBus_ResponseSyntax) **   <a name="eventbridge-CreateEventBus-response-Description"></a>
The event bus description.
Type: String
Length Constraints: Maximum length of 512.

 ** [EventBusArn](#API_CreateEventBus_ResponseSyntax) **   <a name="eventbridge-CreateEventBus-response-EventBusArn"></a>
The ARN of the new event bus.
Type: String

 ** [KmsKeyIdentifier](#API_CreateEventBus_ResponseSyntax) **   <a name="eventbridge-CreateEventBus-response-KmsKeyIdentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use to encrypt events on this event bus, if one has been specified.
For more information, see [Data encryption in EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption.html) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[a-zA-Z0-9_\-/:]*$`

 ** [LogConfig](#API_CreateEventBus_ResponseSyntax) **   <a name="eventbridge-CreateEventBus-response-LogConfig"></a>
The logging configuration settings for the event bus.
For more information, see [Configuring logs for event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html) in the *EventBridge User Guide*.
Type: [LogConfig](API_LogConfig.md) object

## Errors
<a name="API_CreateEventBus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** InvalidStateException **
The specified state is not a valid state for an event source.
HTTP Status Code: 400

 ** LimitExceededException **
The request failed because it attempted to create resource beyond the allowed service quota.
HTTP Status Code: 400

 ** OperationDisabledException **
The operation you are attempting is not available in this region.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The resource you are trying to create already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_CreateEventBus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/CreateEventBus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/CreateEventBus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/CreateEventBus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/CreateEventBus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/CreateEventBus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/CreateEventBus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/CreateEventBus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/CreateEventBus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/CreateEventBus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/CreateEventBus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
