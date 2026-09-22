---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-vocabulary-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Vocabulary Tag
<a name="aws-properties-connect-vocabulary-tag"></a>

<a name="aws-properties-connect-vocabulary-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::Connect::Vocabulary](aws-resource-connect-vocabulary.md).

## Syntax
<a name="aws-properties-connect-vocabulary-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-vocabulary-tag-syntax.json"></a>

```
{
  "[Key](#cfn-connect-vocabulary-tag-key)" : {{String}},
  "[Value](#cfn-connect-vocabulary-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-vocabulary-tag-syntax.yaml"></a>

```
  [Key](#cfn-connect-vocabulary-tag-key): {{String}}
  [Value](#cfn-connect-vocabulary-tag-value): {{String}}
```

## Properties
<a name="aws-properties-connect-vocabulary-tag-properties"></a>

`Key`  <a name="cfn-connect-vocabulary-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-connect-vocabulary-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
