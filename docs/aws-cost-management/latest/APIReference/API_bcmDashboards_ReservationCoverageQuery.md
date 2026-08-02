---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ReservationCoverageQuery.html
---

# ReservationCoverageQuery
<a name="API_bcmDashboards_ReservationCoverageQuery"></a>

Defines the parameters for querying Reserved Instance coverage data, including grouping options, metrics, and sorting preferences.

## Contents
<a name="API_bcmDashboards_ReservationCoverageQuery_Contents"></a>

 ** timeRange **   <a name="awscostmanagement-Type-bcmDashboards_ReservationCoverageQuery-timeRange"></a>
Defines a time period with explicit start and end times for data queries.
Type: [DateTimeRange](API_bcmDashboards_DateTimeRange.md) object
Required: Yes

 ** filter **   <a name="awscostmanagement-Type-bcmDashboards_ReservationCoverageQuery-filter"></a>
Defines complex filtering conditions using logical operators (`AND`, `OR`, `NOT`) and various filter types.
Type: [Expression](API_bcmDashboards_Expression.md) object
Required: No

 ** granularity **   <a name="awscostmanagement-Type-bcmDashboards_ReservationCoverageQuery-granularity"></a>
The time granularity of the retrieved data: `HOURLY`, `DAILY`, or `MONTHLY`.
Type: String
Valid Values: `HOURLY | DAILY | MONTHLY`
Required: No

 ** groupBy **   <a name="awscostmanagement-Type-bcmDashboards_ReservationCoverageQuery-groupBy"></a>
Specifies how to group the Reserved Instance coverage data, such as by service, Region, or instance type.
Type: Array of [GroupDefinition](API_bcmDashboards_GroupDefinition.md) objects
Required: No

 ** metrics **   <a name="awscostmanagement-Type-bcmDashboards_ReservationCoverageQuery-metrics"></a>
The coverage metrics to include in the results.
Valid values for ReservationCoverageQuery metrics are `Hour`, `Unit`, and `Cost`.
Type: Array of strings
Valid Values: `AmortizedCost | BlendedCost | NetAmortizedCost | NetUnblendedCost | NormalizedUsageAmount | UnblendedCost | UsageQuantity | SpendCoveredBySavingsPlans | Hour | Unit | Cost`
Required: No

## See Also
<a name="API_bcmDashboards_ReservationCoverageQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/ReservationCoverageQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/ReservationCoverageQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/ReservationCoverageQuery)
