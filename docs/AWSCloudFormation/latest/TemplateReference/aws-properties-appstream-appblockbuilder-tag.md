---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-appblockbuilder-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::AppBlockBuilder Tag
<a name="aws-properties-appstream-appblockbuilder-tag"></a>

The tag of the app block builder.

## Syntax
<a name="aws-properties-appstream-appblockbuilder-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-appblockbuilder-tag-syntax.json"></a>

```
{
  "[Key](#cfn-appstream-appblockbuilder-tag-key)" : {{String}},
  "[Value](#cfn-appstream-appblockbuilder-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-appblockbuilder-tag-syntax.yaml"></a>

```
  [Key](#cfn-appstream-appblockbuilder-tag-key): {{String}}
  [Value](#cfn-appstream-appblockbuilder-tag-value): {{String}}
```

## Properties
<a name="aws-properties-appstream-appblockbuilder-tag-properties"></a>

`Key`  <a name="cfn-appstream-appblockbuilder-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appstream-appblockbuilder-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
