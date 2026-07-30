---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-budgets-budgetsaction-actionthreshold.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Budgets::BudgetsAction ActionThreshold
<a name="aws-properties-budgets-budgetsaction-actionthreshold"></a>

The trigger threshold of the action.

## Syntax
<a name="aws-properties-budgets-budgetsaction-actionthreshold-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-budgets-budgetsaction-actionthreshold-syntax.json"></a>

```
{
  "[Type](#cfn-budgets-budgetsaction-actionthreshold-type)" : {{String}},
  "[Value](#cfn-budgets-budgetsaction-actionthreshold-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-budgets-budgetsaction-actionthreshold-syntax.yaml"></a>

```
  [Type](#cfn-budgets-budgetsaction-actionthreshold-type): {{String}}
  [Value](#cfn-budgets-budgetsaction-actionthreshold-value): {{Number}}
```

## Properties
<a name="aws-properties-budgets-budgetsaction-actionthreshold-properties"></a>

`Type`  <a name="cfn-budgets-budgetsaction-actionthreshold-type"></a>
The type of threshold for a notification.
*Required*: Yes
*Type*: String
*Allowed values*: `PERCENTAGE | ABSOLUTE_VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-budgets-budgetsaction-actionthreshold-value"></a>
The threshold of a notification.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
