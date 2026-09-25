---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-comprehend-entityrecognizer-entitytypeslistitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::EntityRecognizer EntityTypesListItem
<a name="aws-properties-comprehend-entityrecognizer-entitytypeslistitem"></a>

An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.

## Syntax
<a name="aws-properties-comprehend-entityrecognizer-entitytypeslistitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-comprehend-entityrecognizer-entitytypeslistitem-syntax.json"></a>

```
{
  "[Type](#cfn-comprehend-entityrecognizer-entitytypeslistitem-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-comprehend-entityrecognizer-entitytypeslistitem-syntax.yaml"></a>

```
  [Type](#cfn-comprehend-entityrecognizer-entitytypeslistitem-type): {{String}}
```

## Properties
<a name="aws-properties-comprehend-entityrecognizer-entitytypeslistitem-properties"></a>

`Type`  <a name="cfn-comprehend-entityrecognizer-entitytypeslistitem-type"></a>
An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.
Entity types must not contain the following invalid characters: \\n (line break), \\\\n (escaped line break, \\r (carriage return), \\\\r (escaped carriage return), \\t (tab), \\\\t (escaped tab), and , (comma).
*Required*: Yes
*Type*: String
*Pattern*: `^(?![^\n\r\t,]*\\n|\\r|\\t)[^\n\r\t,]+$`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
