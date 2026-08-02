---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingPlan.html
---

# ScalingPlan
<a name="API_ScalingPlan"></a>

Represents a scaling plan.

## Contents
<a name="API_ScalingPlan_Contents"></a>

 ** ApplicationSource **   <a name="autoscaling-Type-ScalingPlan-ApplicationSource"></a>
A CloudFormation stack or a set of tags. You can create one scaling plan per application source.
Type: [ApplicationSource](API_ApplicationSource.md) object
Required: Yes

 ** ScalingInstructions **   <a name="autoscaling-Type-ScalingPlan-ScalingInstructions"></a>
The scaling instructions.
Type: Array of [ScalingInstruction](API_ScalingInstruction.md) objects
Required: Yes

 ** ScalingPlanName **   <a name="autoscaling-Type-ScalingPlan-ScalingPlanName"></a>
The name of the scaling plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{Print}&&[^|:/]]+`
Required: Yes

 ** ScalingPlanVersion **   <a name="autoscaling-Type-ScalingPlan-ScalingPlanVersion"></a>
The version number of the scaling plan.
Type: Long
Required: Yes

 ** StatusCode **   <a name="autoscaling-Type-ScalingPlan-StatusCode"></a>
The status of the scaling plan.
+  `Active` - The scaling plan is active.
+  `ActiveWithProblems` - The scaling plan is active, but the scaling configuration for one or more resources could not be applied.
+  `CreationInProgress` - The scaling plan is being created.
+  `CreationFailed` - The scaling plan could not be created.
+  `DeletionInProgress` - The scaling plan is being deleted.
+  `DeletionFailed` - The scaling plan could not be deleted.
+  `UpdateInProgress` - The scaling plan is being updated.
+  `UpdateFailed` - The scaling plan could not be updated.
Type: String
Valid Values: `Active | ActiveWithProblems | CreationInProgress | CreationFailed | DeletionInProgress | DeletionFailed | UpdateInProgress | UpdateFailed`
Required: Yes

 ** CreationTime **   <a name="autoscaling-Type-ScalingPlan-CreationTime"></a>
The Unix time stamp when the scaling plan was created.
Type: Timestamp
Required: No

 ** StatusMessage **   <a name="autoscaling-Type-ScalingPlan-StatusMessage"></a>
A simple message about the current status of the scaling plan.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** StatusStartTime **   <a name="autoscaling-Type-ScalingPlan-StatusStartTime"></a>
The Unix time stamp when the scaling plan entered the current status.
Type: Timestamp
Required: No

## See Also
<a name="API_ScalingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/ScalingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/ScalingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/ScalingPlan)
