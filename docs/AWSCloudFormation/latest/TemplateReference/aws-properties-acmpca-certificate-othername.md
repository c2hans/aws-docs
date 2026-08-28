---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificate-othername.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::Certificate OtherName
<a name="aws-properties-acmpca-certificate-othername"></a>

Defines a custom ASN.1 X.400 `GeneralName` using an object identifier (OID) and value. The OID must satisfy the regular expression shown below. For more information, see NIST's definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier).

## Syntax
<a name="aws-properties-acmpca-certificate-othername-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificate-othername-syntax.json"></a>

```
{
  "[TypeId](#cfn-acmpca-certificate-othername-typeid)" : {{String}},
  "[Value](#cfn-acmpca-certificate-othername-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-acmpca-certificate-othername-syntax.yaml"></a>

```
  [TypeId](#cfn-acmpca-certificate-othername-typeid): {{String}}
  [Value](#cfn-acmpca-certificate-othername-value): {{String}}
```

## Properties
<a name="aws-properties-acmpca-certificate-othername-properties"></a>

`TypeId`  <a name="cfn-acmpca-certificate-othername-typeid"></a>
Specifies an OID.
*Required*: Yes
*Type*: String
*Pattern*: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-acmpca-certificate-othername-value"></a>
Specifies an OID value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
