---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-evaluationdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard EvaluationDetail
<a name="aws-properties-sagemaker-modelcard-evaluationdetail"></a>

The evaluation details of the model.

## Syntax
<a name="aws-properties-sagemaker-modelcard-evaluationdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-evaluationdetail-syntax.json"></a>

```
{
  "[Datasets](#cfn-sagemaker-modelcard-evaluationdetail-datasets)" : {{[ String, ... ]}},
  "[EvaluationJobArn](#cfn-sagemaker-modelcard-evaluationdetail-evaluationjobarn)" : {{String}},
  "[EvaluationObservation](#cfn-sagemaker-modelcard-evaluationdetail-evaluationobservation)" : {{String}},
  "[Metadata](#cfn-sagemaker-modelcard-evaluationdetail-metadata)" : {{{{{Key}}: {{Value}}, ...}}},
  "[MetricGroups](#cfn-sagemaker-modelcard-evaluationdetail-metricgroups)" : {{[ MetricGroup, ... ]}},
  "[Name](#cfn-sagemaker-modelcard-evaluationdetail-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-evaluationdetail-syntax.yaml"></a>

```
  [Datasets](#cfn-sagemaker-modelcard-evaluationdetail-datasets): {{
    - String}}
  [EvaluationJobArn](#cfn-sagemaker-modelcard-evaluationdetail-evaluationjobarn): {{String}}
  [EvaluationObservation](#cfn-sagemaker-modelcard-evaluationdetail-evaluationobservation): {{String}}
  [Metadata](#cfn-sagemaker-modelcard-evaluationdetail-metadata): {{
    {{Key}}: {{Value}}}}
  [MetricGroups](#cfn-sagemaker-modelcard-evaluationdetail-metricgroups): {{
    - MetricGroup}}
  [Name](#cfn-sagemaker-modelcard-evaluationdetail-name): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-evaluationdetail-properties"></a>

`Datasets`  <a name="cfn-sagemaker-modelcard-evaluationdetail-datasets"></a>
The location of the datasets used to evaluate the model.
*Required*: No
*Type*: Array of String
*Maximum*: `1024 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EvaluationJobArn`  <a name="cfn-sagemaker-modelcard-evaluationdetail-evaluationjobarn"></a>
The Amazon Resource Name (ARN) of the evaluation job.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EvaluationObservation`  <a name="cfn-sagemaker-modelcard-evaluationdetail-evaluationobservation"></a>
Any observations made during the model evaluation.
*Required*: No
*Type*: String
*Maximum*: `2096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metadata`  <a name="cfn-sagemaker-modelcard-evaluationdetail-metadata"></a>
Additional attributes associated with the evaluation results.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z_][a-zA-Z0-9_]*`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricGroups`  <a name="cfn-sagemaker-modelcard-evaluationdetail-metricgroups"></a>
An evaluation Metric Group object.
*Required*: No
*Type*: Array of [MetricGroup](aws-properties-sagemaker-modelcard-metricgroup.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-sagemaker-modelcard-evaluationdetail-name"></a>
The evaluation job name.
*Required*: Yes
*Type*: String
*Pattern*: `.{1,63}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
