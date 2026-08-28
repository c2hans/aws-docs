---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_MetricsByTime.html
---

# MetricsByTime
<a name="API_CostOptimizationHub_MetricsByTime"></a>

Contains efficiency metrics for a specific point in time, including an efficiency score, potential savings, optimizable spend, and timestamp.

## Contents
<a name="API_CostOptimizationHub_MetricsByTime_Contents"></a>

 ** savings **   <a name="awscostmanagement-Type-CostOptimizationHub_MetricsByTime-savings"></a>
The estimated savings amount for this time period, representing the potential cost reduction achieved through optimization recommendations.
Type: Double
Required: No

 ** score **   <a name="awscostmanagement-Type-CostOptimizationHub_MetricsByTime-score"></a>
The efficiency score for this time period. The score represents a measure of how effectively the cloud resources are being optimized, with higher scores indicating better optimization performance.
Type: Double
Required: No

 ** spend **   <a name="awscostmanagement-Type-CostOptimizationHub_MetricsByTime-spend"></a>
The total spending amount for this time period.
Type: Double
Required: No

 ** timestamp **   <a name="awscostmanagement-Type-CostOptimizationHub_MetricsByTime-timestamp"></a>
The timestamp for this data point. The format depends on the granularity: YYYY-MM-DD for daily metrics, or YYYY-MM for monthly metrics.
Type: String
Required: No

## See Also
<a name="API_CostOptimizationHub_MetricsByTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/MetricsByTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/MetricsByTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/MetricsByTime)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
