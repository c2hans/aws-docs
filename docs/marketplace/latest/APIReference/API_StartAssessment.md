---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_StartAssessment.html
---

# StartAssessment

Starts an assessment of a product entity against a framework. An *assessment* is the result of evaluating an entity against the controls of a framework. You choose the controls to run and provide the input that each control needs.

The assessment runs asynchronously. This action returns the ID of the assessment immediately. To get its status and the results of each control, use the `DescribeAssessment` action. To find assessments that you started earlier, use the `ListAssessments` action.

## Request Syntax
<a name="API_StartAssessment_RequestSyntax"></a>

```
POST /StartAssessment HTTP/1.1
Content-type: application/json

{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "Controls": [
      {
         "ControlId": "{{string}}",
         "Input": {{JSON value}}
      }
   ],
   "EntityId": "{{string}}",
   "FrameworkId": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartAssessment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartAssessment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Catalog](#API_StartAssessment_RequestSyntax) **   <a name="AWSMarketplaceService-StartAssessment-request-Catalog"></a>
The catalog related to the request. Fixed value: `AWSMarketplace`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?![.-])(?!.*[.-]{2})(?![0-9]+\.[0-9.]+$)[a-zA-Z0-9.-]{1,47}(?<![.-])$`
Required: Yes

 ** [EntityId](#API_StartAssessment_RequestSyntax) **   <a name="AWSMarketplaceService-StartAssessment-request-EntityId"></a>
The unique ID of the product entity to assess.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`
Required: Yes

 ** [FrameworkId](#API_StartAssessment_RequestSyntax) **   <a name="AWSMarketplaceService-StartAssessment-request-FrameworkId"></a>
The unique identifier of the framework that defines the controls to run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-@]+$`
Required: Yes

 ** [ClientToken](#API_StartAssessment_RequestSyntax) **   <a name="AWSMarketplaceService-StartAssessment-request-ClientToken"></a>
A unique token to identify the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[!-~]+$`
Required: No

 ** [Controls](#API_StartAssessment_RequestSyntax) **   <a name="AWSMarketplaceService-StartAssessment-request-Controls"></a>
The controls to provide input for. Every control in the framework is included in the assessment, and a control that you don't specify gets no input. You can specify 1–100 controls.
Type: Array of [ControlInput](API_ControlInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [Tags](#API_StartAssessment_RequestSyntax) **   <a name="AWSMarketplaceService-StartAssessment-request-Tags"></a>
A map of tags to apply to the assessment when you create it. Each tag is a key-value pair. You can specify 1–200 tags.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_StartAssessment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AssessmentId": "string"
}
```

## Response Elements
<a name="API_StartAssessment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssessmentId](#API_StartAssessment_ResponseSyntax) **   <a name="AWSMarketplaceService-StartAssessment-response-AssessmentId"></a>
The unique ID of the assessment that was started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(assessment-[a-zA-Z0-9]+|arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:[0-9]*:[a-zA-Z0-9-]+/Assessment/assessment-[a-zA-Z0-9]+)$`

## Errors
<a name="API_StartAssessment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP status code: 403
HTTP Status Code: 403

 ** InternalServiceException **
There was an internal service exception.
HTTP status code: 500
HTTP Status Code: 500

 ** ResourceInUseException **
The resource is currently in use.
HTTP Status Code: 423

 ** ResourceNotFoundException **
The specified resource wasn't found.
HTTP status code: 404
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The maximum number of open requests per account has been exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Too many requests.
HTTP status code: 429
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
HTTP status code: 422
 ** ValidationExceptionFieldList **
A list of detailed entries describing the request fields that failed validation. Present when the failure can be attributed to one or more specific fields.
HTTP Status Code: 422

## See Also
<a name="API_StartAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-catalog-2018-09-17/StartAssessment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-catalog-2018-09-17/StartAssessment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/StartAssessment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-catalog-2018-09-17/StartAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/StartAssessment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-catalog-2018-09-17/StartAssessment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-catalog-2018-09-17/StartAssessment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-catalog-2018-09-17/StartAssessment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/StartAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/StartAssessment)
