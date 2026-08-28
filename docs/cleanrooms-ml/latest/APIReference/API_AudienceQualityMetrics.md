---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AudienceQualityMetrics.html
---

# AudienceQualityMetrics
<a name="API_AudienceQualityMetrics"></a>

Metrics that describe the quality of the generated audience.

## Contents
<a name="API_AudienceQualityMetrics_Contents"></a>

 ** relevanceMetrics **   <a name="API-Type-AudienceQualityMetrics-relevanceMetrics"></a>
The relevance scores of the generated audience.
Type: Array of [RelevanceMetric](API_RelevanceMetric.md) objects
Required: Yes

 ** recallMetric **   <a name="API-Type-AudienceQualityMetrics-recallMetric"></a>
The recall score of the generated audience. Recall is the percentage of the most similar users (by default, the most similar 20%) from a sample of the training data that are included in the seed audience by the audience generation job. Values range from 0-1, larger values indicate a better audience. A recall value approximately equal to the maximum bin size indicates that the audience model is equivalent to random selection.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

## See Also
<a name="API_AudienceQualityMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/AudienceQualityMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/AudienceQualityMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/AudienceQualityMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
