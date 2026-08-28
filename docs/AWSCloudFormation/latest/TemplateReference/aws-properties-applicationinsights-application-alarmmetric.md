---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationinsights-application-alarmmetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationInsights::Application AlarmMetric
<a name="aws-properties-applicationinsights-application-alarmmetric"></a>

The `AWS::ApplicationInsights::Application AlarmMetric` property type defines a metric to monitor for the component.

## Syntax
<a name="aws-properties-applicationinsights-application-alarmmetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationinsights-application-alarmmetric-syntax.json"></a>

```
{
  "[AlarmMetricName](#cfn-applicationinsights-application-alarmmetric-alarmmetricname)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationinsights-application-alarmmetric-syntax.yaml"></a>

```
  [AlarmMetricName](#cfn-applicationinsights-application-alarmmetric-alarmmetricname): {{String}}
```

## Properties
<a name="aws-properties-applicationinsights-application-alarmmetric-properties"></a>

`AlarmMetricName`  <a name="cfn-applicationinsights-application-alarmmetric-alarmmetricname"></a>
The name of the metric to be monitored for the component. For metrics supported by Application Insights, see [Logs and metrics supported by Amazon CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-logs-and-metrics.html).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
