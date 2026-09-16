---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_DescribeScalingPlans.html
---

# DescribeScalingPlans
<a name="API_DescribeScalingPlans"></a>

Describes one or more of your scaling plans.

## Request Syntax
<a name="API_DescribeScalingPlans_RequestSyntax"></a>

```
{
   "ApplicationSources": [
      {
         "CloudFormationStackARN": "{{string}}",
         "TagFilters": [
            {
               "Key": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ScalingPlanNames": [ "{{string}}" ],
   "ScalingPlanVersion": {{number}}
}
```

## Request Parameters
<a name="API_DescribeScalingPlans_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationSources](#API_DescribeScalingPlans_RequestSyntax) **   <a name="autoscaling-DescribeScalingPlans-request-ApplicationSources"></a>
The sources for the applications (up to 10). If you specify scaling plan names, you cannot specify application sources.
Type: Array of [ApplicationSource](API_ApplicationSource.md) objects
Required: No

 ** [MaxResults](#API_DescribeScalingPlans_RequestSyntax) **   <a name="autoscaling-DescribeScalingPlans-request-MaxResults"></a>
The maximum number of scalable resources to return. This value can be between 1 and 50. The default value is 50.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeScalingPlans_RequestSyntax) **   <a name="autoscaling-DescribeScalingPlans-request-NextToken"></a>
The token for the next set of results.
Type: String
Required: No

 ** [ScalingPlanNames](#API_DescribeScalingPlans_RequestSyntax) **   <a name="autoscaling-DescribeScalingPlans-request-ScalingPlanNames"></a>
The names of the scaling plans (up to 10). If you specify application sources, you cannot specify scaling plan names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{Print}&&[^|:/]]+`
Required: No

 ** [ScalingPlanVersion](#API_DescribeScalingPlans_RequestSyntax) **   <a name="autoscaling-DescribeScalingPlans-request-ScalingPlanVersion"></a>
The version number of the scaling plan. Currently, the only valid value is `1`.
If you specify a scaling plan version, you must also specify a scaling plan name.
Type: Long
Required: No

## Response Syntax
<a name="API_DescribeScalingPlans_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ScalingPlans": [
      {
         "ApplicationSource": {
            "CloudFormationStackARN": "string",
            "TagFilters": [
               {
                  "Key": "string",
                  "Values": [ "string" ]
               }
            ]
         },
         "CreationTime": number,
         "ScalingInstructions": [
            {
               "CustomizedLoadMetricSpecification": {
                  "Dimensions": [
                     {
                        "Name": "string",
                        "Value": "string"
                     }
                  ],
                  "MetricName": "string",
                  "Namespace": "string",
                  "Statistic": "string",
                  "Unit": "string"
               },
               "DisableDynamicScaling": boolean,
               "MaxCapacity": number,
               "MinCapacity": number,
               "PredefinedLoadMetricSpecification": {
                  "PredefinedLoadMetricType": "string",
                  "ResourceLabel": "string"
               },
               "PredictiveScalingMaxCapacityBehavior": "string",
               "PredictiveScalingMaxCapacityBuffer": number,
               "PredictiveScalingMode": "string",
               "ResourceId": "string",
               "ScalableDimension": "string",
               "ScalingPolicyUpdateBehavior": "string",
               "ScheduledActionBufferTime": number,
               "ServiceNamespace": "string",
               "TargetTrackingConfigurations": [
                  {
                     "CustomizedScalingMetricSpecification": {
                        "Dimensions": [
                           {
                              "Name": "string",
                              "Value": "string"
                           }
                        ],
                        "MetricName": "string",
                        "Namespace": "string",
                        "Statistic": "string",
                        "Unit": "string"
                     },
                     "DisableScaleIn": boolean,
                     "EstimatedInstanceWarmup": number,
                     "PredefinedScalingMetricSpecification": {
                        "PredefinedScalingMetricType": "string",
                        "ResourceLabel": "string"
                     },
                     "ScaleInCooldown": number,
                     "ScaleOutCooldown": number,
                     "TargetValue": number
                  }
               ]
            }
         ],
         "ScalingPlanName": "string",
         "ScalingPlanVersion": number,
         "StatusCode": "string",
         "StatusMessage": "string",
         "StatusStartTime": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribeScalingPlans_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeScalingPlans_ResponseSyntax) **   <a name="autoscaling-DescribeScalingPlans-response-NextToken"></a>
The token required to get the next set of results. This value is `null` if there are no more results to return.
Type: String

 ** [ScalingPlans](#API_DescribeScalingPlans_ResponseSyntax) **   <a name="autoscaling-DescribeScalingPlans-response-ScalingPlans"></a>
Information about the scaling plans.
Type: Array of [ScalingPlan](API_ScalingPlan.md) objects

## Errors
<a name="API_DescribeScalingPlans_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentUpdateException **
Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.
HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an internal error.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The token provided is not valid.
HTTP Status Code: 400

 ** ValidationException **
An exception was thrown for a validation issue. Review the parameters provided.
HTTP Status Code: 400

## See Also
<a name="API_DescribeScalingPlans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-plans-2018-01-06/DescribeScalingPlans)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-plans-2018-01-06/DescribeScalingPlans)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/DescribeScalingPlans)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-plans-2018-01-06/DescribeScalingPlans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/DescribeScalingPlans)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-plans-2018-01-06/DescribeScalingPlans)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-plans-2018-01-06/DescribeScalingPlans)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-plans-2018-01-06/DescribeScalingPlans)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-plans-2018-01-06/DescribeScalingPlans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/DescribeScalingPlans)
