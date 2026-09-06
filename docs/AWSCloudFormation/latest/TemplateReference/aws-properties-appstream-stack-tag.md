---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-stack-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Stack Tag
<a name="aws-properties-appstream-stack-tag"></a>

The tag of the stack.

## Syntax
<a name="aws-properties-appstream-stack-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-stack-tag-syntax.json"></a>

```
{
  "[Key](#cfn-appstream-stack-tag-key)" : {{String}},
  "[Value](#cfn-appstream-stack-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-stack-tag-syntax.yaml"></a>

```
  [Key](#cfn-appstream-stack-tag-key): {{String}}
  [Value](#cfn-appstream-stack-tag-value): {{String}}
```

## Properties
<a name="aws-properties-appstream-stack-tag-properties"></a>

`Key`  <a name="cfn-appstream-stack-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appstream-stack-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
