---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_RecommendedActionFilter.html
---

# RecommendedActionFilter

A filter used to narrow down recommended action results based on specific criteria. If a filter has more than one value, a recommended action matches the filter when it matches any of the values. If you specify more than one filter, a recommended action must match all of the filters.

## Contents
<a name="API_automation_RecommendedActionFilter_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-automation_RecommendedActionFilter-name"></a>
The name of the filter field to apply.
Type: String
Valid Values: `ResourceType | RecommendedActionType | ResourceId | LookBackPeriodInDays | CurrentResourceDetailsEbsVolumeType | ResourceTagsKey | ResourceTagsValue | AccountId | RestartNeeded`
Required: Yes

 ** values **   <a name="computeoptimizer-Type-automation_RecommendedActionFilter-values"></a>
The list of values to filter by for the specified filter name. Wildcards aren't supported. An asterisk (`*`) or a question mark (`?`) in a value matches only that literal character. How a value is matched depends on the filter name:
ResourceType, RecommendedActionType, ResourceId, and AccountId
The value that you specify must exactly match the corresponding field of the recommended action, including case. For example, specify `EbsVolume`, not `ebsvolume`.
CurrentResourceDetailsEbsVolumeType
Matches when the value appears anywhere in the current resource details of the recommended action, which include the volume type, size, IOPS, and throughput. Matching is case sensitive, and a partial value also matches. For example, `gp` matches both `gp2` and `gp3` volumes, and `100` matches any volume whose size, IOPS, or throughput contains 100. To filter by volume type, specify the complete volume type, such as `gp3` or `io2`.
ResourceTagsKey and ResourceTagsValue
Matches when the value appears anywhere in the tags of the resource. Both filter names search every tag key and tag value. Matching is case sensitive, and a partial value also matches. For example, a `ResourceTagsKey` value of `test` matches a resource that has a tag value of `test`.
LookBackPeriodInDays
Matches when the lookback period of the recommended action equals the value. Specify a number of days, such as `14`.
RestartNeeded
Matches recommended actions based on whether implementing them requires a resource restart. Specify `true` or `false`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-_\.\*\?\s]+`
Required: Yes

## See Also
<a name="API_automation_RecommendedActionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/RecommendedActionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/RecommendedActionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/RecommendedActionFilter)
