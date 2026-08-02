---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-accessgrant-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::AccessGrant Tag
<a name="aws-properties-s3-accessgrant-tag"></a>

A container of a key value name pair.

## Syntax
<a name="aws-properties-s3-accessgrant-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-accessgrant-tag-syntax.json"></a>

```
{
  "[Key](#cfn-s3-accessgrant-tag-key)" : {{String}},
  "[Value](#cfn-s3-accessgrant-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-accessgrant-tag-syntax.yaml"></a>

```
  [Key](#cfn-s3-accessgrant-tag-key): {{String}}
  [Value](#cfn-s3-accessgrant-tag-value): {{String}}
```

## Properties
<a name="aws-properties-s3-accessgrant-tag-properties"></a>

`Key`  <a name="cfn-s3-accessgrant-tag-key"></a>
Name of the object key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-s3-accessgrant-tag-value"></a>
Value of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
