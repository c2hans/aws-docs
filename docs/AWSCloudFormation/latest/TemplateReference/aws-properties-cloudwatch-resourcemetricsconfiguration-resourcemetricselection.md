---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-resourcemetricsconfiguration-resourcemetricselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::ResourceMetricsConfiguration ResourceMetricSelection
<a name="aws-properties-cloudwatch-resourcemetricsconfiguration-resourcemetricselection"></a>

Specifies which metrics Amazon CloudWatch collects for a resource metrics configuration. Include this in a [CreateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CreateResourceMetricsConfiguration.html) or [UpdateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateResourceMetricsConfiguration.html) request to limit collection to a specific set of metrics. If you omit metric selections, Amazon CloudWatch collects all available detailed metrics for the resource.

## Syntax
<a name="aws-properties-cloudwatch-resourcemetricsconfiguration-resourcemetricselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-resourcemetricsconfiguration-resourcemetricselection-syntax.json"></a>

```
{
  "[IncludeMetrics](#cfn-cloudwatch-resourcemetricsconfiguration-resourcemetricselection-includemetrics)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudwatch-resourcemetricsconfiguration-resourcemetricselection-syntax.yaml"></a>

```
  [IncludeMetrics](#cfn-cloudwatch-resourcemetricsconfiguration-resourcemetricselection-includemetrics): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudwatch-resourcemetricsconfiguration-resourcemetricselection-properties"></a>

`IncludeMetrics`  <a name="cfn-cloudwatch-resourcemetricsconfiguration-resourcemetricselection-includemetrics"></a>
The names of the metrics to collect for the resource. Amazon CloudWatch collects only the metrics that you list here.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
