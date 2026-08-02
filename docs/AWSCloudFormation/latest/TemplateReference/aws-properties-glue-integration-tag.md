---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-integration-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Integration Tag
<a name="aws-properties-glue-integration-tag"></a>

The `Tag` object represents a label that you can assign to an AWS resource. Each tag consists of a key and an optional value, both of which you define.

## Syntax
<a name="aws-properties-glue-integration-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-integration-tag-syntax.json"></a>

```
{
  "[Key](#cfn-glue-integration-tag-key)" : {{String}},
  "[Value](#cfn-glue-integration-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-integration-tag-syntax.yaml"></a>

```
  [Key](#cfn-glue-integration-tag-key): {{String}}
  [Value](#cfn-glue-integration-tag-value): {{String}}
```

## Properties
<a name="aws-properties-glue-integration-tag-properties"></a>

`Key`  <a name="cfn-glue-integration-tag-key"></a>
The tag key. The key is required when you create a tag on an object. The key is case-sensitive, and must not contain the prefix aws.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-glue-integration-tag-value"></a>
The tag value. The value is optional when you create a tag on an object. The value is case-sensitive, and must not contain the prefix aws.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
