---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-cloudwatchmetricaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule CloudwatchMetricAction
<a name="aws-properties-iot-topicrule-cloudwatchmetricaction"></a>

Describes an action that captures a CloudWatch metric.

## Syntax
<a name="aws-properties-iot-topicrule-cloudwatchmetricaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-cloudwatchmetricaction-syntax.json"></a>

```
{
  "[MetricName](#cfn-iot-topicrule-cloudwatchmetricaction-metricname)" : {{String}},
  "[MetricNamespace](#cfn-iot-topicrule-cloudwatchmetricaction-metricnamespace)" : {{String}},
  "[MetricTimestamp](#cfn-iot-topicrule-cloudwatchmetricaction-metrictimestamp)" : {{String}},
  "[MetricUnit](#cfn-iot-topicrule-cloudwatchmetricaction-metricunit)" : {{String}},
  "[MetricValue](#cfn-iot-topicrule-cloudwatchmetricaction-metricvalue)" : {{String}},
  "[RoleArn](#cfn-iot-topicrule-cloudwatchmetricaction-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-cloudwatchmetricaction-syntax.yaml"></a>

```
  [MetricName](#cfn-iot-topicrule-cloudwatchmetricaction-metricname): {{String}}
  [MetricNamespace](#cfn-iot-topicrule-cloudwatchmetricaction-metricnamespace): {{String}}
  [MetricTimestamp](#cfn-iot-topicrule-cloudwatchmetricaction-metrictimestamp): {{String}}
  [MetricUnit](#cfn-iot-topicrule-cloudwatchmetricaction-metricunit): {{String}}
  [MetricValue](#cfn-iot-topicrule-cloudwatchmetricaction-metricvalue): {{String}}
  [RoleArn](#cfn-iot-topicrule-cloudwatchmetricaction-rolearn): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-cloudwatchmetricaction-properties"></a>

`MetricName`  <a name="cfn-iot-topicrule-cloudwatchmetricaction-metricname"></a>
The CloudWatch metric name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricNamespace`  <a name="cfn-iot-topicrule-cloudwatchmetricaction-metricnamespace"></a>
The CloudWatch metric namespace name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricTimestamp`  <a name="cfn-iot-topicrule-cloudwatchmetricaction-metrictimestamp"></a>
An optional [Unix timestamp](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricUnit`  <a name="cfn-iot-topicrule-cloudwatchmetricaction-metricunit"></a>
The [metric unit](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit) supported by CloudWatch.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricValue`  <a name="cfn-iot-topicrule-cloudwatchmetricaction-metricvalue"></a>
The CloudWatch metric value.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-topicrule-cloudwatchmetricaction-rolearn"></a>
The IAM role that allows access to the CloudWatch metric.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
