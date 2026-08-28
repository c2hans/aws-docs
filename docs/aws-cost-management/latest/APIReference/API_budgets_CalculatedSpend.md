---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CalculatedSpend.html
---

# CalculatedSpend
<a name="API_budgets_CalculatedSpend"></a>

The spend objects that are associated with this budget. The `actualSpend` tracks how much you've used, cost, usage, RI units, or Savings Plans units and the `forecastedSpend` tracks how much that you're predicted to spend based on your historical usage profile.

For example, if it's the 20th of the month and you have spent `50` dollars on Amazon EC2, your `actualSpend` is `50 USD`, and your `forecastedSpend` is `75 USD`.

## Contents
<a name="API_budgets_CalculatedSpend_Contents"></a>

 ** ActualSpend **   <a name="awscostmanagement-Type-budgets_CalculatedSpend-ActualSpend"></a>
The amount of cost, usage, RI units, or Savings Plans units that you used.
Type: [Spend](API_budgets_Spend.md) object
Required: Yes

 ** ForecastedSpend **   <a name="awscostmanagement-Type-budgets_CalculatedSpend-ForecastedSpend"></a>
The amount of cost, usage, RI units, or Savings Plans units that you're forecasted to use.
Type: [Spend](API_budgets_Spend.md) object
Required: No

## See Also
<a name="API_budgets_CalculatedSpend_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/CalculatedSpend)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/CalculatedSpend)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/CalculatedSpend)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
