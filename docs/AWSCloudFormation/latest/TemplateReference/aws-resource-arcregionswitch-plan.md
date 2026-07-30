---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-arcregionswitch-plan.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan
<a name="aws-resource-arcregionswitch-plan"></a>

Represents a Region switch plan. A plan defines the steps required to shift traffic from one AWS Region to another.

## Syntax
<a name="aws-resource-arcregionswitch-plan-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-arcregionswitch-plan-syntax.json"></a>

```
{
  "Type" : "AWS::ARCRegionSwitch::Plan",
  "Properties" : {
      "[AssociatedAlarms](#cfn-arcregionswitch-plan-associatedalarms)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Description](#cfn-arcregionswitch-plan-description)" : {{String}},
      "[ExecutionRole](#cfn-arcregionswitch-plan-executionrole)" : {{String}},
      "[Name](#cfn-arcregionswitch-plan-name)" : {{String}},
      "[PrimaryRegion](#cfn-arcregionswitch-plan-primaryregion)" : {{String}},
      "[RecoveryApproach](#cfn-arcregionswitch-plan-recoveryapproach)" : {{String}},
      "[RecoveryTimeObjectiveMinutes](#cfn-arcregionswitch-plan-recoverytimeobjectiveminutes)" : {{Number}},
      "[Regions](#cfn-arcregionswitch-plan-regions)" : {{[ String, ... ]}},
      "[ReportConfiguration](#cfn-arcregionswitch-plan-reportconfiguration)" : {{ReportConfiguration}},
      "[Tags](#cfn-arcregionswitch-plan-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Triggers](#cfn-arcregionswitch-plan-triggers)" : {{[ Trigger, ... ]}},
      "[Workflows](#cfn-arcregionswitch-plan-workflows)" : {{[ Workflow, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-arcregionswitch-plan-syntax.yaml"></a>

```
Type: AWS::ARCRegionSwitch::Plan
Properties:
  [AssociatedAlarms](#cfn-arcregionswitch-plan-associatedalarms): {{
    {{Key}}: {{Value}}}}
  [Description](#cfn-arcregionswitch-plan-description): {{String}}
  [ExecutionRole](#cfn-arcregionswitch-plan-executionrole): {{String}}
  [Name](#cfn-arcregionswitch-plan-name): {{String}}
  [PrimaryRegion](#cfn-arcregionswitch-plan-primaryregion): {{String}}
  [RecoveryApproach](#cfn-arcregionswitch-plan-recoveryapproach): {{String}}
  [RecoveryTimeObjectiveMinutes](#cfn-arcregionswitch-plan-recoverytimeobjectiveminutes): {{Number}}
  [Regions](#cfn-arcregionswitch-plan-regions): {{
    - String}}
  [ReportConfiguration](#cfn-arcregionswitch-plan-reportconfiguration): {{
    ReportConfiguration}}
  [Tags](#cfn-arcregionswitch-plan-tags): {{
    {{Key}}: {{Value}}}}
  [Triggers](#cfn-arcregionswitch-plan-triggers): {{
    - Trigger}}
  [Workflows](#cfn-arcregionswitch-plan-workflows): {{
    - Workflow}}
```

## Properties
<a name="aws-resource-arcregionswitch-plan-properties"></a>

`AssociatedAlarms`  <a name="cfn-arcregionswitch-plan-associatedalarms"></a>
The associated application health alarms for a plan.
*Required*: No
*Type*: Object of [AssociatedAlarm](aws-properties-arcregionswitch-plan-associatedalarm.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-arcregionswitch-plan-description"></a>
The description for a plan.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRole`  <a name="cfn-arcregionswitch-plan-executionrole"></a>
The execution role for a plan.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-arcregionswitch-plan-name"></a>
The name for a plan.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrimaryRegion`  <a name="cfn-arcregionswitch-plan-primaryregion"></a>
The primary Region for a plan.
*Required*: No
*Type*: String
*Pattern*: `^[a-z]{2}-[a-z-]+-\d+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecoveryApproach`  <a name="cfn-arcregionswitch-plan-recoveryapproach"></a>
The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).
*Required*: Yes
*Type*: String
*Allowed values*: `activeActive | activePassive`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecoveryTimeObjectiveMinutes`  <a name="cfn-arcregionswitch-plan-recoverytimeobjectiveminutes"></a>
The recovery time objective for a plan.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `10080`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regions`  <a name="cfn-arcregionswitch-plan-regions"></a>
The AWS Regions for a plan.
*Required*: Yes
*Type*: Array of String
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReportConfiguration`  <a name="cfn-arcregionswitch-plan-reportconfiguration"></a>
The report configuration for a plan.
*Required*: No
*Type*: [ReportConfiguration](aws-properties-arcregionswitch-plan-reportconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-arcregionswitch-plan-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Triggers`  <a name="cfn-arcregionswitch-plan-triggers"></a>
The triggers for a plan.
*Required*: No
*Type*: Array of [Trigger](aws-properties-arcregionswitch-plan-trigger.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Workflows`  <a name="cfn-arcregionswitch-plan-workflows"></a>
The workflows for a plan.
*Required*: Yes
*Type*: Array of [Workflow](aws-properties-arcregionswitch-plan-workflow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-arcregionswitch-plan-return-values"></a>

### Ref
<a name="aws-resource-arcregionswitch-plan-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the plan.

### Fn::GetAtt
<a name="aws-resource-arcregionswitch-plan-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-arcregionswitch-plan-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the plan.

`Owner`  <a name="Owner-fn::getatt"></a>
The owner of a plan.

`PlanHealthChecks`  <a name="PlanHealthChecks-fn::getatt"></a>
Property description not available.

`Version`  <a name="Version-fn::getatt"></a>
The version for the plan.
