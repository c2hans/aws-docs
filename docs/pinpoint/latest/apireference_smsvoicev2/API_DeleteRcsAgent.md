---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteRcsAgent.html
---

# DeleteRcsAgent
<a name="API_DeleteRcsAgent"></a>

Deletes an existing RCS agent. If deletion protection is enabled, an error is returned.

## Request Syntax
<a name="API_DeleteRcsAgent_RequestSyntax"></a>

```
{
   "RcsAgentId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteRcsAgent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RcsAgentId](#API_DeleteRcsAgent_RequestSyntax) **   <a name="pinpoint-DeleteRcsAgent-request-RcsAgentId"></a>
The unique identifier of the RCS agent to delete. You can use either the RcsAgentId or RcsAgentArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteRcsAgent_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "DeletionProtectionEnabled": boolean,
   "OptOutListName": "string",
   "RcsAgentArn": "string",
   "RcsAgentId": "string",
   "SelfManagedOptOutsEnabled": boolean,
   "Status": "string",
   "TwoWayChannelArn": "string",
   "TwoWayChannelRole": "string",
   "TwoWayEnabled": boolean,
   "TwoWayRcsEventsEnabled": [ "string" ]
}
```

## Response Elements
<a name="API_DeleteRcsAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_DeleteRcsAgent_ResponseSyntax) **   <a name="pinpoint-DeleteRcsAgent-response-CreatedTimestamp"></a>
The time when the RCS agent was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DeletionProtectionEnabled](#API_DeleteRcsAgent_ResponseSyntax) **   <a name="pinpoint-DeleteRcsAgent-response-DeletionProtectionEnabled"></a>
When set to true deletion protection is enabled. By default this is set to false.
Type: Boolean

 ** [OptOutListName](#API_DeleteRcsAgent_ResponseSyntax) **   <a name="pinpoint-DeleteRcsAgent-response-OptOutListName"></a>
The name of the OptOutList that was associated with the deleted RCS agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [RcsAgentArn](#API_DeleteRcsAgent_ResponseSyntax) **   <a name="pinpoint-DeleteRcsAgent-response-RcsAgentArn"></a>
The Amazon Resource Name (ARN) of the deleted RCS agent.
Type: String

 ** [RcsAgentId](#API_DeleteRcsAgent_ResponseSyntax) **   <a name="pinpoint-DeleteRcsAgent-response-RcsAgentId"></a>
The unique identifier for the deleted RCS agent.
Type: String

 ** [SelfManagedOptOutsEnabled](#API_DeleteRcsAgent_ResponseSyntax) **   <a name="pinpoint-DeleteRcsAgent-response-SelfManagedOptOutsEnabled"></a>
By default this is set to false. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.
Type: Boolean

 ** [Status](#API_DeleteRcsAgent_ResponseSyntax) **   <a name="pinpoint-DeleteRcsAgent-response-Status"></a>
The current status of the RCS agent.
Type: String
Valid Values: `CREATED | PENDING | TESTING | PARTIAL | ACTIVE | DELETED`

 ** [TwoWayChannelArn](#API_DeleteRcsAgent_ResponseSyntax) **   <a name="pinpoint-DeleteRcsAgent-response-TwoWayChannelArn"></a>
The Amazon Resource Name (ARN) of the two way channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`

 ** [TwoWayChannelRole](#API_DeleteRcsAgent_ResponseSyntax) **   <a name="pinpoint-DeleteRcsAgent-response-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`

 ** [TwoWayEnabled](#API_DeleteRcsAgent_ResponseSyntax) **   <a name="pinpoint-DeleteRcsAgent-response-TwoWayEnabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients.
Type: Boolean

 ** [TwoWayRcsEventsEnabled](#API_DeleteRcsAgent_ResponseSyntax) **   <a name="pinpoint-DeleteRcsAgent-response-TwoWayRcsEventsEnabled"></a>
The list of RCS event types that were enabled for two-way messaging on the deleted agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 50.

## Errors
<a name="API_DeleteRcsAgent_Errors"></a>

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
<a name="API_DeleteRcsAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteRcsAgent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteRcsAgent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteRcsAgent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteRcsAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteRcsAgent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteRcsAgent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteRcsAgent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteRcsAgent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteRcsAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteRcsAgent)
