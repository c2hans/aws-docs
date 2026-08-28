---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_MLSyntheticDataParameters.html
---

# MLSyntheticDataParameters
<a name="API_MLSyntheticDataParameters"></a>

Parameters that control the generation of synthetic data for custom model training, including privacy settings and column classification details.

## Contents
<a name="API_MLSyntheticDataParameters_Contents"></a>

 ** epsilon **   <a name="API-Type-MLSyntheticDataParameters-epsilon"></a>
The epsilon value for differential privacy, which controls the privacy-utility tradeoff in synthetic data generation. Lower values provide stronger privacy guarantees but may reduce data utility.
Type: Double
Valid Range: Minimum value of 0.0001. Maximum value of 10.
Required: Yes

 ** maxMembershipInferenceAttackScore **   <a name="API-Type-MLSyntheticDataParameters-maxMembershipInferenceAttackScore"></a>
The maximum acceptable score for membership inference attack vulnerability. Synthetic data generation fails if the score for the resulting data exceeds this threshold.
Type: Double
Valid Range: Minimum value of 0.5. Maximum value of 1.
Required: Yes

 ** columnClassification **   <a name="API-Type-MLSyntheticDataParameters-columnClassification"></a>
Classification details for data columns that specify how each column should be treated during synthetic data generation.
Type: [ColumnClassificationDetails](API_ColumnClassificationDetails.md) object
Required: No

## See Also
<a name="API_MLSyntheticDataParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/MLSyntheticDataParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/MLSyntheticDataParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/MLSyntheticDataParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
