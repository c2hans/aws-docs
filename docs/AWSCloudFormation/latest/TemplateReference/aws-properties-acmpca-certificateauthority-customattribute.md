---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificateauthority-customattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::CertificateAuthority CustomAttribute
<a name="aws-properties-acmpca-certificateauthority-customattribute"></a>

Defines the X.500 relative distinguished name (RDN).

## Syntax
<a name="aws-properties-acmpca-certificateauthority-customattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificateauthority-customattribute-syntax.json"></a>

```
{
  "[ObjectIdentifier](#cfn-acmpca-certificateauthority-customattribute-objectidentifier)" : {{String}},
  "[Value](#cfn-acmpca-certificateauthority-customattribute-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-acmpca-certificateauthority-customattribute-syntax.yaml"></a>

```
  [ObjectIdentifier](#cfn-acmpca-certificateauthority-customattribute-objectidentifier): {{String}}
  [Value](#cfn-acmpca-certificateauthority-customattribute-value): {{String}}
```

## Properties
<a name="aws-properties-acmpca-certificateauthority-customattribute-properties"></a>

`ObjectIdentifier`  <a name="cfn-acmpca-certificateauthority-customattribute-objectidentifier"></a>
Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).
*Required*: Yes
*Type*: String
*Pattern*: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-acmpca-certificateauthority-customattribute-value"></a>

Specifies the attribute value of relative distinguished name (RDN).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
