---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securitylake-subscriber-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::Subscriber Tag
<a name="aws-properties-securitylake-subscriber-tag"></a>

A *tag* is a label that you can define and associate with AWS resources, including certain types of Amazon Security Lake resources. Tags can help you identify, categorize, and manage resources in different ways, such as by owner, environment, or other criteria. You can associate tags with the following types of Security Lake resources: subscribers, and the data lake configuration for your AWS account in individual AWS Regions.

A resource can have up to 50 tags. Each tag consists of a required *tag key* and an associated *tag value*. A *tag key* is a general label that acts as a category for a more specific tag value. Each tag key must be unique and it can have only one tag value. A *tag value* acts as a descriptor for a tag key. Tag keys and values are case sensitive. They can contain letters, numbers, spaces, or the following symbols: \_ . : / = \+ @ -

For more information, see [Tagging Amazon Security Lake resources](https://docs.aws.amazon.com//security-lake/latest/userguide/tagging-resources.html) in the *Amazon Security Lake User Guide*.

## Syntax
<a name="aws-properties-securitylake-subscriber-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securitylake-subscriber-tag-syntax.json"></a>

```
{
  "[Key](#cfn-securitylake-subscriber-tag-key)" : {{String}},
  "[Value](#cfn-securitylake-subscriber-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-securitylake-subscriber-tag-syntax.yaml"></a>

```
  [Key](#cfn-securitylake-subscriber-tag-key): {{String}}
  [Value](#cfn-securitylake-subscriber-tag-value): {{String}}
```

## Properties
<a name="aws-properties-securitylake-subscriber-tag-properties"></a>

`Key`  <a name="cfn-securitylake-subscriber-tag-key"></a>
The name of the tag. This is a general label that acts as a category for a more specific tag value (`value`).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-securitylake-subscriber-tag-value"></a>
The value that’s associated with the specified tag key (`key`). This value acts as a descriptor for the tag key. A tag value cannot be null, but it can be an empty string.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
