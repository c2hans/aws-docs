---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-algorithm-metricdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm MetricDefinition
<a name="aws-properties-sagemaker-algorithm-metricdefinition"></a>

Specifies a metric that the training algorithm writes to `stderr` or `stdout`. You can view these logs to understand how your training job performs and check for any errors encountered during training. SageMaker hyperparameter tuning captures all defined metrics. Specify one of the defined metrics to use as an objective metric using the [TuningObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-TuningObjective) parameter in the `HyperParameterTrainingJobDefinition` API to evaluate job performance during hyperparameter tuning.

## Syntax
<a name="aws-properties-sagemaker-algorithm-metricdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-algorithm-metricdefinition-syntax.json"></a>

```
{
  "[Name](#cfn-sagemaker-algorithm-metricdefinition-name)" : {{String}},
  "[Regex](#cfn-sagemaker-algorithm-metricdefinition-regex)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-algorithm-metricdefinition-syntax.yaml"></a>

```
  [Name](#cfn-sagemaker-algorithm-metricdefinition-name): {{String}}
  [Regex](#cfn-sagemaker-algorithm-metricdefinition-regex): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-algorithm-metricdefinition-properties"></a>

`Name`  <a name="cfn-sagemaker-algorithm-metricdefinition-name"></a>
The name of the metric.
*Required*: Yes
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Regex`  <a name="cfn-sagemaker-algorithm-metricdefinition-regex"></a>
A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see [Defining metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html).
*Required*: Yes
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
