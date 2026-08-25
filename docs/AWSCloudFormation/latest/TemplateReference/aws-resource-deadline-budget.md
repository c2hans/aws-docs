---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-budget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Budget
<a name="aws-resource-deadline-budget"></a>

Creates a budget to set spending thresholds for your rendering activity.

## Syntax
<a name="aws-resource-deadline-budget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-budget-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::Budget",
  "Properties" : {
      "[Actions](#cfn-deadline-budget-actions)" : {{[ BudgetActionToAdd, ... ]}},
      "[ApproximateDollarLimit](#cfn-deadline-budget-approximatedollarlimit)" : {{Number}},
      "[Description](#cfn-deadline-budget-description)" : {{String}},
      "[DisplayName](#cfn-deadline-budget-displayname)" : {{String}},
      "[FarmId](#cfn-deadline-budget-farmid)" : {{String}},
      "[Schedule](#cfn-deadline-budget-schedule)" : {{BudgetSchedule}},
      "[Tags](#cfn-deadline-budget-tags)" : {{[ Tag, ... ]}},
      "[UsageTrackingResource](#cfn-deadline-budget-usagetrackingresource)" : {{UsageTrackingResource}}
    }
}
```

### YAML
<a name="aws-resource-deadline-budget-syntax.yaml"></a>

```
Type: AWS::Deadline::Budget
Properties:
  [Actions](#cfn-deadline-budget-actions): {{
    - BudgetActionToAdd}}
  [ApproximateDollarLimit](#cfn-deadline-budget-approximatedollarlimit): {{Number}}
  [Description](#cfn-deadline-budget-description): {{String}}
  [DisplayName](#cfn-deadline-budget-displayname): {{String}}
  [FarmId](#cfn-deadline-budget-farmid): {{String}}
  [Schedule](#cfn-deadline-budget-schedule): {{
    BudgetSchedule}}
  [Tags](#cfn-deadline-budget-tags): {{
    - Tag}}
  [UsageTrackingResource](#cfn-deadline-budget-usagetrackingresource): {{
    UsageTrackingResource}}
```

## Properties
<a name="aws-resource-deadline-budget-properties"></a>

`Actions`  <a name="cfn-deadline-budget-actions"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [BudgetActionToAdd](aws-properties-deadline-budget-budgetactiontoadd.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApproximateDollarLimit`  <a name="cfn-deadline-budget-approximatedollarlimit"></a>
The approximate dollar limit of the budget.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-deadline-budget-description"></a>
The description of the budget summary.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-deadline-budget-displayname"></a>
The display name of the budget summary to update.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FarmId`  <a name="cfn-deadline-budget-farmid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^farm-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Schedule`  <a name="cfn-deadline-budget-schedule"></a>
Property description not available.
*Required*: Yes
*Type*: [BudgetSchedule](aws-properties-deadline-budget-budgetschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-deadline-budget-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-deadline-budget-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsageTrackingResource`  <a name="cfn-deadline-budget-usagetrackingresource"></a>
The resource used to track expenditure in the budget.
*Required*: Yes
*Type*: [UsageTrackingResource](aws-properties-deadline-budget-usagetrackingresource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-deadline-budget-return-values"></a>

### Ref
<a name="aws-resource-deadline-budget-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-deadline-budget-return-values-fn--getatt"></a>

####
<a name="aws-resource-deadline-budget-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`BudgetId`  <a name="BudgetId-fn::getatt"></a>
The budget ID.

`Status`  <a name="Status-fn::getatt"></a>
The status of the budget.
+ `ACTIVE`–The budget is being evaluated.
+ `INACTIVE`–The budget is inactive. This can include Expired, Canceled, or deleted Deleted statuses.
