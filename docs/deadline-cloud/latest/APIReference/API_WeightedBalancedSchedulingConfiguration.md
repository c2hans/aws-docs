---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_WeightedBalancedSchedulingConfiguration.html
---

# WeightedBalancedSchedulingConfiguration
<a name="API_WeightedBalancedSchedulingConfiguration"></a>

Configuration for weighted balanced scheduling. Workers are assigned to jobs based on a weighted formula:

 `weight = (priority * priorityWeight) + (errors * errorWeight) + ((currentTime - submissionTime) * submissionTimeWeight) + ((renderingTasks - renderingTaskBuffer) * renderingTaskWeight)`

The job with the highest calculated weight is scheduled first. Workers are distributed evenly amongst jobs with the same weight.

## Contents
<a name="API_WeightedBalancedSchedulingConfiguration_Contents"></a>

 ** errorWeight **   <a name="deadlinecloud-Type-WeightedBalancedSchedulingConfiguration-errorWeight"></a>
The weight applied to the number of errors on a job. A negative value means jobs without errors are scheduled first. A value of `0` means errors are ignored. The default value is `-10.0`.
Type: Double
Valid Range: Minimum value of -10000. Maximum value of 10000.
Required: No

 ** maxPriorityOverride **   <a name="deadlinecloud-Type-WeightedBalancedSchedulingConfiguration-maxPriorityOverride"></a>
Overrides the weighted scheduling formula for jobs at the maximum priority (100). When set, jobs with priority 100 are always scheduled first regardless of their calculated weight. When absent, maximum priority jobs use the standard weighted formula.
Type: [SchedulingMaxPriorityOverride](API_SchedulingMaxPriorityOverride.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** minPriorityOverride **   <a name="deadlinecloud-Type-WeightedBalancedSchedulingConfiguration-minPriorityOverride"></a>
Overrides the weighted scheduling formula for jobs at the minimum priority (0). When set, jobs with priority 0 are always scheduled last regardless of their calculated weight. When absent, minimum priority jobs use the standard weighted formula.
Type: [SchedulingMinPriorityOverride](API_SchedulingMinPriorityOverride.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** priorityWeight **   <a name="deadlinecloud-Type-WeightedBalancedSchedulingConfiguration-priorityWeight"></a>
The weight applied to job priority in the scheduling formula. Higher values give more influence to job priority. A value of `0` means priority is ignored. The default value is `100.0`.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** renderingTaskBuffer **   <a name="deadlinecloud-Type-WeightedBalancedSchedulingConfiguration-renderingTaskBuffer"></a>
The rendering task buffer is subtracted from the number of rendering tasks before applying the rendering task weight. This creates a stickiness effect where workers prefer to stay with their current job. Higher values make workers stickier. The default value is `1`. The buffer is only applied in the weight calculation for a job if the worker is currently assigned to that job.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** renderingTaskWeight **   <a name="deadlinecloud-Type-WeightedBalancedSchedulingConfiguration-renderingTaskWeight"></a>
The weight applied to the number of tasks currently rendering on a job. A negative value means jobs that are not already rendering are scheduled next. A value of `0` means the rendering state is ignored. The default value is `-100.0`.
Type: Double
Valid Range: Minimum value of -10000. Maximum value of 10000.
Required: No

 ** submissionTimeWeight **   <a name="deadlinecloud-Type-WeightedBalancedSchedulingConfiguration-submissionTimeWeight"></a>
The weight applied to job submission time. A positive value means earlier jobs are scheduled first. A value of `0` means submission time is ignored. The default value is `3.0`.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

## See Also
<a name="API_WeightedBalancedSchedulingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WeightedBalancedSchedulingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WeightedBalancedSchedulingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WeightedBalancedSchedulingConfiguration)
