---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-metricfilter-metrictransformation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::MetricFilter MetricTransformation
<a name="aws-properties-logs-metricfilter-metrictransformation"></a>

`MetricTransformation` is a property of the `AWS::Logs::MetricFilter` resource that describes how to transform log streams into a CloudWatch metric.

## Syntax
<a name="aws-properties-logs-metricfilter-metrictransformation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-metricfilter-metrictransformation-syntax.json"></a>

```
{
  "[DefaultValue](#cfn-logs-metricfilter-metrictransformation-defaultvalue)" : {{Number}},
  "[Dimensions](#cfn-logs-metricfilter-metrictransformation-dimensions)" : {{[ Dimension, ... ]}},
  "[MetricName](#cfn-logs-metricfilter-metrictransformation-metricname)" : {{String}},
  "[MetricNamespace](#cfn-logs-metricfilter-metrictransformation-metricnamespace)" : {{String}},
  "[MetricValue](#cfn-logs-metricfilter-metrictransformation-metricvalue)" : {{String}},
  "[Unit](#cfn-logs-metricfilter-metrictransformation-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-metricfilter-metrictransformation-syntax.yaml"></a>

```
  [DefaultValue](#cfn-logs-metricfilter-metrictransformation-defaultvalue): {{Number}}
  [Dimensions](#cfn-logs-metricfilter-metrictransformation-dimensions): {{
    - Dimension}}
  [MetricName](#cfn-logs-metricfilter-metrictransformation-metricname): {{String}}
  [MetricNamespace](#cfn-logs-metricfilter-metrictransformation-metricnamespace): {{String}}
  [MetricValue](#cfn-logs-metricfilter-metrictransformation-metricvalue): {{String}}
  [Unit](#cfn-logs-metricfilter-metrictransformation-unit): {{String}}
```

## Properties
<a name="aws-properties-logs-metricfilter-metrictransformation-properties"></a>

`DefaultValue`  <a name="cfn-logs-metricfilter-metrictransformation-defaultvalue"></a>
(Optional) The value to emit when a filter pattern does not match a log event. This value can be null.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dimensions`  <a name="cfn-logs-metricfilter-metrictransformation-dimensions"></a>
The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions.
Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as `IPAddress` or `requestID` as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric.
CloudWatch Logs disables a metric filter if it generates 1000 different name/value pairs for your specified dimensions within a certain amount of time. This helps to prevent accidental high charges.
You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see [ Creating a Billing Alarm to Monitor Your Estimated AWS Charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html).
*Required*: No
*Type*: Array of [Dimension](aws-properties-logs-metricfilter-dimension.md)
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-logs-metricfilter-metrictransformation-metricname"></a>
The name of the CloudWatch metric.
*Required*: Yes
*Type*: String
*Pattern*: `^((?![:*$])[\x00-\x7F]){1,255}`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricNamespace`  <a name="cfn-logs-metricfilter-metrictransformation-metricnamespace"></a>
A custom namespace to contain your metric in CloudWatch. Use namespaces to group together metrics that are similar. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace).
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z\.\-_\/#]{1,256}`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricValue`  <a name="cfn-logs-metricfilter-metrictransformation-metricvalue"></a>
The value that is published to the CloudWatch metric. For example, if you're counting the occurrences of a particular term like `Error`, specify 1 for the metric value. If you're counting the number of bytes transferred, reference the value that is in the log event by using $. followed by the name of the field that you specified in the filter pattern, such as `$.size`.
*Required*: Yes
*Type*: String
*Pattern*: `.{1,100}`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-logs-metricfilter-metrictransformation-unit"></a>
The unit to assign to the metric. If you omit this, the unit is set as `None`.
*Required*: No
*Type*: String
*Allowed values*: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
