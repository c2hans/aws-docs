---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_PriorityBalancedSchedulingConfiguration.html
---

# PriorityBalancedSchedulingConfiguration
<a name="API_PriorityBalancedSchedulingConfiguration"></a>

Configuration for priority balanced scheduling. Workers are distributed evenly across all jobs at the highest priority level.

## Contents
<a name="API_PriorityBalancedSchedulingConfiguration_Contents"></a>

 ** renderingTaskBuffer **   <a name="deadlinecloud-Type-PriorityBalancedSchedulingConfiguration-renderingTaskBuffer"></a>
The rendering task buffer controls worker stickiness. A worker only switches from its current job to another job at the same priority if the other job has fewer rendering tasks by more than this buffer value. Higher values make workers stickier to their current jobs. The default value is `1`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

## See Also
<a name="API_PriorityBalancedSchedulingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/PriorityBalancedSchedulingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/PriorityBalancedSchedulingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/PriorityBalancedSchedulingConfiguration)
