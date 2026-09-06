---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_AssociateOriginationIdentity.html
---

# AssociateOriginationIdentity
<a name="API_AssociateOriginationIdentity"></a>

Associates the specified origination identity with a pool.

If the origination identity is a phone number and is already associated with another pool, an error is returned. A sender ID can be associated with multiple pools.

If the origination identity configuration doesn't match the pool's configuration, an error is returned.

## Request Syntax
<a name="API_AssociateOriginationIdentity_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "IsoCountryCode": "{{string}}",
   "OriginationIdentity": "{{string}}",
   "PoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateOriginationIdentity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_AssociateOriginationIdentity_RequestSyntax) **   <a name="pinpoint-AssociateOriginationIdentity-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [IsoCountryCode](#API_AssociateOriginationIdentity_RequestSyntax) **   <a name="pinpoint-AssociateOriginationIdentity-request-IsoCountryCode"></a>
The new two-character code, in ISO 3166-1 alpha-2 format, for the country or region of the origination identity. This field is optional and is not required for origination identity types that are not country-specific, such as RCS agents.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: No

 ** [OriginationIdentity](#API_AssociateOriginationIdentity_RequestSyntax) **   <a name="pinpoint-AssociateOriginationIdentity-request-OriginationIdentity"></a>
The origination identity to use, such as PhoneNumberId, PhoneNumberArn, SenderId, or SenderIdArn. You can use [DescribePhoneNumbers](API_DescribePhoneNumbers.md) to find the values for PhoneNumberId and PhoneNumberArn, while [DescribeSenderIds](API_DescribeSenderIds.md) can be used to get the values for SenderId and SenderIdArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [PoolId](#API_AssociateOriginationIdentity_RequestSyntax) **   <a name="pinpoint-AssociateOriginationIdentity-request-PoolId"></a>
The pool to update with the new Identity. This value can be either the PoolId or PoolArn, and you can find these values using [DescribePools](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribePools.html).
If you are using a shared AWS End User Messaging SMS; resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]*`
Required: Yes

## Response Syntax
<a name="API_AssociateOriginationIdentity_ResponseSyntax"></a>

```
{
   "IsoCountryCode": "string",
   "OriginationIdentity": "string",
   "OriginationIdentityArn": "string",
   "PoolArn": "string",
   "PoolId": "string"
}
```

## Response Elements
<a name="API_AssociateOriginationIdentity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IsoCountryCode](#API_AssociateOriginationIdentity_ResponseSyntax) **   <a name="pinpoint-AssociateOriginationIdentity-response-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`

 ** [OriginationIdentity](#API_AssociateOriginationIdentity_ResponseSyntax) **   <a name="pinpoint-AssociateOriginationIdentity-response-OriginationIdentity"></a>
The PhoneNumberId or SenderId of the origination identity.
Type: String

 ** [OriginationIdentityArn](#API_AssociateOriginationIdentity_ResponseSyntax) **   <a name="pinpoint-AssociateOriginationIdentity-response-OriginationIdentityArn"></a>
The PhoneNumberArn or SenderIdArn of the origination identity.
Type: String

 ** [PoolArn](#API_AssociateOriginationIdentity_ResponseSyntax) **   <a name="pinpoint-AssociateOriginationIdentity-response-PoolArn"></a>
The Amazon Resource Name (ARN) of the pool that is now associated with the origination identity.
Type: String

 ** [PoolId](#API_AssociateOriginationIdentity_ResponseSyntax) **   <a name="pinpoint-AssociateOriginationIdentity-response-PoolId"></a>
The PoolId of the pool that is now associated with the origination identity.
Type: String

## Errors
<a name="API_AssociateOriginationIdentity_Errors"></a>

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
<a name="API_AssociateOriginationIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/AssociateOriginationIdentity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/AssociateOriginationIdentity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/AssociateOriginationIdentity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/AssociateOriginationIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/AssociateOriginationIdentity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/AssociateOriginationIdentity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/AssociateOriginationIdentity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/AssociateOriginationIdentity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/AssociateOriginationIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/AssociateOriginationIdentity)
