---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_BudgetedAndActualAmounts.html
---

# BudgetedAndActualAmounts
<a name="API_budgets_BudgetedAndActualAmounts"></a>

The amount of cost or usage that you created the budget for, compared to your actual costs or usage.

## Contents
<a name="API_budgets_BudgetedAndActualAmounts_Contents"></a>

 ** ActualAmount **   <a name="awscostmanagement-Type-budgets_BudgetedAndActualAmounts-ActualAmount"></a>
Your actual costs or usage for a budget period.
Type: [Spend](API_budgets_Spend.md) object
Required: No

 ** BudgetedAmount **   <a name="awscostmanagement-Type-budgets_BudgetedAndActualAmounts-BudgetedAmount"></a>
The amount of cost or usage that you created the budget for.
Type: [Spend](API_budgets_Spend.md) object
Required: No

 ** TimePeriod **   <a name="awscostmanagement-Type-budgets_BudgetedAndActualAmounts-TimePeriod"></a>
The time period that's covered by this budget comparison.
Type: [TimePeriod](API_budgets_TimePeriod.md) object
Required: No

## See Also
<a name="API_budgets_BudgetedAndActualAmounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/BudgetedAndActualAmounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/BudgetedAndActualAmounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/BudgetedAndActualAmounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
