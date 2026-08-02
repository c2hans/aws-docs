---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe Tag
<a name="aws-properties-pipes-pipe-tag"></a>

<a name="aws-properties-pipes-pipe-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::Pipes::Pipe](aws-resource-pipes-pipe.md).

## Syntax
<a name="aws-properties-pipes-pipe-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-tag-syntax.json"></a>

```
{
  "[Key](#cfn-pipes-pipe-tag-key)" : {{String}},
  "[Value](#cfn-pipes-pipe-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-tag-syntax.yaml"></a>

```
  [Key](#cfn-pipes-pipe-tag-key): {{String}}
  [Value](#cfn-pipes-pipe-tag-value): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-tag-properties"></a>

`Key`  <a name="cfn-pipes-pipe-tag-key"></a>
The key of the key-value pair.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-pipes-pipe-tag-value"></a>
The value of the key-value pair.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
