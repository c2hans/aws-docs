---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-frauddetector-variable-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FraudDetector::Variable Tag
<a name="aws-properties-frauddetector-variable-tag"></a>

A key and value pair.

## Syntax
<a name="aws-properties-frauddetector-variable-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-frauddetector-variable-tag-syntax.json"></a>

```
{
  "[Key](#cfn-frauddetector-variable-tag-key)" : {{String}},
  "[Value](#cfn-frauddetector-variable-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-frauddetector-variable-tag-syntax.yaml"></a>

```
  [Key](#cfn-frauddetector-variable-tag-key): {{String}}
  [Value](#cfn-frauddetector-variable-tag-value): {{String}}
```

## Properties
<a name="aws-properties-frauddetector-variable-tag-properties"></a>

`Key`  <a name="cfn-frauddetector-variable-tag-key"></a>
A tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-frauddetector-variable-tag-value"></a>
A value assigned to a tag key.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
