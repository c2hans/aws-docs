---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificate-customextension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::Certificate CustomExtension
<a name="aws-properties-acmpca-certificate-customextension"></a>

Specifies the X.509 extension information for a certificate.

Extensions present in `CustomExtensions` follow the `ApiPassthrough`[template rules](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-order-of-operations).

## Syntax
<a name="aws-properties-acmpca-certificate-customextension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificate-customextension-syntax.json"></a>

```
{
  "[Critical](#cfn-acmpca-certificate-customextension-critical)" : {{Boolean}},
  "[ObjectIdentifier](#cfn-acmpca-certificate-customextension-objectidentifier)" : {{String}},
  "[Value](#cfn-acmpca-certificate-customextension-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-acmpca-certificate-customextension-syntax.yaml"></a>

```
  [Critical](#cfn-acmpca-certificate-customextension-critical): {{Boolean}}
  [ObjectIdentifier](#cfn-acmpca-certificate-customextension-objectidentifier): {{String}}
  [Value](#cfn-acmpca-certificate-customextension-value): {{String}}
```

## Properties
<a name="aws-properties-acmpca-certificate-customextension-properties"></a>

`Critical`  <a name="cfn-acmpca-certificate-customextension-critical"></a>

Specifies the critical flag of the X.509 extension.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ObjectIdentifier`  <a name="cfn-acmpca-certificate-customextension-objectidentifier"></a>

Specifies the object identifier (OID) of the X.509 extension. For more information, see the [Global OID reference database.](https://oidref.com/2.5.29)
*Required*: Yes
*Type*: String
*Pattern*: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-acmpca-certificate-customextension-value"></a>

Specifies the base64-encoded value of the X.509 extension.
*Required*: Yes
*Type*: String
*Pattern*: `(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
