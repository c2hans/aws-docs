---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_BudgetPerformanceHistory.html
---

# BudgetPerformanceHistory
<a name="API_budgets_BudgetPerformanceHistory"></a>

A history of the state of a budget at the end of the budget's specified time period.

## Contents
<a name="API_budgets_BudgetPerformanceHistory_Contents"></a>

 ** BillingViewArn **   <a name="awscostmanagement-Type-budgets_BudgetPerformanceHistory-BillingViewArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to AWS Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]$`
Required: No

 ** BudgetedAndActualAmountsList **   <a name="awscostmanagement-Type-budgets_BudgetPerformanceHistory-BudgetedAndActualAmountsList"></a>
A list of amounts of cost or usage that you created budgets for, which are compared to your actual costs or usage.
Type: Array of [BudgetedAndActualAmounts](API_budgets_BudgetedAndActualAmounts.md) objects
Required: No

 ** BudgetName **   <a name="awscostmanagement-Type-budgets_BudgetPerformanceHistory-BudgetName"></a>
 A string that represents the budget name. The ":" and "\\" characters, and the "/action/" substring, aren't allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: No

 ** BudgetType **   <a name="awscostmanagement-Type-budgets_BudgetPerformanceHistory-BudgetType"></a>
 The type of a budget. It must be one of the following types:
 `COST`, `USAGE`, `RI_UTILIZATION`, `RI_COVERAGE`, `SAVINGS_PLANS_UTILIZATION`, or `SAVINGS_PLANS_COVERAGE`.
Type: String
Valid Values: `USAGE | COST | RI_UTILIZATION | RI_COVERAGE | SAVINGS_PLANS_UTILIZATION | SAVINGS_PLANS_COVERAGE`
Required: No

 ** CostFilters **   <a name="awscostmanagement-Type-budgets_BudgetPerformanceHistory-CostFilters"></a>
The history of the cost filters for a budget during the specified time period.
Type: String to array of strings map
Key Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Key Pattern: `.*`
Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Pattern: `[\S\s]*`
Required: No

 ** CostTypes **   <a name="awscostmanagement-Type-budgets_BudgetPerformanceHistory-CostTypes"></a>
The history of the cost types for a budget during the specified time period.
Type: [CostTypes](API_budgets_CostTypes.md) object
Required: No

 ** FilterExpression **   <a name="awscostmanagement-Type-budgets_BudgetPerformanceHistory-FilterExpression"></a>
The filtering dimensions for the budget and their corresponding values.
Type: [Expression](API_budgets_Expression.md) object
Required: No

 ** Metrics **   <a name="awscostmanagement-Type-budgets_BudgetPerformanceHistory-Metrics"></a>
The definition for how the budget data is aggregated.
Type: Array of strings
Array Members: Maximum number of 1 item.
Valid Values: `BlendedCost | UnblendedCost | AmortizedCost | NetUnblendedCost | NetAmortizedCost | UsageQuantity | NormalizedUsageAmount | Hours`
Required: No

 ** TimeUnit **   <a name="awscostmanagement-Type-budgets_BudgetPerformanceHistory-TimeUnit"></a>
 The time unit of the budget, such as MONTHLY or QUARTERLY.
Type: String
Valid Values: `DAILY | MONTHLY | QUARTERLY | ANNUALLY | CUSTOM`
Required: No

## See Also
<a name="API_budgets_BudgetPerformanceHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/BudgetPerformanceHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/BudgetPerformanceHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/BudgetPerformanceHistory)
