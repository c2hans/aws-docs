---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteRegistrationFieldValue.html
---

# DeleteRegistrationFieldValue
<a name="API_DeleteRegistrationFieldValue"></a>

Delete the value in a registration form field.

## Request Syntax
<a name="API_DeleteRegistrationFieldValue_RequestSyntax"></a>

```
{
   "FieldPath": "{{string}}",
   "RegistrationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteRegistrationFieldValue_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FieldPath](#API_DeleteRegistrationFieldValue_RequestSyntax) **   <a name="pinpoint-DeleteRegistrationFieldValue-request-FieldPath"></a>
The path to the registration form field. You can use [DescribeRegistrationFieldDefinitions](API_DescribeRegistrationFieldDefinitions.md) for a list of **FieldPaths**.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9_\.]+`
Required: Yes

 ** [RegistrationId](#API_DeleteRegistrationFieldValue_RequestSyntax) **   <a name="pinpoint-DeleteRegistrationFieldValue-request-RegistrationId"></a>
The unique identifier for the registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteRegistrationFieldValue_ResponseSyntax"></a>

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
<a name="API_DeleteRegistrationFieldValue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FieldPath](#API_DeleteRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-DeleteRegistrationFieldValue-response-FieldPath"></a>
The path to the registration form field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9_\.]+`

 ** [RegistrationArn](#API_DeleteRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-DeleteRegistrationFieldValue-response-RegistrationArn"></a>
The Amazon Resource Name (ARN) for the registration.
Type: String

 ** [RegistrationAttachmentId](#API_DeleteRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-DeleteRegistrationFieldValue-response-RegistrationAttachmentId"></a>
The unique identifier for the registration attachment.
Type: String

 ** [RegistrationId](#API_DeleteRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-DeleteRegistrationFieldValue-response-RegistrationId"></a>
The unique identifier for the registration.
Type: String

 ** [SelectChoices](#API_DeleteRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-DeleteRegistrationFieldValue-response-SelectChoices"></a>
An array of values for the form field.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [TextValue](#API_DeleteRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-DeleteRegistrationFieldValue-response-TextValue"></a>
The text data for a free form field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [VersionNumber](#API_DeleteRegistrationFieldValue_ResponseSyntax) **   <a name="pinpoint-DeleteRegistrationFieldValue-response-VersionNumber"></a>
The version number of the registration.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

## Errors
<a name="API_DeleteRegistrationFieldValue_Errors"></a>

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
<a name="API_DeleteRegistrationFieldValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationFieldValue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationFieldValue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationFieldValue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationFieldValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationFieldValue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationFieldValue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationFieldValue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationFieldValue)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationFieldValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationFieldValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
