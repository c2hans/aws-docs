---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-simplemetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard SimpleMetric
<a name="aws-properties-sagemaker-modelcard-simplemetric"></a>

A simple metric for evaluating model performance.

## Syntax
<a name="aws-properties-sagemaker-modelcard-simplemetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-simplemetric-syntax.json"></a>

```
{
  "[Name](#cfn-sagemaker-modelcard-simplemetric-name)" : {{String}},
  "[Notes](#cfn-sagemaker-modelcard-simplemetric-notes)" : {{String}},
  "[Type](#cfn-sagemaker-modelcard-simplemetric-type)" : {{String}},
  "[Value](#cfn-sagemaker-modelcard-simplemetric-value)" : {{Number}},
  "[XAxisName](#cfn-sagemaker-modelcard-simplemetric-xaxisname)" : {{String}},
  "[YAxisName](#cfn-sagemaker-modelcard-simplemetric-yaxisname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-simplemetric-syntax.yaml"></a>

```
  [Name](#cfn-sagemaker-modelcard-simplemetric-name): {{String}}
  [Notes](#cfn-sagemaker-modelcard-simplemetric-notes): {{String}}
  [Type](#cfn-sagemaker-modelcard-simplemetric-type): {{String}}
  [Value](#cfn-sagemaker-modelcard-simplemetric-value): {{Number}}
  [XAxisName](#cfn-sagemaker-modelcard-simplemetric-xaxisname): {{String}}
  [YAxisName](#cfn-sagemaker-modelcard-simplemetric-yaxisname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-simplemetric-properties"></a>

`Name`  <a name="cfn-sagemaker-modelcard-simplemetric-name"></a>
The name of the metric.
*Required*: Yes
*Type*: String
*Pattern*: `.{1,255}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Notes`  <a name="cfn-sagemaker-modelcard-simplemetric-notes"></a>
Additional notes about the metric.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-sagemaker-modelcard-simplemetric-type"></a>
The type of the metric.
*Required*: Yes
*Type*: String
*Allowed values*: `number | string | boolean`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sagemaker-modelcard-simplemetric-value"></a>
The value of the metric.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxisName`  <a name="cfn-sagemaker-modelcard-simplemetric-xaxisname"></a>
The name of the X-axis for the metric visualization.
*Required*: No
*Type*: String
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`YAxisName`  <a name="cfn-sagemaker-modelcard-simplemetric-yaxisname"></a>
The name of the Y-axis for the metric visualization.
*Required*: No
*Type*: String
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
