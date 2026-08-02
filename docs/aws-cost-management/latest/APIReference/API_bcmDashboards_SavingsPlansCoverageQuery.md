---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_SavingsPlansCoverageQuery.html
---

# SavingsPlansCoverageQuery
<a name="API_bcmDashboards_SavingsPlansCoverageQuery"></a>

Defines the parameters for querying Savings Plans coverage data, including metrics, grouping options, and time granularity.

## Contents
<a name="API_bcmDashboards_SavingsPlansCoverageQuery_Contents"></a>

 ** timeRange **   <a name="awscostmanagement-Type-bcmDashboards_SavingsPlansCoverageQuery-timeRange"></a>
Defines a time period with explicit start and end times for data queries.
Type: [DateTimeRange](API_bcmDashboards_DateTimeRange.md) object
Required: Yes

 ** filter **   <a name="awscostmanagement-Type-bcmDashboards_SavingsPlansCoverageQuery-filter"></a>
Defines complex filtering conditions using logical operators (`AND`, `OR`, `NOT`) and various filter types.
Type: [Expression](API_bcmDashboards_Expression.md) object
Required: No

 ** granularity **   <a name="awscostmanagement-Type-bcmDashboards_SavingsPlansCoverageQuery-granularity"></a>
The time granularity of the retrieved data: `HOURLY`, `DAILY`, or `MONTHLY`.
Type: String
Valid Values: `HOURLY | DAILY | MONTHLY`
Required: No

 ** groupBy **   <a name="awscostmanagement-Type-bcmDashboards_SavingsPlansCoverageQuery-groupBy"></a>
Specifies how to group the Savings Plans coverage data, such as by service or instance family.
Type: Array of [GroupDefinition](API_bcmDashboards_GroupDefinition.md) objects
Required: No

 ** metrics **   <a name="awscostmanagement-Type-bcmDashboards_SavingsPlansCoverageQuery-metrics"></a>
The coverage metrics to include in the results.
Valid value for SavingsPlansCoverageQuery metrics is `SpendCoveredBySavingsPlans`.
Type: Array of strings
Valid Values: `AmortizedCost | BlendedCost | NetAmortizedCost | NetUnblendedCost | NormalizedUsageAmount | UnblendedCost | UsageQuantity | SpendCoveredBySavingsPlans | Hour | Unit | Cost`
Required: No

## See Also
<a name="API_bcmDashboards_SavingsPlansCoverageQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/SavingsPlansCoverageQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/SavingsPlansCoverageQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/SavingsPlansCoverageQuery)
