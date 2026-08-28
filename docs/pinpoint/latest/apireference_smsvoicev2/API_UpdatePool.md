---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdatePool.html
---

# UpdatePool
<a name="API_UpdatePool"></a>

Updates the configuration of an existing pool. You can update the opt-out list, enable or disable two-way messaging, change the `TwoWayChannelArn`, enable or disable self-managed opt-outs, enable or disable deletion protection, and enable or disable shared routes.

## Request Syntax
<a name="API_UpdatePool_RequestSyntax"></a>

```
{
   "DeletionProtectionEnabled": {{boolean}},
   "OptOutListName": "{{string}}",
   "PoolId": "{{string}}",
   "SelfManagedOptOutsEnabled": {{boolean}},
   "SharedRoutesEnabled": {{boolean}},
   "TwoWayChannelArn": "{{string}}",
   "TwoWayChannelRole": "{{string}}",
   "TwoWayEnabled": {{boolean}}
}
```

## Request Parameters
<a name="API_UpdatePool_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeletionProtectionEnabled](#API_UpdatePool_RequestSyntax) **   <a name="pinpoint-UpdatePool-request-DeletionProtectionEnabled"></a>
When set to true the pool can't be deleted.
Type: Boolean
Required: No

 ** [OptOutListName](#API_UpdatePool_RequestSyntax) **   <a name="pinpoint-UpdatePool-request-OptOutListName"></a>
The OptOutList to associate with the pool. Valid values are either OptOutListName or OptOutListArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [PoolId](#API_UpdatePool_RequestSyntax) **   <a name="pinpoint-UpdatePool-request-PoolId"></a>
The unique identifier of the pool to update. Valid values are either the PoolId or PoolArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]*`
Required: Yes

 ** [SelfManagedOptOutsEnabled](#API_UpdatePool_RequestSyntax) **   <a name="pinpoint-UpdatePool-request-SelfManagedOptOutsEnabled"></a>
By default this is set to false. When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.
Type: Boolean
Required: No

 ** [SharedRoutesEnabled](#API_UpdatePool_RequestSyntax) **   <a name="pinpoint-UpdatePool-request-SharedRoutesEnabled"></a>
Indicates whether shared routes are enabled for the pool.
Type: Boolean
Required: No

 ** [TwoWayChannelArn](#API_UpdatePool_RequestSyntax) **   <a name="pinpoint-UpdatePool-request-TwoWayChannelArn"></a>
The Amazon Resource Name (ARN) of the two way channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`
Required: No

 ** [TwoWayChannelRole](#API_UpdatePool_RequestSyntax) **   <a name="pinpoint-UpdatePool-request-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`
Required: No

 ** [TwoWayEnabled](#API_UpdatePool_RequestSyntax) **   <a name="pinpoint-UpdatePool-request-TwoWayEnabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdatePool_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "DeletionProtectionEnabled": boolean,
   "MessageType": "string",
   "OptOutListName": "string",
   "PoolArn": "string",
   "PoolId": "string",
   "SelfManagedOptOutsEnabled": boolean,
   "SharedRoutesEnabled": boolean,
   "Status": "string",
   "TwoWayChannelArn": "string",
   "TwoWayChannelRole": "string",
   "TwoWayEnabled": boolean
}
```

## Response Elements
<a name="API_UpdatePool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_UpdatePool_ResponseSyntax) **   <a name="pinpoint-UpdatePool-response-CreatedTimestamp"></a>
The time when the pool was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DeletionProtectionEnabled](#API_UpdatePool_ResponseSyntax) **   <a name="pinpoint-UpdatePool-response-DeletionProtectionEnabled"></a>
When set to true the pool can't be deleted.
Type: Boolean

 ** [MessageType](#API_UpdatePool_ResponseSyntax) **   <a name="pinpoint-UpdatePool-response-MessageType"></a>
The type of message for the pool to use.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`

 ** [OptOutListName](#API_UpdatePool_ResponseSyntax) **   <a name="pinpoint-UpdatePool-response-OptOutListName"></a>
The name of the OptOutList associated with the pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [PoolArn](#API_UpdatePool_ResponseSyntax) **   <a name="pinpoint-UpdatePool-response-PoolArn"></a>
The ARN of the pool.
Type: String

 ** [PoolId](#API_UpdatePool_ResponseSyntax) **   <a name="pinpoint-UpdatePool-response-PoolId"></a>
The unique identifier of the pool.
Type: String

 ** [SelfManagedOptOutsEnabled](#API_UpdatePool_ResponseSyntax) **   <a name="pinpoint-UpdatePool-response-SelfManagedOptOutsEnabled"></a>
When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.
Type: Boolean

 ** [SharedRoutesEnabled](#API_UpdatePool_ResponseSyntax) **   <a name="pinpoint-UpdatePool-response-SharedRoutesEnabled"></a>
Indicates whether shared routes are enabled for the pool.
Type: Boolean

 ** [Status](#API_UpdatePool_ResponseSyntax) **   <a name="pinpoint-UpdatePool-response-Status"></a>
The current status of the pool update request.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING`

 ** [TwoWayChannelArn](#API_UpdatePool_ResponseSyntax) **   <a name="pinpoint-UpdatePool-response-TwoWayChannelArn"></a>
The Amazon Resource Name (ARN) of the two way channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`

 ** [TwoWayChannelRole](#API_UpdatePool_ResponseSyntax) **   <a name="pinpoint-UpdatePool-response-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`

 ** [TwoWayEnabled](#API_UpdatePool_ResponseSyntax) **   <a name="pinpoint-UpdatePool-response-TwoWayEnabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients.
Type: Boolean

## Errors
<a name="API_UpdatePool_Errors"></a>

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
<a name="API_UpdatePool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/UpdatePool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/UpdatePool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/UpdatePool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/UpdatePool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/UpdatePool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/UpdatePool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/UpdatePool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/UpdatePool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/UpdatePool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/UpdatePool)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
