---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-globalaccelerator-accelerator-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GlobalAccelerator::Accelerator Tag
<a name="aws-properties-globalaccelerator-accelerator-tag"></a>

A complex type that contains a `Tag` key and `Tag` value.

## Syntax
<a name="aws-properties-globalaccelerator-accelerator-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-globalaccelerator-accelerator-tag-syntax.json"></a>

```
{
  "[Key](#cfn-globalaccelerator-accelerator-tag-key)" : {{String}},
  "[Value](#cfn-globalaccelerator-accelerator-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-globalaccelerator-accelerator-tag-syntax.yaml"></a>

```
  [Key](#cfn-globalaccelerator-accelerator-tag-key): {{String}}
  [Value](#cfn-globalaccelerator-accelerator-tag-value): {{String}}
```

## Properties
<a name="aws-properties-globalaccelerator-accelerator-tag-properties"></a>

`Key`  <a name="cfn-globalaccelerator-accelerator-tag-key"></a>
A string that contains a `Tag` key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-globalaccelerator-accelerator-tag-value"></a>
A string that contains a `Tag` value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
