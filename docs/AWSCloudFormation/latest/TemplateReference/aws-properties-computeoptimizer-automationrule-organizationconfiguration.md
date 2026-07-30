---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-computeoptimizer-automationrule-organizationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ComputeOptimizer::AutomationRule OrganizationConfiguration
<a name="aws-properties-computeoptimizer-automationrule-organizationconfiguration"></a>

Configuration settings for organization-wide automation rules.

## Syntax
<a name="aws-properties-computeoptimizer-automationrule-organizationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-computeoptimizer-automationrule-organizationconfiguration-syntax.json"></a>

```
{
  "[AccountIds](#cfn-computeoptimizer-automationrule-organizationconfiguration-accountids)" : {{[ String, ... ]}},
  "[RuleApplyOrder](#cfn-computeoptimizer-automationrule-organizationconfiguration-ruleapplyorder)" : {{String}}
}
```

### YAML
<a name="aws-properties-computeoptimizer-automationrule-organizationconfiguration-syntax.yaml"></a>

```
  [AccountIds](#cfn-computeoptimizer-automationrule-organizationconfiguration-accountids): {{
    - String}}
  [RuleApplyOrder](#cfn-computeoptimizer-automationrule-organizationconfiguration-ruleapplyorder): {{String}}
```

## Properties
<a name="aws-properties-computeoptimizer-automationrule-organizationconfiguration-properties"></a>

`AccountIds`  <a name="cfn-computeoptimizer-automationrule-organizationconfiguration-accountids"></a>
List of specific AWS account IDs where the organization rule should be applied.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleApplyOrder`  <a name="cfn-computeoptimizer-automationrule-organizationconfiguration-ruleapplyorder"></a>
Specifies when organization rules should be applied relative to account rules.
*Required*: No
*Type*: String
*Allowed values*: `BeforeAccountRules | AfterAccountRules`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
