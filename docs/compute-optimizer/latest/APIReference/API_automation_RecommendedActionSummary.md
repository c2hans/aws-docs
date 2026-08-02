---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_RecommendedActionSummary.html
---

# RecommendedActionSummary
<a name="API_automation_RecommendedActionSummary"></a>

Summary information about recommended actions, grouped by specific criteria with totals and counts.

## Contents
<a name="API_automation_RecommendedActionSummary_Contents"></a>

 ** key **   <a name="computeoptimizer-Type-automation_RecommendedActionSummary-key"></a>
The grouping key used to categorize the recommended actions in this summary.
Type: String
Required: Yes

 ** total **   <a name="computeoptimizer-Type-automation_RecommendedActionSummary-total"></a>
Aggregate totals for the recommended actions in this group, including count and estimated savings.
Type: [RecommendedActionTotal](API_automation_RecommendedActionTotal.md) object
Required: Yes

## See Also
<a name="API_automation_RecommendedActionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/RecommendedActionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/RecommendedActionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/RecommendedActionSummary)
