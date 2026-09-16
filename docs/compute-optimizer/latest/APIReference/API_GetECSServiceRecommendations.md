---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetECSServiceRecommendations.html
---

# GetECSServiceRecommendations
<a name="API_GetECSServiceRecommendations"></a>

 Returns Amazon ECS service recommendations.

 AWS Compute Optimizer generates recommendations for Amazon ECS services on Fargate that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the * AWS Compute Optimizer User Guide*.

## Request Syntax
<a name="API_GetECSServiceRecommendations_RequestSyntax"></a>

```
{
   "accountIds": [ "{{string}}" ],
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "serviceArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetECSServiceRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIds](#API_GetECSServiceRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendations-request-accountIds"></a>
 Return the Amazon ECS service recommendations to the specified AWS account IDs.
If your account is the management account or the delegated administrator of an organization, use this parameter to return the Amazon ECS service recommendations to specific member accounts.
You can only specify one account ID per request.
Type: Array of strings
Required: No

 ** [filters](#API_GetECSServiceRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendations-request-filters"></a>
 An array of objects to specify a filter that returns a more specific list of Amazon ECS service recommendations.
Type: Array of [ECSServiceRecommendationFilter](API_ECSServiceRecommendationFilter.md) objects
Required: No

 ** [maxResults](#API_GetECSServiceRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendations-request-maxResults"></a>
 The maximum number of Amazon ECS service recommendations to return with a single request.
To retrieve the remaining results, make another request with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_GetECSServiceRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendations-request-nextToken"></a>
 The token to advance to the next page of Amazon ECS service recommendations.
Type: String
Required: No

 ** [serviceArns](#API_GetECSServiceRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendations-request-serviceArns"></a>
 The ARN that identifies the Amazon ECS service.
 The following is the format of the ARN:
 `arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name`
Type: Array of strings
Required: No

## Response Syntax
<a name="API_GetECSServiceRecommendations_ResponseSyntax"></a>

```
{
   "ecsServiceRecommendations": [
      {
         "accountId": "string",
         "currentPerformanceRisk": "string",
         "currentServiceConfiguration": {
            "autoScalingConfiguration": "string",
            "containerConfigurations": [
               {
                  "containerName": "string",
                  "cpu": number,
                  "memorySizeConfiguration": {
                     "memory": number,
                     "memoryReservation": number
                  }
               }
            ],
            "cpu": number,
            "memory": number,
            "taskDefinitionArn": "string"
         },
         "effectiveRecommendationPreferences": {
            "lookBackPeriod": "string",
            "savingsEstimationMode": {
               "source": "string"
            }
         },
         "finding": "string",
         "findingReasonCodes": [ "string" ],
         "lastRefreshTimestamp": number,
         "launchType": "string",
         "lookbackPeriodInDays": number,
         "serviceArn": "string",
         "serviceRecommendationOptions": [
            {
               "containerRecommendations": [
                  {
                     "containerName": "string",
                     "cpu": number,
                     "memorySizeConfiguration": {
                        "memory": number,
                        "memoryReservation": number
                     }
                  }
               ],
               "cpu": number,
               "memory": number,
               "projectedUtilizationMetrics": [
                  {
                     "lowerBoundValue": number,
                     "name": "string",
                     "statistic": "string",
                     "upperBoundValue": number
                  }
               ],
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
<a name="API_GetECSServiceRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ecsServiceRecommendations](#API_GetECSServiceRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendations-response-ecsServiceRecommendations"></a>
 An array of objects that describe the Amazon ECS service recommendations.
Type: Array of [ECSServiceRecommendation](API_ECSServiceRecommendation.md) objects

 ** [errors](#API_GetECSServiceRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendations-response-errors"></a>
 An array of objects that describe errors of the request.
Type: Array of [GetRecommendationError](API_GetRecommendationError.md) objects

 ** [nextToken](#API_GetECSServiceRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendations-response-nextToken"></a>
 The token to advance to the next page of Amazon ECS service recommendations.
Type: String

## Errors
<a name="API_GetECSServiceRecommendations_Errors"></a>

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
<a name="API_GetECSServiceRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetECSServiceRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetECSServiceRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetECSServiceRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetECSServiceRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetECSServiceRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetECSServiceRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetECSServiceRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetECSServiceRecommendations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetECSServiceRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetECSServiceRecommendations)
