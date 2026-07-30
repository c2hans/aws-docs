---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificateauthority-accessmethod.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::CertificateAuthority AccessMethod
<a name="aws-properties-acmpca-certificateauthority-accessmethod"></a>

Describes the type and format of extension access. Only one of `CustomObjectIdentifier` or `AccessMethodType` may be provided. Providing both results in `InvalidArgsException`.

## Syntax
<a name="aws-properties-acmpca-certificateauthority-accessmethod-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificateauthority-accessmethod-syntax.json"></a>

```
{
  "[AccessMethodType](#cfn-acmpca-certificateauthority-accessmethod-accessmethodtype)" : {{String}},
  "[CustomObjectIdentifier](#cfn-acmpca-certificateauthority-accessmethod-customobjectidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-acmpca-certificateauthority-accessmethod-syntax.yaml"></a>

```
  [AccessMethodType](#cfn-acmpca-certificateauthority-accessmethod-accessmethodtype): {{String}}
  [CustomObjectIdentifier](#cfn-acmpca-certificateauthority-accessmethod-customobjectidentifier): {{String}}
```

## Properties
<a name="aws-properties-acmpca-certificateauthority-accessmethod-properties"></a>

`AccessMethodType`  <a name="cfn-acmpca-certificateauthority-accessmethod-accessmethodtype"></a>
Specifies the `AccessMethod`.
*Required*: No
*Type*: String
*Allowed values*: `CA_REPOSITORY | RESOURCE_PKI_MANIFEST | RESOURCE_PKI_NOTIFY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomObjectIdentifier`  <a name="cfn-acmpca-certificateauthority-accessmethod-customobjectidentifier"></a>
An object identifier (OID) specifying the `AccessMethod`. The OID must satisfy the regular expression shown below. For more information, see NIST's definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier).
*Required*: No
*Type*: String
*Pattern*: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
