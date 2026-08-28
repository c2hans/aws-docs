---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_SyntheticDataConfiguration.html
---

# SyntheticDataConfiguration
<a name="API_SyntheticDataConfiguration"></a>

Configuration settings for synthetic data generation, including the parameters that control data synthesis and the evaluation scores that measure the quality and privacy characteristics of the generated synthetic data.

## Contents
<a name="API_SyntheticDataConfiguration_Contents"></a>

 ** syntheticDataParameters **   <a name="API-Type-SyntheticDataConfiguration-syntheticDataParameters"></a>
The parameters that control how synthetic data is generated, including privacy settings, column classifications, and other configuration options that affect the data synthesis process.
Type: [MLSyntheticDataParameters](API_MLSyntheticDataParameters.md) object
Required: Yes

 ** syntheticDataEvaluationScores **   <a name="API-Type-SyntheticDataConfiguration-syntheticDataEvaluationScores"></a>
Evaluation scores that assess the quality and privacy characteristics of the generated synthetic data, providing metrics on data utility and privacy preservation.
Type: [SyntheticDataEvaluationScores](API_SyntheticDataEvaluationScores.md) object
Required: No

## See Also
<a name="API_SyntheticDataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/SyntheticDataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/SyntheticDataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/SyntheticDataConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
