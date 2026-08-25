---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hyperparametertuningjob-tuningobjective.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HyperParameterTuningJob TuningObjective
<a name="aws-properties-sagemaker-hyperparametertuningjob-tuningobjective"></a>

<a name="aws-properties-sagemaker-hyperparametertuningjob-tuningobjective-description"></a>The `TuningObjective` property type specifies Property description not available. for an [AWS::SageMaker::HyperParameterTuningJob](aws-resource-sagemaker-hyperparametertuningjob.md).

## Syntax
<a name="aws-properties-sagemaker-hyperparametertuningjob-tuningobjective-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hyperparametertuningjob-tuningobjective-syntax.json"></a>

```
{
  "[MetricName](#cfn-sagemaker-hyperparametertuningjob-tuningobjective-metricname)" : {{String}},
  "[Type](#cfn-sagemaker-hyperparametertuningjob-tuningobjective-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-hyperparametertuningjob-tuningobjective-syntax.yaml"></a>

```
  [MetricName](#cfn-sagemaker-hyperparametertuningjob-tuningobjective-metricname): {{String}}
  [Type](#cfn-sagemaker-hyperparametertuningjob-tuningobjective-type): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-hyperparametertuningjob-tuningobjective-properties"></a>

`MetricName`  <a name="cfn-sagemaker-hyperparametertuningjob-tuningobjective-metricname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-sagemaker-hyperparametertuningjob-tuningobjective-type"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `Maximize | Minimize`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
