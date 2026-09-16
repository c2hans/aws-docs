---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteConfigurationSet.html
---

# DeleteConfigurationSet
<a name="API_DeleteConfigurationSet"></a>

Deletes an existing configuration set.

A configuration set is a set of rules that you apply to voice and SMS messages that you send. In a configuration set, you can specify a destination for specific types of events related to voice and SMS messages.

## Request Syntax
<a name="API_DeleteConfigurationSet_RequestSyntax"></a>

```
{
   "ConfigurationSetName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteConfigurationSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_DeleteConfigurationSet_RequestSyntax) **   <a name="pinpoint-DeleteConfigurationSet-request-ConfigurationSetName"></a>
The name of the configuration set or the configuration set ARN that you want to delete. The ConfigurationSetName and ConfigurationSetArn can be found using the [DescribeConfigurationSets](API_DescribeConfigurationSets.md) action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteConfigurationSet_ResponseSyntax"></a>

```
{
   "ConfigurationSetArn": "string",
   "ConfigurationSetName": "string",
   "CreatedTimestamp": number,
   "DefaultMessageFeedbackEnabled": boolean,
   "DefaultMessageType": "string",
   "DefaultSenderId": "string",
   "EventDestinations": [
      {
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
   ]
}
```

## Response Elements
<a name="API_DeleteConfigurationSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationSetArn](#API_DeleteConfigurationSet_ResponseSyntax) **   <a name="pinpoint-DeleteConfigurationSet-response-ConfigurationSetArn"></a>
The Amazon Resource Name (ARN) of the deleted configuration set.
Type: String

 ** [ConfigurationSetName](#API_DeleteConfigurationSet_ResponseSyntax) **   <a name="pinpoint-DeleteConfigurationSet-response-ConfigurationSetName"></a>
The name of the deleted configuration set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [CreatedTimestamp](#API_DeleteConfigurationSet_ResponseSyntax) **   <a name="pinpoint-DeleteConfigurationSet-response-CreatedTimestamp"></a>
The time that the deleted configuration set was created in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DefaultMessageFeedbackEnabled](#API_DeleteConfigurationSet_ResponseSyntax) **   <a name="pinpoint-DeleteConfigurationSet-response-DefaultMessageFeedbackEnabled"></a>
True if the configuration set has message feedback enabled. By default this is set to false.
Type: Boolean

 ** [DefaultMessageType](#API_DeleteConfigurationSet_ResponseSyntax) **   <a name="pinpoint-DeleteConfigurationSet-response-DefaultMessageType"></a>
The default message type of the configuration set that was deleted.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`

 ** [DefaultSenderId](#API_DeleteConfigurationSet_ResponseSyntax) **   <a name="pinpoint-DeleteConfigurationSet-response-DefaultSenderId"></a>
The default Sender ID of the configuration set that was deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `[A-Za-z0-9_-]+`

 ** [EventDestinations](#API_DeleteConfigurationSet_ResponseSyntax) **   <a name="pinpoint-DeleteConfigurationSet-response-EventDestinations"></a>
An array of any EventDestination objects that were associated with the deleted configuration set.
Type: Array of [EventDestination](API_EventDestination.md) objects

## Errors
<a name="API_DeleteConfigurationSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
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
<a name="API_DeleteConfigurationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteConfigurationSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteConfigurationSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteConfigurationSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteConfigurationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteConfigurationSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteConfigurationSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteConfigurationSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteConfigurationSet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteConfigurationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteConfigurationSet)
