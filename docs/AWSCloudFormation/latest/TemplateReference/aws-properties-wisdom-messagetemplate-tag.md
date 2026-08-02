---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate Tag
<a name="aws-properties-wisdom-messagetemplate-tag"></a>

<a name="aws-properties-wisdom-messagetemplate-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::Wisdom::MessageTemplate](aws-resource-wisdom-messagetemplate.md).

## Syntax
<a name="aws-properties-wisdom-messagetemplate-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-tag-syntax.json"></a>

```
{
  "[Key](#cfn-wisdom-messagetemplate-tag-key)" : {{String}},
  "[Value](#cfn-wisdom-messagetemplate-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-tag-syntax.yaml"></a>

```
  [Key](#cfn-wisdom-messagetemplate-tag-key): {{String}}
  [Value](#cfn-wisdom-messagetemplate-tag-value): {{String}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-tag-properties"></a>

`Key`  <a name="cfn-wisdom-messagetemplate-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-wisdom-messagetemplate-tag-value"></a>
The value of the message template tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
