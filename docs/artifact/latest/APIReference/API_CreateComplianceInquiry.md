---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_CreateComplianceInquiry.html
---

# CreateComplianceInquiry
<a name="API_CreateComplianceInquiry"></a>

Create a new compliance inquiry.

## Request Syntax
<a name="API_CreateComplianceInquiry_RequestSyntax"></a>

```
POST /v1/compliance-inquiry/create HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "inquiryContent": { ... },
   "name": "{{string}}",
   "supportMode": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateComplianceInquiry_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateComplianceInquiry_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateComplianceInquiry_RequestSyntax) **   <a name="artifact-CreateComplianceInquiry-request-clientToken"></a>
Idempotency token for the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\-]+`
Required: No

 ** [inquiryContent](#API_CreateComplianceInquiry_RequestSyntax) **   <a name="artifact-CreateComplianceInquiry-request-inquiryContent"></a>
Content for creating a compliance inquiry - either a single query or file content.
Type: [InquiryContent](API_InquiryContent.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [name](#API_CreateComplianceInquiry_RequestSyntax) **   <a name="artifact-CreateComplianceInquiry-request-name"></a>
Title of the inquiry.
Type: String
Required: Yes

 ** [supportMode](#API_CreateComplianceInquiry_RequestSyntax) **   <a name="artifact-CreateComplianceInquiry-request-supportMode"></a>
Support mode for inquiry processing. Only supported for file upload mode. Defaults to AI\_ONLY if not specified.
Type: String
Valid Values: `AI_ONLY | FULL_SUPPORT`
Required: No

 ** [tags](#API_CreateComplianceInquiry_RequestSyntax) **   <a name="artifact-CreateComplianceInquiry-request-tags"></a>
Tags to associate with the compliance inquiry resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9\s_.:/=+\-@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s_.:/=+\-@]*`
Required: No

## Response Syntax
<a name="API_CreateComplianceInquiry_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "complianceInquirySummary": {
      "arn": "string",
      "createdAt": "string",
      "id": "string",
      "inputSource": "string",
      "name": "string",
      "status": "string",
      "statusMessage": "string"
   },
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateComplianceInquiry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [complianceInquirySummary](#API_CreateComplianceInquiry_ResponseSyntax) **   <a name="artifact-CreateComplianceInquiry-response-complianceInquirySummary"></a>
Summary information about the created compliance inquiry.
Type: [InquirySummary](API_InquirySummary.md) object

 ** [tags](#API_CreateComplianceInquiry_ResponseSyntax) **   <a name="artifact-CreateComplianceInquiry-response-tags"></a>
Tags associated with the compliance inquiry resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9\s_.:/=+\-@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s_.:/=+\-@]*`

## Errors
<a name="API_CreateComplianceInquiry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Request to create/modify content would result in a conflict.
 ** resourceId **
Identifier of the affected resource.
 ** resourceType **
Type of the affected resource.
HTTP Status Code: 409

 ** InternalServerException **
An unknown server exception has occurred.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
Code for the affected quota.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
 ** serviceCode **
Code for the affected service.
HTTP Status Code: 429

 ** ValidationException **
Request fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The field that caused the error, if applicable.
 ** reason **
Reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateComplianceInquiry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/CreateComplianceInquiry)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/CreateComplianceInquiry)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/CreateComplianceInquiry)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/CreateComplianceInquiry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/CreateComplianceInquiry)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/CreateComplianceInquiry)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/CreateComplianceInquiry)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/CreateComplianceInquiry)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/CreateComplianceInquiry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/CreateComplianceInquiry)
