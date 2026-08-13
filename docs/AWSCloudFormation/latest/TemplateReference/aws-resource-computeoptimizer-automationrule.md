---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-computeoptimizer-automationrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ComputeOptimizer::AutomationRule
<a name="aws-resource-computeoptimizer-automationrule"></a>

The `AWS::ComputeOptimizer::AutomationRule` resource specifies an automation rule that automatically implements recommended actions based on your defined criteria and schedule.

## Syntax
<a name="aws-resource-computeoptimizer-automationrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-computeoptimizer-automationrule-syntax.json"></a>

```
{
  "Type" : "AWS::ComputeOptimizer::AutomationRule",
  "Properties" : {
      "[Criteria](#cfn-computeoptimizer-automationrule-criteria)" : {{Criteria}},
      "[Description](#cfn-computeoptimizer-automationrule-description)" : {{String}},
      "[Name](#cfn-computeoptimizer-automationrule-name)" : {{String}},
      "[OrganizationConfiguration](#cfn-computeoptimizer-automationrule-organizationconfiguration)" : {{OrganizationConfiguration}},
      "[Priority](#cfn-computeoptimizer-automationrule-priority)" : {{String}},
      "[RecommendedActionTypes](#cfn-computeoptimizer-automationrule-recommendedactiontypes)" : {{[ String, ... ]}},
      "[RuleType](#cfn-computeoptimizer-automationrule-ruletype)" : {{String}},
      "[Schedule](#cfn-computeoptimizer-automationrule-schedule)" : {{Schedule}},
      "[Status](#cfn-computeoptimizer-automationrule-status)" : {{String}},
      "[Tags](#cfn-computeoptimizer-automationrule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-computeoptimizer-automationrule-syntax.yaml"></a>

```
Type: AWS::ComputeOptimizer::AutomationRule
Properties:
  [Criteria](#cfn-computeoptimizer-automationrule-criteria): {{
    Criteria}}
  [Description](#cfn-computeoptimizer-automationrule-description): {{String}}
  [Name](#cfn-computeoptimizer-automationrule-name): {{String}}
  [OrganizationConfiguration](#cfn-computeoptimizer-automationrule-organizationconfiguration): {{
    OrganizationConfiguration}}
  [Priority](#cfn-computeoptimizer-automationrule-priority): {{String}}
  [RecommendedActionTypes](#cfn-computeoptimizer-automationrule-recommendedactiontypes): {{
    - String}}
  [RuleType](#cfn-computeoptimizer-automationrule-ruletype): {{String}}
  [Schedule](#cfn-computeoptimizer-automationrule-schedule): {{
    Schedule}}
  [Status](#cfn-computeoptimizer-automationrule-status): {{String}}
  [Tags](#cfn-computeoptimizer-automationrule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-computeoptimizer-automationrule-properties"></a>

`Criteria`  <a name="cfn-computeoptimizer-automationrule-criteria"></a>
 A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time. You can specify up to 20 conditions per filter criteria and 20 values per condition.
*Required*: No
*Type*: [Criteria](aws-properties-computeoptimizer-automationrule-criteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-computeoptimizer-automationrule-description"></a>
A description of the automation rule.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-\s@\.]*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-computeoptimizer-automationrule-name"></a>
The name of the automation rule.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]*$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrganizationConfiguration`  <a name="cfn-computeoptimizer-automationrule-organizationconfiguration"></a>
Configuration settings for organization-wide rules.
*Required*: No
*Type*: [OrganizationConfiguration](aws-properties-computeoptimizer-automationrule-organizationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Priority`  <a name="cfn-computeoptimizer-automationrule-priority"></a>
A string representation of a decimal number between 0 and 1 (having up to 30 digits after the decimal point) that determines the priority of the rule. When multiple rules match the same recommended action, Compute Optimizer assigns the action to the rule with the lowest priority value (highest priority), even if that rule is scheduled to run later than other matching rules.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecommendedActionTypes`  <a name="cfn-computeoptimizer-automationrule-recommendedactiontypes"></a>
List of recommended action types that this rule can execute.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `SnapshotAndDeleteUnattachedEbsVolume | UpgradeEbsVolumeType`
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleType`  <a name="cfn-computeoptimizer-automationrule-ruletype"></a>
The type of automation rule (OrganizationRule or AccountRule).
*Required*: Yes
*Type*: String
*Allowed values*: `AccountRule | OrganizationRule`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schedule`  <a name="cfn-computeoptimizer-automationrule-schedule"></a>
The schedule configuration for when the automation rule should execute.
*Required*: Yes
*Type*: [Schedule](aws-properties-computeoptimizer-automationrule-schedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-computeoptimizer-automationrule-status"></a>
The current status of the automation rule (Active or Inactive).
*Required*: Yes
*Type*: String
*Allowed values*: `Active | Inactive`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-computeoptimizer-automationrule-tags"></a>
 The tags to associate with the rule.
*Required*: No
*Type*: Array of [Tag](aws-properties-computeoptimizer-automationrule-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-computeoptimizer-automationrule-return-values"></a>

### Ref
<a name="aws-resource-computeoptimizer-automationrule-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the automation rule.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-computeoptimizer-automationrule-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-computeoptimizer-automationrule-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
The 12-digit AWS account ID that owns this automation rule.

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
The timestamp when the automation rule was created.

`LastUpdatedTimestamp`  <a name="LastUpdatedTimestamp-fn::getatt"></a>
The timestamp when the automation rule was last updated.

`RuleArn`  <a name="RuleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the automation rule.

`RuleId`  <a name="RuleId-fn::getatt"></a>
The unique identifier of the automation rule.

`RuleRevision`  <a name="RuleRevision-fn::getatt"></a>
The revision number of the automation rule.
