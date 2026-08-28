---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-licensemanager-licenseassetruleset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::LicenseAssetRuleSet
<a name="aws-resource-licensemanager-licenseassetruleset"></a>

<a name="aws-resource-licensemanager-licenseassetruleset-description"></a>The `AWS::LicenseManager::LicenseAssetRuleSet` resource Property description not available. for LicenseManager.

## Syntax
<a name="aws-resource-licensemanager-licenseassetruleset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-licensemanager-licenseassetruleset-syntax.json"></a>

```
{
  "Type" : "AWS::LicenseManager::LicenseAssetRuleSet",
  "Properties" : {
      "[Description](#cfn-licensemanager-licenseassetruleset-description)" : {{String}},
      "[Name](#cfn-licensemanager-licenseassetruleset-name)" : {{String}},
      "[Rules](#cfn-licensemanager-licenseassetruleset-rules)" : {{[ LicenseAssetRule, ... ]}},
      "[Tags](#cfn-licensemanager-licenseassetruleset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-licensemanager-licenseassetruleset-syntax.yaml"></a>

```
Type: AWS::LicenseManager::LicenseAssetRuleSet
Properties:
  [Description](#cfn-licensemanager-licenseassetruleset-description): {{String}}
  [Name](#cfn-licensemanager-licenseassetruleset-name): {{String}}
  [Rules](#cfn-licensemanager-licenseassetruleset-rules): {{
    - LicenseAssetRule}}
  [Tags](#cfn-licensemanager-licenseassetruleset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-licensemanager-licenseassetruleset-properties"></a>

`Description`  <a name="cfn-licensemanager-licenseassetruleset-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-licensemanager-licenseassetruleset-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rules`  <a name="cfn-licensemanager-licenseassetruleset-rules"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [LicenseAssetRule](aws-properties-licensemanager-licenseassetruleset-licenseassetrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-licensemanager-licenseassetruleset-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-licensemanager-licenseassetruleset-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-licensemanager-licenseassetruleset-return-values"></a>

### Ref
<a name="aws-resource-licensemanager-licenseassetruleset-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-licensemanager-licenseassetruleset-return-values-fn--getatt"></a>

####
<a name="aws-resource-licensemanager-licenseassetruleset-return-values-fn--getatt-fn--getatt"></a>

`LicenseAssetRulesetArn`  <a name="LicenseAssetRulesetArn-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
