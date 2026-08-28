---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-licenseassetruleset-instancerulestatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::LicenseAssetRuleSet InstanceRuleStatement
<a name="aws-properties-licensemanager-licenseassetruleset-instancerulestatement"></a>

Instance rule statement.

## Syntax
<a name="aws-properties-licensemanager-licenseassetruleset-instancerulestatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-licenseassetruleset-instancerulestatement-syntax.json"></a>

```
{
  "[AndRuleStatement](#cfn-licensemanager-licenseassetruleset-instancerulestatement-andrulestatement)" : {{AndRuleStatement}},
  "[MatchingRuleStatement](#cfn-licensemanager-licenseassetruleset-instancerulestatement-matchingrulestatement)" : {{MatchingRuleStatement}},
  "[OrRuleStatement](#cfn-licensemanager-licenseassetruleset-instancerulestatement-orrulestatement)" : {{OrRuleStatement}}
}
```

### YAML
<a name="aws-properties-licensemanager-licenseassetruleset-instancerulestatement-syntax.yaml"></a>

```
  [AndRuleStatement](#cfn-licensemanager-licenseassetruleset-instancerulestatement-andrulestatement): {{
    AndRuleStatement}}
  [MatchingRuleStatement](#cfn-licensemanager-licenseassetruleset-instancerulestatement-matchingrulestatement): {{
    MatchingRuleStatement}}
  [OrRuleStatement](#cfn-licensemanager-licenseassetruleset-instancerulestatement-orrulestatement): {{
    OrRuleStatement}}
```

## Properties
<a name="aws-properties-licensemanager-licenseassetruleset-instancerulestatement-properties"></a>

`AndRuleStatement`  <a name="cfn-licensemanager-licenseassetruleset-instancerulestatement-andrulestatement"></a>
AND rule statement.
*Required*: No
*Type*: [AndRuleStatement](aws-properties-licensemanager-licenseassetruleset-andrulestatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchingRuleStatement`  <a name="cfn-licensemanager-licenseassetruleset-instancerulestatement-matchingrulestatement"></a>
Matching rule statement.
*Required*: No
*Type*: [MatchingRuleStatement](aws-properties-licensemanager-licenseassetruleset-matchingrulestatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrRuleStatement`  <a name="cfn-licensemanager-licenseassetruleset-instancerulestatement-orrulestatement"></a>
OR rule statement.
*Required*: No
*Type*: [OrRuleStatement](aws-properties-licensemanager-licenseassetruleset-orrulestatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
