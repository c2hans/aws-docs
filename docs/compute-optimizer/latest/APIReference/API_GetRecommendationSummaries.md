---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRecommendationSummaries.html
---

# GetRecommendationSummaries
<a name="API_GetRecommendationSummaries"></a>

Returns the optimization findings for an account.

It returns the number of:
+ Amazon EC2 instances in an account that are `Underprovisioned`, `Overprovisioned`, or `Optimized`.
+ EC2Auto Scaling groups in an account that are `NotOptimized`, or `Optimized`.
+ Amazon EBS volumes in an account that are `NotOptimized`, or `Optimized`.
+ Lambda functions in an account that are `NotOptimized`, or `Optimized`.
+ Amazon ECS services in an account that are `Underprovisioned`, `Overprovisioned`, or `Optimized`.
+ Commercial software licenses in an account that are `InsufficientMetrics`, `NotOptimized` or `Optimized`.
+ Amazon Aurora and Amazon RDS databases in an account that are `Underprovisioned`, `Overprovisioned`, `Optimized`, or `NotOptimized`.

## Request Syntax
<a name="API_GetRecommendationSummaries_RequestSyntax"></a>

```
{
   "accountIds": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRecommendationSummaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIds](#API_GetRecommendationSummaries_RequestSyntax) **   <a name="computeoptimizer-GetRecommendationSummaries-request-accountIds"></a>
The ID of the AWS account for which to return recommendation summaries.
If your account is the management account of an organization, use this parameter to specify the member account for which you want to return recommendation summaries.
Only one account ID can be specified per request.
Type: Array of strings
Required: No

 ** [maxResults](#API_GetRecommendationSummaries_RequestSyntax) **   <a name="computeoptimizer-GetRecommendationSummaries-request-maxResults"></a>
The maximum number of recommendation summaries to return with a single request.
To retrieve the remaining results, make another request with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_GetRecommendationSummaries_RequestSyntax) **   <a name="computeoptimizer-GetRecommendationSummaries-request-nextToken"></a>
The token to advance to the next page of recommendation summaries.
Type: String
Required: No

## Response Syntax
<a name="API_GetRecommendationSummaries_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "recommendationSummaries": [
      {
         "accountId": "string",
         "aggregatedSavingsOpportunity": {
            "estimatedMonthlySavings": {
               "currency": "string",
               "value": number
            },
            "savingsOpportunityPercentage": number
         },
         "currentPerformanceRiskRatings": {
            "high": number,
            "low": number,
            "medium": number,
            "veryLow": number
         },
         "idleSavingsOpportunity": {
            "estimatedMonthlySavings": {
               "currency": "string",
               "value": number
            },
            "savingsOpportunityPercentage": number
         },
         "idleSummaries": [
            {
               "name": "string",
               "value": number
            }
         ],
         "inferredWorkloadSavings": [
            {
               "estimatedMonthlySavings": {
                  "currency": "string",
                  "value": number
               },
               "inferredWorkloadTypes": [ "string" ]
            }
         ],
         "recommendationResourceType": "string",
         "savingsOpportunity": {
            "estimatedMonthlySavings": {
               "currency": "string",
               "value": number
            },
            "savingsOpportunityPercentage": number
         },
         "summaries": [
            {
               "name": "string",
               "reasonCodeSummaries": [
                  {
                     "name": "string",
                     "value": number
                  }
               ],
               "value": number
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetRecommendationSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetRecommendationSummaries_ResponseSyntax) **   <a name="computeoptimizer-GetRecommendationSummaries-response-nextToken"></a>
The token to use to advance to the next page of recommendation summaries.
This value is null when there are no more pages of recommendation summaries to return.
Type: String

 ** [recommendationSummaries](#API_GetRecommendationSummaries_ResponseSyntax) **   <a name="computeoptimizer-GetRecommendationSummaries-response-recommendationSummaries"></a>
An array of objects that summarize a recommendation.
Type: Array of [RecommendationSummary](API_RecommendationSummary.md) objects

## Errors
<a name="API_GetRecommendationSummaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An internal error has occurred. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterValueException **
The value supplied for the input parameter is out of range or not valid.
HTTP Status Code: 400

 ** MissingAuthenticationToken **
The request must contain either a valid (registered) AWS access key ID or X.509 certificate.
HTTP Status Code: 400

 ** OptInRequiredException **
The account is not opted in to AWS Compute Optimizer.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed due to a temporary failure of the server.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_GetRecommendationSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetRecommendationSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetRecommendationSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetRecommendationSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetRecommendationSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetRecommendationSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetRecommendationSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetRecommendationSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetRecommendationSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetRecommendationSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetRecommendationSummaries)
