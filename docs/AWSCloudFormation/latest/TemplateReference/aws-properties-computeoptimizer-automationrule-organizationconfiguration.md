---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-computeoptimizer-automationrule-organizationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ComputeOptimizer::AutomationRule OrganizationConfiguration

Configuration settings that define the scope of an organization-wide automation rule. Each organizational unit (OU) list can contain up to 150 OUs or organization roots, and each account list can contain up to 50 accounts. Each included OU or organization root must have an effective organization rule mode of `AnyAllowed`. Exclusions take precedence over inclusions. An account that is in an included OU and is also excluded is excluded. The rule doesn't apply to the management account when the account is reached through an OU or the organization root.

## Syntax
<a name="aws-properties-computeoptimizer-automationrule-organizationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-computeoptimizer-automationrule-organizationconfiguration-syntax.json"></a>

```json
{
  "[AccountIds](#cfn-computeoptimizer-automationrule-organizationconfiguration-accountids)" : {{[ String, ... ]}},
  "[ExcludedAccountIds](#cfn-computeoptimizer-automationrule-organizationconfiguration-excludedaccountids)" : {{[ String, ... ]}},
  "[ExcludedOrganizationalUnitIds](#cfn-computeoptimizer-automationrule-organizationconfiguration-excludedorganizationalunitids)" : {{[ String, ... ]}},
  "[OrganizationalUnitIds](#cfn-computeoptimizer-automationrule-organizationconfiguration-organizationalunitids)" : {{[ String, ... ]}},
  "[RuleApplyOrder](#cfn-computeoptimizer-automationrule-organizationconfiguration-ruleapplyorder)" : {{String}}
}
```

### YAML
<a name="aws-properties-computeoptimizer-automationrule-organizationconfiguration-syntax.yaml"></a>

```yaml
  [AccountIds](#cfn-computeoptimizer-automationrule-organizationconfiguration-accountids): {{
    - String}}
  [ExcludedAccountIds](#cfn-computeoptimizer-automationrule-organizationconfiguration-excludedaccountids): {{
    - String}}
  [ExcludedOrganizationalUnitIds](#cfn-computeoptimizer-automationrule-organizationconfiguration-excludedorganizationalunitids): {{
    - String}}
  [OrganizationalUnitIds](#cfn-computeoptimizer-automationrule-organizationconfiguration-organizationalunitids): {{
    - String}}
  [RuleApplyOrder](#cfn-computeoptimizer-automationrule-organizationconfiguration-ruleapplyorder): {{String}}
```

## Properties
<a name="aws-properties-computeoptimizer-automationrule-organizationconfiguration-properties"></a>

`AccountIds`  <a name="cfn-computeoptimizer-automationrule-organizationconfiguration-accountids"></a>
The specific AWS account IDs where the organization rule should be applied. You can specify up to 50 account IDs.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludedAccountIds`  <a name="cfn-computeoptimizer-automationrule-organizationconfiguration-excludedaccountids"></a>
The AWS account IDs to exclude from the organization rule scope. You can specify up to 50 account IDs. An excluded account remains excluded even if it is in an included OU.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludedOrganizationalUnitIds`  <a name="cfn-computeoptimizer-automationrule-organizationconfiguration-excludedorganizationalunitids"></a>
The organizational unit (OU) or organization root IDs to exclude from the organization rule scope. The rule doesn't apply to accounts in the specified OUs or their child OUs. You can specify up to 150 IDs.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrganizationalUnitIds`  <a name="cfn-computeoptimizer-automationrule-organizationconfiguration-organizationalunitids"></a>
The organizational unit (OU) or organization root IDs to include in the organization rule scope. The rule applies to accounts in the specified OUs and their child OUs. You can specify up to 150 IDs.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleApplyOrder`  <a name="cfn-computeoptimizer-automationrule-organizationconfiguration-ruleapplyorder"></a>
Specifies when organization rules should be applied relative to account rules.
*Required*: No
*Type*: String
*Allowed values*: `BeforeAccountRules | AfterAccountRules`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
