---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trialcomponent-tagsitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrialComponent TagsItems
<a name="aws-properties-sagemaker-trialcomponent-tagsitems"></a>

<a name="aws-properties-sagemaker-trialcomponent-tagsitems-description"></a>The `TagsItems` property type specifies Property description not available. for an [AWS::SageMaker::TrialComponent](aws-resource-sagemaker-trialcomponent.md).

## Syntax
<a name="aws-properties-sagemaker-trialcomponent-tagsitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trialcomponent-tagsitems-syntax.json"></a>

```
{
  "[Key](#cfn-sagemaker-trialcomponent-tagsitems-key)" : {{String}},
  "[Value](#cfn-sagemaker-trialcomponent-tagsitems-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trialcomponent-tagsitems-syntax.yaml"></a>

```
  [Key](#cfn-sagemaker-trialcomponent-tagsitems-key): {{String}}
  [Value](#cfn-sagemaker-trialcomponent-tagsitems-value): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-trialcomponent-tagsitems-properties"></a>

`Key`  <a name="cfn-sagemaker-trialcomponent-tagsitems-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sagemaker-trialcomponent-tagsitems-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
