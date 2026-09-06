---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_SuspendedState.html
---

# SuspendedState
<a name="API_SuspendedState"></a>

Specifies whether the scaling activities for a scalable target are in a suspended state.

## Contents
<a name="API_SuspendedState_Contents"></a>

 ** DynamicScalingInSuspended **   <a name="autoscaling-Type-SuspendedState-DynamicScalingInSuspended"></a>
Whether scale in by a target tracking scaling policy or a step scaling policy is suspended. Set the value to `true` if you don't want Application Auto Scaling to remove capacity when a scaling policy is triggered. The default is `false`.
Type: Boolean
Required: No

 ** DynamicScalingOutSuspended **   <a name="autoscaling-Type-SuspendedState-DynamicScalingOutSuspended"></a>
Whether scale out by a target tracking scaling policy or a step scaling policy is suspended. Set the value to `true` if you don't want Application Auto Scaling to add capacity when a scaling policy is triggered. The default is `false`.
Type: Boolean
Required: No

 ** ScheduledScalingSuspended **   <a name="autoscaling-Type-SuspendedState-ScheduledScalingSuspended"></a>
Whether scheduled scaling is suspended. Set the value to `true` if you don't want Application Auto Scaling to add or remove capacity by initiating scheduled actions. The default is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_SuspendedState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/SuspendedState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/SuspendedState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/SuspendedState)
