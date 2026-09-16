---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRDSDatabaseRecommendations.html
---

# GetRDSDatabaseRecommendations
<a name="API_GetRDSDatabaseRecommendations"></a>

 Returns Amazon Aurora and RDS database recommendations.

 AWS Compute Optimizer generates recommendations for Amazon Aurora and RDS databases that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the * AWS Compute Optimizer User Guide*.

## Request Syntax
<a name="API_GetRDSDatabaseRecommendations_RequestSyntax"></a>

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
   "recommendationPreferences": {
      "cpuVendorArchitectures": [ "{{string}}" ]
   },
   "resourceArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetRDSDatabaseRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIds](#API_GetRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendations-request-accountIds"></a>
 Return the Amazon Aurora and RDS database recommendations to the specified AWS account IDs.
If your account is the management account or the delegated administrator of an organization, use this parameter to return the Amazon Aurora and RDS database recommendations to specific member accounts.
You can only specify one account ID per request.
Type: Array of strings
Required: No

 ** [filters](#API_GetRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendations-request-filters"></a>
 An array of objects to specify a filter that returns a more specific list of Amazon Aurora and RDS database recommendations.
Type: Array of [RDSDBRecommendationFilter](API_RDSDBRecommendationFilter.md) objects
Required: No

 ** [maxResults](#API_GetRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendations-request-maxResults"></a>
The maximum number of Amazon Aurora and RDS database recommendations to return with a single request.
To retrieve the remaining results, make another request with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_GetRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendations-request-nextToken"></a>
 The token to advance to the next page of Amazon Aurora and RDS database recommendations.
Type: String
Required: No

 ** [recommendationPreferences](#API_GetRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendations-request-recommendationPreferences"></a>
Describes the recommendation preferences to return in the response of a [GetAutoScalingGroupRecommendations](API_GetAutoScalingGroupRecommendations.md), [GetEC2InstanceRecommendations](API_GetEC2InstanceRecommendations.md), [GetEC2RecommendationProjectedMetrics](API_GetEC2RecommendationProjectedMetrics.md), [GetRDSDatabaseRecommendations](#API_GetRDSDatabaseRecommendations), and [GetRDSDatabaseRecommendationProjectedMetrics](API_GetRDSDatabaseRecommendationProjectedMetrics.md) request.
Type: [RecommendationPreferences](API_RecommendationPreferences.md) object
Required: No

 ** [resourceArns](#API_GetRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendations-request-resourceArns"></a>
 The ARN that identifies the Amazon Aurora or RDS database.
 The following is the format of the ARN:
 `arn:aws:rds:{region}:{accountId}:db:{resourceName}`
 The following is the format of a DB Cluster ARN:
 `arn:aws:rds:{region}:{accountId}:cluster:{resourceName}`
Type: Array of strings
Required: No

## Response Syntax
<a name="API_GetRDSDatabaseRecommendations_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "code": "string",
         "identifier": "string",
         "message": "string"
      }
   ],
   "nextToken": "string",
   "rdsDBRecommendations": [
      {
         "accountId": "string",
         "currentDBInstanceClass": "string",
         "currentInstancePerformanceRisk": "string",
         "currentStorageConfiguration": {
            "allocatedStorage": number,
            "iops": number,
            "maxAllocatedStorage": number,
            "storageThroughput": number,
            "storageType": "string"
         },
         "currentStorageEstimatedMonthlyVolumeIOPsCostVariation": "string",
         "dbClusterIdentifier": "string",
         "effectiveRecommendationPreferences": {
            "cpuVendorArchitectures": [ "string" ],
            "enhancedInfrastructureMetrics": "string",
            "lookBackPeriod": "string",
            "savingsEstimationMode": {
               "source": "string"
            }
         },
         "engine": "string",
         "engineVersion": "string",
         "idle": "string",
         "instanceFinding": "string",
         "instanceFindingReasonCodes": [ "string" ],
         "instanceRecommendationOptions": [
            {
               "dbInstanceClass": "string",
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
         "lastRefreshTimestamp": number,
         "lookbackPeriodInDays": number,
         "promotionTier": number,
         "resourceArn": "string",
         "storageFinding": "string",
         "storageFindingReasonCodes": [ "string" ],
         "storageRecommendationOptions": [
            {
               "estimatedMonthlyVolumeIOPsCostVariation": "string",
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
               },
               "storageConfiguration": {
                  "allocatedStorage": number,
                  "iops": number,
                  "maxAllocatedStorage": number,
                  "storageThroughput": number,
                  "storageType": "string"
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
   ]
}
```

## Response Elements
<a name="API_GetRDSDatabaseRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_GetRDSDatabaseRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendations-response-errors"></a>
 An array of objects that describe errors of the request.
Type: Array of [GetRecommendationError](API_GetRecommendationError.md) objects

 ** [nextToken](#API_GetRDSDatabaseRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendations-response-nextToken"></a>
 The token to advance to the next page of Amazon Aurora and RDS database recommendations.
Type: String

 ** [rdsDBRecommendations](#API_GetRDSDatabaseRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendations-response-rdsDBRecommendations"></a>
 An array of objects that describe the Amazon Aurora and RDS database recommendations.
Type: Array of [RDSDBRecommendation](API_RDSDBRecommendation.md) objects

## Errors
<a name="API_GetRDSDatabaseRecommendations_Errors"></a>

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
<a name="API_GetRDSDatabaseRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendations)
