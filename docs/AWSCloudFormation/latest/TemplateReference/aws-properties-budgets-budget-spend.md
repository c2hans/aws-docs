---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budget-spend.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::Budget Spend
<a name="aws-properties-budgets-budget-spend"></a>

The amount of cost or usage that's measured for a budget.

*Cost example:* A `Spend` for `3 USD` of costs has the following parameters:
+ An `Amount` of `3`
+ A `Unit` of `USD`

*Usage example:* A `Spend` for `3 GB` of S3 usage has the following parameters:
+ An `Amount` of `3`
+ A `Unit` of `GB`

## Syntax
<a name="aws-properties-budgets-budget-spend-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budget-spend-syntax.json"></a>

```
{
  "[Amount](#cfn-budgets-budget-spend-amount)" : {{Number}},
  "[Unit](#cfn-budgets-budget-spend-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-budgets-budget-spend-syntax.yaml"></a>

```
  [Amount](#cfn-budgets-budget-spend-amount): {{Number}}
  [Unit](#cfn-budgets-budget-spend-unit): {{String}}
```

## Properties
<a name="aws-properties-budgets-budget-spend-properties"></a>

`Amount`  <a name="cfn-budgets-budget-spend-amount"></a>
The cost or usage amount that's associated with a budget forecast, actual spend, or budget threshold.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-budgets-budget-spend-unit"></a>
The unit of measurement that's used for the budget forecast, actual spend, or budget threshold.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-budgets-budget-spend--seealso"></a>
+ [Spend](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Spend.html) in the *AWS Cost Explorer Service Cost Management APIs*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
