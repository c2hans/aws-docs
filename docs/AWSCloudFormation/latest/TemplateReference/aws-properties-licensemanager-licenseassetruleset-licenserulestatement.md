---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-licenseassetruleset-licenserulestatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::LicenseAssetRuleSet LicenseRuleStatement
<a name="aws-properties-licensemanager-licenseassetruleset-licenserulestatement"></a>

License rule statement.

## Syntax
<a name="aws-properties-licensemanager-licenseassetruleset-licenserulestatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-licenseassetruleset-licenserulestatement-syntax.json"></a>

```
{
  "[AndRuleStatement](#cfn-licensemanager-licenseassetruleset-licenserulestatement-andrulestatement)" : {{AndRuleStatement}},
  "[MatchingRuleStatement](#cfn-licensemanager-licenseassetruleset-licenserulestatement-matchingrulestatement)" : {{MatchingRuleStatement}},
  "[OrRuleStatement](#cfn-licensemanager-licenseassetruleset-licenserulestatement-orrulestatement)" : {{OrRuleStatement}}
}
```

### YAML
<a name="aws-properties-licensemanager-licenseassetruleset-licenserulestatement-syntax.yaml"></a>

```
  [AndRuleStatement](#cfn-licensemanager-licenseassetruleset-licenserulestatement-andrulestatement): {{
    AndRuleStatement}}
  [MatchingRuleStatement](#cfn-licensemanager-licenseassetruleset-licenserulestatement-matchingrulestatement): {{
    MatchingRuleStatement}}
  [OrRuleStatement](#cfn-licensemanager-licenseassetruleset-licenserulestatement-orrulestatement): {{
    OrRuleStatement}}
```

## Properties
<a name="aws-properties-licensemanager-licenseassetruleset-licenserulestatement-properties"></a>

`AndRuleStatement`  <a name="cfn-licensemanager-licenseassetruleset-licenserulestatement-andrulestatement"></a>
AND rule statement.
*Required*: No
*Type*: [AndRuleStatement](aws-properties-licensemanager-licenseassetruleset-andrulestatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchingRuleStatement`  <a name="cfn-licensemanager-licenseassetruleset-licenserulestatement-matchingrulestatement"></a>
Matching rule statement.
*Required*: No
*Type*: [MatchingRuleStatement](aws-properties-licensemanager-licenseassetruleset-matchingrulestatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrRuleStatement`  <a name="cfn-licensemanager-licenseassetruleset-licenserulestatement-orrulestatement"></a>
OR rule statement.
*Required*: No
*Type*: [OrRuleStatement](aws-properties-licensemanager-licenseassetruleset-orrulestatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
