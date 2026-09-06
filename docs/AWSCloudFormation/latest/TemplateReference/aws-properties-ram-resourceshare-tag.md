---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ram-resourceshare-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RAM::ResourceShare Tag
<a name="aws-properties-ram-resourceshare-tag"></a>

A structure containing a tag. A tag is metadata that you can attach to your resources to help organize and categorize them. You can also use them to help you secure your resources. For more information, see [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html).

For more information about tags, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference Guide*.

## Syntax
<a name="aws-properties-ram-resourceshare-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ram-resourceshare-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ram-resourceshare-tag-key)" : {{String}},
  "[Value](#cfn-ram-resourceshare-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ram-resourceshare-tag-syntax.yaml"></a>

```
  [Key](#cfn-ram-resourceshare-tag-key): {{String}}
  [Value](#cfn-ram-resourceshare-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ram-resourceshare-tag-properties"></a>

`Key`  <a name="cfn-ram-resourceshare-tag-key"></a>
The key, or name, attached to the tag. Every tag must have a key. Key names are case sensitive.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ram-resourceshare-tag-value"></a>
The string value attached to the tag. The value can be an empty string. Key values are case sensitive.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
