---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdateRcsAgent.html
---

# UpdateRcsAgent
<a name="API_UpdateRcsAgent"></a>

Updates the configuration of an existing RCS agent. You can update the opt-out list, deletion protection, two-way messaging settings, and self-managed opt-outs configuration.

## Request Syntax
<a name="API_UpdateRcsAgent_RequestSyntax"></a>

```
{
   "DeletionProtectionEnabled": {{boolean}},
   "OptOutListName": "{{string}}",
   "RcsAgentId": "{{string}}",
   "SelfManagedOptOutsEnabled": {{boolean}},
   "TwoWayChannelArn": "{{string}}",
   "TwoWayChannelRole": "{{string}}",
   "TwoWayEnabled": {{boolean}},
   "TwoWayMediaS3BucketName": "{{string}}",
   "TwoWayMediaS3KeyPrefix": "{{string}}",
   "TwoWayMediaS3Role": "{{string}}",
   "TwoWayRcsEventsEnabled": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateRcsAgent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeletionProtectionEnabled](#API_UpdateRcsAgent_RequestSyntax) **   <a name="pinpoint-UpdateRcsAgent-request-DeletionProtectionEnabled"></a>
By default this is set to false. When set to true the RCS agent can't be deleted.
Type: Boolean
Required: No

 ** [OptOutListName](#API_UpdateRcsAgent_RequestSyntax) **   <a name="pinpoint-UpdateRcsAgent-request-OptOutListName"></a>
The OptOutList to associate with the RCS agent. Valid values are either OptOutListName or OptOutListArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [RcsAgentId](#API_UpdateRcsAgent_RequestSyntax) **   <a name="pinpoint-UpdateRcsAgent-request-RcsAgentId"></a>
The unique identifier of the RCS agent to update. You can use either the RcsAgentId or RcsAgentArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [SelfManagedOptOutsEnabled](#API_UpdateRcsAgent_RequestSyntax) **   <a name="pinpoint-UpdateRcsAgent-request-SelfManagedOptOutsEnabled"></a>
By default this is set to false. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.
Type: Boolean
Required: No

 ** [TwoWayChannelArn](#API_UpdateRcsAgent_RequestSyntax) **   <a name="pinpoint-UpdateRcsAgent-request-TwoWayChannelArn"></a>
The Amazon Resource Name (ARN) of the two way channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`
Required: No

 ** [TwoWayChannelRole](#API_UpdateRcsAgent_RequestSyntax) **   <a name="pinpoint-UpdateRcsAgent-request-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`
Required: No

 ** [TwoWayEnabled](#API_UpdateRcsAgent_RequestSyntax) **   <a name="pinpoint-UpdateRcsAgent-request-TwoWayEnabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients.
Type: Boolean
Required: No

 ** [TwoWayMediaS3BucketName](#API_UpdateRcsAgent_RequestSyntax) **   <a name="pinpoint-UpdateRcsAgent-request-TwoWayMediaS3BucketName"></a>
The name of the S3 bucket where inbound RCS media files are stored. Two-way messaging must be enabled on the agent. To remove the media configuration, pass the sentinel value `UNSET_RCS_MEDIA_CONFIGURATION` for both this field and TwoWayMediaS3Role.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `([a-z0-9][a-z0-9.-]*[a-z0-9]|UNSET_RCS_MEDIA_CONFIGURATION)`
Required: No

 ** [TwoWayMediaS3KeyPrefix](#API_UpdateRcsAgent_RequestSyntax) **   <a name="pinpoint-UpdateRcsAgent-request-TwoWayMediaS3KeyPrefix"></a>
The key prefix used for inbound RCS media objects in the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S]+`
Required: No

 ** [TwoWayMediaS3Role](#API_UpdateRcsAgent_RequestSyntax) **   <a name="pinpoint-UpdateRcsAgent-request-TwoWayMediaS3Role"></a>
The ARN of the IAM role used to write inbound RCS media files to the S3 bucket. The role must have `s3:PutObject` permission on the bucket and a trust policy allowing `sms-voice.amazonaws.com` to assume it. To remove the media configuration, pass the sentinel value `UNSET_RCS_MEDIA_CONFIGURATION` for both this field and TwoWayMediaS3BucketName.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(arn:\S+|UNSET_RCS_MEDIA_CONFIGURATION)`
Required: No

 ** [TwoWayRcsEventsEnabled](#API_UpdateRcsAgent_RequestSyntax) **   <a name="pinpoint-UpdateRcsAgent-request-TwoWayRcsEventsEnabled"></a>
The list of RCS event types to enable for two-way messaging. Pass an empty list to disable all event types. The special value `ALL` enables all current and future event types and must be the sole element if used.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

## Response Syntax
<a name="API_UpdateRcsAgent_ResponseSyntax"></a>

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
   "TwoWayMediaS3BucketName": "string",
   "TwoWayMediaS3KeyPrefix": "string",
   "TwoWayMediaS3Role": "string",
   "TwoWayRcsEventsEnabled": [ "string" ]
}
```

## Response Elements
<a name="API_UpdateRcsAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-CreatedTimestamp"></a>
The time when the RCS agent was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DeletionProtectionEnabled](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-DeletionProtectionEnabled"></a>
When set to true deletion protection is enabled. By default this is set to false.
Type: Boolean

 ** [OptOutListName](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-OptOutListName"></a>
The name of the OptOutList associated with the RCS agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [RcsAgentArn](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-RcsAgentArn"></a>
The Amazon Resource Name (ARN) of the updated RCS agent.
Type: String

 ** [RcsAgentId](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-RcsAgentId"></a>
The unique identifier for the RCS agent.
Type: String

 ** [SelfManagedOptOutsEnabled](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-SelfManagedOptOutsEnabled"></a>
By default this is set to false. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.
Type: Boolean

 ** [Status](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-Status"></a>
The current status of the RCS agent.
Type: String
Valid Values: `CREATED | PENDING | TESTING | PARTIAL | ACTIVE | DELETED`

 ** [TwoWayChannelArn](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-TwoWayChannelArn"></a>
The Amazon Resource Name (ARN) of the two way channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`

 ** [TwoWayChannelRole](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`

 ** [TwoWayEnabled](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-TwoWayEnabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients.
Type: Boolean

 ** [TwoWayMediaS3BucketName](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-TwoWayMediaS3BucketName"></a>
The name of the S3 bucket where inbound RCS media files are stored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][a-z0-9.-]*[a-z0-9]`

 ** [TwoWayMediaS3KeyPrefix](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-TwoWayMediaS3KeyPrefix"></a>
The key prefix used for inbound RCS media objects in the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S]+`

 ** [TwoWayMediaS3Role](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-TwoWayMediaS3Role"></a>
The ARN of the IAM role used to write inbound RCS media files to the S3 bucket.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`

 ** [TwoWayRcsEventsEnabled](#API_UpdateRcsAgent_ResponseSyntax) **   <a name="pinpoint-UpdateRcsAgent-response-TwoWayRcsEventsEnabled"></a>
The list of RCS event types enabled for two-way messaging on the agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 50.

## Errors
<a name="API_UpdateRcsAgent_Errors"></a>

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
<a name="API_UpdateRcsAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/UpdateRcsAgent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/UpdateRcsAgent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/UpdateRcsAgent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/UpdateRcsAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/UpdateRcsAgent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/UpdateRcsAgent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/UpdateRcsAgent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/UpdateRcsAgent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/UpdateRcsAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/UpdateRcsAgent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
