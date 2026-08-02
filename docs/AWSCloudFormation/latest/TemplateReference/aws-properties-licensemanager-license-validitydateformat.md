---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-license-validitydateformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::License ValidityDateFormat
<a name="aws-properties-licensemanager-license-validitydateformat"></a>

Date and time range during which the license is valid, in ISO8601-UTC format.

## Syntax
<a name="aws-properties-licensemanager-license-validitydateformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-license-validitydateformat-syntax.json"></a>

```
{
  "[Begin](#cfn-licensemanager-license-validitydateformat-begin)" : {{String}},
  "[End](#cfn-licensemanager-license-validitydateformat-end)" : {{String}}
}
```

### YAML
<a name="aws-properties-licensemanager-license-validitydateformat-syntax.yaml"></a>

```
  [Begin](#cfn-licensemanager-license-validitydateformat-begin): {{String}}
  [End](#cfn-licensemanager-license-validitydateformat-end): {{String}}
```

## Properties
<a name="aws-properties-licensemanager-license-validitydateformat-properties"></a>

`Begin`  <a name="cfn-licensemanager-license-validitydateformat-begin"></a>
Start of the time range.
*Required*: Yes
*Type*: String
*Pattern*: `^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[0-1]|0[1-9]|[1-2][0-9])T(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[ 0-3]|[0-1][0-9]):[0-5][0-9])+$`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`End`  <a name="cfn-licensemanager-license-validitydateformat-end"></a>
End of the time range.
*Required*: Yes
*Type*: String
*Pattern*: `^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[0-1]|0[1-9]|[1-2][0-9])T(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[ 0-3]|[0-1][0-9]):[0-5][0-9])+$`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
