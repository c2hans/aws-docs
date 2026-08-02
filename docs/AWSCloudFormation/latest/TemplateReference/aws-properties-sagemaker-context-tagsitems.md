---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-context-tagsitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Context TagsItems
<a name="aws-properties-sagemaker-context-tagsitems"></a>

<a name="aws-properties-sagemaker-context-tagsitems-description"></a>The `TagsItems` property type specifies Property description not available. for an [AWS::SageMaker::Context](aws-resource-sagemaker-context.md).

## Syntax
<a name="aws-properties-sagemaker-context-tagsitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-context-tagsitems-syntax.json"></a>

```
{
  "[Key](#cfn-sagemaker-context-tagsitems-key)" : {{String}},
  "[Value](#cfn-sagemaker-context-tagsitems-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-context-tagsitems-syntax.yaml"></a>

```
  [Key](#cfn-sagemaker-context-tagsitems-key): {{String}}
  [Value](#cfn-sagemaker-context-tagsitems-value): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-context-tagsitems-properties"></a>

`Key`  <a name="cfn-sagemaker-context-tagsitems-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sagemaker-context-tagsitems-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
