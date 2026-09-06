---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdateEventDestination.html
---

# UpdateEventDestination
<a name="API_UpdateEventDestination"></a>

Updates an existing event destination in a configuration set. You can update the IAM role ARN for CloudWatch Logs and Firehose. You can also enable or disable the event destination.

You may want to update an event destination to change its matching event types or updating the destination resource ARN. You can't change an event destination's type between CloudWatch Logs, Firehose, and Amazon SNS.

## Request Syntax
<a name="API_UpdateEventDestination_RequestSyntax"></a>

```
{
   "CloudWatchLogsDestination": {
      "IamRoleArn": "{{string}}",
      "LogGroupArn": "{{string}}"
   },
   "ConfigurationSetName": "{{string}}",
   "Enabled": {{boolean}},
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
<a name="API_UpdateEventDestination_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CloudWatchLogsDestination](#API_UpdateEventDestination_RequestSyntax) **   <a name="pinpoint-UpdateEventDestination-request-CloudWatchLogsDestination"></a>
An object that contains information about an event destination that sends data to CloudWatch Logs.
Type: [CloudWatchLogsDestination](API_CloudWatchLogsDestination.md) object
Required: No

 ** [ConfigurationSetName](#API_UpdateEventDestination_RequestSyntax) **   <a name="pinpoint-UpdateEventDestination-request-ConfigurationSetName"></a>
The configuration set to update with the new event destination. Valid values for this can be the ConfigurationSetName or ConfigurationSetArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [Enabled](#API_UpdateEventDestination_RequestSyntax) **   <a name="pinpoint-UpdateEventDestination-request-Enabled"></a>
When set to true logging is enabled.
Type: Boolean
Required: No

 ** [EventDestinationName](#API_UpdateEventDestination_RequestSyntax) **   <a name="pinpoint-UpdateEventDestination-request-EventDestinationName"></a>
The name to use for the event destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [KinesisFirehoseDestination](#API_UpdateEventDestination_RequestSyntax) **   <a name="pinpoint-UpdateEventDestination-request-KinesisFirehoseDestination"></a>
An object that contains information about an event destination for logging to Firehose.
Type: [KinesisFirehoseDestination](API_KinesisFirehoseDestination.md) object
Required: No

 ** [MatchingEventTypes](#API_UpdateEventDestination_RequestSyntax) **   <a name="pinpoint-UpdateEventDestination-request-MatchingEventTypes"></a>
An array of event types that determine which events to log.
The `TEXT_SENT` event type is not supported.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 52 items.
Valid Values: `ALL | TEXT_ALL | TEXT_SENT | TEXT_PENDING | TEXT_QUEUED | TEXT_SUCCESSFUL | TEXT_DELIVERED | TEXT_INVALID | TEXT_INVALID_MESSAGE | TEXT_UNREACHABLE | TEXT_CARRIER_UNREACHABLE | TEXT_BLOCKED | TEXT_CARRIER_BLOCKED | TEXT_SPAM | TEXT_UNKNOWN | TEXT_TTL_EXPIRED | TEXT_PROTECT_BLOCKED | VOICE_ALL | VOICE_INITIATED | VOICE_RINGING | VOICE_ANSWERED | VOICE_COMPLETED | VOICE_BUSY | VOICE_NO_ANSWER | VOICE_FAILED | VOICE_TTL_EXPIRED | MEDIA_ALL | MEDIA_PENDING | MEDIA_QUEUED | MEDIA_SUCCESSFUL | MEDIA_DELIVERED | MEDIA_INVALID | MEDIA_INVALID_MESSAGE | MEDIA_UNREACHABLE | MEDIA_CARRIER_UNREACHABLE | MEDIA_BLOCKED | MEDIA_CARRIER_BLOCKED | MEDIA_SPAM | MEDIA_UNKNOWN | MEDIA_TTL_EXPIRED | MEDIA_FILE_INACCESSIBLE | MEDIA_FILE_TYPE_UNSUPPORTED | MEDIA_FILE_SIZE_EXCEEDED | RCS_ALL | RCS_QUEUED | RCS_SENT | RCS_DELIVERED | RCS_READ | RCS_FAILED | RCS_TTL_EXPIRED | RCS_PROTECT_BLOCKED | RCS_FALLEN_BACK_TO_SMS`
Required: No

 ** [SnsDestination](#API_UpdateEventDestination_RequestSyntax) **   <a name="pinpoint-UpdateEventDestination-request-SnsDestination"></a>
An object that contains information about an event destination that sends data to Amazon SNS.
Type: [SnsDestination](API_SnsDestination.md) object
Required: No

## Response Syntax
<a name="API_UpdateEventDestination_ResponseSyntax"></a>

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
<a name="API_UpdateEventDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationSetArn](#API_UpdateEventDestination_ResponseSyntax) **   <a name="pinpoint-UpdateEventDestination-response-ConfigurationSetArn"></a>
The Amazon Resource Name (ARN) for the ConfigurationSet that was updated.
Type: String

 ** [ConfigurationSetName](#API_UpdateEventDestination_ResponseSyntax) **   <a name="pinpoint-UpdateEventDestination-response-ConfigurationSetName"></a>
The name of the configuration set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [EventDestination](#API_UpdateEventDestination_ResponseSyntax) **   <a name="pinpoint-UpdateEventDestination-response-EventDestination"></a>
An EventDestination object containing the details of where events will be logged.
Type: [EventDestination](API_EventDestination.md) object

## Errors
<a name="API_UpdateEventDestination_Errors"></a>

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
<a name="API_UpdateEventDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/UpdateEventDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/UpdateEventDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/UpdateEventDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/UpdateEventDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/UpdateEventDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/UpdateEventDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/UpdateEventDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/UpdateEventDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/UpdateEventDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/UpdateEventDestination)
