---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_DescribeScalingPlanResources.html
---

# DescribeScalingPlanResources
<a name="API_DescribeScalingPlanResources"></a>

Describes the scalable resources in the specified scaling plan.

## Request Syntax
<a name="API_DescribeScalingPlanResources_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ScalingPlanName": "{{string}}",
   "ScalingPlanVersion": {{number}}
}
```

## Request Parameters
<a name="API_DescribeScalingPlanResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeScalingPlanResources_RequestSyntax) **   <a name="autoscaling-DescribeScalingPlanResources-request-MaxResults"></a>
The maximum number of scalable resources to return. The value must be between 1 and 50. The default value is 50.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeScalingPlanResources_RequestSyntax) **   <a name="autoscaling-DescribeScalingPlanResources-request-NextToken"></a>
The token for the next set of results.
Type: String
Required: No

 ** [ScalingPlanName](#API_DescribeScalingPlanResources_RequestSyntax) **   <a name="autoscaling-DescribeScalingPlanResources-request-ScalingPlanName"></a>
The name of the scaling plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{Print}&&[^|:/]]+`
Required: Yes

 ** [ScalingPlanVersion](#API_DescribeScalingPlanResources_RequestSyntax) **   <a name="autoscaling-DescribeScalingPlanResources-request-ScalingPlanVersion"></a>
The version number of the scaling plan. Currently, the only valid value is `1`.
Type: Long
Required: Yes

## Response Syntax
<a name="API_DescribeScalingPlanResources_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ScalingPlanResources": [
      {
         "ResourceId": "string",
         "ScalableDimension": "string",
         "ScalingPlanName": "string",
         "ScalingPlanVersion": number,
         "ScalingPolicies": [
            {
               "PolicyName": "string",
               "PolicyType": "string",
               "TargetTrackingConfiguration": {
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
            }
         ],
         "ScalingStatusCode": "string",
         "ScalingStatusMessage": "string",
         "ServiceNamespace": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeScalingPlanResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeScalingPlanResources_ResponseSyntax) **   <a name="autoscaling-DescribeScalingPlanResources-response-NextToken"></a>
The token required to get the next set of results. This value is `null` if there are no more results to return.
Type: String

 ** [ScalingPlanResources](#API_DescribeScalingPlanResources_ResponseSyntax) **   <a name="autoscaling-DescribeScalingPlanResources-response-ScalingPlanResources"></a>
Information about the scalable resources.
Type: Array of [ScalingPlanResource](API_ScalingPlanResource.md) objects

## Errors
<a name="API_DescribeScalingPlanResources_Errors"></a>

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
<a name="API_DescribeScalingPlanResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-plans-2018-01-06/DescribeScalingPlanResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-plans-2018-01-06/DescribeScalingPlanResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/DescribeScalingPlanResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-plans-2018-01-06/DescribeScalingPlanResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/DescribeScalingPlanResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-plans-2018-01-06/DescribeScalingPlanResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-plans-2018-01-06/DescribeScalingPlanResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-plans-2018-01-06/DescribeScalingPlanResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-plans-2018-01-06/DescribeScalingPlanResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/DescribeScalingPlanResources)
