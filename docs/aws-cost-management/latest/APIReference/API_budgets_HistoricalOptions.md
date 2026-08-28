---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_HistoricalOptions.html
---

# HistoricalOptions
<a name="API_budgets_HistoricalOptions"></a>

The parameters that define or describe the historical data that your auto-adjusting budget is based on.

## Contents
<a name="API_budgets_HistoricalOptions_Contents"></a>

 ** BudgetAdjustmentPeriod **   <a name="awscostmanagement-Type-budgets_HistoricalOptions-BudgetAdjustmentPeriod"></a>
The number of budget periods included in the moving-average calculation that determines your auto-adjusted budget amount. The maximum value depends on the `TimeUnit` granularity of the budget:
+ For the `DAILY` granularity, the maximum value is `60`.
+ For the `MONTHLY` granularity, the maximum value is `12`.
+ For the `QUARTERLY` granularity, the maximum value is `4`.
+ For the `ANNUALLY` granularity, the maximum value is `1`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60.
Required: Yes

 ** LookBackAvailablePeriods **   <a name="awscostmanagement-Type-budgets_HistoricalOptions-LookBackAvailablePeriods"></a>
The integer that describes how many budget periods in your `BudgetAdjustmentPeriod` are included in the calculation of your current `BudgetLimit`. If the first budget period in your `BudgetAdjustmentPeriod` has no cost data, then that budget period isn’t included in the average that determines your budget limit.
For example, if you set `BudgetAdjustmentPeriod` as `4` quarters, but your account had no cost data in the first quarter, then only the last three quarters are included in the calculation. In this scenario, `LookBackAvailablePeriods` returns `3`.
You can’t set your own `LookBackAvailablePeriods`. The value is automatically calculated from the `BudgetAdjustmentPeriod` and your historical cost data.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60.
Required: No

## See Also
<a name="API_budgets_HistoricalOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/HistoricalOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/HistoricalOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/HistoricalOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
