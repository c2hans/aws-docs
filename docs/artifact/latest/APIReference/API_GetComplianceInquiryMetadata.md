---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetComplianceInquiryMetadata.html
---

# GetComplianceInquiryMetadata
<a name="API_GetComplianceInquiryMetadata"></a>

Get the metadata for a single compliance inquiry.

## Request Syntax
<a name="API_GetComplianceInquiryMetadata_RequestSyntax"></a>

```
GET /v1/compliance-inquiry/getMetadata?complianceInquiryId={{complianceInquiryId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetComplianceInquiryMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [complianceInquiryId](#API_GetComplianceInquiryMetadata_RequestSyntax) **   <a name="artifact-GetComplianceInquiryMetadata-request-uri-complianceInquiryId"></a>
Unique resource ID for the compliance inquiry.
Pattern: `compliance-inquiry-[a-zA-Z0-9]{16}`
Required: Yes

## Request Body
<a name="API_GetComplianceInquiryMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetComplianceInquiryMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "complianceInquiryDetail": {
      "arn": "string",
      "createdAt": "string",
      "id": "string",
      "inputSource": "string",
      "name": "string",
      "status": "string",
      "statusMessage": "string",
      "supportMode": "string",
      "updatedAt": "string"
   },
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetComplianceInquiryMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [complianceInquiryDetail](#API_GetComplianceInquiryMetadata_ResponseSyntax) **   <a name="artifact-GetComplianceInquiryMetadata-response-complianceInquiryDetail"></a>
Detailed information about the compliance inquiry.
Type: [InquiryDetail](API_InquiryDetail.md) object

 ** [tags](#API_GetComplianceInquiryMetadata_ResponseSyntax) **   <a name="artifact-GetComplianceInquiryMetadata-response-tags"></a>
Tags associated with the compliance inquiry resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9\s_.:/=+\-@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s_.:/=+\-@]*`

## Errors
<a name="API_GetComplianceInquiryMetadata_Errors"></a>

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
<a name="API_GetComplianceInquiryMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/GetComplianceInquiryMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/GetComplianceInquiryMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/GetComplianceInquiryMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/GetComplianceInquiryMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/GetComplianceInquiryMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/GetComplianceInquiryMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/GetComplianceInquiryMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/GetComplianceInquiryMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/GetComplianceInquiryMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/GetComplianceInquiryMetadata)
