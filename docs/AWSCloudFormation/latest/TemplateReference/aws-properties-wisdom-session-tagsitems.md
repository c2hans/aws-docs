---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-session-tagsitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::Session TagsItems
<a name="aws-properties-wisdom-session-tagsitems"></a>

<a name="aws-properties-wisdom-session-tagsitems-description"></a>The `TagsItems` property type specifies Property description not available. for an [AWS::Wisdom::Session](aws-resource-wisdom-session.md).

## Syntax
<a name="aws-properties-wisdom-session-tagsitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-session-tagsitems-syntax.json"></a>

```
{
  "[Key](#cfn-wisdom-session-tagsitems-key)" : {{String}},
  "[Value](#cfn-wisdom-session-tagsitems-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-session-tagsitems-syntax.yaml"></a>

```
  [Key](#cfn-wisdom-session-tagsitems-key): {{String}}
  [Value](#cfn-wisdom-session-tagsitems-value): {{String}}
```

## Properties
<a name="aws-properties-wisdom-session-tagsitems-properties"></a>

`Key`  <a name="cfn-wisdom-session-tagsitems-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-wisdom-session-tagsitems-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
