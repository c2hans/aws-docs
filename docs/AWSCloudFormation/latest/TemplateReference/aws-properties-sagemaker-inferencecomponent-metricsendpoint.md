---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-metricsendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent MetricsEndpoint
<a name="aws-properties-sagemaker-inferencecomponent-metricsendpoint"></a>

Specifies a metrics endpoint for a container, including the path where the container exposes Prometheus-formatted metrics and the frequency at which to publish them to Amazon CloudWatch.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-metricsendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-metricsendpoint-syntax.json"></a>

```
{
  "[MetricPublishFrequencyInSeconds](#cfn-sagemaker-inferencecomponent-metricsendpoint-metricpublishfrequencyinseconds)" : {{Integer}},
  "[MetricsEndpointPath](#cfn-sagemaker-inferencecomponent-metricsendpoint-metricsendpointpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-metricsendpoint-syntax.yaml"></a>

```
  [MetricPublishFrequencyInSeconds](#cfn-sagemaker-inferencecomponent-metricsendpoint-metricpublishfrequencyinseconds): {{Integer}}
  [MetricsEndpointPath](#cfn-sagemaker-inferencecomponent-metricsendpoint-metricsendpointpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-metricsendpoint-properties"></a>

`MetricPublishFrequencyInSeconds`  <a name="cfn-sagemaker-inferencecomponent-metricsendpoint-metricpublishfrequencyinseconds"></a>
The interval, in seconds, at which container metrics scraped from the endpoint are published to Amazon CloudWatch. Valid values: `10`, `30`, `60`, `120`, `180`, `240`, `300`. Defaults to `60`.
*Required*: No
*Type*: Integer
*Minimum*: `10`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricsEndpointPath`  <a name="cfn-sagemaker-inferencecomponent-metricsendpoint-metricsendpointpath"></a>
The path to the metrics endpoint exposed by the container. For example, `/metrics` or `/server/metrics`. The path must start with `/` and can contain alphanumeric characters, forward slashes, underscores, hyphens, and periods. Maximum length is 256 characters. If not specified, defaults to `/metrics`.
*Required*: Yes
*Type*: String
*Pattern*: `^/(?!.*\.\.)[a-zA-Z0-9/_.\-]+$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
