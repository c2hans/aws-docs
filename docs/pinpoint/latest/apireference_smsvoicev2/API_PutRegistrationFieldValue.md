---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutRegistrationFieldValue.html
---

# PutRegistrationFieldValue
<a name="API_PutRegistrationFieldValue"></a>

Creates or updates a field value for a registration.

## Request Syntax
<a name="API_PutRegistrationFieldValue_RequestSyntax"></a>

```
{
   "FieldPath": "{{string}}",
   "RegistrationAttachmentId": "{{string}}",
   "RegistrationId": "{{string}}",
   "SelectChoices": [ "{{string}}" ],
   "TextValue": "{{string}}"
}
```

## Request Parameters
<a name="API_PutRegistrationFieldValue_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FieldPath](#API_PutRegistrationFieldValue_RequestSyntax) **   <a name="pinpoint-PutRegistrationFieldValue-request-FieldPath"></a>
The path to the registration form field. You can use [DescribeRegistrationFieldDefinitions](API_DescribeRegistrationFieldDefinitions.md) for a list of **FieldPaths**.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9_\.]+`
Required: Yes

 ** [RegistrationAttachmentId](#API_PutRegistrationFieldValue_RequestSyntax) **   <a name="pinpoint-PutRegistrationFieldValue-request-RegistrationAttachmentId"></a>
The unique identifier for the registration attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [RegistrationId](#API_PutRegistrationFieldValue_RequestSyntax) **   <a name="pinpoint-PutRegistrationFieldValue-request-RegistrationId"></a>
The unique identifier for the registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [SelectChoices](#API_PutRegistrationFieldValue_RequestSyntax) **   <a name="pinpoint-PutRegistrationFieldValue-request-SelectChoices"></a>
An array of values for the form field.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [TextValue](#API_PutRegistrationFieldValue_RequestSyntax) **   <a name="pinpoint-PutRegistrationFieldValue-request-TextValue"></a>
The text data for a free form field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_PutRegistrationFieldValue_ResponseSyntax"></a>

```
{
   "FieldPath": "string",
   "RegistrationArn": "string",
   "RegistrationAttachmentId": "string",
   "RegistrationId": "string",
   "SelectChoices": [ "string" ],
   "TextValue": "string",
   "VersionNumber": number
}
```

## Response Elements
<a name="API_PutRegistrationFieldValue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FieldPath](#API_PutRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-PutRegistrationFieldValue-response-FieldPath"></a>
The path to the registration form field. You can use [DescribeRegistrationFieldDefinitions](API_DescribeRegistrationFieldDefinitions.md) for a list of **FieldPaths**.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9_\.]+`

 ** [RegistrationArn](#API_PutRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-PutRegistrationFieldValue-response-RegistrationArn"></a>
The Amazon Resource Name (ARN) for the registration.
Type: String

 ** [RegistrationAttachmentId](#API_PutRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-PutRegistrationFieldValue-response-RegistrationAttachmentId"></a>
The unique identifier for the registration attachment.
Type: String

 ** [RegistrationId](#API_PutRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-PutRegistrationFieldValue-response-RegistrationId"></a>
The unique identifier for the registration.
Type: String

 ** [SelectChoices](#API_PutRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-PutRegistrationFieldValue-response-SelectChoices"></a>
An array of values for the form field.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [TextValue](#API_PutRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-PutRegistrationFieldValue-response-TextValue"></a>
The text data for a free form field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [VersionNumber](#API_PutRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-PutRegistrationFieldValue-response-VersionNumber"></a>
The version number of the registration.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

## Errors
<a name="API_PutRegistrationFieldValue_Errors"></a>

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
<a name="API_PutRegistrationFieldValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/PutRegistrationFieldValue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/PutRegistrationFieldValue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/PutRegistrationFieldValue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/PutRegistrationFieldValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/PutRegistrationFieldValue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/PutRegistrationFieldValue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/PutRegistrationFieldValue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/PutRegistrationFieldValue)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/PutRegistrationFieldValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/PutRegistrationFieldValue)
