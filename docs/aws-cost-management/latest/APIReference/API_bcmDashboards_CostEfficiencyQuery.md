---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_CostEfficiencyQuery.html
---

# CostEfficiencyQuery
<a name="API_bcmDashboards_CostEfficiencyQuery"></a>

Contains the time period, granularity, grouping dimensions, and filtering conditions for an AWS cost efficiency data query.

## Contents
<a name="API_bcmDashboards_CostEfficiencyQuery_Contents"></a>

 ** granularity **   <a name="awscostmanagement-Type-bcmDashboards_CostEfficiencyQuery-granularity"></a>
The time granularity of the retrieved data. Set to `DAILY` to aggregate data by day. Set to `MONTHLY` to aggregate data by month.
Type: String
Valid Values: `HOURLY | DAILY | MONTHLY`
Required: Yes

 ** timeRange **   <a name="awscostmanagement-Type-bcmDashboards_CostEfficiencyQuery-timeRange"></a>
The time period for which to retrieve data. Can be specified as absolute dates or relative time periods.
Type: [DateTimeRange](API_bcmDashboards_DateTimeRange.md) object
Required: Yes

 ** filter **   <a name="awscostmanagement-Type-bcmDashboards_CostEfficiencyQuery-filter"></a>
The filter expression to apply to cost efficiency data. You can filter by cost efficiency dimensions such as `AccountId` and `Region`.
Type: [Expression](API_bcmDashboards_Expression.md) object
Required: No

 ** groupBy **   <a name="awscostmanagement-Type-bcmDashboards_CostEfficiencyQuery-groupBy"></a>
Specifies how to group the retrieved data, such as by `Region` or `AccountId`.
Type: Array of [GroupDefinition](API_bcmDashboards_GroupDefinition.md) objects
Required: No

## See Also
<a name="API_bcmDashboards_CostEfficiencyQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/CostEfficiencyQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/CostEfficiencyQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/CostEfficiencyQuery)
