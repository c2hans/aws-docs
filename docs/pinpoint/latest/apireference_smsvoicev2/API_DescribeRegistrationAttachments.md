---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationAttachments.html
---

# DescribeRegistrationAttachments
<a name="API_DescribeRegistrationAttachments"></a>

Retrieves the specified registration attachments or all registration attachments associated with your AWS account.

## Request Syntax
<a name="API_DescribeRegistrationAttachments_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RegistrationAttachmentIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeRegistrationAttachments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeRegistrationAttachments_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationAttachments-request-Filters"></a>
An array of RegistrationAttachmentFilter objects to filter the results.
Type: Array of [RegistrationAttachmentFilter](API_RegistrationAttachmentFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [MaxResults](#API_DescribeRegistrationAttachments_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationAttachments-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeRegistrationAttachments_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationAttachments-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [RegistrationAttachmentIds](#API_DescribeRegistrationAttachments_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationAttachments-request-RegistrationAttachmentIds"></a>
The unique identifier of registration attachments to find. This is an array of **RegistrationAttachmentId**.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

## Response Syntax
<a name="API_DescribeRegistrationAttachments_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RegistrationAttachments": [
      {
         "AttachmentStatus": "string",
         "AttachmentUploadErrorReason": "string",
         "AttachmentUrl": "string",
         "CreatedTimestamp": number,
         "RegistrationAttachmentArn": "string",
         "RegistrationAttachmentId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRegistrationAttachments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeRegistrationAttachments_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationAttachments-response-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [RegistrationAttachments](#API_DescribeRegistrationAttachments_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationAttachments-response-RegistrationAttachments"></a>
An array of **RegistrationAttachments** objects that contain the details for the requested registration attachments.
Type: Array of [RegistrationAttachmentsInformation](API_RegistrationAttachmentsInformation.md) objects

## Errors
<a name="API_DescribeRegistrationAttachments_Errors"></a>

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
<a name="API_DescribeRegistrationAttachments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationAttachments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationAttachments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationAttachments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationAttachments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationAttachments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationAttachments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationAttachments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationAttachments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationAttachments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationAttachments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
