---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_QueryParameters.html
---

# QueryParameters
<a name="API_bcmDashboards_QueryParameters"></a>

Defines the data retrieval parameters for a widget.

## Contents
<a name="API_bcmDashboards_QueryParameters_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** budget **   <a name="awscostmanagement-Type-bcmDashboards_QueryParameters-budget"></a>
The parameters for querying budget data, including budget names, types, and thresholds.
Type: [BudgetQuery](API_bcmDashboards_BudgetQuery.md) object
Required: No

 ** costAndUsage **   <a name="awscostmanagement-Type-bcmDashboards_QueryParameters-costAndUsage"></a>
The parameters for querying cost and usage data, including metrics, time range, granularity, grouping dimensions, and filters.
Type: [CostAndUsageQuery](API_bcmDashboards_CostAndUsageQuery.md) object
Required: No

 ** costEfficiency **   <a name="awscostmanagement-Type-bcmDashboards_QueryParameters-costEfficiency"></a>
The query configuration for retrieving cost efficiency data, filtered by overall score, AWS account, or Region.
Type: [CostEfficiencyQuery](API_bcmDashboards_CostEfficiencyQuery.md) object
Required: No

 ** reservationCoverage **   <a name="awscostmanagement-Type-bcmDashboards_QueryParameters-reservationCoverage"></a>
The parameters for querying Reserved Instance coverage data, showing how much of your eligible instance usage is covered by Reserved Instances.
Type: [ReservationCoverageQuery](API_bcmDashboards_ReservationCoverageQuery.md) object
Required: No

 ** reservationUtilization **   <a name="awscostmanagement-Type-bcmDashboards_QueryParameters-reservationUtilization"></a>
The parameters for querying Reserved Instance utilization data, showing how effectively your Reserved Instances are being used.
Type: [ReservationUtilizationQuery](API_bcmDashboards_ReservationUtilizationQuery.md) object
Required: No

 ** savingsPlansCoverage **   <a name="awscostmanagement-Type-bcmDashboards_QueryParameters-savingsPlansCoverage"></a>
The parameters for querying Savings Plans coverage data, showing how much of your eligible compute usage is covered by Savings Plans.
Type: [SavingsPlansCoverageQuery](API_bcmDashboards_SavingsPlansCoverageQuery.md) object
Required: No

 ** savingsPlansUtilization **   <a name="awscostmanagement-Type-bcmDashboards_QueryParameters-savingsPlansUtilization"></a>
The parameters for querying Savings Plans utilization data, showing how effectively your Savings Plans are being used.
Type: [SavingsPlansUtilizationQuery](API_bcmDashboards_SavingsPlansUtilizationQuery.md) object
Required: No

## See Also
<a name="API_bcmDashboards_QueryParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/QueryParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/QueryParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/QueryParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
