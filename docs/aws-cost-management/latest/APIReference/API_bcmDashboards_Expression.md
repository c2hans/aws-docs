---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_Expression.html
---

# Expression
<a name="API_bcmDashboards_Expression"></a>

Defines complex filtering conditions using logical operators (`AND`, `OR`, `NOT`) and various filter types.

## Contents
<a name="API_bcmDashboards_Expression_Contents"></a>

 ** and **   <a name="awscostmanagement-Type-bcmDashboards_Expression-and"></a>
A list of expressions to combine with AND logic.
Type: Array of [Expression](#API_bcmDashboards_Expression) objects
Required: No

 ** costCategories **   <a name="awscostmanagement-Type-bcmDashboards_Expression-costCategories"></a>
The cost category values to include in the filter expression.
Type: [CostCategoryValues](API_bcmDashboards_CostCategoryValues.md) object
Required: No

 ** dimensions **   <a name="awscostmanagement-Type-bcmDashboards_Expression-dimensions"></a>
The dimension values to include in the filter expression.
Type: [DimensionValues](API_bcmDashboards_DimensionValues.md) object
Required: No

 ** not **   <a name="awscostmanagement-Type-bcmDashboards_Expression-not"></a>
An expression to negate with NOT logic.
Type: [Expression](#API_bcmDashboards_Expression) object
Required: No

 ** or **   <a name="awscostmanagement-Type-bcmDashboards_Expression-or"></a>
A list of expressions to combine with OR logic.
Type: Array of [Expression](#API_bcmDashboards_Expression) objects
Required: No

 ** tags **   <a name="awscostmanagement-Type-bcmDashboards_Expression-tags"></a>
The tag values to include in the filter expression.
Type: [TagValues](API_bcmDashboards_TagValues.md) object
Required: No

## See Also
<a name="API_bcmDashboards_Expression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/Expression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/Expression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/Expression)
