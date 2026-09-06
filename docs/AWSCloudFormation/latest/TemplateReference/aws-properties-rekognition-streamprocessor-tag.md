---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rekognition-streamprocessor-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rekognition::StreamProcessor Tag
<a name="aws-properties-rekognition-streamprocessor-tag"></a>

<a name="aws-properties-rekognition-streamprocessor-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::Rekognition::StreamProcessor](aws-resource-rekognition-streamprocessor.md).

## Syntax
<a name="aws-properties-rekognition-streamprocessor-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rekognition-streamprocessor-tag-syntax.json"></a>

```
{
  "[Key](#cfn-rekognition-streamprocessor-tag-key)" : {{String}},
  "[Value](#cfn-rekognition-streamprocessor-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-rekognition-streamprocessor-tag-syntax.yaml"></a>

```
  [Key](#cfn-rekognition-streamprocessor-tag-key): {{String}}
  [Value](#cfn-rekognition-streamprocessor-tag-value): {{String}}
```

## Properties
<a name="aws-properties-rekognition-streamprocessor-tag-properties"></a>

`Key`  <a name="cfn-rekognition-streamprocessor-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `\A(?!aws:)[a-zA-Z0-9+\-=\._\:\/@]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-rekognition-streamprocessor-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `\A[a-zA-Z0-9+\-=\._\:\/@]+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
