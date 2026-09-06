---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateRcsAgent.html
---

# CreateRcsAgent
<a name="API_CreateRcsAgent"></a>

Creates a new RCS agent for sending rich messages through the RCS channel. The RCS agent serves as an origination identity for sending RCS messages to your recipients.

## Request Syntax
<a name="API_CreateRcsAgent_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DeletionProtectionEnabled": {{boolean}},
   "OptOutListName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateRcsAgent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateRcsAgent_RequestSyntax) **   <a name="pinpoint-CreateRcsAgent-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [DeletionProtectionEnabled](#API_CreateRcsAgent_RequestSyntax) **   <a name="pinpoint-CreateRcsAgent-request-DeletionProtectionEnabled"></a>
By default this is set to false. When set to true the RCS agent can't be deleted. You can change this value using the [UpdateRcsAgent](API_UpdateRcsAgent.md) action.
Type: Boolean
Required: No

 ** [OptOutListName](#API_CreateRcsAgent_RequestSyntax) **   <a name="pinpoint-CreateRcsAgent-request-OptOutListName"></a>
The OptOutList to associate with the RCS agent. Valid values are either OptOutListName or OptOutListArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [Tags](#API_CreateRcsAgent_RequestSyntax) **   <a name="pinpoint-CreateRcsAgent-request-Tags"></a>
An array of tags (key and value pairs) associated with the RCS agent.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateRcsAgent_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "DeletionProtectionEnabled": boolean,
   "OptOutListName": "string",
   "RcsAgentArn": "string",
   "RcsAgentId": "string",
   "SelfManagedOptOutsEnabled": boolean,
   "Status": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ],
   "TwoWayChannelArn": "string",
   "TwoWayChannelRole": "string",
   "TwoWayEnabled": boolean,
   "TwoWayMediaS3BucketName": "string",
   "TwoWayMediaS3KeyPrefix": "string",
   "TwoWayMediaS3Role": "string",
   "TwoWayRcsEventsEnabled": [ "string" ]
}
```

## Response Elements
<a name="API_CreateRcsAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-CreatedTimestamp"></a>
The time when the RCS agent was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DeletionProtectionEnabled](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-DeletionProtectionEnabled"></a>
When set to true deletion protection is enabled. By default this is set to false.
Type: Boolean

 ** [OptOutListName](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-OptOutListName"></a>
The name of the OptOutList associated with the RCS agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [RcsAgentArn](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-RcsAgentArn"></a>
The Amazon Resource Name (ARN) of the newly created RCS agent.
Type: String

 ** [RcsAgentId](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-RcsAgentId"></a>
The unique identifier for the RCS agent.
Type: String

 ** [SelfManagedOptOutsEnabled](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-SelfManagedOptOutsEnabled"></a>
By default this is set to false. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.
Type: Boolean

 ** [Status](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-Status"></a>
The current status of the RCS agent.
Type: String
Valid Values: `CREATED | PENDING | TESTING | PARTIAL | ACTIVE | DELETED`

 ** [Tags](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-Tags"></a>
An array of tags (key and value pairs) associated with the RCS agent.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

 ** [TwoWayChannelArn](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-TwoWayChannelArn"></a>
The Amazon Resource Name (ARN) of the two way channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`

 ** [TwoWayChannelRole](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`

 ** [TwoWayEnabled](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-TwoWayEnabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients.
Type: Boolean

 ** [TwoWayMediaS3BucketName](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-TwoWayMediaS3BucketName"></a>
The name of the S3 bucket where inbound RCS media files are stored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][a-z0-9.-]*[a-z0-9]`

 ** [TwoWayMediaS3KeyPrefix](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-TwoWayMediaS3KeyPrefix"></a>
The key prefix used for inbound RCS media objects in the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S]+`

 ** [TwoWayMediaS3Role](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-TwoWayMediaS3Role"></a>
The ARN of the IAM role used to write inbound RCS media files to the S3 bucket. The role must have `s3:PutObject` permission on the bucket and a trust policy allowing `sms-voice.amazonaws.com` to assume it.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`

 ** [TwoWayRcsEventsEnabled](#API_CreateRcsAgent_ResponseSyntax) **   <a name="pinpoint-CreateRcsAgent-response-TwoWayRcsEventsEnabled"></a>
The list of RCS event types enabled for two-way messaging on the agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 50.

## Errors
<a name="API_CreateRcsAgent_Errors"></a>

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
<a name="API_CreateRcsAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/CreateRcsAgent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/CreateRcsAgent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CreateRcsAgent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/CreateRcsAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CreateRcsAgent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/CreateRcsAgent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/CreateRcsAgent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/CreateRcsAgent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/CreateRcsAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CreateRcsAgent)
