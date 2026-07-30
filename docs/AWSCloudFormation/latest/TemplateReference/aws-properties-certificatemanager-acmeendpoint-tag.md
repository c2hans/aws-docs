---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-certificatemanager-acmeendpoint-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CertificateManager::AcmeEndpoint Tag
<a name="aws-properties-certificatemanager-acmeendpoint-tag"></a>

A key-value pair that identifies or specifies metadata about an ACM resource.

## Syntax
<a name="aws-properties-certificatemanager-acmeendpoint-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-certificatemanager-acmeendpoint-tag-syntax.json"></a>

```
{
  "[Key](#cfn-certificatemanager-acmeendpoint-tag-key)" : {{String}},
  "[Value](#cfn-certificatemanager-acmeendpoint-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-certificatemanager-acmeendpoint-tag-syntax.yaml"></a>

```
  [Key](#cfn-certificatemanager-acmeendpoint-tag-key): {{String}}
  [Value](#cfn-certificatemanager-acmeendpoint-tag-value): {{String}}
```

## Properties
<a name="aws-properties-certificatemanager-acmeendpoint-tag-properties"></a>

`Key`  <a name="cfn-certificatemanager-acmeendpoint-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-certificatemanager-acmeendpoint-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
