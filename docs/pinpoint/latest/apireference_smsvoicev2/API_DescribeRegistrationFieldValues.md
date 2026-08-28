---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationFieldValues.html
---

# DescribeRegistrationFieldValues
<a name="API_DescribeRegistrationFieldValues"></a>

Retrieves the specified registration field values.

## Request Syntax
<a name="API_DescribeRegistrationFieldValues_RequestSyntax"></a>

```
{
   "FieldPaths": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RegistrationId": "{{string}}",
   "SectionPath": "{{string}}",
   "VersionNumber": {{number}}
}
```

## Request Parameters
<a name="API_DescribeRegistrationFieldValues_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FieldPaths](#API_DescribeRegistrationFieldValues_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationFieldValues-request-FieldPaths"></a>
An array of paths to the registration form field.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9_\.]+`
Required: No

 ** [MaxResults](#API_DescribeRegistrationFieldValues_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationFieldValues-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeRegistrationFieldValues_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationFieldValues-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [RegistrationId](#API_DescribeRegistrationFieldValues_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationFieldValues-request-RegistrationId"></a>
The unique identifier for the registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [SectionPath](#API_DescribeRegistrationFieldValues_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationFieldValues-request-SectionPath"></a>
The path to the section of the registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9_]+`
Required: No

 ** [VersionNumber](#API_DescribeRegistrationFieldValues_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationFieldValues-request-VersionNumber"></a>
The version number of the registration.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

## Response Syntax
<a name="API_DescribeRegistrationFieldValues_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RegistrationArn": "string",
   "RegistrationFieldValues": [
      {
         "DeniedReason": "string",
         "Feedback": "string",
         "FieldPath": "string",
         "RegistrationAttachmentId": "string",
         "SelectChoices": [ "string" ],
         "TextValue": "string"
      }
   ],
   "RegistrationId": "string",
   "VersionNumber": number
}
```

## Response Elements
<a name="API_DescribeRegistrationFieldValues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeRegistrationFieldValues_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationFieldValues-response-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [RegistrationArn](#API_DescribeRegistrationFieldValues_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationFieldValues-response-RegistrationArn"></a>
The Amazon Resource Name (ARN) for the registration.
Type: String

 ** [RegistrationFieldValues](#API_DescribeRegistrationFieldValues_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationFieldValues-response-RegistrationFieldValues"></a>
An array of RegistrationFieldValues objects that contain the values for the requested registration.
Type: Array of [RegistrationFieldValueInformation](API_RegistrationFieldValueInformation.md) objects

 ** [RegistrationId](#API_DescribeRegistrationFieldValues_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationFieldValues-response-RegistrationId"></a>
The unique identifier for the registration.
Type: String

 ** [VersionNumber](#API_DescribeRegistrationFieldValues_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationFieldValues-response-VersionNumber"></a>
The current version of the registration.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

## Errors
<a name="API_DescribeRegistrationFieldValues_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
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
<a name="API_DescribeRegistrationFieldValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldValues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldValues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldValues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldValues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldValues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldValues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldValues)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
