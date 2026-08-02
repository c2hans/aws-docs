---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-synthetics-group-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Synthetics::Group Tag
<a name="aws-properties-synthetics-group-tag"></a>

The list of key-value pairs that are associated with the group.

## Syntax
<a name="aws-properties-synthetics-group-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-synthetics-group-tag-syntax.json"></a>

```
{
  "[Key](#cfn-synthetics-group-tag-key)" : {{String}},
  "[Value](#cfn-synthetics-group-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-synthetics-group-tag-syntax.yaml"></a>

```
  [Key](#cfn-synthetics-group-tag-key): {{String}}
  [Value](#cfn-synthetics-group-tag-value): {{String}}
```

## Properties
<a name="aws-properties-synthetics-group-tag-properties"></a>

`Key`  <a name="cfn-synthetics-group-tag-key"></a>
The key of this key-value pair.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)([a-zA-Z\d\s_.:/=+\-@]+)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-synthetics-group-tag-value"></a>
The value of this key-value pair.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z\d\s_.:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
