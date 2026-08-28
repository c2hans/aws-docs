---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-licenseassetruleset-licenseassetrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::LicenseAssetRuleSet LicenseAssetRule
<a name="aws-properties-licensemanager-licenseassetruleset-licenseassetrule"></a>

License asset rule.

## Syntax
<a name="aws-properties-licensemanager-licenseassetruleset-licenseassetrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-licenseassetruleset-licenseassetrule-syntax.json"></a>

```
{
  "[RuleStatement](#cfn-licensemanager-licenseassetruleset-licenseassetrule-rulestatement)" : {{RuleStatement}}
}
```

### YAML
<a name="aws-properties-licensemanager-licenseassetruleset-licenseassetrule-syntax.yaml"></a>

```
  [RuleStatement](#cfn-licensemanager-licenseassetruleset-licenseassetrule-rulestatement): {{
    RuleStatement}}
```

## Properties
<a name="aws-properties-licensemanager-licenseassetruleset-licenseassetrule-properties"></a>

`RuleStatement`  <a name="cfn-licensemanager-licenseassetruleset-licenseassetrule-rulestatement"></a>
Rule statement.
*Required*: Yes
*Type*: [RuleStatement](aws-properties-licensemanager-licenseassetruleset-rulestatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
