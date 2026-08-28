---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-metricstat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective MetricStat
<a name="aws-properties-applicationsignals-servicelevelobjective-metricstat"></a>

This structure defines the metric to be used as the service level indicator, along with the statistics, period, and unit.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-metricstat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-metricstat-syntax.json"></a>

```
{
  "[Metric](#cfn-applicationsignals-servicelevelobjective-metricstat-metric)" : {{Metric}},
  "[Period](#cfn-applicationsignals-servicelevelobjective-metricstat-period)" : {{Integer}},
  "[Stat](#cfn-applicationsignals-servicelevelobjective-metricstat-stat)" : {{String}},
  "[Unit](#cfn-applicationsignals-servicelevelobjective-metricstat-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-metricstat-syntax.yaml"></a>

```
  [Metric](#cfn-applicationsignals-servicelevelobjective-metricstat-metric): {{
    Metric}}
  [Period](#cfn-applicationsignals-servicelevelobjective-metricstat-period): {{Integer}}
  [Stat](#cfn-applicationsignals-servicelevelobjective-metricstat-stat): {{String}}
  [Unit](#cfn-applicationsignals-servicelevelobjective-metricstat-unit): {{String}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-metricstat-properties"></a>

`Metric`  <a name="cfn-applicationsignals-servicelevelobjective-metricstat-metric"></a>
The metric to use as the service level indicator, including the metric name, namespace, and dimensions.
*Required*: Yes
*Type*: [Metric](aws-properties-applicationsignals-servicelevelobjective-metric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Period`  <a name="cfn-applicationsignals-servicelevelobjective-metricstat-period"></a>
The granularity, in seconds, to be used for the metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a `PutMetricData` call that includes a `StorageResolution` of 1 second.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stat`  <a name="cfn-applicationsignals-servicelevelobjective-metricstat-stat"></a>
The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-applicationsignals-servicelevelobjective-metricstat-unit"></a>
If you omit `Unit` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.
*Required*: No
*Type*: String
*Allowed values*: `Microseconds | Milliseconds | Seconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
