---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-explainability.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage Explainability
<a name="aws-properties-sagemaker-modelpackage-explainability"></a>

Contains explainability metrics for a model.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-explainability-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-explainability-syntax.json"></a>

```
{
  "[Report](#cfn-sagemaker-modelpackage-explainability-report)" : {{MetricsSource}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-explainability-syntax.yaml"></a>

```
  [Report](#cfn-sagemaker-modelpackage-explainability-report): {{
    MetricsSource}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-explainability-properties"></a>

`Report`  <a name="cfn-sagemaker-modelpackage-explainability-report"></a>
The explainability report for a model.
*Required*: No
*Type*: [MetricsSource](aws-properties-sagemaker-modelpackage-metricssource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
