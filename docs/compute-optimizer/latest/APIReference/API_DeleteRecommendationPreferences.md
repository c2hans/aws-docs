---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_DeleteRecommendationPreferences.html
---

# DeleteRecommendationPreferences
<a name="API_DeleteRecommendationPreferences"></a>

Deletes a recommendation preference, such as enhanced infrastructure metrics.

For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.

## Request Syntax
<a name="API_DeleteRecommendationPreferences_RequestSyntax"></a>

```
{
   "recommendationPreferenceNames": [ "{{string}}" ],
   "resourceType": "{{string}}",
   "scope": {
      "name": "{{string}}",
      "value": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_DeleteRecommendationPreferences_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [recommendationPreferenceNames](#API_DeleteRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-DeleteRecommendationPreferences-request-recommendationPreferenceNames"></a>
The name of the recommendation preference to delete.
Type: Array of strings
Valid Values: `EnhancedInfrastructureMetrics | InferredWorkloadTypes | ExternalMetricsPreference | LookBackPeriodPreference | PreferredResources | UtilizationPreferences`
Required: Yes

 ** [resourceType](#API_DeleteRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-DeleteRecommendationPreferences-request-resourceType"></a>
The target resource type of the recommendation preference to delete.
The `Ec2Instance` option encompasses standalone instances and instances that are part of Auto Scaling groups. The `AutoScalingGroup` option encompasses only instances that are part of an Auto Scaling group.
Type: String
Valid Values: `Ec2Instance | AutoScalingGroup | EbsVolume | EcsService | RdsDBInstance | AuroraDBClusterStorage`
Required: Yes

 ** [scope](#API_DeleteRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-DeleteRecommendationPreferences-request-scope"></a>
An object that describes the scope of the recommendation preference to delete.
You can delete recommendation preferences that are created at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.
Type: [Scope](API_Scope.md) object
Required: No

## Response Elements
<a name="API_DeleteRecommendationPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteRecommendationPreferences_Errors"></a>

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
<a name="API_DeleteRecommendationPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/DeleteRecommendationPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/DeleteRecommendationPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/DeleteRecommendationPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/DeleteRecommendationPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/DeleteRecommendationPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/DeleteRecommendationPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/DeleteRecommendationPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/DeleteRecommendationPreferences)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/DeleteRecommendationPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/DeleteRecommendationPreferences)
