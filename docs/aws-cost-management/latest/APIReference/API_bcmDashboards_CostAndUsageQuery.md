---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_CostAndUsageQuery.html
---

# CostAndUsageQuery
<a name="API_bcmDashboards_CostAndUsageQuery"></a>

Defines the parameters for retrieving AWS cost and usage data. Includes specifications for metrics, time periods, granularity, grouping dimensions, and filtering conditions.

## Contents
<a name="API_bcmDashboards_CostAndUsageQuery_Contents"></a>

 ** granularity **   <a name="awscostmanagement-Type-bcmDashboards_CostAndUsageQuery-granularity"></a>
The granularity of the retrieved data: `HOURLY`, `DAILY`, or `MONTHLY`.
Type: String
Valid Values: `HOURLY | DAILY | MONTHLY`
Required: Yes

 ** metrics **   <a name="awscostmanagement-Type-bcmDashboards_CostAndUsageQuery-metrics"></a>
The specific cost and usage metrics to retrieve.
Valid values for CostAndUsageQuery metrics are `AmortizedCost`, `BlendedCost`, `NetAmortizedCost`, `NetUnblendedCost`, `NormalizedUsageAmount`, `UnblendedCost`, and `UsageQuantity`.
Type: Array of strings
Valid Values: `AmortizedCost | BlendedCost | NetAmortizedCost | NetUnblendedCost | NormalizedUsageAmount | UnblendedCost | UsageQuantity | SpendCoveredBySavingsPlans | Hour | Unit | Cost`
Required: Yes

 ** timeRange **   <a name="awscostmanagement-Type-bcmDashboards_CostAndUsageQuery-timeRange"></a>
The time period for which to retrieve data. Can be specified as absolute dates or relative time periods.
Type: [DateTimeRange](API_bcmDashboards_DateTimeRange.md) object
Required: Yes

 ** filter **   <a name="awscostmanagement-Type-bcmDashboards_CostAndUsageQuery-filter"></a>
The filter expression to be applied to the cost and usage data.
Type: [Expression](API_bcmDashboards_Expression.md) object
Required: No

 ** groupBy **   <a name="awscostmanagement-Type-bcmDashboards_CostAndUsageQuery-groupBy"></a>
Specifies how to group the retrieved data, such as by `SERVICE`, `ACCOUNT`, or `TAG`.
Type: Array of [GroupDefinition](API_bcmDashboards_GroupDefinition.md) objects
Required: No

## See Also
<a name="API_bcmDashboards_CostAndUsageQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/CostAndUsageQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/CostAndUsageQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/CostAndUsageQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
