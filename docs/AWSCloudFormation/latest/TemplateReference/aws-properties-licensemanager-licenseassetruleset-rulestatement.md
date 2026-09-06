---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-licenseassetruleset-rulestatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::LicenseAssetRuleSet RuleStatement
<a name="aws-properties-licensemanager-licenseassetruleset-rulestatement"></a>

Rule statement.

## Syntax
<a name="aws-properties-licensemanager-licenseassetruleset-rulestatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-licenseassetruleset-rulestatement-syntax.json"></a>

```
{
  "[InstanceRuleStatement](#cfn-licensemanager-licenseassetruleset-rulestatement-instancerulestatement)" : {{InstanceRuleStatement}},
  "[LicenseConfigurationRuleStatement](#cfn-licensemanager-licenseassetruleset-rulestatement-licenseconfigurationrulestatement)" : {{LicenseConfigurationRuleStatement}},
  "[LicenseRuleStatement](#cfn-licensemanager-licenseassetruleset-rulestatement-licenserulestatement)" : {{LicenseRuleStatement}}
}
```

### YAML
<a name="aws-properties-licensemanager-licenseassetruleset-rulestatement-syntax.yaml"></a>

```
  [InstanceRuleStatement](#cfn-licensemanager-licenseassetruleset-rulestatement-instancerulestatement): {{
    InstanceRuleStatement}}
  [LicenseConfigurationRuleStatement](#cfn-licensemanager-licenseassetruleset-rulestatement-licenseconfigurationrulestatement): {{
    LicenseConfigurationRuleStatement}}
  [LicenseRuleStatement](#cfn-licensemanager-licenseassetruleset-rulestatement-licenserulestatement): {{
    LicenseRuleStatement}}
```

## Properties
<a name="aws-properties-licensemanager-licenseassetruleset-rulestatement-properties"></a>

`InstanceRuleStatement`  <a name="cfn-licensemanager-licenseassetruleset-rulestatement-instancerulestatement"></a>
Instance rule statement.
*Required*: No
*Type*: [InstanceRuleStatement](aws-properties-licensemanager-licenseassetruleset-instancerulestatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LicenseConfigurationRuleStatement`  <a name="cfn-licensemanager-licenseassetruleset-rulestatement-licenseconfigurationrulestatement"></a>
License configuration rule statement.
*Required*: No
*Type*: [LicenseConfigurationRuleStatement](aws-properties-licensemanager-licenseassetruleset-licenseconfigurationrulestatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LicenseRuleStatement`  <a name="cfn-licensemanager-licenseassetruleset-rulestatement-licenserulestatement"></a>
License rule statement.
*Required*: No
*Type*: [LicenseRuleStatement](aws-properties-licensemanager-licenseassetruleset-licenserulestatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
