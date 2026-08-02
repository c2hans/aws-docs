---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_PreviewResult.html
---

# PreviewResult
<a name="API_automation_PreviewResult"></a>

Contains the results of previewing an automation rule against available recommendations.

## Contents
<a name="API_automation_PreviewResult_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-automation_PreviewResult-accountId"></a>
The AWS account ID associated with the resource.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** currentResourceDetails **   <a name="computeoptimizer-Type-automation_PreviewResult-currentResourceDetails"></a>
Detailed configuration information for a specific AWS resource, with type-specific details.
Type: [ResourceDetails](API_automation_ResourceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** currentResourceSummary **   <a name="computeoptimizer-Type-automation_PreviewResult-currentResourceSummary"></a>
A summary of the resource's current configuration.
Type: String
Required: No

 ** estimatedMonthlySavings **   <a name="computeoptimizer-Type-automation_PreviewResult-estimatedMonthlySavings"></a>
 Contains information about estimated monthly cost savings.
Type: [EstimatedMonthlySavings](API_automation_EstimatedMonthlySavings.md) object
Required: No

 ** lookBackPeriodInDays **   <a name="computeoptimizer-Type-automation_PreviewResult-lookBackPeriodInDays"></a>
The number of days of historical data used to analyze the resource.
Type: Integer
Required: No

 ** recommendedActionId **   <a name="computeoptimizer-Type-automation_PreviewResult-recommendedActionId"></a>
The ID of the recommended action being previewed.
Type: String
Pattern: `[0-9A-Za-z]{16}`
Required: No

 ** recommendedActionType **   <a name="computeoptimizer-Type-automation_PreviewResult-recommendedActionType"></a>
The type of recommended action being previewed.
Type: String
Valid Values: `SnapshotAndDeleteUnattachedEbsVolume | UpgradeEbsVolumeType`
Required: No

 ** recommendedResourceDetails **   <a name="computeoptimizer-Type-automation_PreviewResult-recommendedResourceDetails"></a>
Detailed configuration information for a specific AWS resource, with type-specific details.
Type: [ResourceDetails](API_automation_ResourceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** recommendedResourceSummary **   <a name="computeoptimizer-Type-automation_PreviewResult-recommendedResourceSummary"></a>
A summary of the resource's recommended configuration.
Type: String
Required: No

 ** region **   <a name="computeoptimizer-Type-automation_PreviewResult-region"></a>
The AWS Region where the resource is located.
Type: String
Required: No

 ** resourceArn **   <a name="computeoptimizer-Type-automation_PreviewResult-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource affected by the recommended action.
Type: String
Pattern: `arn:aws[a-z0-9-]*:[a-z0-9-]+:[a-z0-9-]*:[0-9]{0,12}:[a-zA-Z0-9/_.-]+`
Required: No

 ** resourceId **   <a name="computeoptimizer-Type-automation_PreviewResult-resourceId"></a>
The ID of the resource affected by the recommended action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** resourceTags **   <a name="computeoptimizer-Type-automation_PreviewResult-resourceTags"></a>
The tags associated with the resource.
Type: Array of [Tag](API_automation_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** resourceType **   <a name="computeoptimizer-Type-automation_PreviewResult-resourceType"></a>
The type of resource being evaluated.
Type: String
Valid Values: `EbsVolume`
Required: No

 ** restartNeeded **   <a name="computeoptimizer-Type-automation_PreviewResult-restartNeeded"></a>
Indicates whether implementing the recommended action requires a resource restart.
Type: Boolean
Required: No

## See Also
<a name="API_automation_PreviewResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/PreviewResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/PreviewResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/PreviewResult)
