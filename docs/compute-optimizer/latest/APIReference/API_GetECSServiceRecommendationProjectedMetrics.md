---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetECSServiceRecommendationProjectedMetrics.html
---

# GetECSServiceRecommendationProjectedMetrics
<a name="API_GetECSServiceRecommendationProjectedMetrics"></a>

 Returns the projected metrics of Amazon ECS service recommendations.

## Request Syntax
<a name="API_GetECSServiceRecommendationProjectedMetrics_RequestSyntax"></a>

```
{
   "endTime": {{number}},
   "period": {{number}},
   "serviceArn": "{{string}}",
   "startTime": {{number}},
   "stat": "{{string}}"
}
```

## Request Parameters
<a name="API_GetECSServiceRecommendationProjectedMetrics_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTime](#API_GetECSServiceRecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendationProjectedMetrics-request-endTime"></a>
 The timestamp of the last projected metrics data point to return.
Type: Timestamp
Required: Yes

 ** [period](#API_GetECSServiceRecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendationProjectedMetrics-request-period"></a>
 The granularity, in seconds, of the projected metrics data points.
Type: Integer
Required: Yes

 ** [serviceArn](#API_GetECSServiceRecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendationProjectedMetrics-request-serviceArn"></a>
 The ARN that identifies the Amazon ECS service.
 The following is the format of the ARN:
 `arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name`
Type: String
Required: Yes

 ** [startTime](#API_GetECSServiceRecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendationProjectedMetrics-request-startTime"></a>
 The timestamp of the first projected metrics data point to return.
Type: Timestamp
Required: Yes

 ** [stat](#API_GetECSServiceRecommendationProjectedMetrics_RequestSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendationProjectedMetrics-request-stat"></a>
 The statistic of the projected metrics.
Type: String
Valid Values: `Maximum | Average`
Required: Yes

## Response Syntax
<a name="API_GetECSServiceRecommendationProjectedMetrics_ResponseSyntax"></a>

```
{
   "recommendedOptionProjectedMetrics": [
      {
         "projectedMetrics": [
            {
               "lowerBoundValues": [ number ],
               "name": "string",
               "timestamps": [ number ],
               "upperBoundValues": [ number ]
            }
         ],
         "recommendedCpuUnits": number,
         "recommendedMemorySize": number
      }
   ]
}
```

## Response Elements
<a name="API_GetECSServiceRecommendationProjectedMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recommendedOptionProjectedMetrics](#API_GetECSServiceRecommendationProjectedMetrics_ResponseSyntax) **   <a name="computeoptimizer-GetECSServiceRecommendationProjectedMetrics-response-recommendedOptionProjectedMetrics"></a>
 An array of objects that describes the projected metrics.
Type: Array of [ECSServiceRecommendedOptionProjectedMetric](API_ECSServiceRecommendedOptionProjectedMetric.md) objects

## Errors
<a name="API_GetECSServiceRecommendationProjectedMetrics_Errors"></a>

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
<a name="API_GetECSServiceRecommendationProjectedMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetECSServiceRecommendationProjectedMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetECSServiceRecommendationProjectedMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetECSServiceRecommendationProjectedMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetECSServiceRecommendationProjectedMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetECSServiceRecommendationProjectedMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetECSServiceRecommendationProjectedMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetECSServiceRecommendationProjectedMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetECSServiceRecommendationProjectedMetrics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetECSServiceRecommendationProjectedMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetECSServiceRecommendationProjectedMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
