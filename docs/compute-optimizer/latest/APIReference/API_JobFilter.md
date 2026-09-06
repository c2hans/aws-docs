---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_JobFilter.html
---

# JobFilter
<a name="API_JobFilter"></a>

Describes a filter that returns a more specific list of recommendation export jobs. Use this filter with the [DescribeRecommendationExportJobs](API_DescribeRecommendationExportJobs.md) action.

You can use `EBSFilter` with the [GetEBSVolumeRecommendations](API_GetEBSVolumeRecommendations.md) action, `LambdaFunctionRecommendationFilter` with the [GetLambdaFunctionRecommendations](API_GetLambdaFunctionRecommendations.md) action, and `Filter` with the [GetAutoScalingGroupRecommendations](API_GetAutoScalingGroupRecommendations.md) and [GetEC2InstanceRecommendations](API_GetEC2InstanceRecommendations.md) actions.

## Contents
<a name="API_JobFilter_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-JobFilter-name"></a>
The name of the filter.
Specify `ResourceType` to return export jobs of a specific resource type (for example, `Ec2Instance`).
Specify `JobStatus` to return export jobs with a specific status (e.g, `Complete`).
Type: String
Valid Values: `ResourceType | JobStatus`
Required: No

 ** values **   <a name="computeoptimizer-Type-JobFilter-values"></a>
The value of the filter.
The valid values for this parameter are as follows, depending on what you specify for the `name` parameter:
+ Specify `Ec2Instance` or `AutoScalingGroup` if you specify the `name` parameter as `ResourceType`. There is no filter for EBS volumes because volume recommendations cannot be exported at this time.
+ Specify `Queued`, `InProgress`, `Complete`, or `Failed` if you specify the `name` parameter as `JobStatus`.
Type: Array of strings
Required: No

## See Also
<a name="API_JobFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/JobFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/JobFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/JobFilter)
