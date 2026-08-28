---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_RelevanceMetric.html
---

# RelevanceMetric
<a name="API_RelevanceMetric"></a>

The relevance score of a generated audience.

## Contents
<a name="API_RelevanceMetric_Contents"></a>

 ** audienceSize **   <a name="API-Type-RelevanceMetric-audienceSize"></a>
The size of the generated audience. Must match one of the sizes in the configured audience model.
Type: [AudienceSize](API_AudienceSize.md) object
Required: Yes

 ** score **   <a name="API-Type-RelevanceMetric-score"></a>
The relevance score of the generated audience.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 10.0.
Required: No

## See Also
<a name="API_RelevanceMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/RelevanceMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/RelevanceMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/RelevanceMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
