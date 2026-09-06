---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-customactiontype-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::CustomActionType Tag
<a name="aws-properties-codepipeline-customactiontype-tag"></a>

A tag is a key-value pair that is used to manage the resource.

## Syntax
<a name="aws-properties-codepipeline-customactiontype-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-customactiontype-tag-syntax.json"></a>

```
{
  "[Key](#cfn-codepipeline-customactiontype-tag-key)" : {{String}},
  "[Value](#cfn-codepipeline-customactiontype-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-customactiontype-tag-syntax.yaml"></a>

```
  [Key](#cfn-codepipeline-customactiontype-tag-key): {{String}}
  [Value](#cfn-codepipeline-customactiontype-tag-value): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-customactiontype-tag-properties"></a>

`Key`  <a name="cfn-codepipeline-customactiontype-tag-key"></a>
The tag's key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-codepipeline-customactiontype-tag-value"></a>
The tag's value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
