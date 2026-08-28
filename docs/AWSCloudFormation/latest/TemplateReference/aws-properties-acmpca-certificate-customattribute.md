---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificate-customattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::Certificate CustomAttribute
<a name="aws-properties-acmpca-certificate-customattribute"></a>

Defines the X.500 relative distinguished name (RDN).

## Syntax
<a name="aws-properties-acmpca-certificate-customattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificate-customattribute-syntax.json"></a>

```
{
  "[ObjectIdentifier](#cfn-acmpca-certificate-customattribute-objectidentifier)" : {{String}},
  "[Value](#cfn-acmpca-certificate-customattribute-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-acmpca-certificate-customattribute-syntax.yaml"></a>

```
  [ObjectIdentifier](#cfn-acmpca-certificate-customattribute-objectidentifier): {{String}}
  [Value](#cfn-acmpca-certificate-customattribute-value): {{String}}
```

## Properties
<a name="aws-properties-acmpca-certificate-customattribute-properties"></a>

`ObjectIdentifier`  <a name="cfn-acmpca-certificate-customattribute-objectidentifier"></a>
Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).
*Required*: Yes
*Type*: String
*Pattern*: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-acmpca-certificate-customattribute-value"></a>

Specifies the attribute value of relative distinguished name (RDN).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
