---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificateauthority-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::CertificateAuthority Tag
<a name="aws-properties-acmpca-certificateauthority-tag"></a>

Tags are labels that you can use to identify and organize your private CAs. Each tag consists of a key and an optional value. You can associate up to 50 tags with a private CA. To add one or more tags to a private CA, call the [TagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html) action. To remove a tag, call the [UntagCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UntagCertificateAuthority.html) action.

## Syntax
<a name="aws-properties-acmpca-certificateauthority-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificateauthority-tag-syntax.json"></a>

```
{
  "[Key](#cfn-acmpca-certificateauthority-tag-key)" : {{String}},
  "[Value](#cfn-acmpca-certificateauthority-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-acmpca-certificateauthority-tag-syntax.yaml"></a>

```
  [Key](#cfn-acmpca-certificateauthority-tag-key): {{String}}
  [Value](#cfn-acmpca-certificateauthority-tag-value): {{String}}
```

## Properties
<a name="aws-properties-acmpca-certificateauthority-tag-properties"></a>

`Key`  <a name="cfn-acmpca-certificateauthority-tag-key"></a>
Key (name) of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-acmpca-certificateauthority-tag-value"></a>
Value of the tag.
*Required*: No
*Type*: String
*Pattern*: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
