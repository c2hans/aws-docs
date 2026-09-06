---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-metricsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig MetricsConfig
<a name="aws-properties-sagemaker-endpointconfig-metricsconfig"></a>

The configuration for Utilization metrics.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-metricsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-metricsconfig-syntax.json"></a>

```
{
  "[EnableDetailedObservability](#cfn-sagemaker-endpointconfig-metricsconfig-enabledetailedobservability)" : {{Boolean}},
  "[EnableEnhancedMetrics](#cfn-sagemaker-endpointconfig-metricsconfig-enableenhancedmetrics)" : {{Boolean}},
  "[MetricPublishFrequencyInSeconds](#cfn-sagemaker-endpointconfig-metricsconfig-metricpublishfrequencyinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-metricsconfig-syntax.yaml"></a>

```
  [EnableDetailedObservability](#cfn-sagemaker-endpointconfig-metricsconfig-enabledetailedobservability): {{Boolean}}
  [EnableEnhancedMetrics](#cfn-sagemaker-endpointconfig-metricsconfig-enableenhancedmetrics): {{Boolean}}
  [MetricPublishFrequencyInSeconds](#cfn-sagemaker-endpointconfig-metricsconfig-metricpublishfrequencyinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-metricsconfig-properties"></a>

`EnableDetailedObservability`  <a name="cfn-sagemaker-endpointconfig-metricsconfig-enabledetailedobservability"></a>
Indicates whether detailed observability is enabled for the endpoint. When set to `True`, the following metrics are published at the configured frequency:
+ Container-level inference metrics scraped from the container's Prometheus endpoint (such as request latency, error counts, and throughput). Available metrics vary by framework.
+ Per-GPU metrics (utilization, memory, and temperature) attributed to individual inference components.
+ Per-instance host metrics (CPU, memory, and disk utilization).
+ Inference component placement metrics (copy count per Availability Zone).
For first-party and Deep Learning Containers (DLC), the Prometheus endpoint path is determined automatically. For Bring-Your-Own-Container (BYOC) cases, you can optionally set `ContainerMetricsConfig` to specify a custom endpoint path. If not specified, the default path `/metrics` on port `8080` is used.
When set to `False`, these additional metrics are not published. Standard invocation and utilization metrics controlled by `EnableEnhancedMetrics` are unaffected.
The default value for new endpoint configurations is `True`. For existing endpoint configurations created before this feature, the value is `False` unless explicitly set.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableEnhancedMetrics`  <a name="cfn-sagemaker-endpointconfig-metricsconfig-enableenhancedmetrics"></a>
Specifies whether to enable enhanced metrics for the endpoint. Enhanced metrics provide utilization and invocation data at instance and container granularity. Container granularity is supported for Inference Components. The default is `False`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetricPublishFrequencyInSeconds`  <a name="cfn-sagemaker-endpointconfig-metricsconfig-metricpublishfrequencyinseconds"></a>
The interval, in seconds, at which metrics are published to Amazon CloudWatch. Defaults to `60`. Valid values: `10`, `30`, `60`, `120`, `180`, `240`, `300`.
When `EnableEnhancedMetrics` is set to `False`, this interval applies to utilization metrics only. Invocation metrics continue to be published at the default 60-second interval. When `EnableEnhancedMetrics` is set to `True`, this interval applies to both utilization and invocation metrics.
When `EnableDetailedObservability` is set to `True`, this interval applies to per-GPU metrics, per-instance host metrics, container metrics, and fleet-level inference component lifecycle and placement metrics.
*Required*: No
*Type*: Integer
*Allowed values*: `10 | 30 | 60 | 120 | 180 | 240 | 300`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
