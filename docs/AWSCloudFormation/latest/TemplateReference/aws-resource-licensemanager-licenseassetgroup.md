---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-licensemanager-licenseassetgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::LicenseAssetGroup
<a name="aws-resource-licensemanager-licenseassetgroup"></a>

Creates a license asset group.

## Syntax
<a name="aws-resource-licensemanager-licenseassetgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-licensemanager-licenseassetgroup-syntax.json"></a>

```
{
  "Type" : "AWS::LicenseManager::LicenseAssetGroup",
  "Properties" : {
      "[AssociatedLicenseAssetRulesetARNs](#cfn-licensemanager-licenseassetgroup-associatedlicenseassetrulesetarns)" : {{[ String, ... ]}},
      "[Description](#cfn-licensemanager-licenseassetgroup-description)" : {{String}},
      "[LicenseAssetGroupConfigurations](#cfn-licensemanager-licenseassetgroup-licenseassetgroupconfigurations)" : {{[ LicenseAssetGroupConfiguration, ... ]}},
      "[Name](#cfn-licensemanager-licenseassetgroup-name)" : {{String}},
      "[Properties](#cfn-licensemanager-licenseassetgroup-properties)" : {{[ LicenseAssetGroupProperty, ... ]}},
      "[Tags](#cfn-licensemanager-licenseassetgroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-licensemanager-licenseassetgroup-syntax.yaml"></a>

```
Type: AWS::LicenseManager::LicenseAssetGroup
Properties:
  [AssociatedLicenseAssetRulesetARNs](#cfn-licensemanager-licenseassetgroup-associatedlicenseassetrulesetarns): {{
    - String}}
  [Description](#cfn-licensemanager-licenseassetgroup-description): {{String}}
  [LicenseAssetGroupConfigurations](#cfn-licensemanager-licenseassetgroup-licenseassetgroupconfigurations): {{
    - LicenseAssetGroupConfiguration}}
  [Name](#cfn-licensemanager-licenseassetgroup-name): {{String}}
  [Properties](#cfn-licensemanager-licenseassetgroup-properties): {{
    - LicenseAssetGroupProperty}}
  [Tags](#cfn-licensemanager-licenseassetgroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-licensemanager-licenseassetgroup-properties"></a>

`AssociatedLicenseAssetRulesetARNs`  <a name="cfn-licensemanager-licenseassetgroup-associatedlicenseassetrulesetarns"></a>
ARNs of associated license asset rulesets.
*Required*: Yes
*Type*: Array of String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-licensemanager-licenseassetgroup-description"></a>
License asset group description.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LicenseAssetGroupConfigurations`  <a name="cfn-licensemanager-licenseassetgroup-licenseassetgroupconfigurations"></a>
License asset group configurations.
*Required*: Yes
*Type*: Array of [LicenseAssetGroupConfiguration](aws-properties-licensemanager-licenseassetgroup-licenseassetgroupconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-licensemanager-licenseassetgroup-name"></a>
License asset group name.
*Required*: Yes
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-licensemanager-licenseassetgroup-properties"></a>
License asset group properties.
*Required*: No
*Type*: Array of [LicenseAssetGroupProperty](aws-properties-licensemanager-licenseassetgroup-licenseassetgroupproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-licensemanager-licenseassetgroup-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-licensemanager-licenseassetgroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-licensemanager-licenseassetgroup-return-values"></a>

### Ref
<a name="aws-resource-licensemanager-licenseassetgroup-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-licensemanager-licenseassetgroup-return-values-fn--getatt"></a>

####
<a name="aws-resource-licensemanager-licenseassetgroup-return-values-fn--getatt-fn--getatt"></a>

`LicenseAssetGroupArn`  <a name="LicenseAssetGroupArn-fn::getatt"></a>
Amazon Resource Name (ARN) of the license asset group.
