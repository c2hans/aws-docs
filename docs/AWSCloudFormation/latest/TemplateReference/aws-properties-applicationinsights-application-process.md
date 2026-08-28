---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationinsights-application-process.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationInsights::Application Process
<a name="aws-properties-applicationinsights-application-process"></a>

<a name="aws-properties-applicationinsights-application-process-description"></a>The `Process` property type specifies Property description not available. for an [AWS::ApplicationInsights::Application](aws-resource-applicationinsights-application.md).

## Syntax
<a name="aws-properties-applicationinsights-application-process-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationinsights-application-process-syntax.json"></a>

```
{
  "[AlarmMetrics](#cfn-applicationinsights-application-process-alarmmetrics)" : {{[ AlarmMetric, ... ]}},
  "[ProcessName](#cfn-applicationinsights-application-process-processname)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationinsights-application-process-syntax.yaml"></a>

```
  [AlarmMetrics](#cfn-applicationinsights-application-process-alarmmetrics): {{
    - AlarmMetric}}
  [ProcessName](#cfn-applicationinsights-application-process-processname): {{String}}
```

## Properties
<a name="aws-properties-applicationinsights-application-process-properties"></a>

`AlarmMetrics`  <a name="cfn-applicationinsights-application-process-alarmmetrics"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [AlarmMetric](aws-properties-applicationinsights-application-alarmmetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcessName`  <a name="cfn-applicationinsights-application-process-processname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_,-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
