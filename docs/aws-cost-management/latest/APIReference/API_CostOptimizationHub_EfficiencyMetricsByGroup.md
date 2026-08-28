---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_EfficiencyMetricsByGroup.html
---

# EfficiencyMetricsByGroup
<a name="API_CostOptimizationHub_EfficiencyMetricsByGroup"></a>

Contains cost efficiency metrics for a specific group over time. The group is defined by the grouping dimension specified in the request, such as account ID, AWS Region.

## Contents
<a name="API_CostOptimizationHub_EfficiencyMetricsByGroup_Contents"></a>

 ** group **   <a name="awscostmanagement-Type-CostOptimizationHub_EfficiencyMetricsByGroup-group"></a>
The value of the grouping dimension for this set of metrics. For example, if grouped by account ID, this field contains the account ID. If no grouping is specified, this field is empty.
Type: String
Required: No

 ** message **   <a name="awscostmanagement-Type-CostOptimizationHub_EfficiencyMetricsByGroup-message"></a>
An explanation of why efficiency metrics could not be calculated for this group when the metricsByTime field is null. Common reasons include insufficient or inconclusive cost and usage data during the specified time period. This field is null or empty when metrics are successfully calculated.
Type: String
Required: No

 ** metricsByTime **   <a name="awscostmanagement-Type-CostOptimizationHub_EfficiencyMetricsByGroup-metricsByTime"></a>
A list of time-series data points containing efficiency metrics for this group. Each data point includes an efficiency score, estimated savings, spending, and a timestamp corresponding to the specified granularity. This field is null when efficiency metrics cannot be calculated for the group, in which case the message field provides an explanation.
Type: Array of [MetricsByTime](API_CostOptimizationHub_MetricsByTime.md) objects
Required: No

## See Also
<a name="API_CostOptimizationHub_EfficiencyMetricsByGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/EfficiencyMetricsByGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/EfficiencyMetricsByGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/EfficiencyMetricsByGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
