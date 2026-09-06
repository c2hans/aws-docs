---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRDSDatabaseRecommendationProjectedMetrics.html
---

# GetRDSDatabaseRecommendationProjectedMetrics
<a name="API_GetRDSDatabaseRecommendationProjectedMetrics"></a>

 Returns the projected metrics of Aurora and RDS database recommendations.

## Request Syntax
<a name="API_GetRDSDatabaseRecommendationProjectedMetrics_RequestSyntax"></a>

```
{
   "endTime": {{number}},
   "period": {{number}},
   "recommendationPreferences": {
      "cpuVendorArchitectures": [ "{{string}}" ]
   },
   "resourceArn": "{{string}}",
   "startTime": {{number}},
   "stat": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRDSDatabaseRecommendationProjectedMetrics_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTime](#API_GetRDSDatabaseRecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendationProjectedMetrics-request-endTime"></a>
 The timestamp of the last projected metrics data point to return.
Type: Timestamp
Required: Yes

 ** [period](#API_GetRDSDatabaseRecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendationProjectedMetrics-request-period"></a>
 The granularity, in seconds, of the projected metrics data points.
Type: Integer
Required: Yes

 ** [recommendationPreferences](#API_GetRDSDatabaseRecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendationProjectedMetrics-request-recommendationPreferences"></a>
Describes the recommendation preferences to return in the response of a [GetAutoScalingGroupRecommendations](API_GetAutoScalingGroupRecommendations.md), [GetEC2InstanceRecommendations](API_GetEC2InstanceRecommendations.md), [GetEC2RecommendationProjectedMetrics](API_GetEC2RecommendationProjectedMetrics.md), [GetRDSDatabaseRecommendations](API_GetRDSDatabaseRecommendations.md), and [GetRDSDatabaseRecommendationProjectedMetrics](#API_GetRDSDatabaseRecommendationProjectedMetrics) request.
Type: [RecommendationPreferences](API_RecommendationPreferences.md) object
Required: No

 ** [resourceArn](#API_GetRDSDatabaseRecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendationProjectedMetrics-request-resourceArn"></a>
 The ARN that identifies the Amazon Aurora or RDS database.
 The following is the format of the ARN:
 `arn:aws:rds:{region}:{accountId}:db:{resourceName}`
Type: String
Required: Yes

 ** [startTime](#API_GetRDSDatabaseRecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendationProjectedMetrics-request-startTime"></a>
 The timestamp of the first projected metrics data point to return.
Type: Timestamp
Required: Yes

 ** [stat](#API_GetRDSDatabaseRecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendationProjectedMetrics-request-stat"></a>
 The statistic of the projected metrics.
Type: String
Valid Values: `Maximum | Average`
Required: Yes

## Response Syntax
<a name="API_GetRDSDatabaseRecommendationProjectedMetrics_ResponseSyntax"></a>

```
{
   "recommendedOptionProjectedMetrics": [
      {
         "projectedMetrics": [
            {
               "name": "string",
               "timestamps": [ number ],
               "values": [ number ]
            }
         ],
         "rank": number,
         "recommendedDBInstanceClass": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetRDSDatabaseRecommendationProjectedMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recommendedOptionProjectedMetrics](#API_GetRDSDatabaseRecommendationProjectedMetrics_ResponseSyntax) **   <a name="computeoptimizer-GetRDSDatabaseRecommendationProjectedMetrics-response-recommendedOptionProjectedMetrics"></a>
 An array of objects that describes the projected metrics.
Type: Array of [RDSDatabaseRecommendedOptionProjectedMetric](API_RDSDatabaseRecommendedOptionProjectedMetric.md) objects

## Errors
<a name="API_GetRDSDatabaseRecommendationProjectedMetrics_Errors"></a>

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
<a name="API_GetRDSDatabaseRecommendationProjectedMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendationProjectedMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendationProjectedMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendationProjectedMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendationProjectedMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendationProjectedMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendationProjectedMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendationProjectedMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendationProjectedMetrics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendationProjectedMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetRDSDatabaseRecommendationProjectedMetrics)
