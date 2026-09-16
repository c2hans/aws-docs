---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreatePool.html
---

# CreatePool
<a name="API_CreatePool"></a>

Creates a new pool and associates the specified origination identity to the pool. A pool can include one or more phone numbers and SenderIds that are associated with your AWS account.

The new pool inherits its configuration from the specified origination identity. This includes keywords, message type, opt-out list, two-way configuration, and self-managed opt-out configuration. Deletion protection isn't inherited from the origination identity and defaults to false.

If the origination identity is a phone number and is already associated with another pool, an error is returned. A sender ID can be associated with multiple pools.

## Request Syntax
<a name="API_CreatePool_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DeletionProtectionEnabled": {{boolean}},
   "IsoCountryCode": "{{string}}",
   "MessageType": "{{string}}",
   "OriginationIdentity": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreatePool_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreatePool_RequestSyntax) **   <a name="pinpoint-CreatePool-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [DeletionProtectionEnabled](#API_CreatePool_RequestSyntax) **   <a name="pinpoint-CreatePool-request-DeletionProtectionEnabled"></a>
By default this is set to false. When set to true the pool can't be deleted. You can change this value using the [UpdatePool](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdatePool.html) action.
Type: Boolean
Required: No

 ** [IsoCountryCode](#API_CreatePool_RequestSyntax) **   <a name="pinpoint-CreatePool-request-IsoCountryCode"></a>
The new two-character code, in ISO 3166-1 alpha-2 format, for the country or region of the new pool. This field is optional and is not required for origination identity types that are not country-specific, such as RCS agents.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: No

 ** [MessageType](#API_CreatePool_RequestSyntax) **   <a name="pinpoint-CreatePool-request-MessageType"></a>
The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive. After the pool is created the MessageType can't be changed.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`
Required: Yes

 ** [OriginationIdentity](#API_CreatePool_RequestSyntax) **   <a name="pinpoint-CreatePool-request-OriginationIdentity"></a>
The origination identity to use such as a PhoneNumberId, PhoneNumberArn, SenderId or SenderIdArn. You can use [DescribePhoneNumbers](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribePhoneNumbers.html) to find the values for PhoneNumberId and PhoneNumberArn, and use [DescribeSenderIds](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeSenderIds.html) can be used to get the values for SenderId and SenderIdArn.
After the pool is created you can add more origination identities to the pool by using [AssociateOriginationIdentity](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_AssociateOriginationIdentity.html).
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [Tags](#API_CreatePool_RequestSyntax) **   <a name="pinpoint-CreatePool-request-Tags"></a>
An array of tags (key and value pairs) associated with the pool.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreatePool_ResponseSyntax"></a>

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
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ],
   "TwoWayChannelArn": "string",
   "TwoWayChannelRole": "string",
   "TwoWayEnabled": boolean
}
```

## Response Elements
<a name="API_CreatePool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-CreatedTimestamp"></a>
The time when the pool was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [DeletionProtectionEnabled](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-DeletionProtectionEnabled"></a>
When set to true deletion protection is enabled. By default this is set to false.
Type: Boolean

 ** [MessageType](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-MessageType"></a>
The type of message for the pool to use.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`

 ** [OptOutListName](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-OptOutListName"></a>
The name of the OptOutList associated with the pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [PoolArn](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-PoolArn"></a>
The Amazon Resource Name (ARN) for the pool.
Type: String

 ** [PoolId](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-PoolId"></a>
The unique identifier for the pool.
Type: String

 ** [SelfManagedOptOutsEnabled](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-SelfManagedOptOutsEnabled"></a>
By default this is set to false. When set to false, and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.
Type: Boolean

 ** [SharedRoutesEnabled](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-SharedRoutesEnabled"></a>
Indicates whether shared routes are enabled for the pool. Set to false and only origination identities in this pool are used to send messages.
Type: Boolean

 ** [Status](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-Status"></a>
The current status of the pool.
+ CREATING: The pool is currently being created and isn't yet available for use.
+ ACTIVE: The pool is active and available for use.
+ DELETING: The pool is being deleted.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING`

 ** [Tags](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-Tags"></a>
An array of tags (key and value pairs) associated with the pool.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

 ** [TwoWayChannelArn](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-TwoWayChannelArn"></a>
The Amazon Resource Name (ARN) of the two way channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`

 ** [TwoWayChannelRole](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`

 ** [TwoWayEnabled](#API_CreatePool_ResponseSyntax) **   <a name="pinpoint-CreatePool-response-TwoWayEnabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients.
Type: Boolean

## Errors
<a name="API_CreatePool_Errors"></a>

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
<a name="API_CreatePool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/CreatePool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/CreatePool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CreatePool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/CreatePool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CreatePool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/CreatePool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/CreatePool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/CreatePool)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/CreatePool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CreatePool)
