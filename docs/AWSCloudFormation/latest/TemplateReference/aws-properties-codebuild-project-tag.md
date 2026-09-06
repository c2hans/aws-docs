---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Project Tag
<a name="aws-properties-codebuild-project-tag"></a>

A tag, consisting of a key and a value.

This tag is available for use by AWS services that support tags in AWS CodeBuild.

## Syntax
<a name="aws-properties-codebuild-project-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-project-tag-syntax.json"></a>

```
{
  "[Key](#cfn-codebuild-project-tag-key)" : {{String}},
  "[Value](#cfn-codebuild-project-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-codebuild-project-tag-syntax.yaml"></a>

```
  [Key](#cfn-codebuild-project-tag-key): {{String}}
  [Value](#cfn-codebuild-project-tag-value): {{String}}
```

## Properties
<a name="aws-properties-codebuild-project-tag-properties"></a>

`Key`  <a name="cfn-codebuild-project-tag-key"></a>
The tag's key.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=@+\-]*)$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-codebuild-project-tag-value"></a>
The tag's value.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=@+\-]*)$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
