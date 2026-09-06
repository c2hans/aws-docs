---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-certificatemanager-certificate-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CertificateManager::Certificate Tag
<a name="aws-properties-certificatemanager-certificate-tag"></a>

A key-value pair that identifies or specifies metadata about an ACM resource.

## Syntax
<a name="aws-properties-certificatemanager-certificate-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-certificatemanager-certificate-tag-syntax.json"></a>

```
{
  "[Key](#cfn-certificatemanager-certificate-tag-key)" : {{String}},
  "[Value](#cfn-certificatemanager-certificate-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-certificatemanager-certificate-tag-syntax.yaml"></a>

```
  [Key](#cfn-certificatemanager-certificate-tag-key): {{String}}
  [Value](#cfn-certificatemanager-certificate-tag-value): {{String}}
```

## Properties
<a name="aws-properties-certificatemanager-certificate-tag-properties"></a>

`Key`  <a name="cfn-certificatemanager-certificate-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-certificatemanager-certificate-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
