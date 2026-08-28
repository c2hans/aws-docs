---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_RejectGroupingRecommendationEntry.html
---

# RejectGroupingRecommendationEntry
<a name="API_RejectGroupingRecommendationEntry"></a>

Indicates the rejected grouping recommendation.

## Contents
<a name="API_RejectGroupingRecommendationEntry_Contents"></a>

 ** groupingRecommendationId **   <a name="resiliencehub-Type-RejectGroupingRecommendationEntry-groupingRecommendationId"></a>
Indicates the identifier of the grouping recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** rejectionReason **   <a name="resiliencehub-Type-RejectGroupingRecommendationEntry-rejectionReason"></a>
Indicates the reason you had selected while rejecting a grouping recommendation.
Type: String
Valid Values: `DistinctBusinessPurpose | SeparateDataConcern | DistinctUserGroupHandling | Other`
Required: No

## See Also
<a name="API_RejectGroupingRecommendationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/RejectGroupingRecommendationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/RejectGroupingRecommendationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/RejectGroupingRecommendationEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
