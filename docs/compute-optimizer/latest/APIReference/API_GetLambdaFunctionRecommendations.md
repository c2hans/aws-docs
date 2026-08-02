---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetLambdaFunctionRecommendations.html
---

# GetLambdaFunctionRecommendations
<a name="API_GetLambdaFunctionRecommendations"></a>

Returns AWS Lambda function recommendations.

 AWS Compute Optimizer generates recommendations for functions that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the * AWS Compute Optimizer User Guide*.

## Request Syntax
<a name="API_GetLambdaFunctionRecommendations_RequestSyntax"></a>

```
{
   "accountIds": [ "{{string}}" ],
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "functionArns": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetLambdaFunctionRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIds](#API_GetLambdaFunctionRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetLambdaFunctionRecommendations-request-accountIds"></a>
The ID of the AWS account for which to return function recommendations.
If your account is the management account of an organization, use this parameter to specify the member account for which you want to return function recommendations.
Only one account ID can be specified per request.
Type: Array of strings
Required: No

 ** [filters](#API_GetLambdaFunctionRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetLambdaFunctionRecommendations-request-filters"></a>
An array of objects to specify a filter that returns a more specific list of function recommendations.
Type: Array of [LambdaFunctionRecommendationFilter](API_LambdaFunctionRecommendationFilter.md) objects
Required: No

 ** [functionArns](#API_GetLambdaFunctionRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetLambdaFunctionRecommendations-request-functionArns"></a>
The Amazon Resource Name (ARN) of the functions for which to return recommendations.
You can specify a qualified or unqualified ARN. If you specify an unqualified ARN without a function version suffix, Compute Optimizer will return recommendations for the latest (`$LATEST`) version of the function. If you specify a qualified ARN with a version suffix, Compute Optimizer will return recommendations for the specified function version. For more information about using function versions, see [Using versions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html#versioning-versions-using) in the * AWS Lambda Developer Guide*.
Type: Array of strings
Required: No

 ** [maxResults](#API_GetLambdaFunctionRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetLambdaFunctionRecommendations-request-maxResults"></a>
The maximum number of function recommendations to return with a single request.
To retrieve the remaining results, make another request with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_GetLambdaFunctionRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetLambdaFunctionRecommendations-request-nextToken"></a>
The token to advance to the next page of function recommendations.
Type: String
Required: No

## Response Syntax
<a name="API_GetLambdaFunctionRecommendations_ResponseSyntax"></a>

```
{
   "lambdaFunctionRecommendations": [
      {
         "accountId": "string",
         "currentMemorySize": number,
         "currentPerformanceRisk": "string",
         "effectiveRecommendationPreferences": {
            "savingsEstimationMode": {
               "source": "string"
            }
         },
         "finding": "string",
         "findingReasonCodes": [ "string" ],
         "functionArn": "string",
         "functionVersion": "string",
         "lastRefreshTimestamp": number,
         "lookbackPeriodInDays": number,
         "memorySizeRecommendationOptions": [
            {
               "memorySize": number,
               "projectedUtilizationMetrics": [
                  {
                     "name": "string",
                     "statistic": "string",
                     "value": number
                  }
               ],
               "rank": number,
               "savingsOpportunity": {
                  "estimatedMonthlySavings": {
                     "currency": "string",
                     "value": number
                  },
                  "savingsOpportunityPercentage": number
               },
               "savingsOpportunityAfterDiscounts": {
                  "estimatedMonthlySavings": {
                     "currency": "string",
                     "value": number
                  },
                  "savingsOpportunityPercentage": number
               }
            }
         ],
         "numberOfInvocations": number,
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "utilizationMetrics": [
            {
               "name": "string",
               "statistic": "string",
               "value": number
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetLambdaFunctionRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lambdaFunctionRecommendations](#API_GetLambdaFunctionRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetLambdaFunctionRecommendations-response-lambdaFunctionRecommendations"></a>
An array of objects that describe function recommendations.
Type: Array of [LambdaFunctionRecommendation](API_LambdaFunctionRecommendation.md) objects

 ** [nextToken](#API_GetLambdaFunctionRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetLambdaFunctionRecommendations-response-nextToken"></a>
The token to use to advance to the next page of function recommendations.
This value is null when there are no more pages of function recommendations to return.
Type: String

## Errors
<a name="API_GetLambdaFunctionRecommendations_Errors"></a>

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

 ** LimitExceededException **
The request exceeds a limit of the service.
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
<a name="API_GetLambdaFunctionRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetLambdaFunctionRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetLambdaFunctionRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetLambdaFunctionRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetLambdaFunctionRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetLambdaFunctionRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetLambdaFunctionRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetLambdaFunctionRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetLambdaFunctionRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetLambdaFunctionRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetLambdaFunctionRecommendations)
