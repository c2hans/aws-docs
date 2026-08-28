---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RightsizingRecommendationConfiguration.html
---

# RightsizingRecommendationConfiguration
<a name="API_RightsizingRecommendationConfiguration"></a>

You can use `RightsizingRecommendationConfiguration` to customize recommendations across two attributes. You can choose to view recommendations for instances within the same instance families or across different instance families. You can also choose to view your estimated savings that are associated with recommendations with consideration of existing Savings Plans or Reserved Instance (RI) benefits, or neither.

## Contents
<a name="API_RightsizingRecommendationConfiguration_Contents"></a>

 ** BenefitsConsidered **   <a name="awscostmanagement-Type-RightsizingRecommendationConfiguration-BenefitsConsidered"></a>
The option to consider RI or Savings Plans discount benefits in your savings calculation. The default value is `TRUE`.
Type: Boolean
Required: Yes

 ** RecommendationTarget **   <a name="awscostmanagement-Type-RightsizingRecommendationConfiguration-RecommendationTarget"></a>
The option to see recommendations within the same instance family or recommendations for instances across other families. The default value is `SAME_INSTANCE_FAMILY`.
Type: String
Valid Values: `SAME_INSTANCE_FAMILY | CROSS_INSTANCE_FAMILY`
Required: Yes

## See Also
<a name="API_RightsizingRecommendationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/RightsizingRecommendationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/RightsizingRecommendationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/RightsizingRecommendationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
