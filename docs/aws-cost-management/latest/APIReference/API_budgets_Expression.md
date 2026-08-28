---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Expression.html
---

# Expression
<a name="API_budgets_Expression"></a>

Use Expression to filter in various Budgets APIs.

## Contents
<a name="API_budgets_Expression_Contents"></a>

 ** And **   <a name="awscostmanagement-Type-budgets_Expression-And"></a>
Return results that match both Dimension objects.
Type: Array of [Expression](#API_budgets_Expression) objects
Required: No

 ** CostCategories **   <a name="awscostmanagement-Type-budgets_Expression-CostCategories"></a>
The filter that's based on CostCategoryValues.
Type: [CostCategoryValues](API_budgets_CostCategoryValues.md) object
Required: No

 ** Dimensions **   <a name="awscostmanagement-Type-budgets_Expression-Dimensions"></a>
The specific Dimension to use for Expression.
Type: [ExpressionDimensionValues](API_budgets_ExpressionDimensionValues.md) object
Required: No

 ** Not **   <a name="awscostmanagement-Type-budgets_Expression-Not"></a>
Return results that don't match a Dimension object.
Type: [Expression](#API_budgets_Expression) object
Required: No

 ** Or **   <a name="awscostmanagement-Type-budgets_Expression-Or"></a>
Return results that match either Dimension object.
Type: Array of [Expression](#API_budgets_Expression) objects
Required: No

 ** Tags **   <a name="awscostmanagement-Type-budgets_Expression-Tags"></a>
The specific Tag to use for Expression.
Type: [TagValues](API_budgets_TagValues.md) object
Required: No

## See Also
<a name="API_budgets_Expression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/Expression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/Expression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/Expression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
