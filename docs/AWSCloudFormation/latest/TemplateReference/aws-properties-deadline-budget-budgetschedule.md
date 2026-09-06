---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-budget-budgetschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Budget BudgetSchedule
<a name="aws-properties-deadline-budget-budgetschedule"></a>

The start and end time of the budget.

## Syntax
<a name="aws-properties-deadline-budget-budgetschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-budget-budgetschedule-syntax.json"></a>

```
{
  "[Fixed](#cfn-deadline-budget-budgetschedule-fixed)" : {{FixedBudgetSchedule}}
}
```

### YAML
<a name="aws-properties-deadline-budget-budgetschedule-syntax.yaml"></a>

```
  [Fixed](#cfn-deadline-budget-budgetschedule-fixed): {{
    FixedBudgetSchedule}}
```

## Properties
<a name="aws-properties-deadline-budget-budgetschedule-properties"></a>

`Fixed`  <a name="cfn-deadline-budget-budgetschedule-fixed"></a>
The fixed start and end time of the budget's schedule.
*Required*: Yes
*Type*: [FixedBudgetSchedule](aws-properties-deadline-budget-fixedbudgetschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
