---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEC2RecommendationProjectedMetrics.html
---

# GetEC2RecommendationProjectedMetrics
<a name="API_GetEC2RecommendationProjectedMetrics"></a>

Returns the projected utilization metrics of Amazon EC2 instance recommendations.

**Note**
The `Cpu` and `Memory` metrics are the only projected utilization metrics returned when you run this action. Additionally, the `Memory` metric is returned only for resources that have the unified CloudWatch agent installed on them. For more information, see [Enabling Memory Utilization with the CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent).

## Request Syntax
<a name="API_GetEC2RecommendationProjectedMetrics_RequestSyntax"></a>

```
{
   "endTime": {{number}},
   "instanceArn": "{{string}}",
   "period": {{number}},
   "recommendationPreferences": {
      "cpuVendorArchitectures": [ "{{string}}" ]
   },
   "startTime": {{number}},
   "stat": "{{string}}"
}
```

## Request Parameters
<a name="API_GetEC2RecommendationProjectedMetrics_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTime](#API_GetEC2RecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetEC2RecommendationProjectedMetrics-request-endTime"></a>
The timestamp of the last projected metrics data point to return.
Type: Timestamp
Required: Yes

 ** [instanceArn](#API_GetEC2RecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetEC2RecommendationProjectedMetrics-request-instanceArn"></a>
The Amazon Resource Name (ARN) of the instances for which to return recommendation projected metrics.
Type: String
Required: Yes

 ** [period](#API_GetEC2RecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetEC2RecommendationProjectedMetrics-request-period"></a>
The granularity, in seconds, of the projected metrics data points.
Type: Integer
Required: Yes

 ** [recommendationPreferences](#API_GetEC2RecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetEC2RecommendationProjectedMetrics-request-recommendationPreferences"></a>
An object to specify the preferences for the Amazon EC2 recommendation projected metrics to return in the response.
Type: [RecommendationPreferences](API_RecommendationPreferences.md) object
Required: No

 ** [startTime](#API_GetEC2RecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetEC2RecommendationProjectedMetrics-request-startTime"></a>
The timestamp of the first projected metrics data point to return.
Type: Timestamp
Required: Yes

 ** [stat](#API_GetEC2RecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetEC2RecommendationProjectedMetrics-request-stat"></a>
The statistic of the projected metrics.
Type: String
Valid Values: `Maximum | Average`
Required: Yes

## Response Syntax
<a name="API_GetEC2RecommendationProjectedMetrics_ResponseSyntax"></a>

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
         "recommendedInstanceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetEC2RecommendationProjectedMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recommendedOptionProjectedMetrics](#API_GetEC2RecommendationProjectedMetrics_ResponseSyntax) **   <a name="computeoptimizer-GetEC2RecommendationProjectedMetrics-response-recommendedOptionProjectedMetrics"></a>
An array of objects that describes projected metrics.
Type: Array of [RecommendedOptionProjectedMetric](API_RecommendedOptionProjectedMetric.md) objects

## Errors
<a name="API_GetEC2RecommendationProjectedMetrics_Errors"></a>

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
<a name="API_GetEC2RecommendationProjectedMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetEC2RecommendationProjectedMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetEC2RecommendationProjectedMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetEC2RecommendationProjectedMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetEC2RecommendationProjectedMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetEC2RecommendationProjectedMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetEC2RecommendationProjectedMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetEC2RecommendationProjectedMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetEC2RecommendationProjectedMetrics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetEC2RecommendationProjectedMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetEC2RecommendationProjectedMetrics)
