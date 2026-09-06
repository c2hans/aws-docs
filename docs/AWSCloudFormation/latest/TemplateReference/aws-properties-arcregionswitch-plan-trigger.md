---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-trigger.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan Trigger
<a name="aws-properties-arcregionswitch-plan-trigger"></a>

Defines a condition that can automatically trigger the execution of a Region switch plan.

## Syntax
<a name="aws-properties-arcregionswitch-plan-trigger-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-trigger-syntax.json"></a>

```
{
  "[Action](#cfn-arcregionswitch-plan-trigger-action)" : {{String}},
  "[Conditions](#cfn-arcregionswitch-plan-trigger-conditions)" : {{[ TriggerCondition, ... ]}},
  "[Description](#cfn-arcregionswitch-plan-trigger-description)" : {{String}},
  "[MinDelayMinutesBetweenExecutions](#cfn-arcregionswitch-plan-trigger-mindelayminutesbetweenexecutions)" : {{Number}},
  "[TargetRegion](#cfn-arcregionswitch-plan-trigger-targetregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-trigger-syntax.yaml"></a>

```
  [Action](#cfn-arcregionswitch-plan-trigger-action): {{String}}
  [Conditions](#cfn-arcregionswitch-plan-trigger-conditions): {{
    - TriggerCondition}}
  [Description](#cfn-arcregionswitch-plan-trigger-description): {{String}}
  [MinDelayMinutesBetweenExecutions](#cfn-arcregionswitch-plan-trigger-mindelayminutesbetweenexecutions): {{Number}}
  [TargetRegion](#cfn-arcregionswitch-plan-trigger-targetregion): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-trigger-properties"></a>

`Action`  <a name="cfn-arcregionswitch-plan-trigger-action"></a>
The action to perform when the trigger fires. Valid values include `activate` and `deactivate`.
*Required*: Yes
*Type*: String
*Allowed values*: `activate | deactivate | postRecovery`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Conditions`  <a name="cfn-arcregionswitch-plan-trigger-conditions"></a>
The conditions that must be met for the trigger to fire.
*Required*: Yes
*Type*: Array of [TriggerCondition](aws-properties-arcregionswitch-plan-triggercondition.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-arcregionswitch-plan-trigger-description"></a>
The description for a trigger.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinDelayMinutesBetweenExecutions`  <a name="cfn-arcregionswitch-plan-trigger-mindelayminutesbetweenexecutions"></a>
The minimum time, in minutes, that must elapse between automatic executions of the plan.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetRegion`  <a name="cfn-arcregionswitch-plan-trigger-targetregion"></a>
The AWS Region for a trigger.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z]{2}-[a-z-]+-\d+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
