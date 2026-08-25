---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ListAssessments.html
---

# ListAssessments
<a name="API_ListAssessments"></a>

Returns a paginated list of assessments associated with an entity or change set in AWS Marketplace. An *assessment* is the result of evaluating a product or change set against a framework, such as AMI Security or Container Security.

Use the `AssessmentTargetFilter` to scope results to a specific entity or change set, and use `FrameworkFilters` to scope results to a single framework. To retrieve detailed control-level results for an individual assessment, use the `DescribeAssessment` action.

Results are sorted by assessment creation time in descending order.

## Request Syntax
<a name="API_ListAssessments_RequestSyntax"></a>

```
POST /ListAssessments HTTP/1.1
Content-type: application/json

{
   "AssessmentTargetFilter": {
      "ChangeSetId": "{{string}}",
      "EntityId": "{{string}}"
   },
   "Catalog": "{{string}}",
   "FrameworkFilters": { ... },
   "FrameworkId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListAssessments_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListAssessments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Catalog](#API_ListAssessments_RequestSyntax) **   <a name="AWSMarketplaceService-ListAssessments-request-Catalog"></a>
The catalog related to the request. Fixed value: `AWSMarketplace`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z]+$`
Required: Yes

 ** [AssessmentTargetFilter](#API_ListAssessments_RequestSyntax) **   <a name="AWSMarketplaceService-ListAssessments-request-AssessmentTargetFilter"></a>
Filters the list of assessments to those performed against a specific entity or change set.
Type: [AssessmentTargetFilter](API_AssessmentTargetFilter.md) object
Required: No

 ** [FrameworkFilters](#API_ListAssessments_RequestSyntax) **   <a name="AWSMarketplaceService-ListAssessments-request-FrameworkFilters"></a>
Framework-specific filters. Set exactly one member to filter results to assessments performed against that framework.
Type: [FrameworkFilters](API_FrameworkFilters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [FrameworkId](#API_ListAssessments_RequestSyntax) **   <a name="AWSMarketplaceService-ListAssessments-request-FrameworkId"></a>
The unique identifier of a framework. When specified, only assessments performed against this framework are returned. For example, `AMISecurity`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-@]+$`
Required: No

 ** [MaxResults](#API_ListAssessments_RequestSyntax) **   <a name="AWSMarketplaceService-ListAssessments-request-MaxResults"></a>
Specifies the upper limit of the elements on a single page. If a value isn't provided, the default value is 20. Valid values range from 1 to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListAssessments_RequestSyntax) **   <a name="AWSMarketplaceService-ListAssessments-request-NextToken"></a>
The value of the next token, if it exists. `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^[\w+=.:@\-\/]+$`
Required: No

## Response Syntax
<a name="API_ListAssessments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AssessmentSummaryList": [
      {
         "AssessmentArn": "string",
         "AssessmentId": "string",
         "AssessmentResult": "string",
         "AssessmentTargetSummary": {
            "ChangeSetId": "string",
            "EntityId": "string"
         },
         "CreatedAt": "string",
         "ExpiresAt": "string",
         "FrameworkId": "string",
         "FrameworkSummary": { ... }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAssessments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssessmentSummaryList](#API_ListAssessments_ResponseSyntax) **   <a name="AWSMarketplaceService-ListAssessments-response-AssessmentSummaryList"></a>
An array of `AssessmentSummary` objects.
Type: Array of [AssessmentSummary](API_AssessmentSummary.md) objects

 ** [NextToken](#API_ListAssessments_ResponseSyntax) **   <a name="AWSMarketplaceService-ListAssessments-response-NextToken"></a>
The value of the next token, if it exists. `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^[\w+=.:@\-\/]+$`

## Errors
<a name="API_ListAssessments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP status code: 403
HTTP Status Code: 403

 ** InternalServiceException **
There was an internal service exception.
HTTP status code: 500
HTTP Status Code: 500

 ** ThrottlingException **
Too many requests.
HTTP status code: 429
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
HTTP status code: 422
HTTP Status Code: 422

## See Also
<a name="API_ListAssessments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-catalog-2018-09-17/ListAssessments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-catalog-2018-09-17/ListAssessments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ListAssessments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-catalog-2018-09-17/ListAssessments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ListAssessments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-catalog-2018-09-17/ListAssessments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-catalog-2018-09-17/ListAssessments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-catalog-2018-09-17/ListAssessments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/ListAssessments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ListAssessments)
