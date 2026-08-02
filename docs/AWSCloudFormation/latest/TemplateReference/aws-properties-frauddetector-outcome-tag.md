---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-frauddetector-outcome-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FraudDetector::Outcome Tag
<a name="aws-properties-frauddetector-outcome-tag"></a>

A key and value pair.

## Syntax
<a name="aws-properties-frauddetector-outcome-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-frauddetector-outcome-tag-syntax.json"></a>

```
{
  "[Key](#cfn-frauddetector-outcome-tag-key)" : {{String}},
  "[Value](#cfn-frauddetector-outcome-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-frauddetector-outcome-tag-syntax.yaml"></a>

```
  [Key](#cfn-frauddetector-outcome-tag-key): {{String}}
  [Value](#cfn-frauddetector-outcome-tag-value): {{String}}
```

## Properties
<a name="aws-properties-frauddetector-outcome-tag-properties"></a>

`Key`  <a name="cfn-frauddetector-outcome-tag-key"></a>
A tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-frauddetector-outcome-tag-value"></a>
A value assigned to a tag key.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
