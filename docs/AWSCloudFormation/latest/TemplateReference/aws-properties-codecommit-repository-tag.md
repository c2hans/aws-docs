---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codecommit-repository-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeCommit::Repository Tag
<a name="aws-properties-codecommit-repository-tag"></a>

A tag is a key-value pair that is used to manage the resource.

## Syntax
<a name="aws-properties-codecommit-repository-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codecommit-repository-tag-syntax.json"></a>

```
{
  "[Key](#cfn-codecommit-repository-tag-key)" : {{String}},
  "[Value](#cfn-codecommit-repository-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-codecommit-repository-tag-syntax.yaml"></a>

```
  [Key](#cfn-codecommit-repository-tag-key): {{String}}
  [Value](#cfn-codecommit-repository-tag-value): {{String}}
```

## Properties
<a name="aws-properties-codecommit-repository-tag-properties"></a>

`Key`  <a name="cfn-codecommit-repository-tag-key"></a>
The tag's key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-codecommit-repository-tag-value"></a>
The tag's value.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
