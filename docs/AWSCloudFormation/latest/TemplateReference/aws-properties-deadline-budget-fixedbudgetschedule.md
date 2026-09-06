---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-budget-fixedbudgetschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Budget FixedBudgetSchedule
<a name="aws-properties-deadline-budget-fixedbudgetschedule"></a>

The details of a fixed budget schedule.

## Syntax
<a name="aws-properties-deadline-budget-fixedbudgetschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-budget-fixedbudgetschedule-syntax.json"></a>

```
{
  "[EndTime](#cfn-deadline-budget-fixedbudgetschedule-endtime)" : {{String}},
  "[StartTime](#cfn-deadline-budget-fixedbudgetschedule-starttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-budget-fixedbudgetschedule-syntax.yaml"></a>

```
  [EndTime](#cfn-deadline-budget-fixedbudgetschedule-endtime): {{String}}
  [StartTime](#cfn-deadline-budget-fixedbudgetschedule-starttime): {{String}}
```

## Properties
<a name="aws-properties-deadline-budget-fixedbudgetschedule-properties"></a>

`EndTime`  <a name="cfn-deadline-budget-fixedbudgetschedule-endtime"></a>
When the budget ends.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTime`  <a name="cfn-deadline-budget-fixedbudgetschedule-starttime"></a>
When the budget starts.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
