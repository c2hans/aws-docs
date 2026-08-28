---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_SavingsPlansUtilizationQuery.html
---

# SavingsPlansUtilizationQuery
<a name="API_bcmDashboards_SavingsPlansUtilizationQuery"></a>

Defines the parameters for querying Savings Plans utilization data, including time granularity and sorting preferences.

## Contents
<a name="API_bcmDashboards_SavingsPlansUtilizationQuery_Contents"></a>

 ** timeRange **   <a name="awscostmanagement-Type-bcmDashboards_SavingsPlansUtilizationQuery-timeRange"></a>
Defines a time period with explicit start and end times for data queries.
Type: [DateTimeRange](API_bcmDashboards_DateTimeRange.md) object
Required: Yes

 ** filter **   <a name="awscostmanagement-Type-bcmDashboards_SavingsPlansUtilizationQuery-filter"></a>
Defines complex filtering conditions using logical operators (`AND`, `OR`, `NOT`) and various filter types.
Type: [Expression](API_bcmDashboards_Expression.md) object
Required: No

 ** granularity **   <a name="awscostmanagement-Type-bcmDashboards_SavingsPlansUtilizationQuery-granularity"></a>
The time granularity of the retrieved data: `HOURLY`, `DAILY`, or `MONTHLY`.
Type: String
Valid Values: `HOURLY | DAILY | MONTHLY`
Required: No

## See Also
<a name="API_bcmDashboards_SavingsPlansUtilizationQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/SavingsPlansUtilizationQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/SavingsPlansUtilizationQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/SavingsPlansUtilizationQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
