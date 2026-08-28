---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GenerationSummary.html
---

# GenerationSummary
<a name="API_GenerationSummary"></a>

The summary of the Savings Plans recommendation generation.

## Contents
<a name="API_GenerationSummary_Contents"></a>

 ** EstimatedCompletionTime **   <a name="awscostmanagement-Type-GenerationSummary-EstimatedCompletionTime"></a>
Indicates the estimated time for when the recommendation generation will complete.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** GenerationCompletionTime **   <a name="awscostmanagement-Type-GenerationSummary-GenerationCompletionTime"></a>
Indicates the completion time of the recommendation generation.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** GenerationStartedTime **   <a name="awscostmanagement-Type-GenerationSummary-GenerationStartedTime"></a>
Indicates the start time of the recommendation generation.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** GenerationStatus **   <a name="awscostmanagement-Type-GenerationSummary-GenerationStatus"></a>
Indicates whether the recommendation generation succeeded, is processing, or failed.
Type: String
Valid Values: `SUCCEEDED | PROCESSING | FAILED`
Required: No

 ** RecommendationId **   <a name="awscostmanagement-Type-GenerationSummary-RecommendationId"></a>
Indicates the ID for this specific recommendation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`
Required: No

## See Also
<a name="API_GenerationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GenerationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GenerationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GenerationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
