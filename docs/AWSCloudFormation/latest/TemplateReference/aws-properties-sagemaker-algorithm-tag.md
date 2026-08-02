---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-algorithm-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm Tag
<a name="aws-properties-sagemaker-algorithm-tag"></a>

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker AWS resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html).

For more information on adding metadata to your AWS resources with tagging, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html). For advice on best practices for managing AWS resources with tagging, see [Tagging Best Practices: Implement an Effective AWS Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf).

## Syntax
<a name="aws-properties-sagemaker-algorithm-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-algorithm-tag-syntax.json"></a>

```
{
  "[Key](#cfn-sagemaker-algorithm-tag-key)" : {{String}},
  "[Value](#cfn-sagemaker-algorithm-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-algorithm-tag-syntax.yaml"></a>

```
  [Key](#cfn-sagemaker-algorithm-tag-key): {{String}}
  [Value](#cfn-sagemaker-algorithm-tag-value): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-algorithm-tag-properties"></a>

`Key`  <a name="cfn-sagemaker-algorithm-tag-key"></a>
The tag key. Tag keys must be unique per resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sagemaker-algorithm-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
