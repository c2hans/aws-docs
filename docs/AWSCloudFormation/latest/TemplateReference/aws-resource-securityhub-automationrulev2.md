---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-automationrulev2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2
<a name="aws-resource-securityhub-automationrulev2"></a>

Creates a V2 automation rule.

## Syntax
<a name="aws-resource-securityhub-automationrulev2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-automationrulev2-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::AutomationRuleV2",
  "Properties" : {
      "[Actions](#cfn-securityhub-automationrulev2-actions)" : {{[ AutomationRulesActionV2, ... ]}},
      "[Criteria](#cfn-securityhub-automationrulev2-criteria)" : {{Criteria}},
      "[Description](#cfn-securityhub-automationrulev2-description)" : {{String}},
      "[RuleName](#cfn-securityhub-automationrulev2-rulename)" : {{String}},
      "[RuleOrder](#cfn-securityhub-automationrulev2-ruleorder)" : {{Number}},
      "[RuleStatus](#cfn-securityhub-automationrulev2-rulestatus)" : {{String}},
      "[Tags](#cfn-securityhub-automationrulev2-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-automationrulev2-syntax.yaml"></a>

```
Type: AWS::SecurityHub::AutomationRuleV2
Properties:
  [Actions](#cfn-securityhub-automationrulev2-actions): {{
    - AutomationRulesActionV2}}
  [Criteria](#cfn-securityhub-automationrulev2-criteria): {{
    Criteria}}
  [Description](#cfn-securityhub-automationrulev2-description): {{String}}
  [RuleName](#cfn-securityhub-automationrulev2-rulename): {{String}}
  [RuleOrder](#cfn-securityhub-automationrulev2-ruleorder): {{Number}}
  [RuleStatus](#cfn-securityhub-automationrulev2-rulestatus): {{String}}
  [Tags](#cfn-securityhub-automationrulev2-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-securityhub-automationrulev2-properties"></a>

`Actions`  <a name="cfn-securityhub-automationrulev2-actions"></a>
A list of actions to be performed when the rule criteria is met.
*Required*: Yes
*Type*: Array of [AutomationRulesActionV2](aws-properties-securityhub-automationrulev2-automationrulesactionv2.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Criteria`  <a name="cfn-securityhub-automationrulev2-criteria"></a>
The filtering type and configuration of the automation rule.
*Required*: Yes
*Type*: [Criteria](aws-properties-securityhub-automationrulev2-criteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-securityhub-automationrulev2-description"></a>
A description of the V2 automation rule.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleName`  <a name="cfn-securityhub-automationrulev2-rulename"></a>
The name of the V2 automation rule.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleOrder`  <a name="cfn-securityhub-automationrulev2-ruleorder"></a>
The value for the rule priority.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleStatus`  <a name="cfn-securityhub-automationrulev2-rulestatus"></a>
The status of the V2 automation rule.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-securityhub-automationrulev2-tags"></a>
A list of key-value pairs associated with the V2 automation rule.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]{1,128}$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityhub-automationrulev2-return-values"></a>

### Ref
<a name="aws-resource-securityhub-automationrulev2-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `AutomationRuleV2Arn` for the `AutomationRuleV2Arn` resource created: `arn:aws:securityhub:region:123456789012:automationrulev2/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityhub-automationrulev2-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityhub-automationrulev2-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the V2 automation rule was created.

`RuleArn`  <a name="RuleArn-fn::getatt"></a>
The ARN of the V2 automation rule.

`RuleId`  <a name="RuleId-fn::getatt"></a>
The ID of the V2 automation rule.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the V2 automation rule was updated.
