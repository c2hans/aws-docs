---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_CostCategoryValues.html
---

# CostCategoryValues
<a name="API_bcmDashboards_CostCategoryValues"></a>

Specifies the values and match options for cost category-based filtering in cost and usage queries.

## Contents
<a name="API_bcmDashboards_CostCategoryValues_Contents"></a>

 ** key **   <a name="awscostmanagement-Type-bcmDashboards_CostCategoryValues-key"></a>
The key of the cost category to filter on.
Type: String
Required: No

 ** matchOptions **   <a name="awscostmanagement-Type-bcmDashboards_CostCategoryValues-matchOptions"></a>
The match options for cost category values, such as `EQUALS`, `CONTAINS`, `STARTS_WITH`, or `ENDS_WITH`.
Type: Array of strings
Valid Values: `EQUALS | ABSENT | STARTS_WITH | ENDS_WITH | CONTAINS | GREATER_THAN_OR_EQUAL | CASE_SENSITIVE | CASE_INSENSITIVE`
Required: No

 ** values **   <a name="awscostmanagement-Type-bcmDashboards_CostCategoryValues-values"></a>
The values to match for the specified cost category key.
Type: Array of strings
Required: No

## See Also
<a name="API_bcmDashboards_CostCategoryValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/CostCategoryValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/CostCategoryValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/CostCategoryValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
