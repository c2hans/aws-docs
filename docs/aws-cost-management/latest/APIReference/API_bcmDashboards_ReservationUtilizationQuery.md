---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ReservationUtilizationQuery.html
---

# ReservationUtilizationQuery
<a name="API_bcmDashboards_ReservationUtilizationQuery"></a>

Defines the parameters for querying Reserved Instance utilization data, including grouping options and time granularity.

## Contents
<a name="API_bcmDashboards_ReservationUtilizationQuery_Contents"></a>

 ** timeRange **   <a name="awscostmanagement-Type-bcmDashboards_ReservationUtilizationQuery-timeRange"></a>
Defines a time period with explicit start and end times for data queries.
Type: [DateTimeRange](API_bcmDashboards_DateTimeRange.md) object
Required: Yes

 ** filter **   <a name="awscostmanagement-Type-bcmDashboards_ReservationUtilizationQuery-filter"></a>
Defines complex filtering conditions using logical operators (`AND`, `OR`, `NOT`) and various filter types.
Type: [Expression](API_bcmDashboards_Expression.md) object
Required: No

 ** granularity **   <a name="awscostmanagement-Type-bcmDashboards_ReservationUtilizationQuery-granularity"></a>
The time granularity of the retrieved data: `HOURLY`, `DAILY`, or `MONTHLY`.
Type: String
Valid Values: `HOURLY | DAILY | MONTHLY`
Required: No

 ** groupBy **   <a name="awscostmanagement-Type-bcmDashboards_ReservationUtilizationQuery-groupBy"></a>
Specifies how to group the Reserved Instance utilization data, such as by service, Region, or instance type.
Type: Array of [GroupDefinition](API_bcmDashboards_GroupDefinition.md) objects
Required: No

## See Also
<a name="API_bcmDashboards_ReservationUtilizationQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/ReservationUtilizationQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/ReservationUtilizationQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/ReservationUtilizationQuery)
