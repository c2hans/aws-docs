---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-metric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective Metric
<a name="aws-properties-applicationsignals-servicelevelobjective-metric"></a>

This structure defines the metric used for a service level indicator, including the metric name, namespace, and dimensions

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-metric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-metric-syntax.json"></a>

```
{
  "[Dimensions](#cfn-applicationsignals-servicelevelobjective-metric-dimensions)" : {{[ Dimension, ... ]}},
  "[MetricName](#cfn-applicationsignals-servicelevelobjective-metric-metricname)" : {{String}},
  "[Namespace](#cfn-applicationsignals-servicelevelobjective-metric-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-metric-syntax.yaml"></a>

```
  [Dimensions](#cfn-applicationsignals-servicelevelobjective-metric-dimensions): {{
    - Dimension}}
  [MetricName](#cfn-applicationsignals-servicelevelobjective-metric-metricname): {{String}}
  [Namespace](#cfn-applicationsignals-servicelevelobjective-metric-namespace): {{String}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-metric-properties"></a>

`Dimensions`  <a name="cfn-applicationsignals-servicelevelobjective-metric-dimensions"></a>
An array of one or more dimensions to use to define the metric that you want to use. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension).
*Required*: No
*Type*: Array of [Dimension](aws-properties-applicationsignals-servicelevelobjective-dimension.md)
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-applicationsignals-servicelevelobjective-metric-metricname"></a>
The name of the metric to use.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-applicationsignals-servicelevelobjective-metric-namespace"></a>
The namespace of the metric. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace).
*Required*: No
*Type*: String
*Pattern*: `.*[^:].*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
