---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-solution-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Solution Tag
<a name="aws-properties-personalize-solution-tag"></a>

The optional metadata that you apply to resources to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. For more information see [Tagging Amazon Personalize resources](https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html).

## Syntax
<a name="aws-properties-personalize-solution-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-solution-tag-syntax.json"></a>

```
{
  "[Key](#cfn-personalize-solution-tag-key)" : {{String}},
  "[Value](#cfn-personalize-solution-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-personalize-solution-tag-syntax.yaml"></a>

```
  [Key](#cfn-personalize-solution-tag-key): {{String}}
  [Value](#cfn-personalize-solution-tag-value): {{String}}
```

## Properties
<a name="aws-properties-personalize-solution-tag-properties"></a>

`Key`  <a name="cfn-personalize-solution-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-personalize-solution-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
