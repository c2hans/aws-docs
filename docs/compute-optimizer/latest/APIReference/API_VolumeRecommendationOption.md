---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_VolumeRecommendationOption.html
---

# VolumeRecommendationOption
<a name="API_VolumeRecommendationOption"></a>

Describes a recommendation option for an Amazon Elastic Block Store (Amazon EBS) instance.

## Contents
<a name="API_VolumeRecommendationOption_Contents"></a>

 ** configuration **   <a name="computeoptimizer-Type-VolumeRecommendationOption-configuration"></a>
An array of objects that describe a volume configuration.
Type: [VolumeConfiguration](API_VolumeConfiguration.md) object
Required: No

 ** performanceRisk **   <a name="computeoptimizer-Type-VolumeRecommendationOption-performanceRisk"></a>
The performance risk of the volume recommendation option.
Performance risk is the likelihood of the recommended volume type meeting the performance requirement of your workload.
The value ranges from `0` - `4`, with `0` meaning that the recommended resource is predicted to always provide enough hardware capability. The higher the performance risk is, the more likely you should validate whether the recommendation will meet the performance requirements of your workload before migrating your resource.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 4.
Required: No

 ** rank **   <a name="computeoptimizer-Type-VolumeRecommendationOption-rank"></a>
The rank of the volume recommendation option.
The top recommendation option is ranked as `1`.
Type: Integer
Required: No

 ** savingsOpportunity **   <a name="computeoptimizer-Type-VolumeRecommendationOption-savingsOpportunity"></a>
An object that describes the savings opportunity for the EBS volume recommendation option. Savings opportunity includes the estimated monthly savings amount and percentage.
Type: [SavingsOpportunity](API_SavingsOpportunity.md) object
Required: No

 ** savingsOpportunityAfterDiscounts **   <a name="computeoptimizer-Type-VolumeRecommendationOption-savingsOpportunityAfterDiscounts"></a>
 An object that describes the savings opportunity for the Amazon EBS volume recommendation option with specific discounts. Savings opportunity includes the estimated monthly savings and percentage.
Type: [EBSSavingsOpportunityAfterDiscounts](API_EBSSavingsOpportunityAfterDiscounts.md) object
Required: No

## See Also
<a name="API_VolumeRecommendationOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/VolumeRecommendationOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/VolumeRecommendationOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/VolumeRecommendationOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
