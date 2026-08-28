---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSEffectiveRecommendationPreferences.html
---

# RDSEffectiveRecommendationPreferences
<a name="API_RDSEffectiveRecommendationPreferences"></a>

 Describes the effective recommendation preferences for Amazon Aurora and RDS databases.

## Contents
<a name="API_RDSEffectiveRecommendationPreferences_Contents"></a>

 ** cpuVendorArchitectures **   <a name="computeoptimizer-Type-RDSEffectiveRecommendationPreferences-cpuVendorArchitectures"></a>
 Describes the CPU vendor and architecture for DB instance recommendations.
Type: Array of strings
Valid Values: `AWS_ARM64 | CURRENT`
Required: No

 ** enhancedInfrastructureMetrics **   <a name="computeoptimizer-Type-RDSEffectiveRecommendationPreferences-enhancedInfrastructureMetrics"></a>
Describes the activation status of the enhanced infrastructure metrics preference.
A status of `Active` confirms that the preference is applied in the latest recommendation refresh, and a status of `Inactive` confirms that it's not yet applied to recommendations.
For more information, see [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.
Type: String
Valid Values: `Active | Inactive`
Required: No

 ** lookBackPeriod **   <a name="computeoptimizer-Type-RDSEffectiveRecommendationPreferences-lookBackPeriod"></a>
 The number of days the utilization metrics of the DB instance are analyzed.
Type: String
Valid Values: `DAYS_14 | DAYS_32 | DAYS_93`
Required: No

 ** savingsEstimationMode **   <a name="computeoptimizer-Type-RDSEffectiveRecommendationPreferences-savingsEstimationMode"></a>
 Describes the savings estimation mode preference applied for calculating savings opportunity for DB instances.
Type: [RDSSavingsEstimationMode](API_RDSSavingsEstimationMode.md) object
Required: No

## See Also
<a name="API_RDSEffectiveRecommendationPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RDSEffectiveRecommendationPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RDSEffectiveRecommendationPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RDSEffectiveRecommendationPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
