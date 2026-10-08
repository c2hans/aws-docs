---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-otelenrichment-otelenrichmentmetricselector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::OTelEnrichment OTelEnrichmentMetricSelector
<a name="aws-properties-cloudwatch-otelenrichment-otelenrichmentmetricselector"></a>

Selects the metrics in one namespace, for use in the `IncludeFilters` or `ExcludeFilters` parameter of [StartOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StartOTelEnrichment.html) or [UpdateOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateOTelEnrichment.html).

A maximum of 100 selectors is allowed across `IncludeFilters` and `ExcludeFilters` combined.

## Syntax
<a name="aws-properties-cloudwatch-otelenrichment-otelenrichmentmetricselector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-otelenrichment-otelenrichmentmetricselector-syntax.json"></a>

```
{
  "[MetricNames](#cfn-cloudwatch-otelenrichment-otelenrichmentmetricselector-metricnames)" : {{[ String, ... ]}},
  "[Namespace](#cfn-cloudwatch-otelenrichment-otelenrichmentmetricselector-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-otelenrichment-otelenrichmentmetricselector-syntax.yaml"></a>

```
  [MetricNames](#cfn-cloudwatch-otelenrichment-otelenrichmentmetricselector-metricnames): {{
    - String}}
  [Namespace](#cfn-cloudwatch-otelenrichment-otelenrichmentmetricselector-namespace): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-otelenrichment-otelenrichmentmetricselector-properties"></a>

`MetricNames`  <a name="cfn-cloudwatch-otelenrichment-otelenrichmentmetricselector-metricnames"></a>
The names of the metrics to select within the namespace. Metric names are matched exactly and are case-sensitive. If this parameter is omitted, every metric in the namespace is selected.
A maximum of 100 metric names is allowed for each selector.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `255 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-cloudwatch-otelenrichment-otelenrichmentmetricselector-namespace"></a>
The namespace of the metrics to select. Namespaces are matched exactly and are case-sensitive.
*Required*: Yes
*Type*: String
*Pattern*: `^[^:].*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
