---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_CreateScalingPlan.html
---

# CreateScalingPlan
<a name="API_CreateScalingPlan"></a>

Creates a scaling plan.

## Request Syntax
<a name="API_CreateScalingPlan_RequestSyntax"></a>

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
   "ScalingPlanName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateScalingPlan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationSource](#API_CreateScalingPlan_RequestSyntax) **   <a name="autoscaling-CreateScalingPlan-request-ApplicationSource"></a>
A CloudFormation stack or set of tags. You can create one scaling plan per application source.
Type: [ApplicationSource](API_ApplicationSource.md) object
Required: Yes

 ** [ScalingInstructions](#API_CreateScalingPlan_RequestSyntax) **   <a name="autoscaling-CreateScalingPlan-request-ScalingInstructions"></a>
The scaling instructions.
Type: Array of [ScalingInstruction](API_ScalingInstruction.md) objects
Required: Yes

 ** [ScalingPlanName](#API_CreateScalingPlan_RequestSyntax) **   <a name="autoscaling-CreateScalingPlan-request-ScalingPlanName"></a>
The name of the scaling plan. Names cannot contain vertical bars, colons, or forward slashes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{Print}&&[^|:/]]+`
Required: Yes

## Response Syntax
<a name="API_CreateScalingPlan_ResponseSyntax"></a>

```
{
   "ScalingPlanVersion": number
}
```

## Response Elements
<a name="API_CreateScalingPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ScalingPlanVersion](#API_CreateScalingPlan_ResponseSyntax) **   <a name="autoscaling-CreateScalingPlan-response-ScalingPlanVersion"></a>
The version number of the scaling plan. This value is always `1`. Currently, you cannot have multiple scaling plan versions.
Type: Long

## Errors
<a name="API_CreateScalingPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentUpdateException **
Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.
HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an internal error.
HTTP Status Code: 400

 ** LimitExceededException **
Your account exceeded a limit. This exception is thrown when a per-account resource limit is exceeded.
HTTP Status Code: 400

 ** ValidationException **
An exception was thrown for a validation issue. Review the parameters provided.
HTTP Status Code: 400

## See Also
<a name="API_CreateScalingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-plans-2018-01-06/CreateScalingPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-plans-2018-01-06/CreateScalingPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/CreateScalingPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-plans-2018-01-06/CreateScalingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/CreateScalingPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-plans-2018-01-06/CreateScalingPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-plans-2018-01-06/CreateScalingPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-plans-2018-01-06/CreateScalingPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-plans-2018-01-06/CreateScalingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/CreateScalingPlan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
