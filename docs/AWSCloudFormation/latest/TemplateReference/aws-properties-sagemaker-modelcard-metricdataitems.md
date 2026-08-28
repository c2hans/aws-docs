---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-metricdataitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard MetricDataItems
<a name="aws-properties-sagemaker-modelcard-metricdataitems"></a>

Metric data. The `type` determines the data types that you specify for `value`, `XAxisName` and `YAxisName`. For information about specifying values for metrics, see [model card JSON schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html#model-cards-json-schema).

## Syntax
<a name="aws-properties-sagemaker-modelcard-metricdataitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-metricdataitems-syntax.json"></a>

```
{
  "[MetricDataItems](#cfn-sagemaker-modelcard-metricdataitems-metricdataitems)" : {{SimpleMetric}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-metricdataitems-syntax.yaml"></a>

```
  [MetricDataItems](#cfn-sagemaker-modelcard-metricdataitems-metricdataitems): {{
    SimpleMetric}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-metricdataitems-properties"></a>

`MetricDataItems`  <a name="cfn-sagemaker-modelcard-metricdataitems-metricdataitems"></a>
A list of metric data items for the model.
*Required*: No
*Type*: [SimpleMetric](aws-properties-sagemaker-modelcard-simplemetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
