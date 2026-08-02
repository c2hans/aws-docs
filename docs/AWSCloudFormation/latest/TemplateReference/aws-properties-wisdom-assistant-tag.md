---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-assistant-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::Assistant Tag
<a name="aws-properties-wisdom-assistant-tag"></a>

Metadata to assign to the Wisdom assistant. Tags help organize and categorize your Connect Customer Wisdom resources. Each tag consists of a key and an optional value, both of which you define.

## Syntax
<a name="aws-properties-wisdom-assistant-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-assistant-tag-syntax.json"></a>

```
{
  "[Key](#cfn-wisdom-assistant-tag-key)" : {{String}},
  "[Value](#cfn-wisdom-assistant-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-assistant-tag-syntax.yaml"></a>

```
  [Key](#cfn-wisdom-assistant-tag-key): {{String}}
  [Value](#cfn-wisdom-assistant-tag-value): {{String}}
```

## Properties
<a name="aws-properties-wisdom-assistant-tag-properties"></a>

`Key`  <a name="cfn-wisdom-assistant-tag-key"></a>
The key-value string map. The valid character set is `[a-zA-Z+-=._:/]`. The tag key can be up to 128 characters and must not start with `aws:`.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-wisdom-assistant-tag-value"></a>
The tag value can be up to 256 characters.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
