---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_RecommendedActionFilter.html
---

# RecommendedActionFilter
<a name="API_automation_RecommendedActionFilter"></a>

A filter used to narrow down recommended action results based on specific criteria.

## Contents
<a name="API_automation_RecommendedActionFilter_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-automation_RecommendedActionFilter-name"></a>
The name of the filter field to apply.
Type: String
Valid Values: `ResourceType | RecommendedActionType | ResourceId | LookBackPeriodInDays | CurrentResourceDetailsEbsVolumeType | ResourceTagsKey | ResourceTagsValue | AccountId | RestartNeeded`
Required: Yes

 ** values **   <a name="computeoptimizer-Type-automation_RecommendedActionFilter-values"></a>
List of filter values to match against the specified filter name. Used to narrow down recommended actions based on specific criteria.
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
