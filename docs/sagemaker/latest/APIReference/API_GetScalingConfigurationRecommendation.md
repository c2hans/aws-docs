---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetScalingConfigurationRecommendation.html
---

# GetScalingConfigurationRecommendation
<a name="API_GetScalingConfigurationRecommendation"></a>

Starts an Amazon SageMaker Inference Recommender autoscaling recommendation job. Returns recommendations for autoscaling policies that you can apply to your SageMaker endpoint.

## Request Syntax
<a name="API_GetScalingConfigurationRecommendation_RequestSyntax"></a>

```
{
   "EndpointName": "{{string}}",
   "InferenceRecommendationsJobName": "{{string}}",
   "RecommendationId": "{{string}}",
   "ScalingPolicyObjective": {
      "MaxInvocationsPerMinute": {{number}},
      "MinInvocationsPerMinute": {{number}}
   },
   "TargetCpuUtilizationPerCore": {{number}}
}
```

## Request Parameters
<a name="API_GetScalingConfigurationRecommendation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointName](#API_GetScalingConfigurationRecommendation_RequestSyntax) **   <a name="sagemaker-GetScalingConfigurationRecommendation-request-EndpointName"></a>
The name of an endpoint benchmarked during a previously completed inference recommendation job. This name should come from one of the recommendations returned by the job specified in the `InferenceRecommendationsJobName` field.
Specify either this field or the `RecommendationId` field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [InferenceRecommendationsJobName](#API_GetScalingConfigurationRecommendation_RequestSyntax) **   <a name="sagemaker-GetScalingConfigurationRecommendation-request-InferenceRecommendationsJobName"></a>
The name of a previously completed Inference Recommender job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** [RecommendationId](#API_GetScalingConfigurationRecommendation_RequestSyntax) **   <a name="sagemaker-GetScalingConfigurationRecommendation-request-RecommendationId"></a>
The recommendation ID of a previously completed inference recommendation. This ID should come from one of the recommendations returned by the job specified in the `InferenceRecommendationsJobName` field.
Specify either this field or the `EndpointName` field.
Type: String
Required: No

 ** [ScalingPolicyObjective](#API_GetScalingConfigurationRecommendation_RequestSyntax) **   <a name="sagemaker-GetScalingConfigurationRecommendation-request-ScalingPolicyObjective"></a>
An object where you specify the anticipated traffic pattern for an endpoint.
Type: [ScalingPolicyObjective](API_ScalingPolicyObjective.md) object
Required: No

 ** [TargetCpuUtilizationPerCore](#API_GetScalingConfigurationRecommendation_RequestSyntax) **   <a name="sagemaker-GetScalingConfigurationRecommendation-request-TargetCpuUtilizationPerCore"></a>
The percentage of how much utilization you want an instance to use before autoscaling. The default value is 50%.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## Response Syntax
<a name="API_GetScalingConfigurationRecommendation_ResponseSyntax"></a>

```
{
   "DynamicScalingConfiguration": {
      "MaxCapacity": number,
      "MinCapacity": number,
      "ScaleInCooldown": number,
      "ScaleOutCooldown": number,
      "ScalingPolicies": [
         { ... }
      ]
   },
   "EndpointName": "string",
   "InferenceRecommendationsJobName": "string",
   "Metric": {
      "InvocationsPerInstance": number,
      "ModelLatency": number
   },
   "RecommendationId": "string",
   "ScalingPolicyObjective": {
      "MaxInvocationsPerMinute": number,
      "MinInvocationsPerMinute": number
   },
   "TargetCpuUtilizationPerCore": number
}
```

## Response Elements
<a name="API_GetScalingConfigurationRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DynamicScalingConfiguration](#API_GetScalingConfigurationRecommendation_ResponseSyntax) **   <a name="sagemaker-GetScalingConfigurationRecommendation-response-DynamicScalingConfiguration"></a>
An object with the recommended values for you to specify when creating an autoscaling policy.
Type: [DynamicScalingConfiguration](API_DynamicScalingConfiguration.md) object

 ** [EndpointName](#API_GetScalingConfigurationRecommendation_ResponseSyntax) **   <a name="sagemaker-GetScalingConfigurationRecommendation-response-EndpointName"></a>
The name of an endpoint benchmarked during a previously completed Inference Recommender job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [InferenceRecommendationsJobName](#API_GetScalingConfigurationRecommendation_ResponseSyntax) **   <a name="sagemaker-GetScalingConfigurationRecommendation-response-InferenceRecommendationsJobName"></a>
The name of a previously completed Inference Recommender job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`

 ** [Metric](#API_GetScalingConfigurationRecommendation_ResponseSyntax) **   <a name="sagemaker-GetScalingConfigurationRecommendation-response-Metric"></a>
An object with a list of metrics that were benchmarked during the previously completed Inference Recommender job.
Type: [ScalingPolicyMetric](API_ScalingPolicyMetric.md) object

 ** [RecommendationId](#API_GetScalingConfigurationRecommendation_ResponseSyntax) **   <a name="sagemaker-GetScalingConfigurationRecommendation-response-RecommendationId"></a>
The recommendation ID of a previously completed inference recommendation.
Type: String

 ** [ScalingPolicyObjective](#API_GetScalingConfigurationRecommendation_ResponseSyntax) **   <a name="sagemaker-GetScalingConfigurationRecommendation-response-ScalingPolicyObjective"></a>
An object representing the anticipated traffic pattern for an endpoint that you specified in the request.
Type: [ScalingPolicyObjective](API_ScalingPolicyObjective.md) object

 ** [TargetCpuUtilizationPerCore](#API_GetScalingConfigurationRecommendation_ResponseSyntax) **   <a name="sagemaker-GetScalingConfigurationRecommendation-response-TargetCpuUtilizationPerCore"></a>
The percentage of how much utilization you want an instance to use before autoscaling, which you specified in the request. The default value is 50%.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.

## Errors
<a name="API_GetScalingConfigurationRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_GetScalingConfigurationRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/GetScalingConfigurationRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/GetScalingConfigurationRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/GetScalingConfigurationRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/GetScalingConfigurationRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/GetScalingConfigurationRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/GetScalingConfigurationRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/GetScalingConfigurationRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/GetScalingConfigurationRecommendation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/GetScalingConfigurationRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/GetScalingConfigurationRecommendation)
