---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateEventDestination.html
---

# CreateEventDestination
<a name="API_CreateEventDestination"></a>

Creates a new event destination in a configuration set.

An event destination is a location where you send message events. The event options are Amazon CloudWatch, Amazon Data Firehose, or Amazon SNS. For example, when a message is delivered successfully, you can send information about that event to an event destination, or send notifications to endpoints that are subscribed to an Amazon SNS topic.

You can only create one event destination at a time. You must provide a value for a single event destination using either `CloudWatchLogsDestination`, `KinesisFirehoseDestination` or `SnsDestination`. If an event destination isn't provided then an exception is returned.

Each configuration set can contain between 0 and 5 event destinations. Each event destination can contain a reference to a single destination, such as a CloudWatch or Firehose destination.

## Request Syntax
<a name="API_CreateEventDestination_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "CloudWatchLogsDestination": {
      "IamRoleArn": "{{string}}",
      "LogGroupArn": "{{string}}"
   },
   "ConfigurationSetName": "{{string}}",
   "EventDestinationName": "{{string}}",
   "KinesisFirehoseDestination": {
      "DeliveryStreamArn": "{{string}}",
      "IamRoleArn": "{{string}}"
   },
   "MatchingEventTypes": [ "{{string}}" ],
   "SnsDestination": {
      "TopicArn": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateEventDestination_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateEventDestination_RequestSyntax) **   <a name="pinpoint-CreateEventDestination-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [CloudWatchLogsDestination](#API_CreateEventDestination_RequestSyntax) **   <a name="pinpoint-CreateEventDestination-request-CloudWatchLogsDestination"></a>
An object that contains information about an event destination for logging to Amazon CloudWatch Logs.
Type: [CloudWatchLogsDestination](API_CloudWatchLogsDestination.md) object
Required: No

 ** [ConfigurationSetName](#API_CreateEventDestination_RequestSyntax) **   <a name="pinpoint-CreateEventDestination-request-ConfigurationSetName"></a>
Either the name of the configuration set or the configuration set ARN to apply event logging to. The ConfigurateSetName and ConfigurationSetArn can be found using the [DescribeConfigurationSets](API_DescribeConfigurationSets.md) action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [EventDestinationName](#API_CreateEventDestination_RequestSyntax) **   <a name="pinpoint-CreateEventDestination-request-EventDestinationName"></a>
The name that identifies the event destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [KinesisFirehoseDestination](#API_CreateEventDestination_RequestSyntax) **   <a name="pinpoint-CreateEventDestination-request-KinesisFirehoseDestination"></a>
An object that contains information about an event destination for logging to Amazon Data Firehose.
Type: [KinesisFirehoseDestination](API_KinesisFirehoseDestination.md) object
Required: No

 ** [MatchingEventTypes](#API_CreateEventDestination_RequestSyntax) **   <a name="pinpoint-CreateEventDestination-request-MatchingEventTypes"></a>
An array of event types that determine which events to log. If "ALL" is used, then AWS End User Messaging SMS logs every event type.
The `TEXT_SENT` event type is not supported.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 52 items.
Valid Values: `ALL | TEXT_ALL | TEXT_SENT | TEXT_PENDING | TEXT_QUEUED | TEXT_SUCCESSFUL | TEXT_DELIVERED | TEXT_INVALID | TEXT_INVALID_MESSAGE | TEXT_UNREACHABLE | TEXT_CARRIER_UNREACHABLE | TEXT_BLOCKED | TEXT_CARRIER_BLOCKED | TEXT_SPAM | TEXT_UNKNOWN | TEXT_TTL_EXPIRED | TEXT_PROTECT_BLOCKED | VOICE_ALL | VOICE_INITIATED | VOICE_RINGING | VOICE_ANSWERED | VOICE_COMPLETED | VOICE_BUSY | VOICE_NO_ANSWER | VOICE_FAILED | VOICE_TTL_EXPIRED | MEDIA_ALL | MEDIA_PENDING | MEDIA_QUEUED | MEDIA_SUCCESSFUL | MEDIA_DELIVERED | MEDIA_INVALID | MEDIA_INVALID_MESSAGE | MEDIA_UNREACHABLE | MEDIA_CARRIER_UNREACHABLE | MEDIA_BLOCKED | MEDIA_CARRIER_BLOCKED | MEDIA_SPAM | MEDIA_UNKNOWN | MEDIA_TTL_EXPIRED | MEDIA_FILE_INACCESSIBLE | MEDIA_FILE_TYPE_UNSUPPORTED | MEDIA_FILE_SIZE_EXCEEDED | RCS_ALL | RCS_QUEUED | RCS_SENT | RCS_DELIVERED | RCS_READ | RCS_FAILED | RCS_TTL_EXPIRED | RCS_PROTECT_BLOCKED | RCS_FALLEN_BACK_TO_SMS`
Required: Yes

 ** [SnsDestination](#API_CreateEventDestination_RequestSyntax) **   <a name="pinpoint-CreateEventDestination-request-SnsDestination"></a>
An object that contains information about an event destination for logging to Amazon SNS.
Type: [SnsDestination](API_SnsDestination.md) object
Required: No

## Response Syntax
<a name="API_CreateEventDestination_ResponseSyntax"></a>

```
{
   "ConfigurationSetArn": "string",
   "ConfigurationSetName": "string",
   "EventDestination": {
      "CloudWatchLogsDestination": {
         "IamRoleArn": "string",
         "LogGroupArn": "string"
      },
      "Enabled": boolean,
      "EventDestinationName": "string",
      "KinesisFirehoseDestination": {
         "DeliveryStreamArn": "string",
         "IamRoleArn": "string"
      },
      "MatchingEventTypes": [ "string" ],
      "SnsDestination": {
         "TopicArn": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateEventDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationSetArn](#API_CreateEventDestination_ResponseSyntax) **   <a name="pinpoint-CreateEventDestination-response-ConfigurationSetArn"></a>
The ARN of the configuration set.
Type: String

 ** [ConfigurationSetName](#API_CreateEventDestination_ResponseSyntax) **   <a name="pinpoint-CreateEventDestination-response-ConfigurationSetName"></a>
The name of the configuration set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [EventDestination](#API_CreateEventDestination_ResponseSyntax) **   <a name="pinpoint-CreateEventDestination-response-EventDestination"></a>
The details of the destination where events are logged.
Type: [EventDestination](API_EventDestination.md) object

## Errors
<a name="API_CreateEventDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** ConflictException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.
 ** Reason **
The reason for the exception.
 ** ResourceId **
The unique identifier of the request.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateEventDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/CreateEventDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/CreateEventDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CreateEventDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/CreateEventDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CreateEventDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/CreateEventDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/CreateEventDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/CreateEventDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/CreateEventDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CreateEventDestination)
