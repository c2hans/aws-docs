---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-license-borrowconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::License BorrowConfiguration
<a name="aws-properties-licensemanager-license-borrowconfiguration"></a>

Details about a borrow configuration.

## Syntax
<a name="aws-properties-licensemanager-license-borrowconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-license-borrowconfiguration-syntax.json"></a>

```
{
  "[AllowEarlyCheckIn](#cfn-licensemanager-license-borrowconfiguration-allowearlycheckin)" : {{Boolean}},
  "[MaxTimeToLiveInMinutes](#cfn-licensemanager-license-borrowconfiguration-maxtimetoliveinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-licensemanager-license-borrowconfiguration-syntax.yaml"></a>

```
  [AllowEarlyCheckIn](#cfn-licensemanager-license-borrowconfiguration-allowearlycheckin): {{Boolean}}
  [MaxTimeToLiveInMinutes](#cfn-licensemanager-license-borrowconfiguration-maxtimetoliveinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-licensemanager-license-borrowconfiguration-properties"></a>

`AllowEarlyCheckIn`  <a name="cfn-licensemanager-license-borrowconfiguration-allowearlycheckin"></a>
Indicates whether early check-ins are allowed.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxTimeToLiveInMinutes`  <a name="cfn-licensemanager-license-borrowconfiguration-maxtimetoliveinminutes"></a>
Maximum time for the borrow configuration, in minutes.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
