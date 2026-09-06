---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-containermetricsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent ContainerMetricsConfig
<a name="aws-properties-sagemaker-inferencecomponent-containermetricsconfig"></a>

The configuration for container-level metrics scraping. Use this configuration to specify a custom metrics endpoint path and publishing frequency for container metrics. When `EnableDetailedObservability` is set to `True` in `MetricsConfig`, metrics are scraped from the container's Prometheus endpoint. If this configuration is not provided, the default path `/metrics` on port `8080` is used with a default publishing frequency of `60` seconds. For first-party and Deep Learning Containers (DLC), the endpoint path is determined automatically and this configuration is optional.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-containermetricsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-containermetricsconfig-syntax.json"></a>

```
{
  "[MetricsEndpoints](#cfn-sagemaker-inferencecomponent-containermetricsconfig-metricsendpoints)" : {{[ MetricsEndpoint, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-containermetricsconfig-syntax.yaml"></a>

```
  [MetricsEndpoints](#cfn-sagemaker-inferencecomponent-containermetricsconfig-metricsendpoints): {{
    - MetricsEndpoint}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-containermetricsconfig-properties"></a>

`MetricsEndpoints`  <a name="cfn-sagemaker-inferencecomponent-containermetricsconfig-metricsendpoints"></a>
A list of metrics endpoints to scrape from the container. Each endpoint specifies the path where the container exposes Prometheus-formatted metrics and the frequency at which to publish them. You can specify a maximum of 1 endpoint.
*Required*: Yes
*Type*: Array of [MetricsEndpoint](aws-properties-sagemaker-inferencecomponent-metricsendpoint.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
