---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Budget.html
---

# Budget
<a name="API_budgets_Budget"></a>

Represents the output of the `CreateBudget` operation. The content consists of the detailed metadata and data file information, and the current status of the `budget` object.

This is the Amazon Resource Name (ARN) pattern for a budget:

 `arn:aws:budgets::AccountId:budget/budgetName`

## Contents
<a name="API_budgets_Budget_Contents"></a>

 ** BudgetName **   <a name="awscostmanagement-Type-budgets_Budget-BudgetName"></a>
The name of a budget. The name must be unique within an account. The `:` and `\` characters, and the "/action/" substring, aren't allowed in `BudgetName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: Yes

 ** BudgetType **   <a name="awscostmanagement-Type-budgets_Budget-BudgetType"></a>
Specifies whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage.
Type: String
Valid Values: `USAGE | COST | RI_UTILIZATION | RI_COVERAGE | SAVINGS_PLANS_UTILIZATION | SAVINGS_PLANS_COVERAGE`
Required: Yes

 ** TimeUnit **   <a name="awscostmanagement-Type-budgets_Budget-TimeUnit"></a>
The length of time until a budget resets the actual and forecasted spend.
Type: String
Valid Values: `DAILY | MONTHLY | QUARTERLY | ANNUALLY | CUSTOM`
Required: Yes

 ** AutoAdjustData **   <a name="awscostmanagement-Type-budgets_Budget-AutoAdjustData"></a>
The parameters that determine the budget amount for an auto-adjusting budget.
Type: [AutoAdjustData](API_budgets_AutoAdjustData.md) object
Required: No

 ** BillingViewArn **   <a name="awscostmanagement-Type-budgets_Budget-BillingViewArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to AWS Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]$`
Required: No

 ** BudgetLimit **   <a name="awscostmanagement-Type-budgets_Budget-BudgetLimit"></a>
The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage that you want to track with your budget.
 `BudgetLimit` is required for cost or usage budgets, but optional for RI or Savings Plans utilization or coverage budgets. RI and Savings Plans utilization or coverage budgets default to `100`. This is the only valid value for RI or Savings Plans utilization or coverage budgets. You can't use `BudgetLimit` with `PlannedBudgetLimits` for `CreateBudget` and `UpdateBudget` actions.
Type: [Spend](API_budgets_Spend.md) object
Required: No

 ** CalculatedSpend **   <a name="awscostmanagement-Type-budgets_Budget-CalculatedSpend"></a>
The actual and forecasted cost or usage that the budget tracks.
Type: [CalculatedSpend](API_budgets_CalculatedSpend.md) object
Required: No

 ** CostFilters **   <a name="awscostmanagement-Type-budgets_Budget-CostFilters"></a>
 *This member has been deprecated.*
The cost filters, such as `Region`, `Service`, `LinkedAccount`, `Tag`, or `CostCategory`, that are applied to a budget.
 AWS Budgets supports the following services as a `Service` filter for RI budgets:
+ Amazon EC2
+ Amazon Redshift
+ Amazon Relational Database Service
+ Amazon ElastiCache
+ Amazon OpenSearch Service
Type: String to array of strings map
Key Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Key Pattern: `.*`
Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Pattern: `[\S\s]*`
Required: No

 ** CostTypes **   <a name="awscostmanagement-Type-budgets_Budget-CostTypes"></a>
 *This member has been deprecated.*
The types of costs that are included in this `COST` budget.
 `USAGE`, `RI_UTILIZATION`, `RI_COVERAGE`, `SAVINGS_PLANS_UTILIZATION`, and `SAVINGS_PLANS_COVERAGE` budgets do not have `CostTypes`.
Type: [CostTypes](API_budgets_CostTypes.md) object
Required: No

 ** FilterExpression **   <a name="awscostmanagement-Type-budgets_Budget-FilterExpression"></a>
The filtering dimensions for the budget and their corresponding values.
Type: [Expression](API_budgets_Expression.md) object
Required: No

 ** HealthStatus **   <a name="awscostmanagement-Type-budgets_Budget-HealthStatus"></a>
The current operational state of a Billing View derived resource.
Type: [HealthStatus](API_budgets_HealthStatus.md) object
Required: No

 ** LastUpdatedTime **   <a name="awscostmanagement-Type-budgets_Budget-LastUpdatedTime"></a>
The last time that you updated this budget.
Type: Timestamp
Required: No

 ** Metrics **   <a name="awscostmanagement-Type-budgets_Budget-Metrics"></a>
The definition for how the budget data is aggregated.
Type: Array of strings
Array Members: Maximum number of 1 item.
Valid Values: `BlendedCost | UnblendedCost | AmortizedCost | NetUnblendedCost | NetAmortizedCost | UsageQuantity | NormalizedUsageAmount | Hours`
Required: No

 ** PlannedBudgetLimits **   <a name="awscostmanagement-Type-budgets_Budget-PlannedBudgetLimits"></a>
A map containing multiple `BudgetLimit`, including current or future limits.
 `PlannedBudgetLimits` is available for cost or usage budget and supports both monthly and quarterly `TimeUnit`.
For monthly budgets, provide 12 months of `PlannedBudgetLimits` values. This must start from the current month and include the next 11 months. The `key` is the start of the month, `UTC` in epoch seconds.
For quarterly budgets, provide four quarters of `PlannedBudgetLimits` value entries in standard calendar quarter increments. This must start from the current quarter and include the next three quarters. The `key` is the start of the quarter, `UTC` in epoch seconds.
If the planned budget expires before 12 months for monthly or four quarters for quarterly, provide the `PlannedBudgetLimits` values only for the remaining periods.
If the budget begins at a date in the future, provide `PlannedBudgetLimits` values from the start date of the budget.
After all of the `BudgetLimit` values in `PlannedBudgetLimits` are used, the budget continues to use the last limit as the `BudgetLimit`. At that point, the planned budget provides the same experience as a fixed budget.
 `DescribeBudget` and `DescribeBudgets` response along with `PlannedBudgetLimits` also contain `BudgetLimit` representing the current month or quarter limit present in `PlannedBudgetLimits`. This only applies to budgets that are created with `PlannedBudgetLimits`. Budgets that are created without `PlannedBudgetLimits` only contain `BudgetLimit`. They don't contain `PlannedBudgetLimits`.
Type: String to [Spend](API_budgets_Spend.md) object map
Key Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Key Pattern: `.*`
Required: No

 ** TimePeriod **   <a name="awscostmanagement-Type-budgets_Budget-TimePeriod"></a>
The period of time that's covered by a budget. You set the start date and end date. The start date must come before the end date. The end date must come before `06/15/87 00:00 UTC`.
If you create your budget and don't specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, ANNUALLY, or CUSTOM). For example, if you created your budget on January 24, 2018, chose `DAILY`, and didn't set a start date, AWS set your start date to `01/24/18 00:00 UTC`. If you chose `MONTHLY`, AWS set your start date to `01/01/18 00:00 UTC`. If you didn't specify an end date, AWS set your end date to `06/15/87 00:00 UTC`. The defaults are the same for the AWS Billing and Cost Management console and the API.
You can change either date with the `UpdateBudget` operation.
After the end date, AWS deletes the budget and all the associated notifications and subscribers.
Type: [TimePeriod](API_budgets_TimePeriod.md) object
Required: No

## See Also
<a name="API_budgets_Budget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/Budget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/Budget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/Budget)
