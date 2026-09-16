---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeletePool.html
---

# DeletePool
<a name="API_DeletePool"></a>

Deletes an existing pool. Deleting a pool disassociates all origination identities from that pool.

If the pool status isn't active or if deletion protection is enabled, an error is returned.

A pool is a collection of phone numbers and SenderIds. A pool can include one or more phone numbers and SenderIds that are associated with your AWS account.

## Request Syntax
<a name="API_DeletePool_RequestSyntax"></a>

```
{
   "PoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeletePool_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PoolId](#API_DeletePool_RequestSyntax) **   <a name="pinpoint-DeletePool-request-PoolId"></a>
The PoolId or PoolArn of the pool to delete. You can use [DescribePools](API_DescribePools.md) to find the values for PoolId and PoolArn .
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]*`
Required: Yes

## Response Syntax
<a name="API_DeletePool_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
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
<a name="API_DeletePool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_DeletePool_ResponseSyntax) **   <a name="pinpoint-DeletePool-response-CreatedTimestamp"></a>
The time when the pool was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [MessageType](#API_DeletePool_ResponseSyntax) **   <a name="pinpoint-DeletePool-response-MessageType"></a>
The message type that was associated with the deleted pool.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`

 ** [OptOutListName](#API_DeletePool_ResponseSyntax) **   <a name="pinpoint-DeletePool-response-OptOutListName"></a>
The name of the OptOutList that was associated with the deleted pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [PoolArn](#API_DeletePool_ResponseSyntax) **   <a name="pinpoint-DeletePool-response-PoolArn"></a>
The Amazon Resource Name (ARN) of the pool that was deleted.
Type: String

 ** [PoolId](#API_DeletePool_ResponseSyntax) **   <a name="pinpoint-DeletePool-response-PoolId"></a>
The PoolId of the pool that was deleted.
Type: String

 ** [SelfManagedOptOutsEnabled](#API_DeletePool_ResponseSyntax) **   <a name="pinpoint-DeletePool-response-SelfManagedOptOutsEnabled"></a>
By default this is set to false. When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.
Type: Boolean

 ** [SharedRoutesEnabled](#API_DeletePool_ResponseSyntax) **   <a name="pinpoint-DeletePool-response-SharedRoutesEnabled"></a>
Indicates whether shared routes are enabled for the pool.
Type: Boolean

 ** [Status](#API_DeletePool_ResponseSyntax) **   <a name="pinpoint-DeletePool-response-Status"></a>
The current status of the pool.
+ CREATING: The pool is currently being created and isn't yet available for use.
+ ACTIVE: The pool is active and available for use.
+ DELETING: The pool is being deleted.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING`

 ** [TwoWayChannelArn](#API_DeletePool_ResponseSyntax) **   <a name="pinpoint-DeletePool-response-TwoWayChannelArn"></a>
The Amazon Resource Name (ARN) of the TwoWayChannel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`

 ** [TwoWayChannelRole](#API_DeletePool_ResponseSyntax) **   <a name="pinpoint-DeletePool-response-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`

 ** [TwoWayEnabled](#API_DeletePool_ResponseSyntax) **   <a name="pinpoint-DeletePool-response-TwoWayEnabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients.
Type: Boolean

## Errors
<a name="API_DeletePool_Errors"></a>

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
<a name="API_DeletePool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeletePool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeletePool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeletePool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeletePool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeletePool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeletePool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeletePool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeletePool)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeletePool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeletePool)
