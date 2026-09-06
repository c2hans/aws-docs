---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_ExportComplianceInquiry.html
---

# ExportComplianceInquiry
<a name="API_ExportComplianceInquiry"></a>

Export a compliance inquiry report.

## Request Syntax
<a name="API_ExportComplianceInquiry_RequestSyntax"></a>

```
POST /v1/compliance-inquiry/export HTTP/1.1
Content-type: application/json

{
   "complianceInquiryId": "{{string}}",
   "includeCitations": {{boolean}},
   "queryIdentifiers": [ {{number}} ]
}
```

## URI Request Parameters
<a name="API_ExportComplianceInquiry_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ExportComplianceInquiry_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [complianceInquiryId](#API_ExportComplianceInquiry_RequestSyntax) **   <a name="artifact-ExportComplianceInquiry-request-complianceInquiryId"></a>
Unique resource ID for the compliance inquiry.
Type: String
Pattern: `compliance-inquiry-[a-zA-Z0-9]{16}`
Required: Yes

 ** [includeCitations](#API_ExportComplianceInquiry_RequestSyntax) **   <a name="artifact-ExportComplianceInquiry-request-includeCitations"></a>
When true, include citations in the exported document.
Type: Boolean
Required: No

 ** [queryIdentifiers](#API_ExportComplianceInquiry_RequestSyntax) **   <a name="artifact-ExportComplianceInquiry-request-queryIdentifiers"></a>
List of query identifiers to include in the export.
Type: Array of integers
Required: No

## Response Syntax
<a name="API_ExportComplianceInquiry_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "documentPresignedUrl": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_ExportComplianceInquiry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [documentPresignedUrl](#API_ExportComplianceInquiry_ResponseSyntax) **   <a name="artifact-ExportComplianceInquiry-response-documentPresignedUrl"></a>
Presigned S3 URL to access the exported compliance inquiry report.
Type: String

 ** [tags](#API_ExportComplianceInquiry_ResponseSyntax) **   <a name="artifact-ExportComplianceInquiry-response-tags"></a>
Tags associated with the compliance inquiry resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9\s_.:/=+\-@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s_.:/=+\-@]*`

## Errors
<a name="API_ExportComplianceInquiry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unknown server exception has occurred.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
Identifier of the affected resource.
 ** resourceType **
Type of the affected resource.
HTTP Status Code: 404

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
<a name="API_ExportComplianceInquiry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/ExportComplianceInquiry)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/ExportComplianceInquiry)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/ExportComplianceInquiry)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/ExportComplianceInquiry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/ExportComplianceInquiry)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/ExportComplianceInquiry)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/ExportComplianceInquiry)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/ExportComplianceInquiry)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/ExportComplianceInquiry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/ExportComplianceInquiry)
