---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-licensemanager-licenseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::LicenseConfiguration
<a name="aws-resource-licensemanager-licenseconfiguration"></a>

A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy, Dedicated Instance, Dedicated Host, or all of these), host affinity (how long a VM must be associated with a host), and the number of licenses purchased and used.

## Syntax
<a name="aws-resource-licensemanager-licenseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-licensemanager-licenseconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::LicenseManager::LicenseConfiguration",
  "Properties" : {
      "[Description](#cfn-licensemanager-licenseconfiguration-description)" : {{String}},
      "[DisassociateWhenNotFound](#cfn-licensemanager-licenseconfiguration-disassociatewhennotfound)" : {{Boolean}},
      "[LicenseCount](#cfn-licensemanager-licenseconfiguration-licensecount)" : {{Integer}},
      "[LicenseCountHardLimit](#cfn-licensemanager-licenseconfiguration-licensecounthardlimit)" : {{Boolean}},
      "[LicenseCountingType](#cfn-licensemanager-licenseconfiguration-licensecountingtype)" : {{String}},
      "[LicenseExpiry](#cfn-licensemanager-licenseconfiguration-licenseexpiry)" : {{Integer}},
      "[LicenseRules](#cfn-licensemanager-licenseconfiguration-licenserules)" : {{[ String, ... ]}},
      "[Name](#cfn-licensemanager-licenseconfiguration-name)" : {{String}},
      "[ProductInformationList](#cfn-licensemanager-licenseconfiguration-productinformationlist)" : {{[ ProductInformation, ... ]}},
      "[Tags](#cfn-licensemanager-licenseconfiguration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-licensemanager-licenseconfiguration-syntax.yaml"></a>

```
Type: AWS::LicenseManager::LicenseConfiguration
Properties:
  [Description](#cfn-licensemanager-licenseconfiguration-description): {{String}}
  [DisassociateWhenNotFound](#cfn-licensemanager-licenseconfiguration-disassociatewhennotfound): {{Boolean}}
  [LicenseCount](#cfn-licensemanager-licenseconfiguration-licensecount): {{Integer}}
  [LicenseCountHardLimit](#cfn-licensemanager-licenseconfiguration-licensecounthardlimit): {{Boolean}}
  [LicenseCountingType](#cfn-licensemanager-licenseconfiguration-licensecountingtype): {{String}}
  [LicenseExpiry](#cfn-licensemanager-licenseconfiguration-licenseexpiry): {{Integer}}
  [LicenseRules](#cfn-licensemanager-licenseconfiguration-licenserules): {{
    - String}}
  [Name](#cfn-licensemanager-licenseconfiguration-name): {{String}}
  [ProductInformationList](#cfn-licensemanager-licenseconfiguration-productinformationlist): {{
    - ProductInformation}}
  [Tags](#cfn-licensemanager-licenseconfiguration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-licensemanager-licenseconfiguration-properties"></a>

`Description`  <a name="cfn-licensemanager-licenseconfiguration-description"></a>
Description of the license configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisassociateWhenNotFound`  <a name="cfn-licensemanager-licenseconfiguration-disassociatewhennotfound"></a>
When true, disassociates a resource when software is uninstalled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LicenseCount`  <a name="cfn-licensemanager-licenseconfiguration-licensecount"></a>
Number of licenses managed by the license configuration.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LicenseCountHardLimit`  <a name="cfn-licensemanager-licenseconfiguration-licensecounthardlimit"></a>
Number of available licenses as a hard limit.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LicenseCountingType`  <a name="cfn-licensemanager-licenseconfiguration-licensecountingtype"></a>
Dimension to use to track the license inventory.
*Required*: Yes
*Type*: String
*Allowed values*: `vCPU | Instance | Core | Socket`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LicenseExpiry`  <a name="cfn-licensemanager-licenseconfiguration-licenseexpiry"></a>
License configuration expiry time in Unix timestamp format.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LicenseRules`  <a name="cfn-licensemanager-licenseconfiguration-licenserules"></a>
License rules.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-licensemanager-licenseconfiguration-name"></a>
Name of the license configuration.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProductInformationList`  <a name="cfn-licensemanager-licenseconfiguration-productinformationlist"></a>
Product information.
*Required*: No
*Type*: Array of [ProductInformation](aws-properties-licensemanager-licenseconfiguration-productinformation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-licensemanager-licenseconfiguration-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-licensemanager-licenseconfiguration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-licensemanager-licenseconfiguration-return-values"></a>

### Ref
<a name="aws-resource-licensemanager-licenseconfiguration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-licensemanager-licenseconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-licensemanager-licenseconfiguration-return-values-fn--getatt-fn--getatt"></a>

`LicenseConfigurationArn`  <a name="LicenseConfigurationArn-fn::getatt"></a>
Amazon Resource Name (ARN) of the license configuration.

`LicenseConfigurationId`  <a name="LicenseConfigurationId-fn::getatt"></a>
Unique ID of the license configuration.

`OwnerAccountId`  <a name="OwnerAccountId-fn::getatt"></a>
Account ID of the license configuration's owner.

`Status`  <a name="Status-fn::getatt"></a>
Status of the license configuration.
