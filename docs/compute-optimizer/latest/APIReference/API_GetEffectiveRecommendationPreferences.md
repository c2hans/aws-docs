---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEffectiveRecommendationPreferences.html
---

# GetEffectiveRecommendationPreferences
<a name="API_GetEffectiveRecommendationPreferences"></a>

Returns the recommendation preferences that are in effect for a given resource, such as enhanced infrastructure metrics. Considers all applicable preferences that you might have set at the resource, account, and organization level.

When you create a recommendation preference, you can set its status to `Active` or `Inactive`. Use this action to view the recommendation preferences that are in effect, or `Active`.

## Request Syntax
<a name="API_GetEffectiveRecommendationPreferences_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetEffectiveRecommendationPreferences_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceArn](#API_GetEffectiveRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-GetEffectiveRecommendationPreferences-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource for which to confirm effective recommendation preferences. Only EC2 instance and Auto Scaling group ARNs are currently supported.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetEffectiveRecommendationPreferences_ResponseSyntax"></a>

```
{
   "enhancedInfrastructureMetrics": "string",
   "externalMetricsPreference": {
      "source": "string"
   },
   "lookBackPeriod": "string",
   "preferredResources": [
      {
         "effectiveIncludeList": [ "string" ],
         "excludeList": [ "string" ],
         "includeList": [ "string" ],
         "name": "string"
      }
   ],
   "utilizationPreferences": [
      {
         "metricName": "string",
         "metricParameters": {
            "headroom": "string",
            "threshold": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetEffectiveRecommendationPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [enhancedInfrastructureMetrics](#API_GetEffectiveRecommendationPreferences_ResponseSyntax) **   <a name="computeoptimizer-GetEffectiveRecommendationPreferences-response-enhancedInfrastructureMetrics"></a>
The status of the enhanced infrastructure metrics recommendation preference. Considers all applicable preferences that you might have set at the resource, account, and organization level.
A status of `Active` confirms that the preference is applied in the latest recommendation refresh, and a status of `Inactive` confirms that it's not yet applied to recommendations.
To validate whether the preference is applied to your last generated set of recommendations, review the `effectiveRecommendationPreferences` value in the response of the [GetAutoScalingGroupRecommendations](API_GetAutoScalingGroupRecommendations.md) and [GetEC2InstanceRecommendations](API_GetEC2InstanceRecommendations.md) actions.
For more information, see [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.
Type: String
Valid Values: `Active | Inactive`

 ** [externalMetricsPreference](#API_GetEffectiveRecommendationPreferences_ResponseSyntax) **   <a name="computeoptimizer-GetEffectiveRecommendationPreferences-response-externalMetricsPreference"></a>
The provider of the external metrics recommendation preference. Considers all applicable preferences that you might have set at the account and organization level.
If the preference is applied in the latest recommendation refresh, an object with a valid `source` value appears in the response. If the preference isn't applied to the recommendations already, then this object doesn't appear in the response.
To validate whether the preference is applied to your last generated set of recommendations, review the `effectiveRecommendationPreferences` value in the response of the [GetEC2InstanceRecommendations](API_GetEC2InstanceRecommendations.md) actions.
For more information, see [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion.html) in the * AWS Compute Optimizer User Guide*.
Type: [ExternalMetricsPreference](API_ExternalMetricsPreference.md) object

 ** [lookBackPeriod](#API_GetEffectiveRecommendationPreferences_ResponseSyntax) **   <a name="computeoptimizer-GetEffectiveRecommendationPreferences-response-lookBackPeriod"></a>
 The number of days the utilization metrics of the AWS resource are analyzed.
To validate that the preference is applied to your last generated set of recommendations, review the `effectiveRecommendationPreferences` value in the response of the GetAutoScalingGroupRecommendations, GetEC2InstanceRecommendations, GetEBSVolumeRecommendations, GetECSServiceRecommendations, or GetRDSDatabaseRecommendations actions.
Type: String
Valid Values: `DAYS_14 | DAYS_32 | DAYS_93`

 ** [preferredResources](#API_GetEffectiveRecommendationPreferences_ResponseSyntax) **   <a name="computeoptimizer-GetEffectiveRecommendationPreferences-response-preferredResources"></a>
 The resource type values that are considered as candidates when generating rightsizing recommendations. This object resolves any wildcard expressions and returns the effective list of candidate resource type values. It also considers all applicable preferences that you set at the resource, account, and organization level.
To validate that the preference is applied to your last generated set of recommendations, review the `effectiveRecommendationPreferences` value in the response of the GetAutoScalingGroupRecommendations or GetEC2InstanceRecommendations actions.
Type: Array of [EffectivePreferredResource](API_EffectivePreferredResource.md) objects

 ** [utilizationPreferences](#API_GetEffectiveRecommendationPreferences_ResponseSyntax) **   <a name="computeoptimizer-GetEffectiveRecommendationPreferences-response-utilizationPreferences"></a>
 The resource’s CPU and memory utilization preferences, such as threshold and headroom, that were used to generate rightsizing recommendations. It considers all applicable preferences that you set at the resource, account, and organization level.
To validate that the preference is applied to your last generated set of recommendations, review the `effectiveRecommendationPreferences` value in the response of the GetAutoScalingGroupRecommendations or GetEC2InstanceRecommendations actions.
Type: Array of [UtilizationPreference](API_UtilizationPreference.md) objects

## Errors
<a name="API_GetEffectiveRecommendationPreferences_Errors"></a>

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
<a name="API_GetEffectiveRecommendationPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetEffectiveRecommendationPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetEffectiveRecommendationPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetEffectiveRecommendationPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetEffectiveRecommendationPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetEffectiveRecommendationPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetEffectiveRecommendationPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetEffectiveRecommendationPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetEffectiveRecommendationPreferences)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetEffectiveRecommendationPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetEffectiveRecommendationPreferences)
