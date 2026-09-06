---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filesystem-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileSystem Tag
<a name="aws-properties-fsx-filesystem-tag"></a>

Specifies a key-value pair for a resource tag.

## Syntax
<a name="aws-properties-fsx-filesystem-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filesystem-tag-syntax.json"></a>

```
{
  "[Key](#cfn-fsx-filesystem-tag-key)" : {{String}},
  "[Value](#cfn-fsx-filesystem-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-filesystem-tag-syntax.yaml"></a>

```
  [Key](#cfn-fsx-filesystem-tag-key): {{String}}
  [Value](#cfn-fsx-filesystem-tag-value): {{String}}
```

## Properties
<a name="aws-properties-fsx-filesystem-tag-properties"></a>

`Key`  <a name="cfn-fsx-filesystem-tag-key"></a>
A value that specifies the `TagKey`, the name of the tag. Tag keys must be unique for the resource to which they are attached.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-fsx-filesystem-tag-value"></a>
A value that specifies the `TagValue`, the value assigned to the corresponding tag key. Tag values can be null and don't have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
