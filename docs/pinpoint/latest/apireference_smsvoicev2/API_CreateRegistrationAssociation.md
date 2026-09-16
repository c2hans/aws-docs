---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateRegistrationAssociation.html
---

# CreateRegistrationAssociation
<a name="API_CreateRegistrationAssociation"></a>

Associate the registration with an origination identity such as a phone number or sender ID.

## Request Syntax
<a name="API_CreateRegistrationAssociation_RequestSyntax"></a>

```
{
   "RegistrationId": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateRegistrationAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RegistrationId](#API_CreateRegistrationAssociation_RequestSyntax) **   <a name="pinpoint-CreateRegistrationAssociation-request-RegistrationId"></a>
The unique identifier for the registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [ResourceId](#API_CreateRegistrationAssociation_RequestSyntax) **   <a name="pinpoint-CreateRegistrationAssociation-request-ResourceId"></a>
The unique identifier for the origination identity. For example this could be a **PhoneNumberId** or **SenderId**.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_CreateRegistrationAssociation_ResponseSyntax"></a>

```
{
   "IsoCountryCode": "string",
   "PhoneNumber": "string",
   "RegistrationArn": "string",
   "RegistrationId": "string",
   "RegistrationType": "string",
   "ResourceArn": "string",
   "ResourceId": "string",
   "ResourceType": "string"
}
```

## Response Elements
<a name="API_CreateRegistrationAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IsoCountryCode](#API_CreateRegistrationAssociation_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAssociation-response-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`

 ** [PhoneNumber](#API_CreateRegistrationAssociation_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAssociation-response-PhoneNumber"></a>
The phone number associated with the registration in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`

 ** [RegistrationArn](#API_CreateRegistrationAssociation_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAssociation-response-RegistrationArn"></a>
The Amazon Resource Name (ARN) for the registration.
Type: String

 ** [RegistrationId](#API_CreateRegistrationAssociation_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAssociation-response-RegistrationId"></a>
The unique identifier for the registration.
Type: String

 ** [RegistrationType](#API_CreateRegistrationAssociation_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAssociation-response-RegistrationType"></a>
The type of registration form. The list of **RegistrationTypes** can be found using the [DescribeRegistrationTypeDefinitions](API_DescribeRegistrationTypeDefinitions.md) action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`

 ** [ResourceArn](#API_CreateRegistrationAssociation_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAssociation-response-ResourceArn"></a>
The Amazon Resource Name (ARN) of the origination identity that is associated with the registration.
Type: String

 ** [ResourceId](#API_CreateRegistrationAssociation_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAssociation-response-ResourceId"></a>
The unique identifier for the origination identity. For example this could be a **PhoneNumberId** or **SenderId**.
Type: String

 ** [ResourceType](#API_CreateRegistrationAssociation_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAssociation-response-ResourceType"></a>
The registration type or origination identity type.
Type: String

## Errors
<a name="API_CreateRegistrationAssociation_Errors"></a>

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
<a name="API_CreateRegistrationAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAssociation)
