---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_UpdateScalingPlan.html
---

# UpdateScalingPlan
<a name="API_UpdateScalingPlan"></a>

Updates the specified scaling plan.

You cannot update a scaling plan if it is in the process of being created, updated, or deleted.

## Request Syntax
<a name="API_UpdateScalingPlan_RequestSyntax"></a>

```
{
   "ApplicationSource": {
      "CloudFormationStackARN": "{{string}}",
      "TagFilters": [
         {
            "Key": "{{string}}",
            "Values": [ "{{string}}" ]
         }
      ]
   },
   "ScalingInstructions": [
      {
         "CustomizedLoadMetricSpecification": {
            "Dimensions": [
               {
                  "Name": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "MetricName": "{{string}}",
            "Namespace": "{{string}}",
            "Statistic": "{{string}}",
            "Unit": "{{string}}"
         },
         "DisableDynamicScaling": {{boolean}},
         "MaxCapacity": {{number}},
         "MinCapacity": {{number}},
         "PredefinedLoadMetricSpecification": {
            "PredefinedLoadMetricType": "{{string}}",
            "ResourceLabel": "{{string}}"
         },
         "PredictiveScalingMaxCapacityBehavior": "{{string}}",
         "PredictiveScalingMaxCapacityBuffer": {{number}},
         "PredictiveScalingMode": "{{string}}",
         "ResourceId": "{{string}}",
         "ScalableDimension": "{{string}}",
         "ScalingPolicyUpdateBehavior": "{{string}}",
         "ScheduledActionBufferTime": {{number}},
         "ServiceNamespace": "{{string}}",
         "TargetTrackingConfigurations": [
            {
               "CustomizedScalingMetricSpecification": {
                  "Dimensions": [
                     {
                        "Name": "{{string}}",
                        "Value": "{{string}}"
                     }
                  ],
                  "MetricName": "{{string}}",
                  "Namespace": "{{string}}",
                  "Statistic": "{{string}}",
                  "Unit": "{{string}}"
               },
               "DisableScaleIn": {{boolean}},
               "EstimatedInstanceWarmup": {{number}},
               "PredefinedScalingMetricSpecification": {
                  "PredefinedScalingMetricType": "{{string}}",
                  "ResourceLabel": "{{string}}"
               },
               "ScaleInCooldown": {{number}},
               "ScaleOutCooldown": {{number}},
               "TargetValue": {{number}}
            }
         ]
      }
   ],
   "ScalingPlanName": "{{string}}",
   "ScalingPlanVersion": {{number}}
}
```

## Request Parameters
<a name="API_UpdateScalingPlan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationSource](#API_UpdateScalingPlan_RequestSyntax) **   <a name="autoscaling-UpdateScalingPlan-request-ApplicationSource"></a>
A CloudFormation stack or set of tags.
Type: [ApplicationSource](API_ApplicationSource.md) object
Required: No

 ** [ScalingInstructions](#API_UpdateScalingPlan_RequestSyntax) **   <a name="autoscaling-UpdateScalingPlan-request-ScalingInstructions"></a>
The scaling instructions.
Type: Array of [ScalingInstruction](API_ScalingInstruction.md) objects
Required: No

 ** [ScalingPlanName](#API_UpdateScalingPlan_RequestSyntax) **   <a name="autoscaling-UpdateScalingPlan-request-ScalingPlanName"></a>
The name of the scaling plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{Print}&&[^|:/]]+`
Required: Yes

 ** [ScalingPlanVersion](#API_UpdateScalingPlan_RequestSyntax) **   <a name="autoscaling-UpdateScalingPlan-request-ScalingPlanVersion"></a>
The version number of the scaling plan. The only valid value is `1`. Currently, you cannot have multiple scaling plan versions.
Type: Long
Required: Yes

## Response Elements
<a name="API_UpdateScalingPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateScalingPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentUpdateException **
Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.
HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an internal error.
HTTP Status Code: 400

 ** ObjectNotFoundException **
The specified object could not be found.
HTTP Status Code: 400

 ** ValidationException **
An exception was thrown for a validation issue. Review the parameters provided.
HTTP Status Code: 400

## See Also
<a name="API_UpdateScalingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-plans-2018-01-06/UpdateScalingPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-plans-2018-01-06/UpdateScalingPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/UpdateScalingPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-plans-2018-01-06/UpdateScalingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/UpdateScalingPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-plans-2018-01-06/UpdateScalingPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-plans-2018-01-06/UpdateScalingPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-plans-2018-01-06/UpdateScalingPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-plans-2018-01-06/UpdateScalingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/UpdateScalingPlan)
