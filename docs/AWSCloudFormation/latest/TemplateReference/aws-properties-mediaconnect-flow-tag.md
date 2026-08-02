---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow Tag
<a name="aws-properties-mediaconnect-flow-tag"></a>

Specifies a tag. For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).

## Syntax
<a name="aws-properties-mediaconnect-flow-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-tag-syntax.json"></a>

```
{
  "[Key](#cfn-mediaconnect-flow-tag-key)" : {{String}},
  "[Value](#cfn-mediaconnect-flow-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-tag-syntax.yaml"></a>

```
  [Key](#cfn-mediaconnect-flow-tag-key): {{String}}
  [Value](#cfn-mediaconnect-flow-tag-value): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-tag-properties"></a>

`Key`  <a name="cfn-mediaconnect-flow-tag-key"></a>
The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length. The key is case-sensitive.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-mediaconnect-flow-tag-value"></a>
The value for the tag. You can specify a value that's 0 to 256 Unicode characters in length.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
