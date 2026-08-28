---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-licenseassetruleset-orrulestatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::LicenseAssetRuleSet OrRuleStatement
<a name="aws-properties-licensemanager-licenseassetruleset-orrulestatement"></a>

OR rule statement.

## Syntax
<a name="aws-properties-licensemanager-licenseassetruleset-orrulestatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-licenseassetruleset-orrulestatement-syntax.json"></a>

```
{
  "[MatchingRuleStatements](#cfn-licensemanager-licenseassetruleset-orrulestatement-matchingrulestatements)" : {{[ MatchingRuleStatement, ... ]}}
}
```

### YAML
<a name="aws-properties-licensemanager-licenseassetruleset-orrulestatement-syntax.yaml"></a>

```
  [MatchingRuleStatements](#cfn-licensemanager-licenseassetruleset-orrulestatement-matchingrulestatements): {{
    - MatchingRuleStatement}}
```

## Properties
<a name="aws-properties-licensemanager-licenseassetruleset-orrulestatement-properties"></a>

`MatchingRuleStatements`  <a name="cfn-licensemanager-licenseassetruleset-orrulestatement-matchingrulestatements"></a>
Matching rule statements.
*Required*: No
*Type*: Array of [MatchingRuleStatement](aws-properties-licensemanager-licenseassetruleset-matchingrulestatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
