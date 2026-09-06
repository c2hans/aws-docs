---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-proton-environmenttemplate-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Proton::EnvironmentTemplate Tag
<a name="aws-properties-proton-environmenttemplate-tag"></a>

A description of a resource tag.

## Syntax
<a name="aws-properties-proton-environmenttemplate-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-proton-environmenttemplate-tag-syntax.json"></a>

```
{
  "[Key](#cfn-proton-environmenttemplate-tag-key)" : {{String}},
  "[Value](#cfn-proton-environmenttemplate-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-proton-environmenttemplate-tag-syntax.yaml"></a>

```
  [Key](#cfn-proton-environmenttemplate-tag-key): {{String}}
  [Value](#cfn-proton-environmenttemplate-tag-value): {{String}}
```

## Properties
<a name="aws-properties-proton-environmenttemplate-tag-properties"></a>

`Key`  <a name="cfn-proton-environmenttemplate-tag-key"></a>
The key of the resource tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-proton-environmenttemplate-tag-value"></a>
The value of the resource tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
