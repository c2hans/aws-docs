---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_FailedGroupingRecommendationEntry.html
---

# FailedGroupingRecommendationEntry
<a name="API_FailedGroupingRecommendationEntry"></a>

Indicates the accepted grouping recommendation whose implementation failed.

## Contents
<a name="API_FailedGroupingRecommendationEntry_Contents"></a>

 ** errorMessage **   <a name="resiliencehub-Type-FailedGroupingRecommendationEntry-errorMessage"></a>
Indicates the error that occurred while implementing a grouping recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

 ** groupingRecommendationId **   <a name="resiliencehub-Type-FailedGroupingRecommendationEntry-groupingRecommendationId"></a>
Indicates the identifier of the grouping recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_FailedGroupingRecommendationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/FailedGroupingRecommendationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/FailedGroupingRecommendationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/FailedGroupingRecommendationEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
