---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-licenseassetruleset-andrulestatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::LicenseAssetRuleSet AndRuleStatement
<a name="aws-properties-licensemanager-licenseassetruleset-andrulestatement"></a>

AND rule statement.

## Syntax
<a name="aws-properties-licensemanager-licenseassetruleset-andrulestatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-licenseassetruleset-andrulestatement-syntax.json"></a>

```
{
  "[MatchingRuleStatements](#cfn-licensemanager-licenseassetruleset-andrulestatement-matchingrulestatements)" : {{[ MatchingRuleStatement, ... ]}}
}
```

### YAML
<a name="aws-properties-licensemanager-licenseassetruleset-andrulestatement-syntax.yaml"></a>

```
  [MatchingRuleStatements](#cfn-licensemanager-licenseassetruleset-andrulestatement-matchingrulestatements): {{
    - MatchingRuleStatement}}
```

## Properties
<a name="aws-properties-licensemanager-licenseassetruleset-andrulestatement-properties"></a>

`MatchingRuleStatements`  <a name="cfn-licensemanager-licenseassetruleset-andrulestatement-matchingrulestatements"></a>
Matching rule statements.
*Required*: No
*Type*: Array of [MatchingRuleStatement](aws-properties-licensemanager-licenseassetruleset-matchingrulestatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
