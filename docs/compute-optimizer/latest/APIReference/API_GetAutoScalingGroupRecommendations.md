---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetAutoScalingGroupRecommendations.html
---

# GetAutoScalingGroupRecommendations
<a name="API_GetAutoScalingGroupRecommendations"></a>

Returns Auto Scaling group recommendations.

 AWS Compute Optimizer generates recommendations for Amazon EC2 Auto Scaling groups that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the * AWS Compute Optimizer User Guide*.

## Request Syntax
<a name="API_GetAutoScalingGroupRecommendations_RequestSyntax"></a>

```
{
   "accountIds": [ "{{string}}" ],
   "autoScalingGroupArns": [ "{{string}}" ],
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "recommendationPreferences": {
      "cpuVendorArchitectures": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_GetAutoScalingGroupRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIds](#API_GetAutoScalingGroupRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetAutoScalingGroupRecommendations-request-accountIds"></a>
The ID of the AWS account for which to return Auto Scaling group recommendations.
If your account is the management account of an organization, use this parameter to specify the member account for which you want to return Auto Scaling group recommendations.
Only one account ID can be specified per request.
Type: Array of strings
Required: No

 ** [autoScalingGroupArns](#API_GetAutoScalingGroupRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetAutoScalingGroupRecommendations-request-autoScalingGroupArns"></a>
The Amazon Resource Name (ARN) of the Auto Scaling groups for which to return recommendations.
Type: Array of strings
Required: No

 ** [filters](#API_GetAutoScalingGroupRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetAutoScalingGroupRecommendations-request-filters"></a>
An array of objects to specify a filter that returns a more specific list of Auto Scaling group recommendations.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [maxResults](#API_GetAutoScalingGroupRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetAutoScalingGroupRecommendations-request-maxResults"></a>
The maximum number of Auto Scaling group recommendations to return with a single request.
To retrieve the remaining results, make another request with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_GetAutoScalingGroupRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetAutoScalingGroupRecommendations-request-nextToken"></a>
The token to advance to the next page of Auto Scaling group recommendations.
Type: String
Required: No

 ** [recommendationPreferences](#API_GetAutoScalingGroupRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetAutoScalingGroupRecommendations-request-recommendationPreferences"></a>
An object to specify the preferences for the Auto Scaling group recommendations to return in the response.
Type: [RecommendationPreferences](API_RecommendationPreferences.md) object
Required: No

## Response Syntax
<a name="API_GetAutoScalingGroupRecommendations_ResponseSyntax"></a>

```
{
   "autoScalingGroupRecommendations": [
      {
         "accountId": "string",
         "autoScalingGroupArn": "string",
         "autoScalingGroupName": "string",
         "currentConfiguration": {
            "allocationStrategy": "string",
            "desiredCapacity": number,
            "estimatedInstanceHourReductionPercentage": number,
            "instanceType": "string",
            "maxSize": number,
            "minSize": number,
            "mixedInstanceTypes": [ "string" ],
            "type": "string"
         },
         "currentInstanceGpuInfo": {
            "gpus": [
               {
                  "gpuCount": number,
                  "gpuMemorySizeInMiB": number
               }
            ]
         },
         "currentPerformanceRisk": "string",
         "effectiveRecommendationPreferences": {
            "cpuVendorArchitectures": [ "string" ],
            "enhancedInfrastructureMetrics": "string",
            "externalMetricsPreference": {
               "source": "string"
            },
            "inferredWorkloadTypes": "string",
            "lookBackPeriod": "string",
            "preferredResources": [
               {
                  "effectiveIncludeList": [ "string" ],
                  "excludeList": [ "string" ],
                  "includeList": [ "string" ],
                  "name": "string"
               }
            ],
            "savingsEstimationMode": {
               "source": "string"
            },
            "utilizationPreferences": [
               {
                  "metricName": "string",
                  "metricParameters": {
                     "headroom": "string",
                     "threshold": "string"
                  }
               }
            ]
         },
         "finding": "string",
         "inferredWorkloadTypes": [ "string" ],
         "lastRefreshTimestamp": number,
         "lookBackPeriodInDays": number,
         "recommendationOptions": [
            {
               "configuration": {
                  "allocationStrategy": "string",
                  "desiredCapacity": number,
                  "estimatedInstanceHourReductionPercentage": number,
                  "instanceType": "string",
                  "maxSize": number,
                  "minSize": number,
                  "mixedInstanceTypes": [ "string" ],
                  "type": "string"
               },
               "instanceGpuInfo": {
                  "gpus": [
                     {
                        "gpuCount": number,
                        "gpuMemorySizeInMiB": number
                     }
                  ]
               },
               "migrationEffort": "string",
               "performanceRisk": number,
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
         "utilizationMetrics": [
            {
               "name": "string",
               "statistic": "string",
               "value": number
            }
         ]
      }
   ],
   "errors": [
      {
         "code": "string",
         "identifier": "string",
         "message": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetAutoScalingGroupRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autoScalingGroupRecommendations](#API_GetAutoScalingGroupRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetAutoScalingGroupRecommendations-response-autoScalingGroupRecommendations"></a>
An array of objects that describe Auto Scaling group recommendations.
Type: Array of [AutoScalingGroupRecommendation](API_AutoScalingGroupRecommendation.md) objects

 ** [errors](#API_GetAutoScalingGroupRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetAutoScalingGroupRecommendations-response-errors"></a>
An array of objects that describe errors of the request.
For example, an error is returned if you request recommendations for an unsupported Auto Scaling group.
Type: Array of [GetRecommendationError](API_GetRecommendationError.md) objects

 ** [nextToken](#API_GetAutoScalingGroupRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetAutoScalingGroupRecommendations-response-nextToken"></a>
The token to use to advance to the next page of Auto Scaling group recommendations.
This value is null when there are no more pages of Auto Scaling group recommendations to return.
Type: String

## Errors
<a name="API_GetAutoScalingGroupRecommendations_Errors"></a>

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

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed due to a temporary failure of the server.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_GetAutoScalingGroupRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetAutoScalingGroupRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetAutoScalingGroupRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetAutoScalingGroupRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetAutoScalingGroupRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetAutoScalingGroupRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetAutoScalingGroupRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetAutoScalingGroupRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetAutoScalingGroupRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetAutoScalingGroupRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetAutoScalingGroupRecommendations)
