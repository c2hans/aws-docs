---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-budget-budgetactiontoadd.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Budget BudgetActionToAdd
<a name="aws-properties-deadline-budget-budgetactiontoadd"></a>

The budget action to add.

## Syntax
<a name="aws-properties-deadline-budget-budgetactiontoadd-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-budget-budgetactiontoadd-syntax.json"></a>

```
{
  "[Description](#cfn-deadline-budget-budgetactiontoadd-description)" : {{String}},
  "[ThresholdPercentage](#cfn-deadline-budget-budgetactiontoadd-thresholdpercentage)" : {{Number}},
  "[Type](#cfn-deadline-budget-budgetactiontoadd-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-budget-budgetactiontoadd-syntax.yaml"></a>

```
  [Description](#cfn-deadline-budget-budgetactiontoadd-description): {{String}}
  [ThresholdPercentage](#cfn-deadline-budget-budgetactiontoadd-thresholdpercentage): {{Number}}
  [Type](#cfn-deadline-budget-budgetactiontoadd-type): {{String}}
```

## Properties
<a name="aws-properties-deadline-budget-budgetactiontoadd-properties"></a>

`Description`  <a name="cfn-deadline-budget-budgetactiontoadd-description"></a>
A description for the budget action to add.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdPercentage`  <a name="cfn-deadline-budget-budgetactiontoadd-thresholdpercentage"></a>
The percentage threshold for the budget action to add.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-deadline-budget-budgetactiontoadd-type"></a>
The type of budget action to add.
*Required*: Yes
*Type*: String
*Allowed values*: `STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
