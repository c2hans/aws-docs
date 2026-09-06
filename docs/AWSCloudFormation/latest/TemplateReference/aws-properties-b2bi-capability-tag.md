---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-capability-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Capability Tag
<a name="aws-properties-b2bi-capability-tag"></a>

A key-value pair for a specific capability. Tags are metadata that you can use to search for and group capabilities for various purposes.

## Syntax
<a name="aws-properties-b2bi-capability-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-capability-tag-syntax.json"></a>

```
{
  "[Key](#cfn-b2bi-capability-tag-key)" : {{String}},
  "[Value](#cfn-b2bi-capability-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-capability-tag-syntax.yaml"></a>

```
  [Key](#cfn-b2bi-capability-tag-key): {{String}}
  [Value](#cfn-b2bi-capability-tag-value): {{String}}
```

## Properties
<a name="aws-properties-b2bi-capability-tag-properties"></a>

`Key`  <a name="cfn-b2bi-capability-tag-key"></a>
Specifies the name assigned to the tag that you create.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-b2bi-capability-tag-value"></a>
Contains one or more values that you assigned to the key name that you create.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
