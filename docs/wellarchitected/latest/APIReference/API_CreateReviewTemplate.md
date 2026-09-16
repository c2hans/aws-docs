---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateReviewTemplate.html
---

# CreateReviewTemplate
<a name="API_CreateReviewTemplate"></a>

Create a review template.

**Note**
 **Disclaimer**
Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your review templates. If your review template or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.

## Request Syntax
<a name="API_CreateReviewTemplate_RequestSyntax"></a>

```
POST /reviewTemplates HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "Description": "{{string}}",
   "Lenses": [ "{{string}}" ],
   "Notes": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TemplateName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateReviewTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateReviewTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateReviewTemplate_RequestSyntax) **   <a name="wellarchitected-CreateReviewTemplate-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure that this request is idempotent (executes only once).
You should not reuse the same token for other requests. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.
This token is listed as required, however, if you do not specify it, the AWS SDKs automatically generate one for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the request will fail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\x00-\x7F]*$`
Required: Yes

 ** [Description](#API_CreateReviewTemplate_RequestSyntax) **   <a name="wellarchitected-CreateReviewTemplate-request-Description"></a>
The review template description.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 250.
Pattern: `^[A-Za-z0-9-_.,:/()@!&?#+'’\s]+$`
Required: Yes

 ** [Lenses](#API_CreateReviewTemplate_RequestSyntax) **   <a name="wellarchitected-CreateReviewTemplate-request-Lenses"></a>
Lenses applied to the review template.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [Notes](#API_CreateReviewTemplate_RequestSyntax) **   <a name="wellarchitected-CreateReviewTemplate-request-Notes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
Type: String
Length Constraints: Maximum length of 2084.
Required: No

 ** [Tags](#API_CreateReviewTemplate_RequestSyntax) **   <a name="wellarchitected-CreateReviewTemplate-request-Tags"></a>
The tags assigned to the review template.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [TemplateName](#API_CreateReviewTemplate_RequestSyntax) **   <a name="wellarchitected-CreateReviewTemplate-request-TemplateName"></a>
Name of the review template.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `^[A-Za-z0-9-_.,:/()@!&?#+'’\s]+$`
Required: Yes

## Response Syntax
<a name="API_CreateReviewTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "TemplateArn": "string"
}
```

## Response Elements
<a name="API_CreateReviewTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TemplateArn](#API_CreateReviewTemplate_ResponseSyntax) **   <a name="wellarchitected-CreateReviewTemplate-response-TemplateArn"></a>
The review template ARN.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`

## Errors
<a name="API_CreateReviewTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The user has reached their resource quota.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateReviewTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/CreateReviewTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/CreateReviewTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CreateReviewTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/CreateReviewTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CreateReviewTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/CreateReviewTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/CreateReviewTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/CreateReviewTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/CreateReviewTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CreateReviewTemplate)
