---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-metricgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard MetricGroup
<a name="aws-properties-sagemaker-modelcard-metricgroup"></a>

A group of metric data that you use to initialize a metric group object.

## Syntax
<a name="aws-properties-sagemaker-modelcard-metricgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-metricgroup-syntax.json"></a>

```
{
  "[MetricData](#cfn-sagemaker-modelcard-metricgroup-metricdata)" : {{[ MetricDataItems, ... ]}},
  "[Name](#cfn-sagemaker-modelcard-metricgroup-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-metricgroup-syntax.yaml"></a>

```
  [MetricData](#cfn-sagemaker-modelcard-metricgroup-metricdata): {{
    - MetricDataItems}}
  [Name](#cfn-sagemaker-modelcard-metricgroup-name): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-metricgroup-properties"></a>

`MetricData`  <a name="cfn-sagemaker-modelcard-metricgroup-metricdata"></a>
A list of metric objects. The `MetricDataItems` list can have one of the following values:
+  `bar_chart_metric`
+  `matrix_metric`
+  `simple_metric`
+  `linear_graph_metric`
For more information about the metric schema, see the definition section of the [model card JSON schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html#model-cards-json-schema).
*Required*: Yes
*Type*: Array of [MetricDataItems](aws-properties-sagemaker-modelcard-metricdataitems.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-sagemaker-modelcard-metricgroup-name"></a>
The metric group name.
*Required*: Yes
*Type*: String
*Pattern*: `.{1,63}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
