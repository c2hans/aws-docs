---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-bias.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage Bias
<a name="aws-properties-sagemaker-modelpackage-bias"></a>

Contains bias metrics for a model.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-bias-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-bias-syntax.json"></a>

```
{
  "[PostTrainingReport](#cfn-sagemaker-modelpackage-bias-posttrainingreport)" : {{MetricsSource}},
  "[PreTrainingReport](#cfn-sagemaker-modelpackage-bias-pretrainingreport)" : {{MetricsSource}},
  "[Report](#cfn-sagemaker-modelpackage-bias-report)" : {{MetricsSource}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-bias-syntax.yaml"></a>

```
  [PostTrainingReport](#cfn-sagemaker-modelpackage-bias-posttrainingreport): {{
    MetricsSource}}
  [PreTrainingReport](#cfn-sagemaker-modelpackage-bias-pretrainingreport): {{
    MetricsSource}}
  [Report](#cfn-sagemaker-modelpackage-bias-report): {{
    MetricsSource}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-bias-properties"></a>

`PostTrainingReport`  <a name="cfn-sagemaker-modelpackage-bias-posttrainingreport"></a>
The post-training bias report for a model.
*Required*: No
*Type*: [MetricsSource](aws-properties-sagemaker-modelpackage-metricssource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreTrainingReport`  <a name="cfn-sagemaker-modelpackage-bias-pretrainingreport"></a>
The pre-training bias report for a model.
*Required*: No
*Type*: [MetricsSource](aws-properties-sagemaker-modelpackage-metricssource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Report`  <a name="cfn-sagemaker-modelpackage-bias-report"></a>
The bias report for a model
*Required*: No
*Type*: [MetricsSource](aws-properties-sagemaker-modelpackage-metricssource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
