---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devicefarm-testgridproject-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DeviceFarm::TestGridProject Tag
<a name="aws-properties-devicefarm-testgridproject-tag"></a>

The metadata that you apply to a resource to help you categorize and organize it. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters. Tag values can have a maximum length of 256 characters.

## Syntax
<a name="aws-properties-devicefarm-testgridproject-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devicefarm-testgridproject-tag-syntax.json"></a>

```
{
  "[Key](#cfn-devicefarm-testgridproject-tag-key)" : {{String}},
  "[Value](#cfn-devicefarm-testgridproject-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-devicefarm-testgridproject-tag-syntax.yaml"></a>

```
  [Key](#cfn-devicefarm-testgridproject-tag-key): {{String}}
  [Value](#cfn-devicefarm-testgridproject-tag-value): {{String}}
```

## Properties
<a name="aws-properties-devicefarm-testgridproject-tag-properties"></a>

`Key`  <a name="cfn-devicefarm-testgridproject-tag-key"></a>
One part of a key-value pair that makes up a tag. A `key` is a general label that acts like a category for more specific tag values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-devicefarm-testgridproject-tag-value"></a>
The optional part of a key-value pair that makes up a tag. A `value` acts as a descriptor in a tag category (key).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
