---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budget-historicaloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::Budget HistoricalOptions
<a name="aws-properties-budgets-budget-historicaloptions"></a>

The parameters that define or describe the historical data that your auto-adjusting budget is based on.

## Syntax
<a name="aws-properties-budgets-budget-historicaloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budget-historicaloptions-syntax.json"></a>

```
{
  "[BudgetAdjustmentPeriod](#cfn-budgets-budget-historicaloptions-budgetadjustmentperiod)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-budgets-budget-historicaloptions-syntax.yaml"></a>

```
  [BudgetAdjustmentPeriod](#cfn-budgets-budget-historicaloptions-budgetadjustmentperiod): {{Integer}}
```

## Properties
<a name="aws-properties-budgets-budget-historicaloptions-properties"></a>

`BudgetAdjustmentPeriod`  <a name="cfn-budgets-budget-historicaloptions-budgetadjustmentperiod"></a>
The number of budget periods included in the moving-average calculation that determines your auto-adjusted budget amount. The maximum value depends on the `TimeUnit` granularity of the budget:
+ For the `DAILY` granularity, the maximum value is `60`.
+ For the `MONTHLY` granularity, the maximum value is `12`.
+ For the `QUARTERLY` granularity, the maximum value is `4`.
+ For the `ANNUALLY` granularity, the maximum value is `1`.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
