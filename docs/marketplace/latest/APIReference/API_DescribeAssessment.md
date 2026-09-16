---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_DescribeAssessment.html
---

# DescribeAssessment
<a name="API_DescribeAssessment"></a>

Returns the metadata and detailed results of a single assessment, including the framework that was evaluated, the overall assessment result, and a paginated list of individual control evaluation results.

To list available assessments before describing one, use the `ListAssessments` action.

## Request Syntax
<a name="API_DescribeAssessment_RequestSyntax"></a>

```
POST /DescribeAssessment HTTP/1.1
Content-type: application/json

{
   "AssessmentIdentifier": "{{string}}",
   "Catalog": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeAssessment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeAssessment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AssessmentIdentifier](#API_DescribeAssessment_RequestSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-request-AssessmentIdentifier"></a>
The unique identifier of the assessment to describe. You can provide either the assessment ID (for example, `assessment-12345`) or the full assessment ARN (for example, `arn:aws:aws-marketplace:us-east-1::AWSMarketplace/Assessment/assessment-12345`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(assessment-[a-zA-Z0-9]+|arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:[0-9]*:[a-zA-Z0-9-]+/Assessment/assessment-[a-zA-Z0-9]+)$`
Required: Yes

 ** [Catalog](#API_DescribeAssessment_RequestSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-request-Catalog"></a>
The catalog related to the request. Fixed value: `AWSMarketplace`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z]+$`
Required: Yes

 ** [MaxResults](#API_DescribeAssessment_RequestSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-request-MaxResults"></a>
Specifies the upper limit of `ControlAssessment` elements returned on a single page. If a value isn't provided, the default value is 50. Valid values range from 1 to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeAssessment_RequestSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-request-NextToken"></a>
The value of the next token, if it exists. `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^[\w+=.:@\-\/]+$`
Required: No

## Response Syntax
<a name="API_DescribeAssessment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AssessmentArn": "string",
   "AssessmentId": "string",
   "AssessmentResult": "string",
   "AssessmentTargetSummary": {
      "ChangeSetId": "string",
      "EntityId": "string"
   },
   "ControlAssessments": [
      {
         "ControlAssessmentResult": "string",
         "ControlId": "string",
         "Errors": [
            {
               "Code": "string",
               "Message": "string",
               "Scope": [
                  {
                     "Name": "string",
                     "Value": "string"
                  }
               ]
            }
         ]
      }
   ],
   "CreatedAt": "string",
   "ExpiresAt": "string",
   "FrameworkId": "string",
   "FrameworkSummary": { ... },
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAssessment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssessmentArn](#API_DescribeAssessment_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-response-AssessmentArn"></a>
The ARN associated with the assessment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9:*/-]+$`

 ** [AssessmentId](#API_DescribeAssessment_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-response-AssessmentId"></a>
The unique ID of the assessment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`

 ** [AssessmentResult](#API_DescribeAssessment_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-response-AssessmentResult"></a>
The overall result of the assessment.
Type: String
Valid Values: `PASS | FAIL`

 ** [AssessmentTargetSummary](#API_DescribeAssessment_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-response-AssessmentTargetSummary"></a>
Identifies the entity or change set that was assessed.
Type: [AssessmentTargetSummary](API_AssessmentTargetSummary.md) object

 ** [ControlAssessments](#API_DescribeAssessment_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-response-ControlAssessments"></a>
An array of `ControlAssessment` objects, each containing the result of an individual control evaluated as part of the assessment.
Type: Array of [ControlAssessment](API_ControlAssessment.md) objects

 ** [CreatedAt](#API_DescribeAssessment_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-response-CreatedAt"></a>
The date and time the assessment was created, in ISO 8601 format (`2018-02-27T13:45:22Z`).
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`

 ** [ExpiresAt](#API_DescribeAssessment_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-response-ExpiresAt"></a>
The date and time the assessment expires, in ISO 8601 format (`2018-02-27T13:45:22Z`).
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`

 ** [FrameworkId](#API_DescribeAssessment_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-response-FrameworkId"></a>
The identifier of the framework that was evaluated by this assessment, in the format `frameworkId@version` (for example, `AMISecurity@1.0`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-@.]+$`

 ** [FrameworkSummary](#API_DescribeAssessment_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-response-FrameworkSummary"></a>
The framework-specific details of the assessed resource. The set member corresponds to the framework identified by `FrameworkId`.
Type: [FrameworkSummary](API_FrameworkSummary.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [NextToken](#API_DescribeAssessment_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeAssessment-response-NextToken"></a>
The value of the next token, if it exists. `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^[\w+=.:@\-\/]+$`

## Errors
<a name="API_DescribeAssessment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP status code: 403
HTTP Status Code: 403

 ** InternalServiceException **
There was an internal service exception.
HTTP status code: 500
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource wasn't found.
HTTP status code: 404
HTTP Status Code: 404

 ** ThrottlingException **
Too many requests.
HTTP status code: 429
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
HTTP status code: 422
HTTP Status Code: 422

## See Also
<a name="API_DescribeAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-catalog-2018-09-17/DescribeAssessment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-catalog-2018-09-17/DescribeAssessment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/DescribeAssessment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-catalog-2018-09-17/DescribeAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/DescribeAssessment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-catalog-2018-09-17/DescribeAssessment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-catalog-2018-09-17/DescribeAssessment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-catalog-2018-09-17/DescribeAssessment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/DescribeAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/DescribeAssessment)
