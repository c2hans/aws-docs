---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSEffectiveRecommendationPreferences.html
---

# ECSEffectiveRecommendationPreferences
<a name="API_ECSEffectiveRecommendationPreferences"></a>

 Describes the effective recommendation preferences for Amazon ECS services.

## Contents
<a name="API_ECSEffectiveRecommendationPreferences_Contents"></a>

 ** lookBackPeriod **   <a name="computeoptimizer-Type-ECSEffectiveRecommendationPreferences-lookBackPeriod"></a>
 The number of days the Amazon ECS service utilization metrics were analyzed.
Type: String
Valid Values: `DAYS_14 | DAYS_32 | DAYS_93`
Required: No

 ** savingsEstimationMode **   <a name="computeoptimizer-Type-ECSEffectiveRecommendationPreferences-savingsEstimationMode"></a>
 Describes the savings estimation mode preference applied for calculating savings opportunity for Amazon ECS services.
Type: [ECSSavingsEstimationMode](API_ECSSavingsEstimationMode.md) object
Required: No

## See Also
<a name="API_ECSEffectiveRecommendationPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ECSEffectiveRecommendationPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ECSEffectiveRecommendationPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ECSEffectiveRecommendationPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
