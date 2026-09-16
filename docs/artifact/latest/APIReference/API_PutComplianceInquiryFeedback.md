---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_PutComplianceInquiryFeedback.html
---

# PutComplianceInquiryFeedback
<a name="API_PutComplianceInquiryFeedback"></a>

Submits feedback on a compliance inquiry response.

## Request Syntax
<a name="API_PutComplianceInquiryFeedback_RequestSyntax"></a>

```
PUT /v1/compliance-inquiry/putFeedback HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "comment": "{{string}}",
   "complianceInquiryId": "{{string}}",
   "queryIdentifier": {{number}},
   "rating": "{{string}}",
   "reasonCodes": [ "{{string}}" ],
   "responseRevisionId": {{number}}
}
```

## URI Request Parameters
<a name="API_PutComplianceInquiryFeedback_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutComplianceInquiryFeedback_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_PutComplianceInquiryFeedback_RequestSyntax) **   <a name="artifact-PutComplianceInquiryFeedback-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\-]+`
Required: No

 ** [comment](#API_PutComplianceInquiryFeedback_RequestSyntax) **   <a name="artifact-PutComplianceInquiryFeedback-request-comment"></a>
An optional comment for the feedback.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9\s.,;:!?'\-()/@#&+=]+`
Required: No

 ** [complianceInquiryId](#API_PutComplianceInquiryFeedback_RequestSyntax) **   <a name="artifact-PutComplianceInquiryFeedback-request-complianceInquiryId"></a>
The unique identifier for the compliance inquiry.
Type: String
Pattern: `compliance-inquiry-[a-zA-Z0-9]{16}`
Required: Yes

 ** [queryIdentifier](#API_PutComplianceInquiryFeedback_RequestSyntax) **   <a name="artifact-PutComplianceInquiryFeedback-request-queryIdentifier"></a>
The sequential identifier of the query to provide feedback on.
Type: Integer
Required: No

 ** [rating](#API_PutComplianceInquiryFeedback_RequestSyntax) **   <a name="artifact-PutComplianceInquiryFeedback-request-rating"></a>
The rating for the feedback. Valid values are THUMBS\_UP and THUMBS\_DOWN.
Type: String
Valid Values: `THUMBS_UP | THUMBS_DOWN`
Required: Yes

 ** [reasonCodes](#API_PutComplianceInquiryFeedback_RequestSyntax) **   <a name="artifact-PutComplianceInquiryFeedback-request-reasonCodes"></a>
The reason codes that describe why you rated the response. Valid values are OTHER, PARTIAL\_RESPONSE, and IRRELEVANT\_RESPONSE.
Type: Array of strings
Valid Values: `OTHER | PARTIAL_RESPONSE | IRRELEVANT_RESPONSE`
Required: No

 ** [responseRevisionId](#API_PutComplianceInquiryFeedback_RequestSyntax) **   <a name="artifact-PutComplianceInquiryFeedback-request-responseRevisionId"></a>
The response revision ID. Use this value to prevent submitting feedback on a stale response.
Type: Integer
Required: No

## Response Syntax
<a name="API_PutComplianceInquiryFeedback_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "submittedAt": "string"
}
```

## Response Elements
<a name="API_PutComplianceInquiryFeedback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [submittedAt](#API_PutComplianceInquiryFeedback_ResponseSyntax) **   <a name="artifact-PutComplianceInquiryFeedback-response-submittedAt"></a>
The timestamp when the feedback was submitted.
Type: Timestamp

## Errors
<a name="API_PutComplianceInquiryFeedback_Errors"></a>

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
<a name="API_PutComplianceInquiryFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/PutComplianceInquiryFeedback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/PutComplianceInquiryFeedback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/PutComplianceInquiryFeedback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/PutComplianceInquiryFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/PutComplianceInquiryFeedback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/PutComplianceInquiryFeedback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/PutComplianceInquiryFeedback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/PutComplianceInquiryFeedback)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/PutComplianceInquiryFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/PutComplianceInquiryFeedback)
