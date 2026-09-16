---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_DeleteScalingPlan.html
---

# DeleteScalingPlan
<a name="API_DeleteScalingPlan"></a>

Deletes the specified scaling plan.

Deleting a scaling plan deletes the underlying [ScalingInstruction](API_ScalingInstruction.md) for all of the scalable resources that are covered by the plan.

If the plan has launched resources or has scaling activities in progress, you must delete those resources separately.

## Request Syntax
<a name="API_DeleteScalingPlan_RequestSyntax"></a>

```
{
   "ScalingPlanName": "{{string}}",
   "ScalingPlanVersion": {{number}}
}
```

## Request Parameters
<a name="API_DeleteScalingPlan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ScalingPlanName](#API_DeleteScalingPlan_RequestSyntax) **   <a name="autoscaling-DeleteScalingPlan-request-ScalingPlanName"></a>
The name of the scaling plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{Print}&&[^|:/]]+`
Required: Yes

 ** [ScalingPlanVersion](#API_DeleteScalingPlan_RequestSyntax) **   <a name="autoscaling-DeleteScalingPlan-request-ScalingPlanVersion"></a>
The version number of the scaling plan. Currently, the only valid value is `1`.
Type: Long
Required: Yes

## Response Elements
<a name="API_DeleteScalingPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteScalingPlan_Errors"></a>

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
<a name="API_DeleteScalingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-plans-2018-01-06/DeleteScalingPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-plans-2018-01-06/DeleteScalingPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/DeleteScalingPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-plans-2018-01-06/DeleteScalingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/DeleteScalingPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-plans-2018-01-06/DeleteScalingPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-plans-2018-01-06/DeleteScalingPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-plans-2018-01-06/DeleteScalingPlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-plans-2018-01-06/DeleteScalingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/DeleteScalingPlan)
